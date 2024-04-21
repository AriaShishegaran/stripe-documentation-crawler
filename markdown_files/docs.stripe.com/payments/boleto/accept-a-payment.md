htmlBoleto payments | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fboleto%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fboleto%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Vouchers](/docs/payments/vouchers)[Boleto](/docs/payments/boleto)# Boleto payments

Learn how to accept Boleto, a common payment method in Brazil.Prebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Boleto is a single use payment method where customers are required to take additional steps to complete their payment. Customers pay by using a Boleto voucher with a generated number either in ATMs, banks, bank portals or authorized agencies.

[Determine compatibility](#compatibility)Supported business locations: BR

Supported currencies: brl

Presentment currencies: brl

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Boleto payments:

- [Prices](/api/prices)for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring[subscription](/billing/subscriptions/creating)plans are not supported).

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

Use this guide to learn how to enable Boleto—it shows the differences between accepting a card payment and using Boleto.

### Enable Boleto as a payment method

When creating a new Checkout Session, you need to:

1. Add`boleto`to the list of`payment_method_types`
2. Make sure all your`line_items`use the`brl`currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'boleto'],
  # The parameter is optional. The default value of expires_after_days is 3.
  payment_method_options: {
    boleto: {
      expires_after_days: 7
    }
  },
  line_items: [{
    price_data: {
      # To accept `boleto`, all line items must have currency: brl
      currency: 'brl',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`### Additional payment method options

You can specify an optional expires_after_days parameter in the payment method options for your Session that sets the number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set expires_after_days to 2, the Boleto voucher expires on Wednesday at 23:59 America/Sao_Paulo (UTC-3) time. If you set it to 0, the Boleto voucher expires at the end of the day. The expires_after_days parameter can be set from 0 to 60 days. The default is 3 days. You can customize the default expiration days on your account in the Payment methods settings

### Redirect to Stripe hosted voucher page

NoteUnlike card payments, the customer won’t be redirected to the success_url with Boleto payment.

After submitting the Checkout form successfully, the customer is redirected to the hosted_voucher_url. The customer can copy the Boleto number or download the voucher PDF from the hosted voucher page.

Stripe sends a payment_intent.requires_action event when a Boleto voucher is created successfully. If you need to email your customers the voucher link, you can locate the hosted_voucher_url in payment_intent.next_action.boleto_display_details. Learn more about how to monitor a PaymentIntent with webhooks.

Stripe allows customization of customer-facing UIs on the Branding Settings page. The following brand settings can be applied to the voucher:

- Icon—your brand image and public business name
- Accent color—used as the color of the Copy Number button
- Brand color—used as the background color

### Fulfill your orders

Because Boleto is a delayed notification payment method, you need to use a method such as webhooks to monitor the payment status and handle order fulfillment. Learn more about setting up webhooks and fulfilling orders.

The following events are sent when the payment status changes:

Event NameDescriptionNext stepscheckout.session.completed

The customer has successfully submitted the Checkout form. Stripe has generated the Boleto voucher.

You can choose to email the hosted_voucher_url to your customer in case they lose the Boleto voucher.

Wait for the customer to pay the Boleto.

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)The customer has successfully paid the Boleto. The`PaymentIntent`transitions to`succeeded`.Fulfill the goods or services that the customer purchased.[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)The Boleto voucher has expired, or the payment has failed for some other reason. The`PaymentIntent`returns to a status of`requires_payment_method`.Contact the customer via email and request that they place a new order.[Test your integration](#test-integration)When testing your Checkout integration, select Boleto as the payment method and click the Pay button.

EmailDescription{any_prefix}@{any_domain}

Simulates a Boleto voucher which a customer pays after 3 minutes and the payment_intent.succeeded webhook arrives after about 3 minutes. In production, this webhook arrives 1 business day after a payment.

Example: fulaninho@example.com

{any_prefix}succeed_immediately@{any_domain}

Simulates a Boleto voucher which a customer pays immediately and the payment_intent.succeeded webhook arrives within several seconds. In production, this webhook arrives 1 business day after a payment.

Example: succeed_immediately@example.com

{any_prefix}expire_immediately@{any_domain}

Simulates a Boleto voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives within several seconds.

The expires_at field in next_action.boleto_display_details is set to the current time regardless of what the expires_after_days parameter in payment method options is set to.

Example: expire_immediately@example.com

{any_prefix}expire_with_delay@{any_domain}

Simulates a Boleto voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives after about 3 minutes.

The expires_at field in next_action.boleto_display_details is set to 3 minutes in the future regardless of what the expires_after_days parameter in payment method options is set to.

Example: expire_with_delay@example.com

{any_prefix}fill_never@{any_domain}

Simulates a Boleto voucher which never succeeds; it expires according to the expires_at field in next_action.boleto_display_details per the provided parameters in the payment method options and the payment_intent.payment_failed webhook arrives after that.

Example: fill_never@example.com

Tax IDDescriptionCPF 000.000.000-00

CNPJ 00.000.000/0000-00

In test mode, set tax_id to these values, so they bypass the tax ID validation.

[Handle refunds](#refunds)Boleto payments can’t be refunded. Some merchants have created a separate process to credit their customers who reach out directly.

[Handle disputes](#disputes)Boleto payments can’t be disputed by the customer.

[OptionalSend payment instruction emails](#instruction-emails)## See also

- [After the Payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds](#refunds)[Handle disputes](#disputes)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
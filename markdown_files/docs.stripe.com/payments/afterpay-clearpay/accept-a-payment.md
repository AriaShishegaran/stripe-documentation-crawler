htmlAccept an Afterpay or Clearpay payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fafterpay-clearpay%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fafterpay-clearpay%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)[Afterpay / Clearpay](/docs/payments/afterpay-clearpay)# Accept an Afterpay or Clearpay payment

Learn how to accept Afterpay (also known as Clearpay in the UK), a payment method in the US, CA, UK, AU, and NZ.WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Afterpay is a single use, immediate notification payment method that requires customers to authenticate their payment. Customers are redirected to the Afterpay site, where they agree to the terms of an installment plan. When the customer accepts the terms, Afterpay guarantees that the funds are available to the customer and transfers the funds to your Stripe account. The customer repays Afterpay directly over time.

NoteBefore you start the integration, make sure your account is eligible for Afterpay by navigating to your Payment methods settings.

[Determine compatibility](#compatibility)Customer Geography: Australia, Canada, New Zealand, UK, US

Supported currencies: aud, cad, nzd, gbp, usd

Presentment currencies: aud, cad, nzd, gbp, usd

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Afterpay payments:

- You can only use one-time line items (recurring[subscription](/billing/subscriptions/creating)plans are not supported).
- You must express[Prices](/api/prices)in your domestic currency.
- Shipping addresses must be provided.

[Accept a payment](#accept-a-payment)NoteThis guide builds on the foundational accept a payment Checkout integration.

Use this guide to learn how to enable Afterpay—it shows the differences between accepting a card payment and using Afterpay.

### Enable Afterpay as a payment method

When creating a new Checkout Session, you need to:

1. Add`afterpay_clearpay`to the list of`payment_method_types`.
2. Make sure all your`line_items`use your domestic currency.
3. Collect shipping addresses by adding your country to`shipping_address_collection[allowed_countries]`. If you don’t collect shipping addresses with Checkout, provide the shipping address using`payment_intent_data[shipping]`.

[Ruby](#)`Stripe::Checkout::Session.create({
      mode: 'payment',
      payment_method_types: ['card'],
      payment_method_types: ['card', 'afterpay_clearpay'],
      line_items: [{
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          # Make sure the total amount fits within Afterpay transaction amount limits:
          # https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
          unit_amount: 2000,
        },
        quantity: 1,
      }],
      shipping_address_collection: {
        # Specify which shipping countries Checkout should provide as options for shipping locations
        allowed_countries: ['AU', 'CA', 'GB', 'NZ', 'US'],
      },
      # If you already have the shipping address, provide it in payment_intent_data:
      # payment_intent_data: {
      #   shipping: {
      #     name: 'Jenny Rosen',
      #     address: {
      #       line1: '1234 Main Street',
      #       city: 'San Francisco',
      #       state: 'CA',
      #       country: 'US',
      #       postal_code: '94111',
      #     },
      #   },
      # },
      success_url: 'https://example.com/success',
      cancel_url: 'https://example.com/cancel',
    })`### Fulfill your orders

Use a method such as webhooks to handle order fulfillment, instead of relying on your customer to return to the payment status page.

The following events are sent when the payment status changes:

Event NameDescriptionNext steps[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)The customer successfully authorized the payment by submitting the Checkout form.Wait for the payment to succeed or fail.[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)The customer’s payment succeeded. The`PaymentIntent`transitions to`succeeded`.Fulfill the goods or services that the customer purchased.[payment_intent.payment_failed](/api/events/types#event_types-payment_intent.payment_failed)The customer’s payment was declined, or failed for some other reason. The`PaymentIntent`returns to the`requires_payment_method`status.Email the customer to request that they place a new order.Learn more about fulfilling orders.

[Test your integration](#test-integration)When testing your Checkout integration, select Afterpay as the payment method and click the Pay button.

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from requires_action to succeeded.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent will transition from requires_action to requires_payment_method.

For manual capture PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

[Failed payments](#failed-payments)Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as card in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

For an Afterpay PaymentIntent with a status of requires_action, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the PaymentMethod detaches and the object status for the PaymentIntent automatically transitions to requires_payment_method.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

[Error codes](#error-codes)These are the common error codes and corresponding recommended actions:

Error CodeRecommended Action`invalid_amount_too_small`Enter an amount within Afterpay’s[default transactions limits](/payments/afterpay-clearpay#collection-schedule)for the country.`invalid_amount_too_large`Enter an amount within Afterpay’s[default transactions limits](/payments/afterpay-clearpay#collection-schedule)for the country.`payment_intent_invalid_currency`Enter the appropriate currency. Afterpay only supports[domestic transactions](/payments/afterpay-clearpay#collection-schedule).`missing_required_parameter`Check the error message for more information about the required parameter.`nonexistent_country`Enter a valid[two-letter ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)for the`country`property in the shipping and billing details.`payment_intent_redirect_confirmation_without_return_url`Provide a`return_url`when confirming a PaymentIntent with Afterpay.## See also

- [More about Afterpay](/payments/afterpay-clearpay)
- [After the Payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Failed payments](#failed-payments)[Error codes](#error-codes)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
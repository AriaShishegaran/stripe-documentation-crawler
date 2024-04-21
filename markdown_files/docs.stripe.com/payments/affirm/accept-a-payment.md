htmlAccept an Affirm payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faffirm%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faffirm%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)[Affirm](/docs/payments/affirm)# Accept an Affirm payment

Learn how to accept Affirm, a buy now and pay later payment method.Prebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Affirm is a single use, immediate notification payment method that requires customers to authenticate their payment. Customers are redirected to the Affirm site, where they agree to the terms of an installment plan. When the customer accepts the terms, funds are guaranteed and transferred to your Stripe account. The customer repays Affirm directly over time.

NoteBefore you start the integration, make sure your account is eligible for Affirm by navigating to your Payment methods settings.

[Determine compatibility](#compatibility)Customer Geography: Canada, US

Supported currencies: cad, usd

Presentment currencies: cad, usd

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Affirm payments:

- You can only use one-time line items. Affirm doesn’t support recurring[subscription](/billing/subscriptions/creating)plans.
- Express all[Prices](/api/prices)in your domestic currency.

[Accept a payment](#accept-a-payment)NoteThis guide builds on the foundational accept a payment Checkout integration.

Use this guide to learn how to enable Affirm—it shows the differences between accepting a card payment and using Affirm.

### Enable Affirm as a payment method

When creating a new Checkout Session, you need to:

1. Add`affirm`to the list of`payment_method_types`.
2. Make sure all your`line_items`use your domestic currency.
3. We recommend collecting shipping addresses by adding your country to`shipping_address_collection[allowed_countries]`. If you don’t want to collect shipping addresses with Checkout, you can also provide the shipping address using`payment_intent_data[shipping]`. Doing so helps with loan acceptance rates.

[Ruby](#)`Stripe::Checkout::Session.create({
      mode: 'payment',
      payment_method_types: ['card'],
      payment_method_types: ['card', 'affirm'],
      line_items: [{
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          # Make sure the total amount fits within Affirm's transaction amount limits
          unit_amount: 5000,
        },
        quantity: 1,
      }],
      shipping_address_collection: {
        # Shipping address is optional but recommended to pass in
        # Specify which shipping countries Checkout should provide as options for shipping locations
        allowed_countries: ['CA', 'US'],
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

[Test your integration](#test-integration)When testing your Checkout integration, select Affirm as the payment method and click the Pay button.

Test your Affirm integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from requires_action to succeeded.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent transitions from requires_action to requires_payment_method.

For manual capture PaymentIntents in testmode, the uncaptured PaymentIntent auto-expires 10 minutes after successful authorization.

[Failed payments](#failed-payments)Affirm takes into account multiple factors when deciding to accept or decline a transaction (for example, the length of time buyer has used Affirm, the outstanding amount the customer has to repay, and the value of the current order).

Always present additional payment options such as card in your checkout flow, as Affirm payments have a higher rate of decline than many payment methods. In these cases, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

Other than a payment being declined, for an Affirm PaymentIntent with a status of requires_action, customers need to complete the payment within 12 hours after you redirect them to the Affirm site. If the customer takes no action within 12 hours, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

[Error codes](#error-codes)These are the common error codes and corresponding recommended actions:

Error codeRecommended action`invalid_amount_too_small`Enter an amount within Affirm’s[default transaction limits](/payments/affirm), for the country.`invalid_amount_too_large`Enter an amount within Affirm’s[default transaction limits](/payments/affirm), for the country.`missing_required_parameter`Check the error message for more information on the required parameter.`nonexistent_country`Enter a valid[two-letter ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)for the`country`property in the shipping and billing details.`payment_intent_invalid_currency`Enter the appropriate currency. Affirm only supports payments in your local currency.`payment_intent_redirect_confirmation_without_return_url`Provide a`return_url`when confirming a PaymentIntent with Affirm.`payment_method_invalid_parameter`Check the error message for more information on the parameter.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Failed payments](#failed-payments)[Error codes](#error-codes)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
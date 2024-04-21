htmlPayment Element integration best practices | Stripe Documentation[Skip to content](#main-content)Payment Element best practices[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element%2Fbest-practices)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element%2Fbest-practices)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Payment Element](/docs/payments/payment-element)# Payment Element integration best practices

Learn about best practices before building your Payment Element integration.Use the checklist on this page to make sure you build your Payment Element integration for optimal performance. The following features enable you to access additional integration options. For example, if you use Dynamic payment methods, you can use payment method rules to present payment methods with custom criteria.

## Integration checklist

- Choose a layoutChoose the Payment Element’s layout to match the style of your site, then run an A/B test to confirm the best choice. If you have over 4 payment methods, we recommend the accordion layout.


- Add stylingStyle the Payment Element to match the visual design of your website using the Appearance API. You can apply this style to any element you add to your integration.


- Choose how to collect a paymentConsider if you want to collect a payment before you create the PaymentIntent API call. To accept a payment, you must create a PaymentIntent that contains an amount and currency, and confirm that payment to trigger Stripe to make a charge. However, you can alternate the order that you collect the payment and create the PaymentIntent. We recommend that you collect the payment first.


- Send metadataSend metadata in your PaymentIntent to allow metadata to show up in your reports. This indexes your metadata to make sure that it’s searchable in the Stripe Dashboard. You can use this metadata to find and reference transactions.


- Make sure to use the latest APICheck to make sure your PaymentIntent uses the latest API version.


- Select the payment methods you want to displayUse Dynamic payment methods, part of the default Stripe integration, to present eligible payment methods to your customers. Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer to maximize conversion based on factors such as the amount, currency, location, and so on. Dynamic payment methods allow you to:

  - Choose the[payment methods](https://stripe.com/guides/payment-methods-guide)that your customers can use from the[Dashboard](https://dashboard.stripe.com/settings/payment_methods).
  - Use additional features, such as[payment method rules](/payments/payment-method-rules), which allows you to present payment methods using custom criteria.


- Test payment methodsWhen your integration is complete, test and View how payment methods appear to customers. From the Review displayed payment methods form, enter a PaymentIntent ID to learn which payment methods were and weren’t available for that specific transaction. You can also simulate which payment methods display in a given scenario by changing factors such as the amount, currency, capture method, and future usage.



## Additional features checklist

- Enable LinkAfter you integrate your UI and dynamic payment methods, enable Link in the Payment Method settings page. Link securely saves and fills in customer payment and shipping details. It supports various payment methods, including credit cards, debit cards, and US bank accounts. For logged-in customers that already use Link, this feature prefills their information, regardless of whether they initially saved it on the checkout page of another business.


- Add the Link Authentication ElementTo collect and prefill shipping addresses and sell physical goods, we recommend using the Link Authentication Element to create a single email input field for both email collection and Link authentication.


- Add the Address ElementThe Address Element streamlines collection of shipping and billing information during checkout. It integrates with other elements and prefills addresses with Link. It supports auto-suggestions for new address entry using free Google Autocomplete support.

  - In`shipping`mode, customers have the option to use their shipping address as their billing address.
  - In`billing`mode, Stripe hides billing fields within the Payment Element to make sure that customers only need to enter their details once.


- Add the Payment Method Messaging ElementIf you choose to offer BNPLs, we recommend that you promote them ahead of checkout to help drive awareness, increase order value, and positively impact conversion using the Payment Method Messaging Element.

  - You can display this unified embeddable component on product detail, cart, and payment pages.
  - This element includes support for[Affirm](/payments/affirm),[Afterpay](/payments/afterpay-clearpay), and[Klarna](/payments/klarna).


- Add the Express Checkout ElementUse the Express Checkout Element to show customers multiple one-click payment buttons in a single UI component, including Apple Pay, Google Pay, PayPal, and Link.



## Next steps

Accept a payment

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integration checklist](#integration-checklist)[Additional features checklist](#additional-features-checklist)[Next steps](#next-steps)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
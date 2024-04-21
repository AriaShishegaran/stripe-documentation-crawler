htmlLink in the Payment Element | Stripe Documentation[Skip to content](#main-content)Link in the Payment Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fpayment-element-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fpayment-element-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)[Link with Web Elements](/docs/payments/link/elements-link)# Link in the Payment Element

Link in the Payment Element lets your customers check out faster.Let your customer check out faster by using Link in the Payment Element. You can autofill information for any logged-in customer already using Link, regardless of whether they initially saved their information in Link with another business. The default Payment Element integration includes a Link prompt in the card form. To manage Link in the Payment Element, go to your payment method settings.

![Authenticate or enroll with Link directly in the Payment Element during checkout](https://b.stripecdn.com/docs-statics-srv/assets/link-in-pe.2efb5138a4708b781b8a913ebddd9aba.png)

Collect a customer email address for Link authentication or enrollment

## Integration options

There are two ways you can integrate Link with the Payment Element. Of these, Stripe recommends passing a customer email address to the Payment Element if available. Remember to consider how your checkout flow works when deciding between these options:

Integration optionCheckout flowDescription[Pass a customer email address](/payments/link/add-link-elements-integration?link-integration-type=before-payment)to the Payment ElementRecommended- Your customer enters their email address before landing on the checkout page (in a previous account creation step, for example).
- You prefer to use your own email input field.

Programmatically pass a customer email address to the Payment Element. In this scenario, a customer authenticates to Link directly in the payment form instead of a separate UI component.[Collect a customer email address](/payments/link/add-link-elements-integration?link-integration-type=collect-email)in the Payment ElementYour customers enter their email and authenticate or enroll with Link directly in the Payment Element during checkout.If a customer hasn’t enrolled with Link and they choose a supported payment method in the Payment Element, they’re prompted to save their details using Link. For those who have already enrolled, Link automatically populates their payment information.## The defaultValues parameter

If you’re planning on passing customer email addresses to the Payment Element, use the defaultValues object to specify a customer’s billingDetails. Prefilling as much information as possible streamlines the checkout process:

checkout.js`// Pass in defaultValues to prefill consumer information
const paymentElement = elements.create('payment', {
  defaultValues: {
    billingDetails: {
      name: 'John Doe',
      email: 'john.doe@example.com',
      address: {
        city: 'New York',
        country: 'US',
        line1: '123 Main St',
        postal_code: '10001',
        state: 'NY'
      }
    },
}});`## Automatically prefill Link for your customers

Save your customers from re-entering details to sign up for or log into Link when they’ve already provided them elsewhere on your checkout page. Link includes a prefill tool that detects customer information such as email or phone number in your checkout, then automatically populates corresponding Link fields.  This convenience encourages your customers to use Link, which has been shown to increase the likelihood that a customer successfully completes checkout. Prefilled values are never stored unless the customer completes a Link sign-up.

When a customer enters information such as their email, phone number, or name on the same checkout page as the Element where Link is enabled, Link’s prefill tool can:

- Populate the Link sign-up form with the customer email/phone/name. The customer must proceed with Link sign-up to create an account.
- Populate the Link login with the customer’s email when they already have a Link account, so they can just enter the one time password.

### Enable the prefill tool

The Link prefill tool requires no changes to your existing integration. The prefill tool is on by default when you enable Link. You can disable the prefill tool in the Link settings on your Dashboard at any time.

How it works![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When a customer loads a page containing the Element with Link enabled and the defaultValue parameter hasn’t already provided Stripe customer data, our system analyzes the surrounding checkout page to locate input fields containing details that match Link sign-up or login fields.  Link only looks for information applicable to creating or reusing a Link account.

If Stripe detects such data fields, we use the values to prefill the Link login with email, or prefill sign-up fields with customer information required to create a Link account. We don’t store the prefilled values on the browser using cookies or local storage or any other service. We only hold the values temporarily in local memory for use in the context of the session.

For current Link users, we use the prefilled information to trigger a login to Link, and don’t store any information from the page.

Customers who haven’t previously created a Link account can choose whether to use the prefilled information to sign up for Link. We only store the prefilled information if the customer takes action and provides consent to create a Link account.

## See also

- [Stripe Web Elements](/payments/elements)
- [Payment Element](/payments/payment-element)
- [Address Element](/elements/address-element)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integration options](#integration-options)[The defaultValues parameter](#pass-email-defaultvalues)[Automatically prefill Link for your customers](#automatic-link-prefill)[See also](#see-also)Related Guides[Build a custom checkout page that includes Link](/docs/payments/link/add-link-elements-integration?link-integration-type=before-payment)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
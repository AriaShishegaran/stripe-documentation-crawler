htmlPayment Method Messaging Element | Stripe Documentation[Skip to content](#main-content)Payment Method Messaging Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-messaging)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-messaging)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)# Payment Method Messaging Element

Automatically explain buy now, pay later payment options.The Payment Method Messaging Element is a UI component for informing a customer about available buy-now-pay-later plans. It automatically determines the available plans and conditions, generates a localized description, and displays it in your form’s theme.

United States (USD)Payment Methods$99.00![Prince of Persia book](https://b.stripecdn.com/docs-statics-srv/assets/c2815bda1cf26cedf5b8603b4667acae.png)

The Making of Prince of Persia: Journals 1985-1993Jordan Mechner$99.00CautionThe Payment Method Messaging Element for Klarna in the UK is currently disabled as we update it to adhere to the UK Financial Promotion rules.

NoteApple Pay Later is available on Apple devices and browsers.

## Create and mount the Payment Method Messaging Element

HTML + JSReactUse Stripe Elements to include the Payment Method Messaging Element on your site.

1. Add the Stripe.js script on your page by adding it to the head of your HTML file:

`<script src="https://js.stripe.com/v3/"></script>`
2. Create a placeholder element in your page where you want to mount the Payment Method Messaging Element:

`<div id="payment-method-messaging-element"></div>`
3. On your product, cart, and payment pages, include the following code to create an instance of Stripe.js (with locale) and mount the Payment Method Messaging Element:

`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const elements = stripe.elements();
const options = {
  amount: 9900, // $99.00 USD
  currency: 'USD',
  // the country that the end-buyer is in
  countryCode: 'US',
};
const PaymentMessageElement =
  elements.create('paymentMethodMessaging', options);
PaymentMessageElement.mount('#payment-method-messaging-element');`

CautionIf your integration requires you to list payment methods manually, see Customize payment methods.

## Dynamic display

The element dynamically displays payment plans that the customer is eligible for. These depend on the customer’s location and currency. They also depend on the amount of the payment, as in this example:

$0$99$1200When available, the interest-bearing loan payment plans are shown on a separate line from the pay-in-x plans, which might increase the space needed for the element.

## Customize Payment Methods

If you use Dynamic payment methods, the Payment Method Messaging Element automatically pulls your payment method preferences from the Stripe Dashboard to dynamically show the most relevant payment methods to your customers. Alternatively, you can list payment methods manually using paymentMethodTypes. The Payment Method Messaging Element still only displays plans that the customer is eligible for based on their location, the currency, and the amount of the payment.

HTML + JSReact`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const elements = stripe.elements();
const options = {
  amount: 9900, // $99.00 USD
  currency: 'USD',
  paymentMethodTypes: ['klarna', 'afterpay_clearpay', 'apple_pay_later', 'affirm'],
  // the country that the end-buyer is in
  countryCode: 'US',
};
const PaymentMessageElement =
  elements.create('paymentMethodMessaging', options);
PaymentMessageElement.mount('#payment-method-messaging-element');`## Info modal

When the customer selects the info icon (ⓘ), the Payment Method Messaging Element displays a modal with details about buy now, pay later payment plans.

![The info modal](https://b.stripecdn.com/docs-statics-srv/assets/pmme-learn-more.9524cd414b7b63883418460935a107f9.png)

A preview of the info modal

The modal includes:

- A step-by-step overview of how to use a buy now, pay later payment method
- A summary of terms for each available payment plan
- A link to the full terms for each available payment plan

## Supported plans

The Payment Method Messaging Element supports these payment methods and payment plans:

KlarnaAfterpayAffirmApple Pay Later- Pay in 3
- Pay in 4
- Pay in 30 days

- Pay in 4
- Interest-bearing loan installments

- Pay in 4
- 0% interest loan installments
- Interest-bearing loan installments

- Pay in 4

It supports these values for countryCode: US, CA, AU, NZ, GB, IE, FR, ES, DE, AT, BE, DK, FI, IT, NL, NO, SE.

It supports these values for currency: USD, GBP, EUR, DKK, NOK, SEK, CAD, AUD.

CautionMessaging does not render if the countryCode and currency combination passed has no eligible payment plans.

## Appearance

Use the Appearance API to customize the font and logo of your messaging. You can select a theme as in the example below.

FlatNightStripeUse variables for additional customization.

`const appearance = {
  variables: {
    colorText: 'rgb(84, 51, 255)',
    colorTextSecondary: 'rgb(28, 198, 255)', // info icon color
    fontSizeBase: '16px',
    spacingUnit: '10px',
    fontWeightMedium: 'bolder',
    fontFamily: 'Ideal Sans, system-ui, sans-serif',
  }
};`See all 19 linesThe Payment Method Messaging Element is a tool that allows you to message various buy now, pay later payment options to your customers. You’re responsible for compliance with applicable laws, rules, and regulations regarding the promotion of buy now, pay later payment options.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create and mount the Payment Method Messaging Element](#create-and-mount-the-payment-method-messaging-element)[Dynamic display](#dynamic-display)[Customize Payment Methods](#customize-payment-methods)[Info modal](#info-modal)[Supported plans](#supported-plans)[Appearance](#appearance)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
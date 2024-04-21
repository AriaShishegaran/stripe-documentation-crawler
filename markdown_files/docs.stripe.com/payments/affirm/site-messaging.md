htmlDisplay Affirm messaging | Stripe Documentation[Skip to content](#main-content)Site messaging[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faffirm%2Fsite-messaging)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faffirm%2Fsite-messaging)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)[Affirm](/docs/payments/affirm)# Display Affirm messagingDeprecated

Increase conversion by informing customers that you offer Affirm ahead of checkout.CautionThe content in this topic refers to a Legacy feature. We recommend that you use the Payment Method Messaging Element to dynamically show your customers relevant buy now, pay later payment options for a given purchase. Stripe continues to maintain continuity for the affirmMessage Element, but has halted new feature development.

Let your customers know you accept payments with Affirm by including the Affirm messaging Element on your site. We suggest adding the messaging Element to your product, cart, and payment pages. The Affirm messaging Element takes care of:

- Calculating and displaying the installments amount
- Displaying the Affirm information modal

The Making of Prince of Persia: Journals 1985-1993Jordan Mechner$50## Include the Element

CautionAffirm’s minimum transaction amount is 50 USD or 50 CAD. The promotional message isn’t rendered if the amount parameter is set to a number less than 50 USD or 50 CAD.

HTML + JSReactUse Stripe Elements to include the affirmMessage Element on your site.

If you haven’t already, include the Stripe.js script on your page by adding it to the head of your HTML file:

`<script src="https://js.stripe.com/v3/"></script>`Create a placeholder element on your page where you want to mount the messaging Element:

`<div id="affirm-message"></div>`On your product, cart, and payment pages, include the following code to create an instance of Stripe.js and mount the messaging Element:

`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const elements = stripe.elements();

const options = {
  amount: 5000, // $50.00 USD
  currency: 'USD'
};

const affirmMessageElement =
  elements.create('affirmMessage', options);

affirmMessageElement.mount('#affirm-message');`## Customize the message

There are many options available to customize the appearance and contents of the messaging Element. See the API reference for the full list of options.

### Logo color

Use the logoColor option to choose between the following styles:

primaryblackwhite![](https://b.stripecdn.com/docs-statics-srv/assets/8a710e77e5d037fe3dd3417b5a889872.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/56a640c0ceb1a427eef9db8d2a32ebf4.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/ba4bb7fd9fb7c8031d8ae1dd9b096626.png)

### Style with CSS

Additional configuration options allow you to use CSS to style the messaging to better fit the look and feel of your site. You can customize the fontColor, fontSize, and textAlign of the messaging:

Code Example`const options = {
  amount: 5000,
  currency: 'USD',
  fontColor: '#5B63FF',
  logoColor: 'black',
  fontSize: '16px',
  textAlign: 'center',
};

const affirmMessageElement = elements.create('affirmMessage', options);`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Include the Element](#include-the-element)[Customize the message](#customize-the-message)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
# Payment Method Messaging Element

The Payment Method Messaging Element is a UI component for informing a customer about available buy-now-pay-later plans. It automatically determines the available plans and conditions, generates a localized description, and displays it in your form’s theme.

The Payment Method Messaging Element for Klarna in the UK is currently disabled as we update it to adhere to the UK Financial Promotion rules.

[UK Financial Promotion](https://docs.klarna.com/marketing/solutions/grab-and-go/gb/Klarna-Financial-Promotion-Rules/Klarna-Financial-Promotion-Rules/)

Apple Pay Later is available on Apple devices and browsers.

## Create and mount the Payment Method Messaging Element

Use Stripe Elements to include the Payment Method Messaging Element on your site.

[Payment Method Messaging](/js/elements_object/create_element?type=paymentMethodMessaging)

- Add the Stripe.js script on your page by adding it to the head of your HTML file:<script src="https://js.stripe.com/v3/"></script>

Add the Stripe.js script on your page by adding it to the head of your HTML file:

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

- Create a placeholder element in your page where you want to mount the Payment Method Messaging Element:<div id="payment-method-messaging-element"></div>

Create a placeholder element in your page where you want to mount the Payment Method Messaging Element:

- On your product, cart, and payment pages, include the following code to create an instance of Stripe.js (with locale) and mount the Payment Method Messaging Element:// Set your publishable key. Remember to change this to your live publishable key in production!
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
PaymentMessageElement.mount('#payment-method-messaging-element');

On your product, cart, and payment pages, include the following code to create an instance of Stripe.js (with locale) and mount the Payment Method Messaging Element:

[with locale](/js/appendix/supported_locales)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

If your integration requires you to list payment methods manually, see Customize payment methods.

[Customize payment methods](#customize-payment-methods)

## Dynamic display

The element dynamically displays payment plans that the customer is eligible for. These depend on the customer’s location and currency. They also depend on the amount of the payment, as in this example:

When available, the interest-bearing loan payment plans are shown on a separate line from the pay-in-x plans, which might increase the space needed for the element.

## Customize Payment Methods

If you use Dynamic payment methods, the Payment Method Messaging Element automatically pulls your payment method preferences from the Stripe Dashboard to dynamically show the most relevant payment methods to your customers. Alternatively, you can list payment methods manually using paymentMethodTypes. The Payment Method Messaging Element still only displays plans that the customer is eligible for based on their location, the currency, and the amount of the payment.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

## Info modal

When the customer selects the info icon (ⓘ), the Payment Method Messaging Element displays a modal with details about buy now, pay later payment plans.

A preview of the info modal

The modal includes:

- A step-by-step overview of how to use a buy now, pay later payment method

- A summary of terms for each available payment plan

- A link to the full terms for each available payment plan

## Supported plans

The Payment Method Messaging Element supports these payment methods and payment plans:

- Pay in 3

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

Messaging does not render if the countryCode and currency combination passed has no eligible payment plans.

## Appearance

Use the Appearance API to customize the font and logo of your messaging. You can select a theme as in the example below.

[Appearance API](/elements/appearance-api)

[theme](/elements/appearance-api?platform=web#theme)

Use variables for additional customization.

[variables](/elements/appearance-api#variables)

The Payment Method Messaging Element is a tool that allows you to message various buy now, pay later payment options to your customers. You’re responsible for compliance with applicable laws, rules, and regulations regarding the promotion of buy now, pay later payment options.

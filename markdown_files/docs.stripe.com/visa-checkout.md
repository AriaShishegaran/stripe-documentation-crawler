htmlStripe payments with Visa Checkout | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fvisa-checkout)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fvisa-checkout)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Stripe payments with Visa CheckoutDeprecated

Accept payments via Visa Checkout in your existing Stripe integration.WarningVisa terminated support for Visa Checkout in favor of Secure Remote Commerce, which delivers unified online checkout supporting multiple of card brands. Stripe doesn’t support new Visa Checkout integrations and existing Visa Checkout integrations must migrate to Secure Remote Commerce as soon as possible.

### Visa Checkout guidelines

Before implementing, please refer to the Visa Checkout terms of service and user interface guidelines.

Visa Checkout is a third-party service that stores payment and shipping information for its users in order to streamline the checkout process. Instead of entering payment information on your checkout page, users can click the Visa Checkout button instead. Your Stripe integration receives a unique ID that it can use to create a charge against the payment information stored in the user’s Visa Checkout account.

## Integrating the Visa Checkout button

To get started, generate your Visa Checkout API key in the Dashboard. There are two keys, a sandbox key that you can use in test mode, and a production key that works in live mode.

SandboxProductionTo use Visa Checkout on your website, add the following script tag to the end of your document’s body tag:

`<script type="text/javascript" src="https://sandbox-assets.secure.checkout.visa.com/checkout-widget/resources/js/integration/v1/sdk.js"></script>`To display the Visa Checkout button, use the following image:

`<img alt="Visa Checkout" class="v-button" role="button" src="https://sandbox.secure.checkout.visa.com/wallet-services-web/xo/button.png">`To initialize the button, add an onVisaCheckoutReady function that invokes V.init:

`function onVisaCheckoutReady() {
  V.init({
    apikey: '{{VISA_CHECKOUT_ID}}',
    paymentRequest:{
      subtotal: '10.00',
      currencyCode: 'USD'
    },
    settings: {
      displayName: 'My Website'
    }
  });
}`The Visa Checkout JavaScript SDK automatically invokes the onVisaCheckoutReady function when it finishes loading. The paymentRequest property accepted by V.init requires the following parameters:

ParameterDescription`subtotal`The amount of the transaction, expressed in decimal format`currencyCode`The currency in which to perform the transactionBy default, American Express, MasterCard, Visa, and Discover card brands are accepted, all shipping and billing countries are also enabled.

For more details about the V.init function and the parameters that it accepts, refer to Visa’s documentation. There are optional paymentRequest properties that support a range of other features, including promotions, discounts, and taxes. There are also optional settings properties that allow you to control the shipping information options.

## Completing the payment

When the user clicks the Visa Checkout button on your checkout page, it opens a lightbox where they can select an existing payment method from their account or input a new one. When the user completes the process, the Visa Checkout JavaScript SDK in the browser emits a payment.success event with a unique ID that your application can use to complete the transaction.

The following code shows how to handle the payment.success event and confirm the PaymentIntent you created at the beginning of the checkout flow. See accept a payment to learn how to manage your checkout flow using Payment Intents.

`// PaymentIntent client secret passed from server-side.
// See: https://stripe.com/docs/payments/accept-a-payment?platform=web
// for more information on how to do this.
const clientSecret = '{{CLIENT_SECRET}}';

V.on('payment.success', async (payment) => {
  const intent = await stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: {
        visa_checkout: {
          callid: payment.callid,
        },
      },
    },
  });
  // Perform logic for payment completion here
});`## Testing Visa Checkout

To test your integration against Visa Checkout’s sandbox, create a new Visa Checkout user account during the checkout process on your website. Configure the account to use the test card number 4242 4242 4242 4242, a random three-digit CVC number, and any expiration date in the future. Complete the checkout process as normal. If everything works correctly, Visa Checkout redirects you back to your application, which creates the charge as expected.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integrating the Visa Checkout button](#integrating)[Completing the payment](#completing-the-payment)[Testing Visa Checkout](#testing-visa-checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
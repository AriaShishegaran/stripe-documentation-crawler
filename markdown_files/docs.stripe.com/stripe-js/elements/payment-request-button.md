htmlPayment Request Button | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-js%2Felements%2Fpayment-request-button)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-js%2Felements%2Fpayment-request-button)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Payment Request Button

Collect payment and address information from customers who use Apple Pay, Google Pay, or Link.CautionEither your browser does not support the Payment Request API, or you do not have a saved payment method. To try out the Payment Request Button live demo, switch to one of the[supported browsers](#html-js-testing)below, and make sure you have a saved payment method.HTML + JSReactThe Payment Request Button Element dynamically displays wallet options during checkout, giving you a single integration for Apple Pay, Google Pay, and Link. Alternatively, you can use the Express Checkout Element to offer multiple one-click payment buttons to your customers. Compare the Express Checkout Element and Payment Request Button.

![Apple Pay, Google Pay, and Link](https://b.stripecdn.com/docs-statics-srv/assets/payment-request-buttons.6a7ec08882965cea94413852e053bbb5.png)

Apple Pay, Google Pay, and Link

Customers see Apple Pay or Google Pay if they enabled them on their device, and depending on the browser they use. If Link appears, it could be because customers:

- Don’t have Apple Pay or Google Pay enabled on their device.
- Use Chrome with active, authenticated Link sessions.

Browser + WalletPayment ButtonSafari + Apple Pay enabledApple PayChrome + Link authenticatedLinkChrome + Google Pay enabled and Link not authenticatedGoogle PayChrome on iOS 16 + Apple Pay and Google Pay enabledApple PayAny browser + No active Apple Pay or Google PayLink[Prerequisites](#html-js-prerequisites)Before you start, you need to:

- Review the requirements for each payment button type:

  - Apple Pay and Google Pay don’t display for IP addresses in India, so plan your integration testing accordingly.
  - Apple Pay requires macOS 10.12.1+ or iOS 10.1+.
  - Compatible devices automatically support Google Pay.


- Register and verify your domain in both test mode and live mode.


- Add a payment method to your browser. For example, you can save a card in Chrome, add a card to your Google Pay account, or add a card to your Wallet for Safari.


- Serve your application over HTTPS. This is a requirement both in development and production. One way to get started is to use a service such as ngrok.



[Set up Stripe ElementsClient-side](#html-js-set-up-stripe-elements)Elements is available as part of Stripe.js. Include this in your page and create a container to use for the paymentRequestButton Element:

`<script src="https://js.stripe.com/v3/"></script>
<div id="payment-request-button">
  <!-- A Stripe Element will be inserted here. -->
</div>`Your Stripe publishable API key is also required as it identifies your website to Stripe:

client.js`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  apiVersion: "2024-04-10",
});`[Create a paymentRequest instanceClient-side](#html-js-create-payment-request-instance)Create an instance of stripe.paymentRequest with all required options.

client.js`const paymentRequest = stripe.paymentRequest({
  country: 'US',
  currency: 'usd',
  total: {
    label: 'Demo total',
    amount: 1099,
  },
  requestPayerName: true,
  requestPayerEmail: true,
});`NoteUse the requestPayerName parameter to collect the payer’s billing address for Apple Pay and Link. You can use the billing address to perform address verification and block fraudulent payments. All other payment methods automatically collect the billing address when one is available.

[Create and mount the paymentRequestButtonClient-side](#html-js-mount-element)Create the paymentRequestButton Element and check to make sure that your customer has an active payment method using canMakePayment(). If they do, mount the Element to the container to display the Payment Request button. If they don’t, you can’t mount the Element, and we recommend that you show a traditional checkout form instead.

NoteIf you accept Apple Pay with the Payment Request Button, you must offer Apple Pay as the primary payment option on your website per Apple guidelines. Internally, the Payment Request Button uses the Apple Pay canMakePaymentWithActiveCard API.

client.js`const elements = stripe.elements();
const prButton = elements.create('paymentRequestButton', {
  paymentRequest,
});

(async () => {
  // Check the availability of the Payment Request API first.
  const result = await paymentRequest.canMakePayment();
  if (result) {
    prButton.mount('#payment-request-button');
  } else {
    document.getElementById('payment-request-button').style.display = 'none';
  }
})();`[Create a PaymentIntentServer-side](#html-js-create-payment)Stripe uses a PaymentIntent object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

![](https://b.stripecdn.com/docs-statics-srv/assets/accept-a-payment-web.d86e3fb67cf265d70d77d77244464e0a.png)

Create a PaymentIntent on your server with an amount and currency. Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=card`Included in the returned PaymentIntent is a client secret, which you use to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client to use in the next step.

[Complete the paymentClient-side](#html-js-complete-payment)Listen to the paymentmethod event to receive a PaymentMethod object. Pass the PaymentMethod ID and the PaymentIntent’s client secret to stripe.confirmCardPayment to complete the payment.

client.js`paymentRequest.on('paymentmethod', async (ev) => {
  // Confirm the PaymentIntent without handling potential next actions (yet).
  const {paymentIntent, error: confirmError} = await stripe.confirmCardPayment(
    clientSecret,
    {payment_method: ev.paymentMethod.id},
    {handleActions: false}
  );

  if (confirmError) {
    // Report to the browser that the payment failed, prompting it to
    // re-show the payment interface, or show an error message and close
    // the payment interface.
    ev.complete('fail');
  } else {
    // Report to the browser that the confirmation was successful, prompting
    // it to close the browser payment method collection interface.
    ev.complete('success');
    // Check if the PaymentIntent requires any actions and, if so, let Stripe.js
    // handle the flow. If using an API version older than "2019-02-11"
    // instead check for: `paymentIntent.status === "requires_source_action"`.
    if (paymentIntent.status === "requires_action") {
      // Let Stripe.js handle the rest of the payment flow.
      const {error} = await stripe.confirmCardPayment(clientSecret);
      if (error) {
        // The payment failed -- ask your customer for a new payment method.
      } else {
        // The payment has succeeded -- show a success message to your customer.
      }
    } else {
      // The payment has succeeded -- show a success message to your customer.
    }
  }
});`CautionThe customer can dismiss the payment interface in some browsers even after they authorize the payment. This means that you might receive a cancel event on your PaymentRequest object after receiving a paymentmethod event. If you use the cancel event as a hook for canceling the customer’s order, make sure you also refund the payment that you just created.

[Test your integration](#html-js-testing)To test your integration, you must use HTTPS and a supported browser. If you use the paymentRequestButton Element within an iframe, the iframe must have the allow attribute set to equal “payment *”.

Regional TestingIndiaStripe Elements doesn’t support Google Pay or Apple Pay for Stripe accounts and customers in India. Therefore, you can’t test your Google Pay or Apple Pay integration if the tester’s IP address is in India, even if the Stripe account is based outside India.

In addition, each payment method and browser has specific requirements:

Apple PayGoogle PayLinkSafari![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Safari on Mac running macOS Sierra or later
- A compatible device with a card in its Wallet paired to your Mac with Handoff, or a Mac with TouchID. You can find instructions on the[Apple Support site](https://support.apple.com/en-us/HT204681).
- A[verified domain with Apple Pay](/payments/payment-methods/pmd-registration).
- When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying`allow="payment"`attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

Mobile Safari![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Mobile Safari on iOS 10.1 or later
- A card in your Wallet (go toSettings>Wallet & Apple Pay).
- A[verified domain with Apple Pay](/payments/payment-methods/pmd-registration).
- When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying`allow="payment"`attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

As of iOS 16, Apple Pay might work in some non-Safari mobile browsers with a card saved in your Wallet.

## Collect shipping information

To collect shipping information, begin by including requestShipping: true when creating the payment request.

You can also provide an array of shippingOptions at this point, if your shipping options don’t depend on the customer’s address.

`const paymentRequest = stripe.paymentRequest({
  country: 'US',
  currency: 'usd',
  total: {
    label: 'Demo total',
    amount: 1099,
  },

  requestShipping: true,
  // `shippingOptions` is optional at this point:
  shippingOptions: [
    // The first shipping option in this list appears as the default
    // option in the browser payment interface.
    {
      id: 'free-shipping',
      label: 'Free shipping',
      detail: 'Arrives in 5 to 7 days',
      amount: 0,
    },
  ],
});`Next, listen to the shippingaddresschange event to detect when a customer selects a shipping address. Use the address to fetch valid shipping options from your server, update the total, or perform other business logic. You can anonymize the address data on the shippingaddresschange event in the browser to not reveal sensitive information that isn’t necessary for shipping cost calculation.

The customer must provide valid shippingOptions at this point to proceed in the flow.

`paymentRequest.on('shippingaddresschange', async (ev) => {
  if (ev.shippingAddress.country !== 'US') {
    ev.updateWith({status: 'invalid_shipping_address'});
  } else {
    // Perform server-side request to fetch shipping options
    const response = await fetch('/calculateShipping', {
      data: JSON.stringify({
        shippingAddress: ev.shippingAddress
      })
    });
    const result = await response.json();

    ev.updateWith({
      status: 'success',
      shippingOptions: result.supportedShippingOptions,
    });
  }
});`## Display line items

Use displayItems to display PaymentItem objects and show the price breakdown in the browser’s payment interface.

`const paymentRequest = stripe.paymentRequest({
  country: 'US',
  currency: 'usd',
  total: {
    label: 'Demo total',
    amount: 2000,
  },

  displayItems: [
    {
      label: 'Sample item',
      amount: 1000,
    },
    {
      label: 'Shipping cost',
      amount: 1000,
    }
  ],
});`## Style the button

Use the following parameters to customize the Element:

`elements.create('paymentRequestButton', {
  paymentRequest,
  style: {
    paymentRequestButton: {
      type: 'default',
      // One of 'default', 'book', 'buy', or 'donate'
      // Defaults to 'default'

      theme: 'dark',
      // One of 'dark', 'light', or 'light-outline'
      // Defaults to 'dark'

      height: '64px',
      // Defaults to '40px'. The width is always '100%'.
    },
  },
});`### Using your own button

If you want to design your own button instead of using the paymentRequestButton Element, you can show your custom button based on the result of paymentRequest.canMakePayment(). Then, use paymentRequest.show() to display the browser interface when your button is clicked.

When building your own button, follow the Apple Pay Human Interface Guidelines and Google Pay Brand Guidelines.

CautionLink isn’t supported in custom button configurations and won’t display for the customer if you decide to use one.

## Add an Apple Pay merchant token for merchant initiated transactions

Set up your Payment Request Button to request an Apple Pay MPAN to facilitate merchant initiated transactions (MIT) for recurring, auto-load, or deferred payments.

1. Create an instance of the[Payment Request](#html-js-create-payment-request-instance).
2. Pass the`applePay`object relevant to your MPAN use case (choose from the drop-down to see use case code samples).
3. Include relevant parameters for your use case.

MPAN use case:Recurring paymentsAutomatic reloadDeferred paymentcheckout.js`const paymentRequest = stripe.paymentRequest({
  applePay: {
    recurringPaymentRequest: {
      paymentDescription: 'My subscription',
      managementURL: 'https://example.com/billing',
      regularBilling: {
        amount: 2500,
        label: 'Monthly subscription fee',
        recurringPaymentIntervalUnit: 'month',
        recurringPaymentIntervalCount: 1,
      },
    },
  },
  // Other options
});`## Use the Payment Request Button with Stripe Connect

Connect platforms that either create direct charges or add the token to a Customer on the connected account must take additional steps when using the Payment Request Button.

1. On your frontend, before creating the`PaymentRequest`instance, set the`stripeAccount`option on the Stripeinstance:

`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  apiVersion: "2024-04-10",
  stripeAccount: 'CONNECTED_STRIPE_ACCOUNT_ID',
});`1. [Register all domains](/payments/payment-methods/pmd-registration?dashboard-or-api=api#register-your-domain-while-using-connect)where you plan to show the Payment Request Button.

## Link for the Payment Request Button

When new customers come to your site, they can use Link in the Payment Request Button to pay with their saved payment details. With Link, they don’t need to manually enter their payment information. Link requires domain registration.

[Disclose Stripe to your customers](#disclose-cookies)Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our privacy center.

## See also

- [Learn about Apple Pay](/apple-pay)
- [Learn about Google Pay](/google-pay)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prerequisites](#html-js-prerequisites)[Set up Stripe Elements](#html-js-set-up-stripe-elements)[Create a paymentRequest instance](#html-js-create-payment-request-instance)[Create and mount the paymentRequestButton](#html-js-mount-element)[Create a PaymentIntent](#html-js-create-payment)[Complete the payment](#html-js-complete-payment)[Test your integration](#html-js-testing)[Collect shipping information](#html-js-collecting-shipping-info)[Display line items](#html-js-display-line-items)[Style the button](#html-js-styling-the-element)[Add an Apple Pay merchant token for merchant initiated transactions](#add-an-apple-pay-merchant-token-for-merchant-initiated-transactions)[Use the Payment Request Button with Stripe Connect](#html-js-using-with-connect)[Link for the Payment Request Button](#link-prb)[Disclose Stripe to your customers](#disclose-cookies)[See also](#see-also)Products Used[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
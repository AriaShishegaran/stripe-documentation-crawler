# Payment Request Button

[supported browsers](#html-js-testing)

The Payment Request Button Element dynamically displays wallet options during checkout, giving you a single integration for Apple Pay, Google Pay, and Link. Alternatively, you can use the Express Checkout Element to offer multiple one-click payment buttons to your customers. Compare the Express Checkout Element and Payment Request Button.

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[Link](#link-prb)

[Express Checkout Element](/elements/express-checkout-element)

[Compare](/elements/express-checkout-element/comparison)

Apple Pay, Google Pay, and Link

Customers see Apple Pay or Google Pay if they enabled them on their device, and depending on the browser they use. If Link appears, it could be because customers:

- Don’t have Apple Pay or Google Pay enabled on their device.

- Use Chrome with active, authenticated Link sessions.

[Prerequisites](#html-js-prerequisites)

## Prerequisites

Before you start, you need to:

- Review the requirements for each payment button type:Apple Pay and Google Pay don’t display for IP addresses in India, so plan your integration testing accordingly.Apple Pay requires macOS 10.12.1+ or iOS 10.1+.Compatible devices automatically support Google Pay.

Review the requirements for each payment button type:

- Apple Pay and Google Pay don’t display for IP addresses in India, so plan your integration testing accordingly.

- Apple Pay requires macOS 10.12.1+ or iOS 10.1+.

- Compatible devices automatically support Google Pay.

- Register and verify your domain in both test mode and live mode.

Register and verify your domain in both test mode and live mode.

[Register and verify your domain](/payments/payment-methods/pmd-registration)

- Add a payment method to your browser. For example, you can save a card in Chrome, add a card to your Google Pay account, or add a card to your Wallet for Safari.

Add a payment method to your browser. For example, you can save a card in Chrome, add a card to your Google Pay account, or add a card to your Wallet for Safari.

[Add a payment method to your browser.](#html-js-testing)

- Serve your application over HTTPS. This is a requirement both in development and production. One way to get started is to use a service such as ngrok.

Serve your application over HTTPS. This is a requirement both in development and production. One way to get started is to use a service such as ngrok.

[ngrok](https://ngrok.com)

[Set up Stripe ElementsClient-side](#html-js-set-up-stripe-elements)

## Set up Stripe ElementsClient-side

Elements is available as part of Stripe.js. Include this in your page and create a container to use for the paymentRequestButton Element:

[Stripe.js](/payments/elements)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Your Stripe publishable API key is also required as it identifies your website to Stripe:

[API key](/keys)

[Create a paymentRequest instanceClient-side](#html-js-create-payment-request-instance)

## Create a paymentRequest instanceClient-side

Create an instance of stripe.paymentRequest with all required options.

[stripe.paymentRequest](/js#stripe-payment-request)

Use the requestPayerName parameter to collect the payer’s billing address for Apple Pay and Link. You can use the billing address to perform address verification and block fraudulent payments. All other payment methods automatically collect the billing address when one is available.

[Create and mount the paymentRequestButtonClient-side](#html-js-mount-element)

## Create and mount the paymentRequestButtonClient-side

Create the paymentRequestButton Element and check to make sure that your customer has an active payment method using canMakePayment(). If they do, mount the Element to the container to display the Payment Request button. If they don’t, you can’t mount the Element, and we recommend that you show a traditional checkout form instead.

If you accept Apple Pay with the Payment Request Button, you must offer Apple Pay as the primary payment option on your website per Apple guidelines. Internally, the Payment Request Button uses the Apple Pay canMakePaymentWithActiveCard API.

[Apple guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/#:~:text=canMakePaymentWithActiveCard)

[Create a PaymentIntentServer-side](#html-js-create-payment)

## Create a PaymentIntentServer-side

Stripe uses a PaymentIntent object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

[PaymentIntent](/api/payment_intents)

Create a PaymentIntent on your server with an amount and currency. Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

Included in the returned PaymentIntent is a client secret, which you use to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client to use in the next step.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[Complete the paymentClient-side](#html-js-complete-payment)

## Complete the paymentClient-side

Listen to the paymentmethod event to receive a PaymentMethod object. Pass the PaymentMethod ID and the PaymentIntent’s client secret to stripe.confirmCardPayment to complete the payment.

[PaymentMethod](/api/payment_methods)

[stripe.confirmCardPayment](/js#stripe-confirm-card-payment)

The customer can dismiss the payment interface in some browsers even after they authorize the payment. This means that you might receive a cancel event on your PaymentRequest object after receiving a paymentmethod event. If you use the cancel event as a hook for canceling the customer’s order, make sure you also refund the payment that you just created.

[cancel event](/js#payment-request-on)

[Test your integration](#html-js-testing)

## Test your integration

To test your integration, you must use HTTPS and a supported browser. If you use the paymentRequestButton Element within an iframe, the iframe must have the allow attribute set to equal “payment *”.

[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)

Stripe Elements doesn’t support Google Pay or Apple Pay for Stripe accounts and customers in India. Therefore, you can’t test your Google Pay or Apple Pay integration if the tester’s IP address is in India, even if the Stripe account is based outside India.

In addition, each payment method and browser has specific requirements:

- Safari on Mac running macOS Sierra or later

- A compatible device with a card in its Wallet paired to your Mac with Handoff, or a Mac with TouchID. You can find instructions on the Apple Support site.

[Apple Support site](https://support.apple.com/en-us/HT204681)

- A verified domain with Apple Pay.

[verified domain with Apple Pay](/payments/payment-methods/pmd-registration)

- When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying allow="payment" attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

- Mobile Safari on iOS 10.1 or later

- A card in your Wallet (go to Settings > Wallet & Apple Pay).

- A verified domain with Apple Pay.

[verified domain with Apple Pay](/payments/payment-methods/pmd-registration)

- When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying allow="payment" attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

As of iOS 16, Apple Pay might work in some non-Safari mobile browsers with a card saved in your Wallet.

## Collect shipping information

To collect shipping information, begin by including requestShipping: true when creating the payment request.

You can also provide an array of shippingOptions at this point, if your shipping options don’t depend on the customer’s address.

Next, listen to the shippingaddresschange event to detect when a customer selects a shipping address. Use the address to fetch valid shipping options from your server, update the total, or perform other business logic. You can anonymize the address data on the shippingaddresschange event in the browser to not reveal sensitive information that isn’t necessary for shipping cost calculation.

The customer must provide valid shippingOptions at this point to proceed in the flow.

## Display line items

Use displayItems to display PaymentItem objects and show the price breakdown in the browser’s payment interface.

[displayItems](/js/payment_request/create#stripe_payment_request-options-displayItems)

[PaymentItem](/js/appendix/payment_item_object)

## Style the button

Use the following parameters to customize the Element:

If you want to design your own button instead of using the paymentRequestButton Element, you can show your custom button based on the result of paymentRequest.canMakePayment(). Then, use paymentRequest.show() to display the browser interface when your button is clicked.

[paymentRequest.canMakePayment()](/js#payment-request-can-make-payment)

[paymentRequest.show()](/js#payment-request-show)

When building your own button, follow the Apple Pay Human Interface Guidelines and Google Pay Brand Guidelines.

[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)

[Brand Guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines)

Link isn’t supported in custom button configurations and won’t display for the customer if you decide to use one.

## Add an Apple Pay merchant token for merchant initiated transactions

Set up your Payment Request Button to request an Apple Pay MPAN to facilitate merchant initiated transactions (MIT) for recurring, auto-load, or deferred payments.

[Apple Pay MPAN](/apple-pay/merchant-tokens)

- Create an instance of the Payment Request.

[Payment Request](#html-js-create-payment-request-instance)

- Pass the applePay object relevant to your MPAN use case (choose from the drop-down to see use case code samples).

- Include relevant parameters for your use case.

[https://example.com/billing](https://example.com/billing)

## Use the Payment Request Button with Stripe Connect

Connect platforms that either create direct charges or add the token to a Customer on the connected account must take additional steps when using the Payment Request Button.

[Connect](/connect)

- On your frontend, before creating the PaymentRequest instance, set the stripeAccount option on the Stripe instance:

- Register all domains where you plan to show the Payment Request Button.

[Register all domains](/payments/payment-methods/pmd-registration?dashboard-or-api=api#register-your-domain-while-using-connect)

## Link for the Payment Request Button

When new customers come to your site, they can use Link in the Payment Request Button to pay with their saved payment details. With Link, they don’t need to manually enter their payment information. Link requires domain registration.

[Link in the Payment Request Button](/payments/link/payment-request-button-link)

[Link](/payments/link/what-is-link)

[domain registration](/payments/payment-methods/pmd-registration)

[Disclose Stripe to your customers](#disclose-cookies)

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our privacy center.

[privacy center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)

## See also

- Learn about Apple Pay

[Learn about Apple Pay](/apple-pay)

- Learn about Google Pay

[Learn about Google Pay](/google-pay)

# Secure Remote Commerce program guide

Secure Remote Commerce (SRC) is an easy and secure way to pay online and is powered by the global payments industry to protect users’ payment information. Users can add cards from Visa, Mastercard, American Express, and Discover to enable Click to Pay simply and securely. Secure Remote Commerce delivers an enhanced online checkout experience and supports all network brands participating in SRC.

[Secure Remote Commerce (SRC)](https://www.mastercard.us/en-us/merchants/grow-your-business/find-solutions-by-need/improve-checkout/secure-digital-checkout.html)

Secure Remote Commerce is only available in the US at this time.

## Integrating the Secure Remote Commerce button

If you are currently using Visa Checkout or Masterpass to accept payments, we recommend migrating these integrations to SRC, which delivers a unified checkout experience that supports a number of card brands.

[Visa Checkout](/visa-checkout)

[Masterpass](/masterpass)

To get started, generate your Masterpass Checkout ID in the Dashboard and configure your sandbox and production callback URLs. Note that Mastercard is offering SRC as an update to their Masterpass service, so you will see references to Masterpass within the documentation and code.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

To use SRC on your website, add the following script tag to your HTML document:

[https://sandbox.src.mastercard.com/srci/integration/merchant.js?locale=en_us&checkoutid={checkoutId}](https://sandbox.src.mastercard.com/srci/integration/merchant.js?locale=en_us&checkoutid={checkoutId})

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

To display the Masterpass button, use one of the following images:

For a button with black Masterpass text

[https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}](https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId})

For a button with white Masterpass text

[https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}](https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId})

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

Attach a click handler to the image and use it to invoke the masterpass.checkout function with the desired parameters:

The masterpass.checkout function requires the following parameters:

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

For more details about the masterpass.checkout function and the parameters that it accepts, refer to Mastercard’s documentation.

[Mastercard’s documentation](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1)

## Completing the payment

When the user clicks the Masterpass button on your checkout page, it takes them to the Masterpass website where they can select an existing payment method from their account or input a new one. When the user completes the process, Masterpass redirects them to the callback URL that you configured when activating Masterpass, or to the specified callback URL when invoking masterpass.checkout function. It appends an oauth_verifier URL query parameter that your application can use to complete the transaction.

In the route handler for the redirect destination, extract the URL query parameter and use it to confirm the PaymentIntent that you have created at the beginning of the checkout flow. See accept a payment to learn how to manage your checkout flow using Payment Intents.

[confirm](/api/payment_intents/confirm)

[PaymentIntent](/api/payment_intents)

[accept a payment](/payments/accept-a-payment)

The following code example demonstrates how to confirm a PaymentIntent with SRC in Node.js with the Express framework:

## Testing Secure Remote Commerce

To test your SRC integration against Mastercard’s sandbox, create a new SRC user account during the checkout process on your website. Configure the account to use one of the test cards from the Masterpass documentation. Complete the checkout process as normal, selecting the test card as your payment method. If everything works correctly, Mastercard redirects you back to your application, which creates the charge as expected.

[test cards](https://developer.mastercard.com/masterpass/documentation/migration/masterpass_to_src_migration/#mastercard-test-cards)

The SRC integration only works correctly when included on an http or https page. Serving from the filesystem is not supported, even during testing.

# Masterpass guideDeprecated

Mastercard plans to deprecate Masterpass in favor of Secure Remote Commerce, which delivers unified online checkout supporting a number of card brands. Stripe doesn’t support new Masterpass integrations and existing integrations must migrate to Secure Remote Commerce as soon as possible.

[Secure Remote Commerce](/secure-remote-commerce)

Before implementing, please refer to the implementation requirements. By using Masterpass through Stripe, you agree to the Masterpass Operating Rules.

[implementation requirements](https://developer.mastercard.com)

[Operating Rules](https://masterpass.com/assets/pdf/masterpassoperatingrules.pdf)

Masterpass is a third-party service that stores payment and shipping information for its users in order to streamline the checkout process. Instead of entering payment information on your checkout page, users can click the Masterpass button instead. Your Stripe integration receives a unique transaction ID that it can use to create a charge against the payment information stored in the user’s Masterpass account.

## Integrating the Masterpass button

To get started, generate your Masterpass Checkout ID in the Dashboard and configure your sandbox and production callback URLs.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

To use Masterpass on your website, add the following script tag to your HTML document:

[https://sandbox.masterpass.com/integration/merchant.js](https://sandbox.masterpass.com/integration/merchant.js)

To display the Masterpass button, use the following image:

[https://static.masterpass.com/dyn/img/btn/global/mp_chk_btn_147x034px.svg](https://static.masterpass.com/dyn/img/btn/global/mp_chk_btn_147x034px.svg)

Attach a click handler to the image and use it to invoke the masterpass.checkout function with the desired parameters:

The masterpass.checkout function requires the following parameters:

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

For more details about the masterpass.checkout function and the parameters that it accepts, refer to Mastercard’s documentation.

[refer](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1)

## Completing the payment

When the user clicks the Masterpass button on your checkout page, it takes them to the Masterpass website where they can select an existing payment method from their account or input a new one. When the user completes the process, Masterpass redirects them to the callback URL that you configured when activating Masterpass, or the specified callback URL when invoking masterpass.checkout function. It appends an oauth_verifier URL query parameter that your application can use to complete the transaction.

In the route handler for the redirect destination, extract the URL query parameter and use it to confirm the PaymentIntent that you have created at the beginning of the checkout flow. See accept a payment to learn how to manage your checkout flow using Payment Intents.

[confirm](/api/payment_intents/confirm)

[PaymentIntent](/api/payment_intents)

[accept a payment](/payments/accept-a-payment)

The following code example demonstrates how to confirm a PaymentIntent with Masterpass in Node.js with the Express framework:

Use the Masterpass sandbox environment in Stripe’s test mode, and the Masterpass production environment in Stripe’s live mode. When creating the source, be sure to use the same unique value for the cart_id property that you used on your checkout page.

## Testing Masterpass

To test your Masterpass integration against Mastercard’s sandbox, create a new Masterpass user account during the checkout process on your website. Configure the account to use one of the test cards from the Masterpass documentation. Complete the checkout process as normal, selecting the test card as your Masterpass payment method. If everything works correctly, Masterpass redirects you back to your application, which creates the charge as expected.

[test cards](https://developer.mastercard.com/page/masterpass-sandbox-testing-guidelines#new-web-experience)

# External payment methods

Use the Stripe Payment Element to display payment methods you’re already integrated with. Adding external payment methods simplifies your user interface by displaying all the payment methods you offer in the Stripe Payment Element. Integrating external payment methods requires additional integration work because external payment method transactions are processed and finalized outside of Stripe.

[Payment Element](/payments/payment-element)

When customers choose an external payment method, they’re redirected to a URL you configured for the external payment method. Learn about what you’re responsible for and the ongoing availability of external payment methods.

[what you’re responsible for and the ongoing availability of external payment methods](#external-payment-methods-disclaimer)

This guide adds an external payment method, Divido, using the HTML/JS example from the Payment Element quickstart.

[Payment Element quickstart](/payments/quickstart)

## Before you begin

- Create a Stripe account or sign in.

[Create a Stripe account](https://dashboard.stripe.com/register)

[sign in](https://dashboard.stripe.com/login)

- Follow the Payment Element quickstart to complete a payments integration.

[Payment Element quickstart](/payments/quickstart)

- For each external payment method you want to add, ensure you have completed the integration with each external payment method and confirmed that it is working in the region you want to enable them.

[Add external payment method types](#add-external-payment-method-types)

## Add external payment method types

In your checkout.js file, where you initialize Stripe Elements, specify the external payment methods you want to add to the Payment Element. This example adds Divido:

[initialize Stripe Elements](/payments/quickstart#init-elements)

[Handle payment method selection listener](#handle-external-payment-method-selection)

## Handle payment method selection listener

There are two ways to handle the redirect to the external payment method:

- Replace the action of the Stripe Pay now button to redirect to the external payment method.

- Replace the Stripe Pay now button with the external payment method provider’s button.

This listener replaces the action of the Stripe Pay now button to redirect the customer to the Divido checkout page where they can complete the transaction. In checkout.js, add the listener code after the paymentElement.mount call:

Update the handleSubmit function to redirect to the Divido checkout page:

[OptionalPosition external payment methods](#position-payment-methods)

## OptionalPosition external payment methods

[Test your integration](#testing)

## Test your integration

- Go through your checkout flow and verify that the Payment Element displays Divido. This example configures Divido in the second position after cards.Payment Element with Divido

Payment Element with Divido

- Choose the Divido payment method to verify messaging about the next step redirecting to Divido.

- Click Pay now to test your existing Divido integration. Verify that you are redirected to Divido to complete the transaction and any post-payment actions (for example, display a confirmation page, success message, or failure message) still work with your Divido integration.

## Dashboard considerations

PaymentIntents for transactions processed with an external payment method provider have an  incomplete status in the Stripe Dashboard. Stripe isn’t involved in external payment method transactions and can’t determine the status of these transactions.

[PaymentIntents](/api/payment_intents)

If you collect payment details before creating an Intent, you won’t see any incomplete transactions in the Stripe Dashboard for transactions that were processed with an external payment method provider.

[collect payment details before creating an Intent](/payments/accept-a-payment-deferred)

## External payment methods disclaimer

You can use the Stripe Payment Element to show some external payment methods that aren’t supported by Stripe but that you directly integrate with. When customers choose an external payment method, they’re redirected to a URL that you configure for the external payment method. You acknowledge that:

- External payment methods aren’t offered nor supported by Stripe. The operation and support of external payment methods is provided by the external payment method provider.

- You’re responsible for maintaining a direct integration with the external payment method provider.

- You need to maintain an agreement with the external payment method provider and are responsible for complying with your agreements with each external payment method provider.

- You’re responsible for obtaining all necessary rights to use the external payment method provider’s marks and logos within your checkout as described in these docs.

- Stripe isn’t responsible for the processing of any transactions with any external payment method provider including, for example, any charges, refunds, disputes, settlements or funds flows.

- You or the external payment method provider are responsible for the completion of the purchase flow after a customer has selected an external payment method, including, for example, the order confirmation and reconciliation of orders.

- You’re responsible for properly configuring the redirect URL for the external payment method.

- You must immediately remove any external payment methods in the event your agreements with any external payment method provider terminate or Stripe removes the availability of an external payment method.

- You’re only permitted to integrate with and present in the Payment Element the external payment methods listed in this guide.

- You’re solely responsible for making sure that buyers are redirected correctly to their chosen external payment method.

Stripe might at any time decide to remove the availability of any payment method as an external payment method. Stripe will notify you of any removal of an external payment method that you’re using, and you must immediately remove the external payment method in your code. Failure to do so will result in the external payment method not rendering to your customers.

## Available external payment methods

You can display the following external payment methods. You must use the corresponding external payment method type in your code.

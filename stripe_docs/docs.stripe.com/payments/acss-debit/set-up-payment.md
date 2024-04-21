# Save details for future payments with pre-authorized debit in Canada

You can use the Setup Intents API to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

[Setup Intents API](/payments/setup-intents)

- Saving payment methods to a wallet to streamline future purchases

- Collecting surcharges after fulfilling a service

- Starting a free trial for a subscription

[subscription](/billing/subscriptions/creating)

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It is possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so results in a delayed payment failure that takes up to five business days.

To avoid these failures, it is safest to set up PAD bank accounts in CAD unless you are confident your customer’s account accepts USD debits.

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create or retrieve a CustomerServer-side](#web-create-customer)

## Create or retrieve a CustomerServer-side

To reuse a bank account for future payments, it must be attached to a Customer.

[Customer](/api/customers)

You should create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

Create a new Customer or retrieve an existing Customer to associate with these payment details. Include the following code on your server to create a new Customer.

[Create a SetupIntentServer-side](#web-create-setup-intent)

## Create a SetupIntentServer-side

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

[SetupIntent](/api/setup_intents)

In order to use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see PAD Mandates). The Mandate object records this agreement and authorization.

[PAD Mandates](/payments/acss-debit#mandates)

[Mandate](/api/mandates)

Create a SetupIntent on your server with payment_method_types set to acss_debit and specify the Customer’s id. In order to define a payment schedule on the Mandate for this SetupIntent, also include the following parameters:

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

[id](/api/customers/object#customer_object-id)

[Mandate](/api/mandates)

[PAD Mandates](/payments/acss-debit#mandates)

[PAD Mandates](/payments/acss-debit#mandates)

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

[Collect payment method details and mandate acknowledgementClient-side](#web-collect-mandate-and-submit)

## Collect payment method details and mandate acknowledgementClient-side

When a customer clicks to pay with Canadian pre-authorized debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

[Stripe.js](/payments/elements)

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe.js with the following JavaScript on your checkout page.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Rather than sending the entire PaymentIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmAcssDebitSetup to collect bank account details and verification, confirm the mandate, and complete the setup when the user submits the form. Including the customer’s email address and the account holder’s name in the billing_details property of the payment_method parameter is required to create a PAD payment method.

[stripe.confirmAcssDebitSetup](/js/setup_intents/confirm_acss_debit_setup)

Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

stripe.confirmAcssDebitSetup may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

[SetupIntent](/api/setup_intents/object)

[Verifying bank accounts with micro-deposits](#web-verify-with-microdeposits)

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to send custom notifications if you prefer.

[send custom notifications](/payments/acss-debit#mandate-and-debit-notification-emails)

Mandate confirmation emails will not be sent to the customer’s email address when testing the integration.

If the customer chooses to close the modal without completing the verification flow, Stripe.js returns the following error:

[Verify bank account with micro-depositsClient-side](#web-verify-with-microdeposits)

## Verify bank account with micro-depositsClient-side

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In this case, Stripe automatically sends two micro-deposits to the customer’s bank account. These deposits take one to two business days to appear on the customer’s online statement and have statement descriptors that include ACCTVERIFY.

The result of the stripe.confirmAcssDebitSetup method call is a SetupIntent in the requires_action state. The SetupIntent contains a next_action field that contains some useful information for completing the verification.

Stripe notifies your customer at the billing email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

[billing email](/api/payment_methods/object#payment_method_object-billing_details-email)

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits are not verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

If you choose to send custom email notifications, you have to email your customer instead. To do this, you can use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.

[custom email notifications](/payments/acss-debit#mandate-and-debit-notification-emails)

If you are sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using Stripe.js.

[Stripe.js](/js/payment_intents/verify_microdeposits_for_payment)

When the bank account is successfully verified, Stripe returns the SetupIntent object, with a status of succeeded, and sends a setup_intent.succeeded webhook event.

[SetupIntent object](/api/setup_intents/object)

Verification can fail for several reasons. The failure may happen synchronously as a direct error response, or asynchronously through a setup_intent.payment_failed webhook event (shown in the following examples).

[Test your integration](#web-test-integration)

## Test your integration

In order to receive the micro-deposit verification email in test mode after collecting the bank account details and accepting a mandate, provide an email in the payment_method[billing_details][email] field in the form of {any_prefix}+test_email@{any_domain} when confirming the payment method details.

Stripe provides several test account numbers you can use to make sure your integration for manually-entered bank accounts is ready for production. All test accounts that automatically succeed or fail the payment must be verified using the test micro-deposit amounts below before they can be completed.

To mimic successful or failed bank account verifications in test mode, use these meaningful amounts for micro-deposits:

[OptionalAccept future paymentsServer-side](#charge-later)

## OptionalAccept future paymentsServer-side

[OptionalInstant only verificationServer-side](#web-instant-only)

## OptionalInstant only verificationServer-side

[OptionalMicro-deposit only verificationServer-side](#web-microdeposit-only)

## OptionalMicro-deposit only verificationServer-side

## See also

- Accept a Canadian pre-authorized debit payment

[Accept a Canadian pre-authorized debit payment](/payments/acss-debit/accept-a-payment)

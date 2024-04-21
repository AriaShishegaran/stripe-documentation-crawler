# Save details for future payments with ACH Direct Debit

You can use the Setup Intents API to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

[Setup Intents API](/payments/setup-intents)

- Saving payment methods to a wallet to streamline future purchases

- Collecting surcharges after fulfilling a service

- Starting a free trial for a subscription

[subscription](/billing/subscriptions/creating)

ACH Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

[delayed notification](/payments/payment-methods#payment-notification)

[Create or retrieve a customerRecommendedServer-side](#web-create-customer)

## Create or retrieve a customerRecommendedServer-side

Create a Customer object when your user creates an account with your business, or retrieve an existing Customer associated with this user. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the Customer to enable Financial Connections’ return user optimization.

[Customer](/api/customers)

[return user optimization](/financial-connections/fundamentals#return-user-optimization)

[Create a SetupIntentServer-side](#web-create-setup-intent)

## Create a SetupIntentServer-side

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

[SetupIntent](/api/setup_intents)

Create a SetupIntent on your server with payment_method_types set to us_bank_account and specify the Customer’s id.

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

[id](/api/customers/object#customer_object-id)

For more information on Financial Connections fees, see pricing details.

[pricing details](https://stripe.com/financial-connections#pricing)

By default, collecting bank account payment information uses Financial Connections to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the Financial Connections docs to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

[Financial Connections](/financial-connections)

[Financial Connections docs](/financial-connections/ach-direct-debit-payments)

To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

[Collect payment method detailsClient-side](#web-collect-details)

## Collect payment method detailsClient-side

When a customer clicks to pay with ACH Direct Debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

[Stripe.js](/payments/elements)

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe.js with the following JavaScript on your checkout page.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Rather than sending the entire SetupIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Handle the client secret carefully because it can complete the Payment Method setup process. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.collectBankAccountForSetup  to collect bank account details with Financial Connections, create a PaymentMethod, and attach that PaymentMethod to the SetupIntent. Including the account holder’s name in the billing_details parameter is required to create an ACH Direct Debit PaymentMethod.

[stripe.collectBankAccountForSetup](/js/setup_intents/collect_bank_account_for_setup)

[Financial Connections](/financial-connections)

[PaymentMethod](/api/payment_methods)

The Financial Connections authentication flow automatically handles bank account details collection and verification. When your customer completes the authentication flow, the PaymentMethod automatically attaches to the SetupIntent, and creates a Financial Connections Account.

[Financial Connections authentication flow](/financial-connections/fundamentals#authentication-flow)

[PaymentMethod](/api/payment_methods)

[Financial Connections Account](/api/financial_connections/accounts)

Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.



To provide the best user experience on all devices, set the viewport minimum-scale for your page to 1 using the viewport meta tag.

[OptionalAccess data on a Financial Connections bank accountServer-side](#access-data-on-a-financial-connections-bank-account)

## OptionalAccess data on a Financial Connections bank accountServer-side

[Collect mandate acknowledgement and submitClient-side](#web-collect-mandate-and-submit)

## Collect mandate acknowledgement and submitClient-side

Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see Mandates.

[Mandates](/payments/ach-debit#mandates)

When the customer accepts the mandate terms, you must confirm the SetupIntent. Use stripe.confirmUsBankAccountSetup to complete the payment when the customer submits the form.

[stripe.confirmUsBankAccountSetup](/js/setup_intents/confirm_us_bank_account_setup)

stripe.confirmUsBankAccountSetup may take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

[stripe.confirmUsBankAccountSetup](/js/setup_intents/confirm_us_bank_account_setup)

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

[Verifying bank accounts with microdeposits](/payments/ach-debit/accept-a-payment#web-verify-with-microdeposits)

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to send custom notifications if you prefer.

[send custom notifications](/payments/ach-debit#mandate-and-microdeposit-emails)

[Verify bank account with microdepositsClient-side](#web-verify-with-microdeposits)

## Verify bank account with microdepositsClient-side

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a descriptor_code microdeposit and might fall back to an amount microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- Descriptor code. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit descriptor_code that starts with SM. Your customer uses this string to verify their bank account.

- Amount. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads ACCTVERIFY. Your customer uses the deposit amounts to verify their bank account.

The result of the stripe.confirmUsBankAccountSetup method call in the previous step is a SetupIntent in the requires_action state. The SetupIntent contains a next_action field that contains some useful information for completing the verification.

[stripe.confirmUsBankAccountSetup](/js/setup_intents/confirm_us_bank_account_setup)

[https://payments.stripe.com/…](https://payments.stripe.com/…)

If you supplied a billing email, Stripe notifies your customer via this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

[billing email](/api/payment_methods/object#payment_method_object-billing_details-email)

Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the SetupIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

Optionally, you can send custom email notifications to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose one of the following:

[custom email notifications](/payments/ach-debit#mandate-and-microdeposit-emails)

- Use the Stripe-hosted verification page. To do this, use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.

Use the Stripe-hosted verification page. To do this, use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.

[next_action](/api/payment_intents/object#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url)

- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using Stripe.js.At minimum, set up the form to handle the descriptor code parameter, which is a 6-digit string for verification purposes.Stripe also recommends that you set your form to handle the amounts parameter, as some banks your customers use may require it.Integrations only pass in the descriptor_code or amounts. To determine which one your integration uses, check the value for verify_with_microdeposits[microdeposit_type] in the next_action object.

If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using Stripe.js.

[Stripe.js](/js/payment_intents/verify_microdeposits_for_payment)

- At minimum, set up the form to handle the descriptor code parameter, which is a 6-digit string for verification purposes.

- Stripe also recommends that you set your form to handle the amounts parameter, as some banks your customers use may require it.

Integrations only pass in the descriptor_code or amounts. To determine which one your integration uses, check the value for verify_with_microdeposits[microdeposit_type] in the next_action object.

When the bank account is successfully verified, Stripe returns the SetupIntent object with a status of succeeded, and sends a setup_intent.succeeded webhook event.

[setup_intent.succeeded](/api/events/types#event_types-setup_intent.succeeded)

[webhook](/webhooks)

Verification can fail for several reasons. The failure may happen synchronously as a direct error response, or asynchronously through a setup_intent.setup_failed webhook event (shown in the following examples).

[setup_intent.setup_failed](/api/events/types#event_types-setup_intent.setup_failed)

[Test your integration](#test-integration)

## Test your integration

Learn how to test scenarios with instant verifications using Financial Connections.

[Financial Connections](/financial-connections/testing#web-how-to-use-test-accounts)

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

[payment method details](#web-collect-details)

You need to activate your Stripe account before you can trigger these emails in Test mode.

[activate your Stripe account](/get-started/account/activate)

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

[PaymentIntent cancellation](/api/payment_intents/cancel)

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

[Accepting future paymentsServer-side](#web-future-payments)

## Accepting future paymentsServer-side

When the SetupIntent succeeds, it will create a new PaymentMethod attached to a Customer. These can be used to initiate future payments without having to prompt the customer for their bank account a second time.

[PaymentMethod](/api/payment_methods)

[Customer](/api/customers)

[OptionalInstant only verificationServer-side](#instant-only-verification)

## OptionalInstant only verificationServer-side

[OptionalMicrodeposit only verificationServer-side](#microdeposit-only-verification)

## OptionalMicrodeposit only verificationServer-side

[OptionalUpdating the default payment methodServer-side](#update-default-payment-method)

## OptionalUpdating the default payment methodServer-side

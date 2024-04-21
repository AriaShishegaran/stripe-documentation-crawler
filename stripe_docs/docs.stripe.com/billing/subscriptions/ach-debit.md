# Set up a subscription with ACH Direct Debit

If you’re a new user, use the Payment Element instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see Build a subscription.

[Payment Element](/payments/payment-element)

[Build a subscription](/billing/subscriptions/build-subscriptions?ui=elements)

[Create a product and priceDashboard](#create-product-plan-code)

## Create a product and priceDashboard

Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

[Products](/api/products)

[Prices](/api/prices)

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

- Navigate to the Add a product page.

[Add a product](https://dashboard.stripe.com/test/products/create)

- Enter a Name for the product.

- Enter 15 for the price.

- Select USD as the currency.

- Click Save product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create the subscriptionServer-side](#create-subscription)

## Create the subscriptionServer-side

To create a subscription with a free trial period, see Subscription trials.

[subscription](/billing/subscriptions/creating)

[Subscription trials](#trial-periods)

Create a subscription with the price and customer with status incomplete by providing the payment_behavior parameter with the value of default_incomplete.

[subscription](/api/subscriptions)

[payment_behavior](/api/subscriptions/create#create_subscription-payment_behavior)

Included in the response is the subscription’s first PaymentIntent, containing the client secret, which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the client_secret to the frontend to complete payment.

[subscription](/billing/subscriptions/creating)

[PaymentIntent](/payments/payment-intents)

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[Collect payment method detailsClient-side](#collect-payment-details)

## Collect payment method detailsClient-side

When a customer clicks to pay with ACH Direct Debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

[Stripe.js](/payments/elements)

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe.js with the following JavaScript on your checkout page.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Rather than sending the entire PaymentIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.collectBankAccountForPayment  to collect bank account details with Financial Connections, create a PaymentMethod, and attach that PaymentMethod to the PaymentIntent. Including the account holder’s name in the billing_details parameter is required to create an ACH Direct Debit PaymentMethod.

[stripe.collectBankAccountForPayment](/js/payment_intents/collect_bank_account_for_payment)

[Financial Connections](/financial-connections)

[PaymentMethod](/api/payment_methods)

The Financial Connections authentication flow automatically handles bank account details collection and verification. When your customer completes the authentication flow, the PaymentMethod automatically attaches to the PaymentIntent, and creates a Financial Connections Account.

[Financial Connections authentication flow](/financial-connections/fundamentals#authentication-flow)

[PaymentMethod](/api/payment_methods)

[Financial Connections Account](/api/financial_connections/accounts)

Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.



To provide the best user experience on all devices, set the viewport minimum-scale for your page to 1 using the viewport meta tag.

[Collect mandate acknowledgement and submitClient-side](#collect-mandate-and-submit)

## Collect mandate acknowledgement and submitClient-side

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see Mandates.

[Mandates](/payments/ach-debit#mandates)

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use stripe.confirmUsBankAccountPayment to complete the payment when the customer submits the form.

[stripe.confirmUsBankAccountPayment](/js/payment_intents/confirm_us_bank_account_payment)

stripe.confirmUsBankAccountPayment may take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

[stripe.confirmUsBankAccountPayment](/js/payment_intents/confirm_us_bank_account_payment)

If the customer completes instant verification, the subscription automatically becomes active. Otherwise, see Verify bank account with microdeposits to learn how to handle microdeposit verification while the subscription remains incomplete.

[Verify bank account with microdeposits](#verify-with-microdeposits)

[Verify bank account with microdepositsClient-side](#verify-with-microdeposits)

## Verify bank account with microdepositsClient-side

Customers have 10 days to successfully verify microdeposits for a subscription, instead of the 23 hours normally given in the subscription lifecycle. However, this expiration can’t be later than the billing cycle date.

[Customers](/api/customers)

[subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)

[billing cycle date](#billing-cycle)

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a descriptor_code microdeposit and might fall back to an amount microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- Descriptor code. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit descriptor_code that starts with SM. Your customer uses this string to verify their bank account.

- Amount. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads ACCTVERIFY. Your customer uses the deposit amounts to verify their bank account.

The result of the stripe.confirmUsBankAccountPayment method call in the previous step is a PaymentIntent in the requires_action state. The PaymentIntent contains a next_action field that contains some useful information for completing the verification.

[stripe.confirmUsBankAccountPayment](/js/payment_intents/confirm_us_bank_account_payment)

[https://payments.stripe.com/…](https://payments.stripe.com/…)

If you supplied a billing email, Stripe notifies your customer via this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

[billing email](/api/payment_methods/object#payment_method_object-billing_details-email)

Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

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

[Set the default payment methodServer](#default-payment-method)

## Set the default payment methodServer

You now have an active subscription belonging to a customer with a payment method, but this payment method isn’t automatically used for future payments. To automatically bill this payment method in the future, use a webhook consumer to listen to the invoice.payment_succeeded event for new subscriptions and set the default payment method.

[subscription](/billing/subscriptions/creating)

[webhook](/webhooks)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[Manage subscription statusClient-side](#manage-sub-status)

## Manage subscription statusClient-side

Assuming the initial payment succeeds, the state of the subscription is active and requires no further action. When payments fail, the status changes to the Subscription status configured in your automatic collection settings. Notify the customer upon failure and charge them with a different payment method.

[automatic collection settings](/invoicing/automatic-collection)

[charge them with a different payment method](/billing/subscriptions/overview#requires-payment-method)

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

[OptionalSetting the billing cycle](#billing-cycle)

## OptionalSetting the billing cycle

[OptionalSubscription trials](#trial-periods)

## OptionalSubscription trials

[OptionalSaving payment method details for future use](#save-payment-method-for-future-subscriptions)

## OptionalSaving payment method details for future use

# Accept an ACH Direct Debit payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Stripe users in the US can use Checkout in payment mode to accept ACH Direct Debit payments.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. After your customer has completed a purchase, they are redirected back to your site.

With Checkout, you can create a Checkout Session with us_bank_account as a payment method type to track and handle the states of the payment until the payment completes.

ACH Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

[delayed notification](/payments/payment-methods#payment-notification)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: US

Supported currencies: usd

Presentment currencies: usd

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support ACH Direct Debit payments:

- Express all Prices for all line items in US dollars (currency code  usd).

[Prices](/api/prices)

[Create or retrieve a customerRecommendedServer-side](#create-customer)

## Create or retrieve a customerRecommendedServer-side

Create a Customer object when your user creates an account with your business, or retrieve an existing Customer associated with this user. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the Customer to enable Financial Connections’ return user optimization.

[Customer](/api/customers)

[return user optimization](/financial-connections/fundamentals#return-user-optimization)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guides you through enabling ACH Direct Debit and shows the differences between accepting a card payment and using this payment method.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add us_bank_account to the list of payment_method_types.

- Make sure all your line_items use the usd currency.

For more information on Financial Connections fees, see pricing details.

[pricing details](https://stripe.com/financial-connections#pricing)

By default, collecting bank account payment information uses Financial Connections to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the Financial Connections docs to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

[Financial Connections](/financial-connections)

[Financial Connections docs](/financial-connections/ach-direct-debit-payments)

To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

If the customer opts for microdeposit verification instead of Financial Connections, Stripe automatically sends two small deposits to the provided bank account. These deposits can take 1-2 business days to appear on the customer’s online bank statement. When the deposits are expected to arrive, the customer receives an email with a link to confirm these amounts and verify the bank account with Stripe. After verification is complete, the payment begins processing.

We recommend including the payment_intent_data.setup_future_usage parameter with a value of off_session when creating a payment mode Session for ACH Direct Debit so you can save payment method details.

[payment_intent_data.setup_future_usage](/api/payment_intents/object#payment_intent_object-setup_future_usage)

[save payment method details](/payments/accept-a-payment?platform=web&ui=stripe-hosted#save-payment-method-details)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

Because ACH Direct Debit is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[handle delayed notification payment methods](/payments/checkout/fulfill-orders#delayed-notification)

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

[Additional considerations](#additional-considerations)

## Additional considerations

When a bank account is pending verification with microdeposits, the customer can fail to verify for three reasons:

- The microdeposits failed to send to the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).

- The customer made 10 failed verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.

- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can handle the checkout.session.async_payment_failed event to contact the customer about placing a new order.

[handle the checkout.session.async_payment_failed event](/payments/checkout/fulfill-orders#delayed-notification)

[OptionalInstant only verification](#instant-only-verification)

## OptionalInstant only verification

[OptionalAccess data on a Financial Connections bank account](#access-data-on-a-financial-connections-bank-account)

## OptionalAccess data on a Financial Connections bank account

[OptionalResolve disputesServer-side](#resolving-disputes)

## OptionalResolve disputesServer-side

[OptionalPayment Reference](#payment-reference)

## OptionalPayment Reference

## See also

- Save ACH Direct Debit pre-authorized debit details for future payments

[Save ACH Direct Debit pre-authorized debit details for future payments](/payments/ach-debit/set-up-payment)

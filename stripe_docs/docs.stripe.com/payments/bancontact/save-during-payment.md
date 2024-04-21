# Save bank details during a Bancontact payment

We recommend that you follow the Save payment details during payment guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

[Save payment details during payment](/payments/save-during-payment)

[Payment Element migration guide](/payments/payment-element/migration)

See accepting SEPA Direct Debit payments to integrate without Bancontact.

[accepting SEPA Direct Debit payments](/payments/sepa-debit/accept-a-payment)

Bancontact is a popular single use payment method in Belgium where customers are required to authenticate their payment. Customers pay with Bancontact by redirecting from your website, authorizing the payment, then returning to your website where you get immediate notification on whether the payment succeeded or failed.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[immediate notification](/payments/payment-methods#payment-notification)

You can use Bancontact to save your customer’s IBAN bank details into a SEPA Direct Debit PaymentMethod. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription. This reduces friction for your customer as they don’t have to enter their IBAN again. You also receive their verified name and validated IBAN.

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[PaymentMethod](/api/payment_methods)

[accept payments](/payments/sepa-debit/accept-a-payment)

[set up a subscription](/billing/subscriptions/sepa-debit)

To use Bancontact to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the Bancontact Terms of Service and SEPA Direct Debit Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[Bancontact Terms of Service](https://stripe.com/bancontact/legal)

[SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal)

Accepting Bancontact payments consists of creating a PaymentIntent object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit PaymentMethod collected from your initial Bancontact PaymentIntent to create future payments.

[PaymentIntent](/api/payment_intents/object)

[PaymentMethod](/api/payment_methods)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create a CustomerServer-side](#web-create-customer)

## Create a CustomerServer-side

Create a Customer when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

[Customer](/api/customers)

[Create a PaymentIntentServer-side](#web-create-payment-intent)

## Create a PaymentIntentServer-side

Create a PaymentIntent on your server and specify the amount to collect, the eur currency, the customer ID, and off_session as an argument for setup future usage. If you have an existing Payment Intents integration, add bancontact to the list of payment method types.

[setup future usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[Payment Intents](/payments/payment-intents)

[payment method types](/api/payment_intents/create#create_payment_intent-payment_method_types)

The PaymentIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

[Collect payment method details and mandate acknowledgementClient-side](#web-collect-payment-method-details)

## Collect payment method details and mandate acknowledgementClient-side

Create a payment form on your client to collect the required billing details from the customer.

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace Rocket Rides with your company name.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

[Submit the payment to StripeClient-side](#web-submit-payment)

## Submit the payment to StripeClient-side

Create a payment on the client side with the client secret of the PaymentIntent. The client secret is different from your API keys that authenticate Stripe API requests. It should be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Call stripe.confirmBancontactPayment to redirect your customer to Bancontact’s website or app to complete the payment. Include a return_url to redirect your customer after they complete the payment. You must also provide the customer’s full name and email in billing_details.

[stripe.confirmBancontactPayment](/js/payment_intents/confirm_bancontact_payment)

[return_url](/api/payment_intents/create#create_payment_intent-return_url)

When your customer submits a payment, Stripe redirects them to the return_url and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the return_url, you can also append your own query parameters for use on the return page.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

When the customer is redirected back to your site, you can use the payment_intent_client_secret to query for the PaymentIntent and display the transaction status to your customer.

[Charge the SEPA Direct Debit PaymentMethod later](#web-charge-sepa-pm)

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by retrieving the previous PaymentIntent and expanding the latest_charge field where you will find the generated_sepa_debit ID inside of payment_method_details.

[retrieving](/api/payment_intents/retrieve)

[expanding](/api/expanding_objects)

The SEPA Direct Debit payment method ID is the generated_sepa_debit ID under payment_method_details in the response.

[payment_method_details](/api/charges/object#charge_object-payment_method_details-ideal)

Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

[Test your integration](#test-your-integration)

## Test your integration

Set payment_method.billing_details.email to one of the following values to test the PaymentIntent status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, test_1_generatedSepaDebitIntentsFail@example.com results in a SEPA Direct Debit PaymentMethod that always fails when used with a PaymentIntent.

[OptionalHandle post-payment events](#web-fulfillment)

## OptionalHandle post-payment events

[OptionalHandle the Bancontact redirect manually](#web-handle-redirect)

## OptionalHandle the Bancontact redirect manually

## See also

- Accept a SEPA Direct Debit payment

[Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)

- Set up a subscription with SEPA Direct Debit in the EU

[Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)

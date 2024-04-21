# Save bank details during a Sofort payment

Our financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

[support page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)

We recommend that you follow the Save payment details during payment guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

[Save payment details during payment](/payments/save-during-payment)

[Payment Element migration guide](/payments/payment-element/migration)

See accepting SEPA Direct Debit payments to integrate without Sofort.

[accepting SEPA Direct Debit payments](/payments/sepa-debit/accept-a-payment)

Sofort is a single use, delayed notification payment method that requires customers to authenticate their payment. Customers pay with Sofort by redirecting from your website to their bank’s portal to authenticate the payment. It typically takes 2 to 14 days to receive notification of success or failure.

[single use](/payments/payment-methods#usage)

[delayed notification](/payments/payment-methods#payment-notification)

[authenticate](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

You can use Sofort to save your customer’s IBAN bank details into a SEPA Direct Debit PaymentMethod. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription. This reduces friction for your customer as they don’t have to enter their IBAN again. You also receive their verified name and validated IBAN.

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[PaymentMethod](/api/payment_methods)

[accept payments](/payments/sepa-debit/accept-a-payment)

[set up a subscription](/billing/subscriptions/sepa-debit)

To use Sofort to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the Sofort Terms of Service and SEPA Direct Debit Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[Sofort Terms of Service](https://stripe.com/sofort/legal)

[SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal)

Accepting Sofort payments consists of creating a PaymentIntent object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit PaymentMethod collected from your initial Sofort PaymentIntent to create PaymentIntents for future payments.

[PaymentIntent](/api/payment_intents)

[PaymentMethod](/api/payment_methods)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create a CustomerServer-side](#create-customer)

## Create a CustomerServer-side

Create a Customer when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

[Customer](/api/customers)

[Create a PaymentIntentServer-side](#create-payment-intent)

## Create a PaymentIntentServer-side

Create a PaymentIntent on your server and specify the amount to collect, the eur currency, the customer ID, and off_session as an argument for setup future usage. If you have an existing Payment Intents integration, add sofort to the list of payment method types.

[setup future usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[Payment Intents](/payments/payment-intents)

[payment method types](/api/payment_intents/create#create_payment_intent-payment_method_types)

The PaymentIntent includes the payment method ID and a client secret, which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[Collect payment method details and mandate acknowledgementClient-side](#collect-payment-method-details)

## Collect payment method details and mandate acknowledgementClient-side

Create a payment form on your client to collect the required billing details from the customer.

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace Rocket Rides with your company name.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

[Submit the payment to StripeClient-side](#submit-payment)

## Submit the payment to StripeClient-side

Rather than sending the entire PaymentIntent object to the client, use its client secret from step 3. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[step 3](#web-create-payment-intent)

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmSofortPayment to handle the redirect away from your page and to complete the payment. Add a return_url to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

[stripe.confirmSofortPayment](/js/payment_intents/confirm_sofort_payment)

[return_url](/api/payment_intents/create#create_payment_intent-return_url)

Include your customer’s name and email address in payment_method[billing_details]. They will be used when generating the SEPA Direct Debit PaymentMethod.

When your customer submits a payment, Stripe redirects them to the return_url and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the return_url, you can also append your own query parameters for use on the return page.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

When the customer is redirected back to your site, you can use the payment_intent_client_secret to query for the PaymentIntent and display the transaction status to your customer.

[Charge the SEPA Direct Debit PaymentMethod later](#charge-sepa-pm)

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by retrieving the previous PaymentIntent and expanding the latest_charge field where you will find the generated_sepa_debit ID inside of payment_method_details.

[retrieving](/api/payment_intents/retrieve)

[expanding](/api/expanding_objects)

The SEPA Direct Debit payment method ID is the generated_sepa_debit ID under payment_method_details in the response.

[payment_method_details](/api/charges/object#charge_object-payment_method_details-sofort)

Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

[Test your integration](#test-your-integration)

## Test your integration

Set payment_method.billing_details.email to one of the following values to test the PaymentIntent status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, test_1_generatedSepaDebitIntentsFail@example.com results in a SEPA Direct Debit PaymentMethod that will always fail when used with a PaymentIntent.

[Handle post-payment events](#fulfillment)

## Handle post-payment events

As Sofort is a delayed notification payment method, the PaymentIntent’s status remains in a payment_intent.processing state for up to 14 days from its creation (also known as the cutoff date). In test mode, the PaymentIntent’s status remains in the processing state for three minutes to simulate this.

[delayed notification](/payments/payment-methods#payment-notification)

[payment_intent.processing](/api/events/types#event_types-payment_intent.processing)

- Stripe recommends fulfilling purchases during the processing state. On average, you can expect approximately 0.2% of Sofort payment attempts to fail after entering the processing state. This only applies to Sofort payments due to its low payment failure rate and doesn’t apply to other delayed notification payment methods.

[delayed notification](/payments/payment-methods#payment-notification)

- You may prefer to fulfill orders only after receiving the payment_intent.succeeded event. Stripe sends this event after the payment attempt is confirmed and the funds are guaranteed.

[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)

- If a customer doesn’t pay, Stripe sends the payment_intent.failed event and the PaymentIntent returns to a status of requires_payment_method.

[payment_intent.failed](/api/events/types#event_types-payment_intent.failed)

Use the Dashboard, a custom webhook, or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[webhook](/webhooks)

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- View your test payments in the Dashboard

[View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- Build a custom webhook

[Build a custom webhook](/payments/handling-payment-events#build-your-own-webhook)

Handle common business events, like automation or marketing and sales, by integrating a partner application.

[automation](https://stripe.partners/?f_category=automation)

[marketing and sales](https://stripe.partners/?f_category=marketing-and-sales)

[OptionalHandle the Sofort redirect manually](#handle-redirect)

## OptionalHandle the Sofort redirect manually

## See also

- Accept a SEPA Direct Debit payment

[Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)

- Set up a subscription with SEPA Direct Debit in the EU

[Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)

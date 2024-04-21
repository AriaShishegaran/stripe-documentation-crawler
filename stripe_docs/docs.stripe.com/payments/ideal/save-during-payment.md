# Save bank details during an iDEAL payment

We recommend that you follow the Save payment details during payment guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

[Save payment details during payment](/payments/save-during-payment)

[Payment Element migration guide](/payments/payment-element/migration)

See accepting SEPA Direct Debit payments to integrate without iDEAL.

[accepting SEPA Direct Debit payments](/payments/sepa-debit/accept-a-payment)

iDEAL is a popular single use payment method in the Netherlands where customers are required to authenticate their payment. Customers pay with iDEAL by redirecting to a webview, authorizing the payment, then returning to your app where you get immediate notification on whether the payment succeeded or failed.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[immediate notification](/payments/payment-methods#payment-notification)

You can also use iDEAL to save your customer’s IBAN bank details into a SEPA Direct Debit PaymentMethod. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription. This reduces friction for your customer as they don’t have to enter their IBAN again. You also receive their verified name and validated IBAN.

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[PaymentMethod](/api/payment_methods)

[accept payments](/payments/sepa-debit/accept-a-payment)

[set up a subscription](/billing/subscriptions/sepa-debit)

To use iDEAL to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the iDEAL Terms of Service and SEPA Direct Debit Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[iDEAL Terms of Service](https://stripe.com/ideal/legal)

[SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal)

Accepting iDEAL payments consists of creating a PaymentIntent object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit PaymentMethod collected from your initial iDEAL PaymentIntent to create future payments.

[PaymentIntent](/api/payment_intents/object)

[PaymentMethod](/api/payment_methods)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create a CustomerServer-side](#create-customer)

## Create a CustomerServer-side

Create a Customer when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

[Customer](/api/customers)

[Create a PaymentIntentServer-side](#web-create-payment-intent)

## Create a PaymentIntentServer-side

Create a PaymentIntent on your server and specify the amount to collect, the eur currency, the customer ID, and off_session as an argument for setup future usage. There is no minimum charge amount and iDEAL doesn’t support other currencies. If you have an existing Payment Intents API integration, add ideal to the list of payment method types.

[setup future usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[Payment Intents API](/payments/payment-intents)

[payment method types](/api/payment_intents/create#create_payment_intent-payment_method_types)

The PaymentIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

[Collect payment method details and mandate acknowledgementClient-side](#web-collect-payment-method-details)

## Collect payment method details and mandate acknowledgementClient-side

Collect payment information on the client with Stripe Elements. Elements is a set of prebuilt UI components for collecting payment details. A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection.

[Stripe Elements](/payments/elements)

The checkout page address must also start with https:// rather than http:// for your integration to work. You can test your integration without using HTTPS. Enable it when you’re ready to accept live payments.

[Enable it](/security/guide#tls)

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Do not include the script in a bundle or host a copy of it yourself.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Elements with the following JavaScript on your checkout page:

Elements needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form and then pass those IDs to Elements.

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace Rocket Rides with your company name.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

When the form above has loaded, create an instance of an idealBank Element and mount it to the Element container created above:

[create an instance](/js/elements_object/create_element?type=idealBank)

Elements are completely customizable. You can style Elements to match the look and feel of your site, providing a seamless checkout experience for your customers. It’s also possible to style various input states, for example when the Element has focus.

[style Elements](/js/elements_object/create_element?type=idealBank#elements_create-options)

[Submit the payment to StripeClient-side](#web-submit-payment)

## Submit the payment to StripeClient-side

Rather than sending the entire PaymentIntent object to the client, use its client secret from step 3. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[step 3](#web-create-payment-intent)

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmIdealPayment to handle the redirect away from your page and to complete the payment. Add a return_url to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

[stripe.confirmIdealPayment](/js/payment_intents/confirm_ideal_payment)

[return_url](/api/payment_intents/create#create_payment_intent-return_url)

Include your customer’s name and email address in payment_method[billing_details]. They will be used when generating the SEPA Direct Debit PaymentMethod.

In order to pass the setup_future_usage parameter as shown below, you must modify the API version you passed when creating your instance of Elements. Review the instructions for setting up Stripe Elements from above if you are unable to pass setup_future_usage at this step.

[setting up Stripe Elements](/payments/ideal/save-during-payment#set-up-stripe-elements)

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

Using your test API keys, select any bank from the list. After confirming the PaymentIntent, you’re redirected to a test page with options to authorize or fail the payment.

[test API keys](/keys#test-live-modes)

- Click Authorize test payment to test the case when the payment is successful. The PaymentIntent transitions from requires_action to succeeded.

- Click Fail test payment to test the case when the customer fails to authenticate. The PaymentIntent transitions from requires_action to requires_payment_method.

Set payment_method.billing_details.email to one of the following values to test the PaymentIntent status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, test_1_generatedSepaDebitIntentsFail@example.com results in a SEPA Direct Debit PaymentMethod that always fails when used with a PaymentIntent.

[OptionalHandle post-payment events](#web-fulfillment)

## OptionalHandle post-payment events

[OptionalHandle iDEAL Bank Element changes](#web-handle-bank-element)

## OptionalHandle iDEAL Bank Element changes

[OptionalHandle the iDEAL redirect manually](#web-handle-redirect)

## OptionalHandle the iDEAL redirect manually

## See also

- Accept a SEPA Direct Debit payment

[Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)

- Set up a subscription with SEPA Direct Debit in the EU

[Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)

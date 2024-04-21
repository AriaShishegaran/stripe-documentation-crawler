# Save BECS Direct Debit details for future payments

Use Stripe Elements, our prebuilt UI components, to create a payment form that lets you securely collect bank details without handling the sensitive data. You can use the Setup Intents API to collect BECS Direct Debit payment method details in advance, with the final amount or payment date determined later. This is useful for:

[Stripe Elements](/payments/elements)

[Setup Intents API](/payments/setup-intents)

- Saving payment methods to a wallet to streamline future purchases

- Collecting surcharges after fulfilling a service

- Starting a free trial for a subscription

[Starting a free trial for a subscription](/billing/subscriptions/trials)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create or retrieve a CustomerServer-side](#web-create-customer)

## Create or retrieve a CustomerServer-side

To reuse a BECS Direct Debit account for future payments, you must attach it to a Customer.

[Customer](/api/customers)

Create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of them enables you to retrieve and use the stored payment method details later.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

[Create a SetupIntentServer-side](#web-create-setup-intent)

## Create a SetupIntentServer-side

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

[SetupIntent](/api/setup_intents)

Create a SetupIntent on your server with payment_method_types set to au_becs_debit and specify the Customer’s id:

[SetupIntent](/api/setup_intents)

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

[Customer](/api/customers)

[id](/api/customers/object#customer_object-id)

After creating a SetupIntent on your server, you can associate the SetupIntent ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you have successfully collected a payment method.

The returned SetupIntent object contains a client_secret property. Pass the client secret to the client-side application to continue with the setup process.

[Collect payment method details and mandate acknowledgmentClient-side](#web-collect-payment-method-details)

## Collect payment method details and mandate acknowledgmentClient-side

You’re ready to collect payment information on the client with Stripe Elements. Elements is a set of prebuilt UI components for collecting payment details.

[Stripe Elements](/payments/elements)

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. Enable it when you’re ready to accept live payments.

[Enable it](/security/guide#tls)

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Elements with the following JavaScript on your payment page:

[Elements](/js#stripe-elements)

Before you can create a BECS Direct Debit payment, your customer must agree with the Direct Debit Request Service Agreement. They do so by submitting a completed Direct Debit Request (DDR). The approval gives you a mandate to debit their account. The Mandate is a record of the permission to debit a payment method.

For online mandate acceptance, you can create a form to collect the necessary information. Serve the form over HTTPS and capture the following information:

[HTTPS](/security/guide#tls)

When collecting a Direct Debit Request, follow our BECS Direct Debit Terms and as part of your checkout form:

[BECS Direct Debit Terms](https://stripe.com/au-becs/legal)

- Display the exact terms of Stripe’s DDR service agreement either inline on the form, or on a page linked from the form, and identifying it as the “DDR service agreement.”

[Stripe’s DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)

- Make sure the accepted DDR and its accompanying DDR service agreement can be shared with your customer at all times, either as a printed or non-changeable electronic copy (such as email). Stripe hosts this for you.

[DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)

- Display the following standard authorization text for your customer to accept the BECS DDR, where you replace Rocketship Inc with your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

By providing your bank account details, you agree to this Direct Debit Request and the Direct Debit Request service agreement, and authorize Stripe Payments Australia Pty Ltd ACN 160 180 343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of Rocketship Inc (the “Merchant”) for any amounts separately communicated to you by the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

[Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)

The details of the accepted mandate are generated when setting up a PaymentMethod or confirming a PaymentIntent. At all times, you should be able to share this mandate—the accepted DDR and its accompanying DDR service agreement—with your customer, either in print or as a non-changeable electronic copy (such as email). Stripe hosts this for you under the url property of the Mandate object linked to the PaymentMethod.

[PaymentMethod](/payments/payment-methods)

The Australia Bank Account Element will help you collect and validate both the BSB number and the account number. It needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form. Additionally, your customer must read and accept the Direct Debit Request service agreement.

[Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)

When the form loads, you can create an instance of the Australia Bank Account Element and mount it to the Element container:

[create an instance](/js/elements_object/create_element?type=au_bank_account)

[Submit the payment method details to StripeClient-side](#web-submit-payment-method)

## Submit the payment method details to StripeClient-side

Rather than sending the entire SetupIntent object to the client, use its client secret from step 2. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/setup_intents/object#setup_intent_object-client_secret)

[step 2](#web-create-setup-intent)

The client secret should be handled carefully because it can complete the setup. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmAuBecsDebitSetup to complete the setup when the user submits the form. A successful setup returns a succeeded value for the SetupIntent’s status property. If the setup isn’t successful, inspect the returned error to determine the cause.

[stripe.confirmAuBecsDebitSetup](/js/setup_intents/confirm_au_becs_debit_setup)

As customer was set, the PaymentMethod is attached to the provided Customer object after a successful setup. At this point, you can associate the ID of the Customer object with your internal representation of a customer. This allows you to use the stored PaymentMethod to collect future payments without prompting for your customer’s payment method details.

[customer](/api/setup_intents/create#create_setup_intent-customer)

[PaymentMethod](/api/payment_methods)

After successfully confirming the SetupIntent, you should share the mandate URL from the Mandate object with your customer. We also recommend including the following details to your customer when you confirm their mandate has been established:

[mandate URL](/api/mandates/object#mandate_object-payment_method_details-au_becs_debit-url)

[Mandate object](/api/mandates)

- an explicit confirmation message that indicates a Direct Debit arrangement has been set up

- the business name that will appear on the customer’s bank statement whenever their account gets debited

[business name](#statement-descriptors)

- the payment amount and schedule (if applicable)

- a link to the generated DDR mandate URL

The Mandate object’s ID is accessible from the mandate on the SetupIntent object, which is sent as part of the setup_intent.succeeded event sent after confirmation, but can also be retrieved through the API.

[retrieved through the API](/api/setup_intents/retrieve)

[Test the integration](#web-test-integration)

## Test the integration

You can test your form using the test BSB number 000-000 and one of the test account numbers below with your confirmAuBecsDebitSetup request.

[confirmAuBecsDebitSetup](/js/setup_intents/confirm_au_becs_debit_setup)

[OptionalValidate the Australia Bank Account ElementClient-side](#web-validate-element)

## OptionalValidate the Australia Bank Account ElementClient-side

[OptionalAccepting future paymentsClient-side](#web-future-payments)

## OptionalAccepting future paymentsClient-side

## See also

- Accept a BECS Debit payment

[Accept a BECS Debit payment](/payments/au-becs-debit/accept-a-payment)

- Connect platforms using the Payment Methods API

[Connect platforms using the Payment Methods API](/payments/payment-methods/connect)

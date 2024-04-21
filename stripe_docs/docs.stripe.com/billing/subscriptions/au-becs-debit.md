# Set up a subscription with BECS Direct Debit in Australia

If you’re a new user, use the Payment Element instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see Build a subscription.

[Payment Element](/payments/payment-element)

[Build a subscription](/billing/subscriptions/build-subscriptions?ui=elements)

[Create a product and priceDashboard](#create-product-plan-code)

## Create a product and priceDashboard

Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

[Products](/api/products)

[Prices](/api/prices)

This guide uses a stock photo service as an example and charges customers a 15 AUD monthly subscription. To model this:

- Navigate to the Add a product page.

[Add a product](https://dashboard.stripe.com/test/products/create)

- Enter a Name for the product.

- Enter 15 for the price.

- Select AUD as the currency.

- Click Save product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create a SetupIntentServer-side](#create-setup-intent)

## Create a SetupIntentServer-side

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

[SetupIntent](/api/setup_intents)

Create a SetupIntent on your server with payment_method_types set to au_becs_debit:

[SetupIntent](/api/setup_intents)

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

The returned SetupIntent object contains a client_secret property. Pass the client secret to the client-side application to continue with the setup process.

[Collect payment method details and mandate acknowledgmentClient-side](#collect-payment-method-details)

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

[Submit the payment method details to StripeClient-side](#submit-payment-method)

## Submit the payment method details to StripeClient-side

Rather than sending the entire SetupIntent object to the client, use its client secret from step 2. This is different from your API keys that authenticate Stripe API requests.

[client secret](/api/setup_intents/object#setup_intent_object-client_secret)

[step 2](#web-create-setup-intent)

The client secret should be handled carefully because it can complete the setup. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmAuBecsDebitSetup to complete the setup when the user submits the form. A successful setup returns a succeeded value for the SetupIntent’s status property. If the setup isn’t successful, inspect the returned error to determine the cause.

[stripe.confirmAuBecsDebitSetup](/js/setup_intents/confirm_au_becs_debit_setup)

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

[Create a customer with a PaymentMethodServer-side](#create-customer)

## Create a customer with a PaymentMethodServer-side

Creating subscriptions requires a customer, which represents the customer purchasing your product. Because the price you created charges on a monthly basis, you need to add a stored payment method to the customer so future payments are successful. You do this by setting the payment method you just collected at the top level of the Customer object and as the default payment method for invoices:

[subscriptions](/billing/subscriptions/creating)

[customer](/api#customer_object)

[Customer](/api/customers)

[default payment method](/api/customers/create#create_customer-invoice_settings-default_payment_method)

[invoices](/api/invoices)

This returns a Customer object. You can see the default payment method in the invoice_settings object:

After creating the customer, store the id value in your own database so you can use it later. The next step also requires this ID.

[Create the subscriptionServer-side](#create-subscription-code)

## Create the subscriptionServer-side

Create a subscription with the price and customer:

[subscription](/api/subscriptions)

Creating subscriptions automatically charges customers because the default payment method is set. After a successful payment, the status in the Stripe Dashboard changes to Active. The price you created earlier determines subsequent billings.

[default payment method](/api/customers/create#create_customer-invoice_settings-default_payment_method)

[Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions)

[Manage subscription statusClient-side](#manage-sub-status)

## Manage subscription statusClient-side

Assuming the initial payment succeeds, the state of the subscription is active and no further action is needed. When payments fail, the status is changed to the Subscription status configured in your automatic collection settings. You should notify the customer on failure and charge them with a different payment method.

[subscription](/billing/subscriptions/creating)

[automatic collection settings](/invoicing/automatic-collection)

[charge them with a different payment method](/billing/subscriptions/overview#requires-payment-method)

BECS Direct Debit payments are never automatically retried, even if you have a retry schedule configured for other payment methods.

[retry schedule](/invoicing/automatic-collection)

[Test the integration](#test-integration)

## Test the integration

You can test your form using the test BSB number 000-000 and one of the test account numbers below with your confirmAuBecsDebitSetup request.

[confirmAuBecsDebitSetup](/js/setup_intents/confirm_au_becs_debit_setup)

[OptionalSetting the billing cycle](#billing-cycle)

## OptionalSetting the billing cycle

[OptionalSubscription trials](#trial-periods)

## OptionalSubscription trials

# Save directly without charging

Use SetupIntents to collect card details without charging the card. Saving cards with Stripe Terminal using SetupIntents requires you to:

[SetupIntents](/payments/setup-intents)

- Create or retrieve a Customer object.

[Customer](/api/customers)

- Create a SetupIntent object to track the process.

[SetupIntent](/api/setup_intents)

- Collect a payment method after collecting the customer’s consent.

- Submit the payment method details to Stripe.

## Availability

You can use SetupIntents to collect card details on Visa, Mastercard, American Express, Discover, and co-branded eftpos cards. Interac cards, single-branded eftpos cards, and mobile wallets (for example, Apple Pay or Google Pay) aren’t supported.

[SetupIntents](/payments/setup-intents)

[mobile wallets](/payments/wallets)

The server-driven-based SetupIntents API is compatible with BBPOS WisePOS E and Stripe Reader S700.

[Create or retrieve a customer](#create-customer)

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a Customer.

[Customer](/api/customers)

When you include a customer in your SetupIntent before confirming, Stripe automatically attaches the generated card payment method to the Customer object you provide.

[SetupIntent](/api/setup_intents)

[Customer](/api/customers)

Include the following code on your server to create a new Customer.

[Create a SetupIntent](#create-setupintent)

## Create a SetupIntent

We recommend providing a customer ID while creating a SetupIntent—doing so attaches the card payment method to the Customer upon successful setup. If you don’t provide a customer ID, you must attach the payment method in a separate call.

[customer ID](/api/setup_intents/create#create_setup_intent-customer)

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

[SetupIntent](/api/setup_intents)

- Create a SetupIntent

[Create a SetupIntent](/api/setup_intents/create)

You must create the SetupIntent on your server and include card_present on the payment_method_types parameter.

The SetupIntent contains a client secret, which is a key that’s unique to the individual SetupIntent. You must obtain the client secret from the SetupIntent on your server and pass it to the client side.

[client secret](/api/setup_intents/object#setup_intent_object-client_secret)

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[Collect a payment method for saving cards](#collect-payment-method)

## Collect a payment method for saving cards

- process_setup_intent

[process_setup_intent](/api/terminal/readers/process_setup_intent)

After you create a SetupIntent, you need to collect a payment method with the SDK and collect customer consent. If the customer provides the required form of agreement or consent, set the  customer_consent_collected  boolean to true.

Collect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

You must call the process_setup_intent endpoint, which handles both collecting and confirming the SetupIntent. If the customer provides consent, set the customer_consent_collected boolean to true.

[process_setup_intent](/api/terminal/readers/process_setup_intent)

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

- cancel_action

[cancel_action](/api/terminal/readers/cancel_action)

You can cancel collecting a payment method by calling cancel_action.

[cancel_action](/api/terminal/readers/cancel_action)

Collecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

[Submit the payment method details to Stripe](#submit-payment-method)

## Submit the payment method details to Stripe

Your previous call to process_setup_intent handles the confirm for you, so no further action is necessary.

[process_setup_intent](/api/terminal/readers/process_setup_intent)

A successful setup returns a succeeded value for the SetupIntent’s status property, along with a generated_card, which is a reusable card payment method you can use for online payments.

[status](/api/setup_intents/object#setup_intent_object-status)

[generated_card](/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card)

The setup_intent.payment_method is a card_present PaymentMethod that represents the tokenization of the card in-store and isn’t chargeable online.

[setup_intent.payment_method](/api/setup_intents/object#setup_intent_object-payment_method)

The generated_card payment method automatically attaches to the customer you provided during SetupIntent creation. You can retrieve the generated_card payment method by expanding the SetupIntent’s latest_attempt property.

[SetupIntent creation](/terminal/features/saving-cards/save-cards-directly#create-setupintent)

Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

If you didn’t provide a customer during SetupIntent creation, you can attach the generated_card to a Customer object in a separate call.

If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).

- How the payment amount is determined.

- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

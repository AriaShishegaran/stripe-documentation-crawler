# Saving cards using MOTOBeta

MOTO SetupIntents allow you to enter the card information on the reader and save the payment details without charging the card. As when saving cards directly without charging with the server-driven integration, you can:

[saving cards directly without charging](/terminal/features/saving-cards/save-cards-directly)

- Create or retrieve a Customer object.

[Customer](/api/customers)

- Create a SetupIntent object to track the process.

[SetupIntent](/payments/setup-intents)

- Process the payment method.

- Verify the reader state.

- Use the PaymentMethod.

[PaymentMethod](/api/payment_method)

Saving a card with MOTO flow

[Create or retrieve a customer](#create-customer)

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a Customer.

[Customer](/api/customers)

When you include a customer in your SetupIntent before confirming, Stripe automatically attaches the generated card payment method to the provided Customer object.

[SetupIntent](/api/setup_intents)

[Customer](/api/customers)

Include the following code on your server to create a new Customer.

[Create a SetupIntent](#create-setupintent)

## Create a SetupIntent

- Create a SetupIntent

[Create a SetupIntent](/api/setup_intents/create)

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. The payment_method_types must include card.

[SetupIntent](/api/setup_intents)

[payment_method_types](/api/payment_intents/create#create_payment_intent-payment_method_types)

[Process the SetupIntent](#process-setupintent)

## Process the SetupIntent

After you create the SetupIntent, use process_setup_intent to process the payment, setting process_config[moto] to true. If the customer provides the required form of agreement or consent, set the customer_consent_collected Boolean to true.

[process_setup_intent](/api/terminal/readers/process_setup_intent)

[process_config[moto]](/api/terminal/readers/process_setup_intent#process_setup_intent-process_config)

The process_setup_intent request is asynchronous. After the request, the reader prompts you to enter the cardholder’s card number, CVC, expiration date, and postal code. You can then confirm the cardholder’s details to submit the card details for authorization.

[process_setup_intent](/api/terminal/readers/process_setup_intent)

[Verify the reader state](#verify-reader-state)

## Verify the reader state

Your application must follow the instructions for verifying the reader state to confirm a successful (approved) SetupIntent.

[verifying the reader state](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)

[Use the PaymentMethod](#use-payment-method)

## Use the PaymentMethod

You can now charge the saved PaymentMethod associated with the Customer using a PaymentIntent.

[PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method)

[Compliance](#compliance)

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).

- How the payment amount is determined.

- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

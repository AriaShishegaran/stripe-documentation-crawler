# Add custom fields

Don’t use custom fields to collect personal, protected, or sensitive data, or information restricted by law.

You can add custom fields on the payment form to collect additional information from your customers. The information is available after the payment is complete and is useful for fulfilling the purchase.

- Up to three fields allowed.

- Not available in setup mode.

- Support for up to 255 characters on text fields.

- Support for up to 255 digits on numeric fields.

- Support for up to 200 options on dropdown fields.

[Create a Checkout Session](#create-session)

## Create a Checkout Session

Create a Checkout Session while specifying an array of custom fields. Each field must have a unique key that your integration uses to reconcile the field. Also provide a label for the field that you display to your customer. Labels for custom fields aren’t translated, but you can use the locale parameter to set the language of your Checkout Session to match the same language as your labels.

[custom fields](/api/checkout/sessions/create#create_checkout_session-custom_fields)

[locale](/api/checkout/sessions/create#create_checkout_session-locale)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Retrieve custom fields](#retrieve-fields)

## Retrieve custom fields

When your customer completes the Checkout Session, we send a checkout.session.completed webhook with the completed fields.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[webhook](/webhooks)

Example checkout.session.completed payload:

[Do more with custom fields](#more-custom-fields)

## Do more with custom fields

htmlAdd custom fields | Stripe Documentation[Skip to content](#main-content)Add custom fields[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-fields)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-fields)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Add custom fields

Learn how to add additional fields to a prebuilt payment page with Checkout.CautionDon’t use custom fields to collect personal, protected, or sensitive data, or information restricted by law.

You can add custom fields on the payment form to collect additional information from your customers. The information is available after the payment is complete and is useful for fulfilling the purchase.

### Limitations

- Up to three fields allowed.
- Not available in`setup`mode.
- Support for up to 255 characters on text fields.
- Support for up to 255 digits on numeric fields.
- Support for up to 200 options on dropdown fields.

[Create a Checkout Session](#create-session)Create a Checkout Session while specifying an array of custom fields. Each field must have a unique key that your integration uses to reconcile the field. Also provide a label for the field that you display to your customer. Labels for custom fields aren’t translated, but you can use the locale parameter to set the language of your Checkout Session to match the same language as your labels.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "custom_fields[0][key]"=engraving \
  -d "custom_fields[0][label][type]"=custom \
  -d "custom_fields[0][label][custom]"="Personalized engraving" \
  -d "custom_fields[0][type]"=text`![A checkout page with custom fields](https://b.stripecdn.com/docs-statics-srv/assets/required.b8a7aedd127b6e37c710488ad4478ddc.png)

[Retrieve custom fields](#retrieve-fields)When your customer completes the Checkout Session, we send a checkout.session.completed webhook with the completed fields.

Example checkout.session.completed payload:

`{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2022-11-15",
  "created": 1664928000,
  "data": {
    "object": {
      "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
      "object": "checkout.session",
      "custom_fields": [{
        "key": "engraving",
        "label": {
          "type": "custom",
          "custom": "Personalized engraving"
        },
        "optional": false,
        "type": "text",
        "text": {
          "value": "Jane",
        }
      }],
      "mode": "payment",
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "checkout.session.completed"
}`[Do more with custom fields](#more-custom-fields)### Mark a field as optional

### Add a dropdown field

### Add a numbers only field

### Retrieve custom fields for a subscription

### Add character length validations

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a Checkout Session](#create-session)[Retrieve custom fields](#retrieve-fields)[Do more with custom fields](#more-custom-fields)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
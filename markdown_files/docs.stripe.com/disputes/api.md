htmlUse the API to respond to disputes | Stripe Documentation[Skip to content](#main-content)Using the API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fapi)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fapi)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)[Responding to disputes](/docs/disputes/responding)# Use the API to respond to disputes

Learn how to manage disputes programmatically.You can respond to disputes in the Stripe Dashboard, where we guide you through submitting the optimal evidence for each dispute reason.

You can also programmatically manage disputes using the API. With the API, you can upload evidence, respond to disputes, and receive dispute events using webhooks.

## Retrieve a dispute

For details about a dispute, retrieve a Dispute object:

Command Line[curl](#)`curl https://api.stripe.com/v1/disputes/{{DISPUTE_ID}} \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz`The response contains information about the dispute and any response or evidence that’s already been provided.

`{
  object: "dispute"
  id: "{{DISPUTE_ID}}",
  charge: "ch_5Q4BjL06oPWwho",
  evidence: {
    customer_name: "Jane Austen",
    customer_purchase_ip: "127.0.0.1",
    product_description: "Widget ABC, color: red",
    shipping_tracking_number: "Z01234567890",
    uncategorized_text: "Additional notes and comments",
  },
  evidence_details: {
    due_by: 1403047735,
    submission_count: 1
  }
  ...
}`## Update a dispute

You update the Dispute object and pass structured evidence with the evidence parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/disputes/{{DISPUTE_ID}} \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz \
  -d "evidence[customer_email_address]"="email@example.com" \
  -d "evidence[shipping_date]"=3/22/2024 \
  -d "evidence[shipping_documentation]"="{{FILE_ID}}"`To view all available fields for the evidence parameter, see Dispute evidence. There are two types of evidence you can provide, depending on the field being updated:

- Text-based evidence, such as`customer_email`and`service_date`. These types of evidence take a string of text.
- File-based evidence, such as`service_documentation`and`customer_communication`. These take a[file_upload](/api#file_object)object ID.

NoteThe combined character count for all text-based evidence field submissions is limited to 150,000.

You can provide documents or images (for example, a contract or screenshot) as part of dispute evidence using the File Upload API. You first upload a document with the purpose of dispute_evidence, which generates a File_upload object that you can use when submitting evidence. Make sure the file meets Stripe’s recommendations before uploading it for evidence submission.

If you’re only interested in submitting a single file or a large amount of plaintext as evidence, use uncategorized_text or uncategorized_file. However, fill in as many fields as possible so you have the best chance at overturning a dispute.

NoteYou must use the Dashboard to submit evidence for Visa Compelling Evidence 3.0 eligible disputes, because we don’t support providing prior transaction data through the API.

## Multiple disputes on a single payment

It’s not typical, but it’s possible for a customer to dispute the same payment more than once. For example, a customer might partially dispute a payment for one of the items in an order if it was damaged in delivery, and then file a second dispute against a different item in the same order because the item didn’t work properly.

Stripe distinguishes all disputes by a unique identifier, regardless of whether they’re related to a single payment. When you list disputes, you can filter the results to show only disputes for a particular payment by specifying the id of the PaymentIntent or Charge object and including the payment_intent filter or charge filter.

By PaymentIntentBy ChargeCommand Line[curl](#)`curl -G https://api.stripe.com/v1/disputes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d payment_intent={{PAYMENT_INTENT_ID}}`When a payment has multiple disputes, use the id provided for each returned dispute in the list to make sure you’re responding to the correct dispute by specifying its id when you retrieve or update the dispute.

## See also

- [Dispute categories](/disputes/categories)
- [Measuring disputes](/disputes/measuring)
- [Preventing disputes and fraud](/disputes/prevention)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Retrieve a dispute](#retrieve-a-dispute)[Update a dispute](#update-a-dispute)[Multiple disputes on a single payment](#multiple-disputes-on-a-single-payment)[See also](#see-also)Products Used[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
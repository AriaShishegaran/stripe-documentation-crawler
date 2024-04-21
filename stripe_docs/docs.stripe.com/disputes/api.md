# Use the API to respond to disputes

You can respond to disputes in the Stripe Dashboard, where we guide you through submitting the optimal evidence for each dispute reason.

[dispute reason](/disputes/categories)

You can also programmatically manage disputes using the API. With the API, you can upload evidence, respond to disputes, and receive dispute events using webhooks.

## Retrieve a dispute

For details about a dispute, retrieve a Dispute object:

[retrieve](/api#retrieve_dispute)

The response contains information about the dispute and any response or evidence that’s already been provided.

## Update a dispute

You update the Dispute object and pass structured evidence with the evidence parameter.

[update](/api#update_dispute)

To view all available fields for the evidence parameter, see Dispute evidence. There are two types of evidence you can provide, depending on the field being updated:

[Dispute evidence](/api#dispute_evidence_object)

- Text-based evidence, such as customer_email and service_date. These types of evidence take a string of text.

- File-based evidence, such as service_documentation and customer_communication. These take a file_upload object ID.

[file_upload](/api#file_object)

The combined character count for all text-based evidence field submissions is limited to 150,000.

You can provide documents or images (for example, a contract or screenshot) as part of dispute evidence using the File Upload API. You first upload a document with the purpose of dispute_evidence, which generates a File_upload object that you can use when submitting evidence. Make sure the file meets Stripe’s recommendations before uploading it for evidence submission.

[File Upload API](/file-upload)

[Stripe’s recommendations](/disputes/best-practices#file-upload-recommendations)

If you’re only interested in submitting a single file or a large amount of plaintext as evidence, use uncategorized_text or uncategorized_file. However, fill in as many fields as possible so you have the best chance at overturning a dispute.

You must use the Dashboard to submit evidence for Visa Compelling Evidence 3.0 eligible disputes, because we don’t support providing prior transaction data through the API.

[submit evidence](/disputes/responding#respond)

[Visa Compelling Evidence 3.0](/disputes/categories#visa-ce-30)

## Multiple disputes on a single payment

It’s not typical, but it’s possible for a customer to dispute the same payment more than once. For example, a customer might partially dispute a payment for one of the items in an order if it was damaged in delivery, and then file a second dispute against a different item in the same order because the item didn’t work properly.

Stripe distinguishes all disputes by a unique identifier, regardless of whether they’re related to a single payment. When you list disputes, you can filter the results to show only disputes for a particular payment by specifying the id of the PaymentIntent or Charge object and including the payment_intent filter or charge filter.

[list disputes](/api#list_disputes)

[payment_intent filter](/api/disputes/list#list_disputes-charge)

[charge filter](/api/disputes/list#list_disputes-payment_intent)

When a payment has multiple disputes, use the id provided for each returned dispute in the list to make sure you’re responding to the correct dispute by specifying its id when you retrieve or update the dispute.

[retrieve](#retrieve-a-dispute)

[update the dispute](#update-a-dispute)

## See also

- Dispute categories

[Dispute categories](/disputes/categories)

- Measuring disputes

[Measuring disputes](/disputes/measuring)

- Preventing disputes and fraud

[Preventing disputes and fraud](/disputes/prevention)

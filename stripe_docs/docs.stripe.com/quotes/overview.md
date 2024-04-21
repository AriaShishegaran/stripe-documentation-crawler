# How quotes work

You can use quotes in test mode, but you must upgrade to Invoicing Plus or Billing Scale to unlock full functionality in live mode. See which plan is right for you.

[Invoicing Plus](https://stripe.com/invoicing/pricing)

[Billing Scale](https://stripe.com/billing/pricing)

[is right for you](https://support.stripe.com/questions/how-to-access-quotes)

​​Quotes allow you to deliver estimated pricing for requested goods or services and can help facilitate negotiation before beginning a subscription or invoice.

[invoice](/api/invoices)

​​We designed the quote statuses to mirror a typical quoting flow that a sales agent follows, where they create a quote with line items that specify the items for purchase. This includes applying any discounts or taxes, sending the quote to a prospective customer, and provisioning the corresponding services upon their acceptance.

[Finalize](#finalize)

[cancel](#cancel)

[cancel](#cancel)

When a customer rejects a quote or you no longer want it to be valid, you can cancel it. You can no longer accept canceled quotes. Quotes that are in a draft or open state automatically cancel when they reach the expiration date. Stripe generates a quote.canceled webhook.

​​After the customer agrees to your quote, you can mark it as accepted. Accepted quotes generate an invoice, subscription, or subscription schedule ​​automatically, depending on whether or not there are recurring prices on the quote or if the effective date of the quote is in the future.

## Workflow transitions

Quotes can transition between these statuses:

[POST /v1/quotes/:id/cancel](/api/quotes/cancel)

[POST /v1/quotes/:id/finalize](/api/quotes/finalize)

[POST /v1/quotes/:id/cancel](/api/quotes/cancel)

[POST /v1/quotes/:id/accept](/api/quotes/accept)

Quotes are initially created as a draft. In this status, you can edit the quote and make any required changes. ​​You can finalize a quote as soon as you’re ready to send it to the customer, which moves it to the open​ status while you await action from them.

Finalizing a quote also assigns a number to it. This number consists of four parts: the prefix QT, the customer’s invoice prefix, the quote sequence, and the revision sequence. For example, QT-68BB114-0001-1 is the first quote for a customer, and the quote is on the first revision. Quote number QT-68BB114-0001-2is the same quote but on the second revision. QT-68BB114-0002-1 would be the second quote for the customer.

You can finalize a quote through the API as shown in the following example.

You can mark a quote as accepted only if it’s in the open status. Doing so transitions the quote to the accepted status and creates the invoice, subscription or subscription schedule.

If the quote doesn’t have a recurring price on any of its line items, a draft invoice is created from the quote with auto_advance set to false. You can make modifications to the invoice before finalizing and sending it to your customer for payment.

If the quote has at least one recurring price on a line item, then a subscription or subscription schedule is created. A subscription schedule is created if the effective date on the quote is in the future, otherwise a subscription is created. The first invoice on the subscription is in draft status with auto_advance set to true.

In the Dashboard, you can mark a quote as accepted through the Convert to invoice and Convert to subscription buttons on the quote detail page. You can mark a quote as accepted through the API as shown in the following example.

You can cancel a quote if its status is draft or open. Cancel a quote through the Dashboard on the quote detail page, or using the API as shown in the following example.

The PDF method functions differently from the majority of the SDK methods you might be accustomed to that typically return data in JSON format. Instead, the PDF method has a unique output.

It directly returns a stream of data that represents the byte sequences of the incoming data.

In effect, instead of waiting for the entire data set to load before it becomes available, the byte stream can be read in ‘chunks’ or segments as the data streams in.

This method is especially useful for handling large data or real-time data processing, where you can start processing incoming data before the entire data load is complete.

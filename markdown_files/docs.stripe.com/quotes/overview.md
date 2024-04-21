htmlHow quotes work | Stripe Documentation[Skip to content](#main-content)How quotes work[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fquotes%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fquotes%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Quotes](/docs/quotes)# How quotes work

Learn about the quotes workflow.NoteYou can use quotes in test mode, but you must upgrade to Invoicing Plus or Billing Scale to unlock full functionality in live mode. See which plan is right for you.

​​Quotes allow you to deliver estimated pricing for requested goods or services and can help facilitate negotiation before beginning a subscription or invoice.

​​We designed the quote statuses to mirror a typical quoting flow that a sales agent follows, where they create a quote with line items that specify the items for purchase. This includes applying any discounts or taxes, sending the quote to a prospective customer, and provisioning the corresponding services upon their acceptance.

StatusDescriptionPossible actions`draft`​​Starting status for all quotes—at this point, you can still edit the quote.[Finalize](#finalize)the quote into`open`or[cancel](#cancel)the quote.`open`The quote is finalized and is now awaiting action from the customer. ​​You can only edit the expiration date now.Mark the quote as`accepted`or[cancel](#cancel)the quote.`accepted`​​The customer accepted the quote. The quote generates an invoice, subscription or subscription schedule.N/A`canceled`​​The quote expired or was canceled. You can no longer accept it.N/A### Canceled quotes

When a customer rejects a quote or you no longer want it to be valid, you can cancel it. You can no longer accept canceled quotes. Quotes that are in a draft or open state automatically cancel when they reach the expiration date. Stripe generates a quote.canceled webhook.

### Accepted quotes

​​After the customer agrees to your quote, you can mark it as accepted. Accepted quotes generate an invoice, subscription, or subscription schedule ​​automatically, depending on whether or not there are recurring prices on the quote or if the effective date of the quote is in the future.

## Workflow transitions

Quotes can transition between these statuses:

StatusAPI endpointEmitted webhookEnd Status`draft`[POST /v1/quotes/:id/cancel](/api/quotes/cancel)`quote.canceled``canceled``draft`[POST /v1/quotes/:id/finalize](/api/quotes/finalize)`quote.finalized``open``open`[POST /v1/quotes/:id/cancel](/api/quotes/cancel)`quote.canceled``canceled``open`[POST /v1/quotes/:id/accept](/api/quotes/accept)`quote.accepted``accepted`### Finalize draft quotes

Quotes are initially created as a draft. In this status, you can edit the quote and make any required changes. ​​You can finalize a quote as soon as you’re ready to send it to the customer, which moves it to the open​ status while you await action from them.

Finalizing a quote also assigns a number to it. This number consists of four parts: the prefix QT, the customer’s invoice prefix, the quote sequence, and the revision sequence. For example, QT-68BB114-0001-1 is the first quote for a customer, and the quote is on the first revision. Quote number QT-68BB114-0001-2is the same quote but on the second revision. QT-68BB114-0002-1 would be the second quote for the customer.

You can finalize a quote through the API as shown in the following example.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/quotes/qt_1HDGlYClCIKljWvsIGaAA06B/finalize \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`### Accept a quote

You can mark a quote as accepted only if it’s in the open status. Doing so transitions the quote to the accepted status and creates the invoice, subscription or subscription schedule.

If the quote doesn’t have a recurring price on any of its line items, a draft invoice is created from the quote with auto_advance set to false. You can make modifications to the invoice before finalizing and sending it to your customer for payment.

If the quote has at least one recurring price on a line item, then a subscription or subscription schedule is created. A subscription schedule is created if the effective date on the quote is in the future, otherwise a subscription is created. The first invoice on the subscription is in draft status with auto_advance set to true.

In the Dashboard, you can mark a quote as accepted through the Convert to invoice and Convert to subscription buttons on the quote detail page. You can mark a quote as accepted through the API as shown in the following example.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/quotes/qt_1HDGlYClCIKljWvsIGaAA06B/accept \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`### Cancel a quote

You can cancel a quote if its status is draft or open. Cancel a quote through the Dashboard on the quote detail page, or using the API as shown in the following example.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/quotes/qt_1HDGlYClCIKljWvsIGaAA06B/cancel \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`### Download a quote’s PDF

The PDF method functions differently from the majority of the SDK methods you might be accustomed to that typically return data in JSON format. Instead, the PDF method has a unique output.

It directly returns a stream of data that represents the byte sequences of the incoming data.

In effect, instead of waiting for the entire data set to load before it becomes available, the byte stream can be read in ‘chunks’ or segments as the data streams in.

This method is especially useful for handling large data or real-time data processing, where you can start processing incoming data before the entire data load is complete.

Command Line[curl](#)`curl https://files.stripe.com/v1/quotes/qt_0J1EnX589O8KAxCGEdmhZY3r/pdf \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
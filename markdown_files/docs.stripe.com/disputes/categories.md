htmlDispute categories | Stripe Documentation[Skip to content](#main-content)Categories[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fcategories)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fcategories)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)[Responding to disputes](/docs/disputes/responding)# Dispute categories

Learn more about the reasons for disputes and how to respond to each.### Learn how to prevent disputes

Disputes happen all the time for lots of reasons, but there are ways you can protect your business. Refer to our prevention guide to learn how.

Each card network defines hundreds of codes representing very specific reasons for dispute claims, many of which overlap across all the networks that Stripe does business with. Stripe maps each network code into one of eight categories, based on the general claim and the evidence you need to submit to effectively challenge that type of claim.

## Dispute network reason codes categorization

The following tables show the Stripe categories for each card network’s dispute reason codes. Network reason code is available on the dispute object.

VisaMastercardAmerican ExpressDiscoverKlarnaPayPalStripe CategoryVisa CodeCredit not processed- 13.6 Credit not processed
- 13.7 Cancelled Merchandise/Services

Duplicate- 12.6.1  Duplicate processing
- 12.6.2  Paid by other means

Fraudulent- 33    Fraud analysis request
- 10.1  EMV Liability Shift Counterfeit Fraud
- 10.2  EMV Liability Shift Non-Counterfeit Fraud
- 10.3  Other Fraud - Card Present Environment
- 10.4  Other Fraud - Card Absent Environment
- 10.5  Visa Fraud Monitoring Program

General- 28    Request for copy bearing signature
- 30    Cardholder request due to dispute
- 34    Legal process request
- 11.1  Card Recovery Bulletin
- 11.2  Declined Authorization
- 11.3  No Authorization
- 12.1  Late Presentment
- 12.2  Incorrect Transaction Code
- 12.3  Incorrect Currency
- 12.4  Incorrect Account Number
- 12.5  Incorrect Amount
- 12.7  Invalid Data
- 13.8  Original Credit Transaction Not Accepted

Product not received- 13.1	Merchandise/Services Not Received
- 13.9	Non-Receipt of Cash or Load Transaction Value

Product unacceptable- 13.3	Not as Described or Defective Merchandise/Services
- 13.4	Counterfeit Merchandise
- 13.5	Misrepresentation

Subscription canceled- 13.2	Cancelled Recurring

UnrecognizedNone## General evidence for all dispute categories

While each dispute reason requires specific types of evidence to show why the payment should stand, some types of evidence are universal for all dispute responses.

Evidence file size limitsSubmit as much relevant evidence as possible while keeping the size and length of the final file within card issuer maximums:

- 4.5 MB for all networks
- 19 pages for Mastercard. See[Limit evidence file length](/disputes/best-practices#limit-file-length)for recommendations.

### Discrediting evidence

Providing evidence of one of the following has a high likelihood of proving a dispute invalid and overturning the chargeback:

EvidenceDashboard Evidence CategoryAPI Evidence ParameterAny documentation of the account owner[withdrawing the dispute](/disputes/withdrawing).Customer communication`customer_communication`Proof that you already compensated the customer before they initiated the dispute (either within Stripe or using some other method).Customer communication`refund_refusal_explanation`### Background evidence

The following types of evidence are relevant for most dispute types. Include them in every dispute response when possible. In the API, all of these data points are attributes of the dispute evidence object. In the Dashboard, many of them are fields of information separate from the Supporting evidence section of the response form.

When your integration supports it, Stripe automatically captures most of the data for background evidence and pre-populates both the API evidence object attributes and the form fields in the Dashboard. The more information your integration collects and passes to Stripe when your customer makes a payment, the better your ability to prevent disputes and fraud from occurring, and challenge them effectively when they do.

EvidenceDashboard Evidence CategoryAPI Evidence ParameterThe billing address provided by the customer (if the[AVS](/disputes/prevention/verification#avs-check)check was successful). This field is automatically filled when possible.Billing address`billing_address`The name of the customer. This field is automatically filled when possible.Customer name`customer_name`The email address of the customer. This field is automatically filled when possible.Email`customer_email_address`The IP address that the customer used when making the purchase. When possible, Stripe captures this data in the response and expands it to include geographical data.Other`customer_purchase_ip`A relevant document or contract showing the customer’s signature.Customer signature`customer_signature`Any communication with the customer that you feel is relevant to your case (for example, emails proving that they received the product or service, or demonstrating their use of or satisfaction with the product or service). If you have multiple items of this type, consolidate them into a single file.Customer communication`customer_communication`Any receipt or message sent to the customer notifying them of the charge. This field is automatically filled with a Stripe generated email receipt if any such receipt was sent.Receipt`receipt`A description of the product or service and any relevant details on how this was presented to the customer at the time of purchase.Product or service details Description`product_description`## Compelling evidence for Visa disputes

The Visa network has a technical specification for the evidence required to overturn disputes with a reason of fraudulent, which they call Compelling Evidence.

You must provide at least one item (more is always better) that satisfies Visa’s Compelling Evidence specification for fraud disputes. Examples of evidence that meet Visa’s specification are labeled as Compelling Evidence in the Dashboard and in the fraudulent dispute type documentation.

If you don’t submit Compelling Evidence, your likelihood of overturning a Visa fraud dispute is very low, and while Visa is the only card network that designates this specification, Stripe recommends you apply the practice to all disputes.

### Visa CE 3.0

Visa Compelling Evidence 3.0 (CE 3.0) introduced new qualifying criteria that allows businesses to show prior non-fraudulent history with the cardholder to combat friendly fraud. Submitting qualifying evidence for Visa CE 3.0 eligible disputes significantly increases the likelihood of an issuer overturning friendly fraud disputes in favor of the business. Stripe supports this feature by:

- Flagging disputes that are eligible for Visa CE 3.0 by searching your history for prior qualifying transactions
- Notifying you in the dispute email and in the[Dispute details page](https://dashboard.stripe.com/test/disputes)that the dispute qualifies for a Visa CE 3.0 counter response.
- Automatically adding qualifying transactions to your dispute evidence.
- Identifying required elements in the evidence form withRequired for Visa CE 3.0badge.
- Pre-populating required information from qualifying transactions, when available.

If you get a dispute that qualifies for a Visa CE 3.0 counter response, we recommend that you submit evidence.

Read more about Visa CE 3.0 in our Support FAQ.

## Dispute category types

Use the selector to choose the category that matches the reason given for your dispute to see guidelines for responding.

Credit not processedDuplicateFraudulentGeneralProduct not receivedProduct unacceptableSubscription canceledUnrecognizedThe customer claims they’re entitled to a full or partial refund because they returned the purchased product or didn’t fully use it, or the transaction was otherwise canceled or not fully fulfilled, but you haven’t yet provided a refund or credit.

### How to prevent it

- Have a clear return or cancellation policy that’s easy to find or explicitly disclosed to the customer prior to purchase.
- Honor your written policies promptly when a customer requests and is entitled to a full or partial refund.

### How to overturn it

Explain and demonstrate one or more of the following:

- You already issued the refund your customer is entitled to
- The customer isn’t entitled to a refund
- The customer[withdrew the dispute](/disputes/withdrawing)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- Physical productsare tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- Digital products or servicesare often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- Offline servicesinclude purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

evidence you can submit for:Physical productDigital product or serviceOffline serviceFor this type of recommended evidenceDesignate this Dashboard label or API parameterThe language of your refund policy, as provided to the customer. This might be:- The text copied from your policy page
- A screenshot of the policy on a receipt
- A PDF of the applicable part of your business’s terms and conditions

`refund_policy`An explanation of how and where the applicable policy was provided to your customer prior to purchase.`refund_policy_disclosure`Your explanation for why the customer isn’t entitled to a refund, or no further refund, if you already issued a partial refund.`refund_refusal_explanation`Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

- A screenshot of a text conversation
- A PDF of an email exchange
- A PDF of your written account of a phone conversation, including dates of contact

customer_communication

Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

- Whether you already issued the refund the cardholder is entitled to
- Whether or not the customer returned the merchandise in whole or in part. If they partially used the merchandise or returned it, or whether the dispute amount exceeds the value of the unused portion
- Whether the cardholder withdrew the dispute

uncategorized_text uncategorized_file

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Dispute network reason codes categorization](#network-code-map)[General evidence for all dispute categories](#general-evidence)[Compelling evidence for Visa disputes](#compelling-evidence-for-visa-disputes)[Dispute category types](#dispute-category-types)Related Guides[Responding to disputes](/docs/disputes/responding)[Dispute withdrawals](/docs/disputes/withdrawing)[Preventing disputes and fraud](/docs/disputes/prevention)Products Used[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
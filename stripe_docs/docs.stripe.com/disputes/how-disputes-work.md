# How disputes work

A dispute occurs when an account owner contacts their bank to contest a payment to you for a number of possible reasons. When someone files a dispute, the process varies slightly across different card networks, but typically follows a standard pattern shown here:

[reasons](/disputes/categories)

When an account owner disputes a charge to their payment account, Stripe:

- Notifies you of the dispute through the Stripe Dashboard, email, webhooks, and the API

[webhooks](/webhooks)

- Debits the disputed amount, plus a dispute fee, from your Stripe account

- Provides you with an explanation of the dispute and access to the account owner’s claim to their bank

- Steps you through the process of submitting convincing evidence to counter the dispute

Throughout this process, Stripe facilitates your case, but doesn’t have influence over the outcome, which is at the sole discretion of the account owner’s bank.

## Before the dispute

Sometimes, Stripe alerts you to pre-dispute notifications before an actual dispute is filed. Pay attention to these notifications because:

- You might avoid a dispute entirely with proactive customer service and transaction clarification

- Failure to respond in the pre-dispute phase can have negative implications in the formal dispute phase

Early fraud warnings (EFWs) are messages sourced from Visa TC40 reports and Mastercard SAFE (System to Avoid Fraud Effectively) reports that card issuers on these two networks generate to flag payments they suspect might be fraudulent. The networks require issuers to report fraud, but that requirement doesn’t affect an issuer’s decision whether to initiate a dispute.

As with any fraud signal, EFWs don’t require any action or response from you. You can proactively refund the charge to prevent the cardholder from initiating a dispute, or you might wait and see if a fraud dispute happens. Unless the payment was covered by the liability shift rule, 80% of EFWs convert into a fraud dispute if you do nothing. If the payment was covered by liability shift, then you might still receive a dispute. In that case, Stripe automatically provides some evidence for you, such as data from 3D Secure.

[refund the charge](/disputes/prevention/best-practices#consider-proactively-refunding-suspicious-payments)

[liability shift](/payments/3d-secure/authentication-flow#disputed-payments)

[3D Secure](/payments/3d-secure)

Automatically refunding all EFWs regardless of the likelihood of escalation isn’t a good strategy. If you’re too aggressive in issuing refunds for all EFWs, you’ll inevitably refund some transactions that would never have become disputes.

All other things being equal, our analysis suggests that the optimal point for issuing a refund on early fraud warnings is on charges that are roughly less than or equal to your dispute fee. It’s probably not worthwhile to refund EFWs on charges more than 35 percent higher than your dispute fee.

[dispute fee](/disputes/how-disputes-work#dispute-fees)

Proactively refunding a flagged payment doesn’t affect the fraud warning. The only time a refund can prevent a fraud report is when it’s processed as a reversal, which usually happens within 2 hours of the payment capture.

The main exception to the optimal refund strategy above is if you have reason to worry about the effect of the dispute itself on your business or account.

If any of the conditions described under the Best practices for preventing fraud apply to your situation, it makes sense to more aggressively refund EFWs.

[Best practices for preventing fraud](/disputes/prevention/best-practices#consider-proactively-refunding-suspicious-payments)

Although it’s called an early fraud warning, it’s possible to receive an EFW even after you receive a fraud dispute on a charge. This is generally because the systems the networks use to process EFWs are separate from the systems they use to process disputes, and the two aren’t necessarily in sync.

You can listen for EFW webhooks using our API.

[webhooks](/webhooks)

[API](/api/radar/early_fraud_warnings)

Some card networks initiate a preliminary phase before creating a formal dispute and chargeback. Stripe calls this preliminary phase an inquiry, though these are sometimes also called a “retrieval” or a “request for information”. American Express and Discover are the networks that most often use this phase, while Mastercard and Visa don’t use it anymore.

[chargeback](/disputes)

During the inquiry phase, the cardholder’s bank requests transaction clarification, often because the cardholder doesn’t recognize the transaction description. You can resolve the case without incurring a dispute fee by either providing satisfactory evidence that answers the dispute type for the inquiry, or by issuing a full refund. Inquiries on partially refunded charges can still escalate to a chargeback.

[dispute type](/disputes/categories)

Stripe presents EUR bank transfer recall requests as Inquiries in the Dashboard. From the Inquiry details page, you can either decline the recall, which closes it with no further action, or you can refund the bank transfer. If you take no action, the inquiry is automatically rejected.

[bank transfer recall](/payments/customer-balance/recalls)

With charges on American Express and Discover cards, failing to respond to an inquiry can signal to the issuer your implicit acceptance of the claim, resulting in an escalation to a formal, and likely unwinnable, chargeback. Unless you intend to accept financial liability, always respond to inquiries immediately, and make every effort to resolve issues amicably with your customer during this stage.

The Dashboard payment page describes inquiries as an “inquiry” or “dispute inquiry”, and as a “warning” or “dispute warning” in the API events summary, to mirror the language in the API.

If an inquiry has been open for 120 days without escalation to a chargeback, Stripe marks it as closed in the Dashboard and API. At this point, you can be confident the card network won’t escalate it—they don’t provide an explicit “win” message for inquiries.

## During the dispute

Whether it’s because of an inquiry that escalated, or for some other reason, when an account owner files a formal dispute against a payment, the action initiates a chargeback where the card network pulls the funds for the dispute from your Stripe balance and holds it for the entire duration of the dispute. This might be for the full amount of the charge or a different amount. Why the debited amount is different from the original payment

[Why the debited amount is different from the original payment](#disputed-amount)

The initiation of a dispute triggers several processes:

- The card network debits Stripe for your disputed payment and related dispute fees

- Stripe in turn debits your Stripe balance for the disputed amount plus a dispute fee

- You can’t issue a refund outside the dispute process while the dispute is open

- Your dispute rate with that card network increases

[dispute rate](/disputes/measuring)

Card networks typically allow cardholders to initiate disputes within 120 days of the original payment, but their rules allow more time in some situations. Certain industries, such as travel or event ticketing—where the payment might be made long before the event occurs—are prone to longer time intervals between the original purchase and a dispute. Generally speaking, when a customer makes a payment for something that will happen in the future (like a vacation reservation, a professional services appointment, or an event ticket), the clock starts on the date of the event, not the date of the payment.

Following the creation of the chargeback, you have a limited amount of time (usually 7-21 days, depending on the card network) to respond to the card issuer.

If you submit evidence, the issuer also has a limited amount of time (usually 60–75 days, depending on the card network) to evaluate the evidence and decide the outcome.

The full lifecycle of a dispute, from initiation to the final decision from the issuer, can take as long as 2-3 months to complete. There are no actions a business can take to reliably accelerate this timeline, other than to decline to contest the dispute by accepting it in the Dashboard or API.

At the completion of the dispute process, the issuer either overturns the dispute in your favor or upholds the dispute in their cardholder’s favor.

If the issuer overturns the dispute, they return the debited chargeback amount to Stripe, and Stripe passes this amount back to you.

If the issuer upholds the dispute, nothing changes from your perspective and no money moves—Stripe credited the issuer when they initiated the chargeback. The issuer will return the funds to the cardholder at some point during—or even after—this process. The timing of the cardholder’s credit is entirely at the issuer’s discretion.

The dispute fee for your country can be found on the Stripe Pricing page. This fee is deducted from your account balance when a cardholder initiates a dispute.

[on the Stripe Pricing page](https://www.stripe.com/pricing)

For businesses outside Mexico, the dispute fee is nonrefundable. For businesses in Mexico, the dispute fee for a won or withdrawn dispute might be returned.

For businesses in the Single Euro Payments Area (SEPA), cards processed on the Cartes Bancaires network incur no dispute fee.

[Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)

[Cartes Bancaires network](/payments/cartes-bancaires)

In most cases, you have the ability to challenge a disputed payment, as long as you submit strong evidence to the card issuer that invalidates the dispute claim before the deadline.

As soon as a dispute is active, the only way to overturn it is by submitting evidence in a response. Even in cases where your customer claims to have withdrawn the dispute, you must respond with evidence for the dispute to be closed in your favor. Submitting evidence is what signals to the issuer that you don’t accept the dispute and want to have the funds returned to you.

[withdrawn the dispute](/disputes/withdrawing)

See Responding to disputes for information on how to:

[Responding to disputes](/disputes/responding)

- Review the cardholder’s claim

- Evaluate whether to accept or challenge the dispute

- Gather appropriate evidence to respond to the dispute

- Use the Dashboard or API to submit your response

You can’t challenge some types of disputes under the rules of the card network they were processed on. In general, Stripe immediately closes them as lost as soon as we notify you about them, and you have no opportunity to present evidence to the issuer.

The Dashboard payment page and timeline describes these disputes as those where the card issuer doesn’t allow you to submit evidence.

- Inquiries for Discover cards can turn into unchallengeable disputes if you don’t submit evidence for the inquiry.

[Inquiries](#inquiries)

- The Cartes Bancaires network requires a higher standard of evidence from the cardholder before allowing them to initiate a dispute, but then prohibits you from challenging the dispute. This affects only businesses in the Single Euro Payments Area (SEPA) processing payments on the Cartes Bancaires network, and not businesses elsewhere charging cards issued by Cartes Bancaires. Learn more at Cartes Bancaires.

[Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)

[Cartes Bancaires](/payments/cartes-bancaires)

In extremely rare cases, you might receive more than one dispute per payment. This can happen when a customer files a new dispute with a different reason code, for a new line item in the original transaction, on multi-capture payments or simply because the issuer acquired new information about the payment allowing them to refile a dispute.

Handle each dispute the same way as any other dispute; each dispute requires you to either accept or counter the dispute. Pay special attention to the outlined amount, currency, category, and claim details before managing the dispute. Learn more here.

[Learn more here](https://support.stripe.com/questions/receiving-multiple-disputes-per-payment-faq)

A disputed amount might be lower or higher than the amount of the original charge. The following table outlines some of the most common reasons for this difference.

[Disputes on partially refunded payments best practice](/disputes/best-practices#partial-refund-bp)

## After the decision

After you submit your evidence, the next notification from the card issuer to both Stripe and you is the final decision. Stripe updates the status of the dispute to won or lost and notifies you through the Stripe Dashboard, email, and any other configured communication channels as soon as the issuer makes its decision clear.

This outcome is final for all parties. You can’t overturn a lost dispute, but your customer also can’t overturn a dispute decided in your favor.

Some card networks support an arbitration phase for lost disputes that carries a substantial fee of around 500 USD, but Stripe doesn’t support this dispute phase.

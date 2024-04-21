# Issuing disputes

You can’t dispute an authorization. Acquiring businesses reverse authorizations at their discretion. You can file a dispute after the authorization is complete and the acquiring business captures the transaction.

The purpose of a dispute is to recover funds for captured transactions. Disputes are often used to correct fraudulent transactions or problems with the quality or delivery of the product.

Stripe offers a guided Dashboard process and an API to submit disputes and monitor them through to resolution. This process typically takes between 30 and 90 days. For users managing occasional disputes, we recommend using the Dashboard. Users that handle a high volume of disputes may find it easier to programmatically manage disputes using the API.

If you think a card has been compromised, cancel and replace it using the Dashboard or the API before continuing with the dispute process.

[cancel and replace it](/issuing/cards/physical/standard#cancelling-cards)

## Considerations before initiating a dispute

Check the transaction’s dispute eligibility.

- The transaction must be a capture and not a refund.

The transaction must be a capture and not a refund.

[capture](/issuing/purchases/transactions)

- Fewer than 110 days have passed since the business captured the transaction.However, if you plan to file a no-authorization dispute (categorized as other), this deadline is shorter:For Visa, the transaction was captured fewer than 65 days ago.For Mastercard, the transaction was captured fewer than 80 days ago.

Fewer than 110 days have passed since the business captured the transaction.

- However, if you plan to file a no-authorization dispute (categorized as other), this deadline is shorter:For Visa, the transaction was captured fewer than 65 days ago.For Mastercard, the transaction was captured fewer than 80 days ago.

- For Visa, the transaction was captured fewer than 65 days ago.

- For Mastercard, the transaction was captured fewer than 80 days ago.

- The transaction isn’t a mobile push payment transaction.

The transaction isn’t a mobile push payment transaction.

- If you’re considering filing a fraud dispute, consider the following:For Visa card-absent fraud: Verify whether fewer than 35 fraud disputes have been lodged on the credit card in the last 120 days.For any type of Mastercard fraud disputes: Check whether the credit card has fewer than 35 fraud disputes filed over its entire lifespan.

If you’re considering filing a fraud dispute, consider the following:

- For Visa card-absent fraud: Verify whether fewer than 35 fraud disputes have been lodged on the credit card in the last 120 days.

- For any type of Mastercard fraud disputes: Check whether the credit card has fewer than 35 fraud disputes filed over its entire lifespan.

In the Dashboard, the Dispute transaction button is only enabled for eligible transactions. Similarly, in the API, attempting to dispute an ineligible transaction results in an error.

Next, ensure that the cardholder has exhausted other means of resolving the issue. They must attempt to return any products they received, cancel any ongoing services, and seek a refund directly from the business. Collect documentation of these attempts to use as evidence when filing the dispute.

Although you can file disputes in any language, our partner payment networks only acknowledge evidence in English or with an English translation.

## Lifecycle

In the above diagram, merchant refers to the acquiring merchant, the business receiving the payment.

Newly-created disputes begin in an unsubmitted status. At this point, you can update their evidence and metadata. After you’ve added all the required evidence, you can then submit the dispute. If you don’t submit a dispute within 110 days of the transaction clearing, its status becomes expired.

Stripe and card networks process disputes that have a status of submitted. As such, you can’t update dispute evidence, but you can still update their metadata. Submitted disputes enter into a multi-step process defined by card networks and participating banks. After a dispute is resolved, Stripe transitions it to either the terminal won or lost status.

## Creation

Fill out the Dispute Amount field to indicate the disputed amount (full or partial). The field’s initial value is the transaction amount. Submissions that have empty Dispute Amount fields create disputes with the full transaction amount.

Dispute Amount field on the Issuing dispute creation page

Click Dispute transaction when viewing an eligible transaction. You’ll be redirected to a form which requests different information based on the dispute reason and product type (merchandise, services or digital goods). A dispute is created the first time you click Save. If you click Submit without saving, we create a dispute before submitting it.

Once you submit a dispute, you can’t modify the information or resubmit the dispute.

## Update

Use the Unsubmitted tab to access disputes that are in progress. The Submit before date indicates when the dispute expires.

From the individual dispute page, click Edit submission to access the form where you can update the evidence.

## Submission

The Submit button on the evidence form is enabled when all required evidence is present.

Review the evidence thoroughly before you submit, because you can’t modify dispute information after submitting the dispute.

## Resolution

Dispute statuses are updated once we hear back from the card network. If the acquiring business wins the dispute, the dispute’s status changes to lost and no funds are transferred.

If you win the dispute, the status changes to won and funds are transferred back to your Issuing balance. The credit to your account takes the form of a balance transaction of type “Issuing dispute” accessible in the Dashboard under All transactions and on the bottom of the dispute detail page.

[balance transaction](/reports/balance-transaction-types#issuing_related)

[All transactions](https://dashboard.stripe.com/balance)

Viewing a dispute’s balance transactions in the Dashboard.

Stripe is bound by rules that are set by the card network, and these rules can change twice a year. You can review these rules by network:

- Visa: Visa Core Rules and Visa Product and Service Rules

[Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf)

- Mastercard: Mastercard Rules

[Mastercard Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)

If you make a transaction in a currency that’s different from your account’s default currency (for example, a GBP transaction that your USD card pays), Stripe refunds the won dispute in the transaction’s original currency.

## Testing

Stripe processes test mode disputes as if they are live to demonstrate the expected behavior. For example, we fire off webhook events, create balance transactions, and update your Issuing balance. All this happens in the seconds after you submit the dispute.

[balance transactions](/reports/balance-transaction-types)

Select the desired test mode outcome on the top panel of the submission form. Selecting Won or Lost causes the explanation field to be auto-filled with “winning_evidence” or “losing_evidence” respectively to record the selected outcome.

Similar to live mode, a test mode dispute transitions to expired 110 days after the transaction is captured.

## Webhooks

You can register a webhook endpoint to be informed of changes to your disputes. All Issuing dispute webhooks contain the latest Dispute object.

[webhook](/webhooks)

[Dispute](/api/#issuing_dispute_object)

## Dispute reasons and evidence

The strongest disputes have clear explanations and descriptive responses to required fields. This information is what is used to weigh whether the dispute leans in favor of the cardholder or merchant. Users should aim to provide as much documentation and information as possible. In addition, it’s imperative to review and select the correct dispute reason when filing as these directly impact the supportive information needed to win or lose the dispute.

Disputes can be submitted with one of these reasons:

- Canceled: Cardholder canceled or returned merchandise or canceled services, and the merchant didn’t process a credit or void a transaction receipt.

- Duplicate: Covers processing error dispute types, including duplicate transaction, incorrect amount, paid by other means, and so on.

- Fraudulent: The cardholder’s details were compromised and the transaction wasn’t authorized by the cardholder.

- Merchandise not as described: Cardholder received the merchandise, but it didn’t match what was presented at time of purchase, or it was damaged or defective.

- Service not as described: Cardholder received the service, but it didn’t match what was presented at time of purchase.

- Not received: Cardholder participated in the transaction but didn’t receive the merchandise or service.

- Other: A dispute scenario that doesn’t clearly qualify as any other dispute reason.

In the Dashboard, “Merchandise not as described” and “Service not as described” are consolidated under “Not as described”.

Each reason requires a different set of evidence:

A transaction might be disputed as fraud if the cardholder believes their card details are compromised and they didn’t authorize the transaction. If a fraudulent transaction occurs on a card, that card should be canceled before filing a dispute.

Before filing a dispute, users should confirm with the cardholder that the transaction wasn’t made in error by the cardholder, or made by someone known to the cardholder. Transactions made by a friend or family member, for example, don’t constitute fraud for dispute purposes.

A card network might automatically reject a fraud dispute if it was a card-present transaction, because liability defaults to the issuer.

In a Card-Not-Present transaction, the dispute could automatically be rejected by the card network if the merchant attempted 3DS.

## Withdrawing

Once a dispute has been submitted, we can only attempt to withdraw the dispute within one day of its submission. If you want to attempt to withdraw the dispute, please contact Stripe support as soon as possible.

[Stripe support](https://support.stripe.com/contact)

## Liability for fraud (platforms in the USA)

Most aspects of Regulation Z don’t apply to business-purpose cards, but Regulation Z does protect users of business-purpose cards from fraud and other types of “unauthorized card use," which means the use of a charge card by a person who doesn’t have the authority to use it. In most cases, an accountholder can’t be held responsible for unauthorized use of cards linked to their account unless a reasonable investigation into the fraud is conducted. However, if the account holder has 10 or more employee authorized users, they might not qualify for this protection.

When one of your users disputes a transaction because the user believes it was unauthorized, Stripe sends the dispute to the card network for adjudication (as with any other type of disputed transaction). Stripe or the card network determines who must pay for the fraud: you or the merchant.

If Stripe or the card network determines the merchant is liable for the fraud, then neither you nor your user are responsible for the disputed transactions.

If Stripe or the card network determines that you’re liable for the fraud, then you might be required to pay for the disputed transaction. Stripe performs a reasonable investigation into the dispute to determine whether fraud actually occurred or whether the user doesn’t qualify for protection under Regulation Z. If the investigation uncovers that unauthorized card use actually occurred and that the user qualifies for protection, then you remain liable for the unauthorized transactions. Alternatively, if the investigation uncovers that unauthorized card use didn’t occur or that the user doesn’t qualify for protection, then we hold the accountholder responsible for the disputed charges.

## Emailing connect accounts

Issuing platforms must send regulated notice emails to connected accounts when a dispute is submitted, and again when a dispute is won or lost. Learn more about regulated notices.

[Learn more about regulated notices](/issuing/compliance-us/issuing-regulated-customer-notices)

## Use with Stripe Treasury

Disputes of ReceivedDebits on FinancialAccounts have a corresponding DebitReversal once the dispute is submitted.

[DebitReversal](/api/treasury/debit_reversals)

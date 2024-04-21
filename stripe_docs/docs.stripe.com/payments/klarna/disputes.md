# Respond to disputes

You can counter wrongful chargeback disputes in the Stripe Dashboard or with the API. You must submit evidence to counter chargeback disputes.

[submit evidence](/payments/klarna/disputes#evidence-submission)

Almost all disputes begin as inquiry disputes, except for fraudulent transaction disputes, which escalate immediately to chargeback disputes. You must contact your customer directly and attempt to resolve the inquiry dispute within 21 days. During this period, you can’t submit evidence to Klarna in the Stripe Dashboard or with the API. You can close the inquiry, accepting the customer’s dispute, by issuing a refund equal to the amount the customer is disputing. Confirm this amount is correct with the customer before issuing the refund. You aren’t charged a dispute fee for transactions refunded during the inquiry stage.

If you fail to resolve the dispute within this 21 day time frame, the inquiry dispute automatically becomes a chargeback dispute. Stripe withholds the disputed funds and the associated dispute fee from your account for chargeback disputes.

[dispute fee](https://support.stripe.com/questions/klarna-fees-and-dispute-automation-will-be-introduced-starting-november-15-2023)

For chargeback disputes, you can counter the dispute by submitting one single round of evidence in the Stripe Dashboard or with the API. You have 12 days to submit this evidence from the creation date of the chargeback dispute. If you counter the dispute, Klarna evaluates your evidence and decides the final outcome. If you win the dispute, Stripe releases the withheld funds to your account. If you lose the dispute, Stripe debits the withheld funds, including the dispute fee. Klarna then returns the disputed amount to the customer.

[dispute fee](https://support.stripe.com/questions/klarna-fees-and-dispute-automation-will-be-introduced-starting-november-15-2023)

You resolve the inquiry dispute without chargeback escalation

Stripe doesn’t withhold funds for resolved inquiry disputes, and we don’t apply any dispute fees.

You win the chargeback dispute after escalation:

When a chargeback dispute is created, Stripe withholds the disputed funds, including the dispute fee, until Klarna informs us about the dispute outcome. If you win the dispute, we immediately release the funds to your account, and don’t charge a dispute fee.

You lose the chargeback dispute after escalation:

When a chargeback dispute is created, Stripe withholds the funds, including the dispute fee, until Klarna informs us about the dispute outcome. If you lose the dispute, we release the funds to Klarna and charge the dispute fee.

[dispute fee](https://support.stripe.com/questions/klarna-fees-and-dispute-automation-will-be-introduced-starting-november-15-2023)

Prior to November 15 2023, Stripe only supported disputes for Klarna through emails directly from Klarna to you. Now, Klarna disputes are managed in the Stripe Dashboard and with the API. This table highlights key differences between the old email-based disputes process and the new Dashboard and API process:

When an inquiry dispute starts off as an email dispute, it persists as an email dispute, even after onboarding to use the Dashboard or API for new disputes. If you lose an email dispute, it displays as lost in the Dashboard, you receive a webhook, and Stripe applies the dispute fee.

[dispute fee](https://support.stripe.com/questions/klarna-fees-and-dispute-automation-will-be-introduced-starting-november-15-2023)

## Evidence submission

To submit evidence against a chargeback dispute, use either the Dashboard or API:

## Submit evidence

- Navigate to the Disputes Dashboard, and click the Needs Response tab.

[Disputes Dashboard](https://dashboard.stripe.com/disputes)

- Click the disputed payment. If you want to counter the dispute, click Counter dispute.

- Select the reason why you should win the dispute, and click Next.

- Enter and attach all the applicable supporting evidence. The recommended label indicates the best documents for the type of dispute.

- After entering all the evidence, verify the information is correct by selecting the checkbox.

- Click Submit Evidence.

For additional guidance on how to submit evidence, see Responding to disputes.

[Responding to disputes](/disputes/responding)

If you fail to submit evidence, Klarna will rule the dispute in favor of the customer.

[OptionalAccept dispute loss](#accept-loss)

## OptionalAccept dispute loss

## Guidelines

Follow these guidelines to submit the most relevant evidence for both Dashboard and API disputes.

- Attach all the shipping details, such as the tracking number, carrier, shipped date, and customer communication.

- If you receive the returned product, attach the date when the customer initiated the return and any other information related to the return.

- If the customer confirms that the dispute is for a partial order, share the customer communication and the return order amount.

- If the return hasn’t been received, share when the customer initiated the return and note that the return hasn’t yet been received.

- If the customer didn’t communicate or failed to reply to your request, document in the evidence when your team attempted to contact the customer, the number of attempts made, and the lack of response received.

- If you fully or partially refunded the payment prior to it becoming a chargeback dispute, attach the refund details.

- Share the shipping policy as an attachment or link to your shipping policy.

- If the customer confirms that the price is incorrect, attach all the supporting documents against the claim, such as order details.

- If you fully or partially refunded the payment prior to it becoming a chargeback dispute, attach the refund details.

[Create test disputes](#create-test-disputes)

## Create test disputes

You can simulate dispute creation in test mode by creating a transaction in test mode using the following email addresses and phone numbers in the given Klarna checkout region. A dispute automatically opens on the transaction. You can submit evidence on the dispute, but you can’t simulate the final dispute outcome in test mode.

Below, we have specially selected test data for the currently supported customer countries.

## See also

- Responding to disputes

[Responding to disputes](/disputes/responding)

- Dispute Categories

[Dispute Categories](/disputes/categories)

- Dispute evidence object

[Dispute evidence object](/api/disputes/evidence_object)

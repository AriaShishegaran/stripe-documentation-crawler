# Review tools

While Stripe’s programmatic systems work to detect fraudulent verifications, you can perform manual reviews to provide an extra layer of fraud protection.

For example, you might want to review verifications when:

- Your customer submits a document from an unexpected country

- Your customer contacts you about a potential mistake in their verification

- Your business requirements differ from Stripe Identity’s default risk thresholds

Manual reviews and insights in Stripe Identity allow you to examine unusual verifications and update verification statuses.

[insights](/identity/insights)

## Reviewing verifications

You can review verifications in two ways. The list view allows you to scan a list of verifications without seeing details about a verification, while the detailed view provides more context.

[list view](#list-view)

[detailed view](#detailed-view)

The list view contains information to help you quickly get a sense of the state of each verification. It includes information on overall verification status, document country, extracted name, and individual verification check status.

Verification list view

To see more information about a verification before making a decision, select the verification from the list view to navigate to a detailed view. In this view, you can inspect the individual images collected alongside available insights.

[insights](/identity/insights)

After you review a verification, take one of the following actions:

- Override status: Manually override the verification status to match your decision on whether or not the customer is verified. Stripe sends a webhook event with the new status.

[webhook event](/identity/handle-verification-outcomes)

- Add to blocklist: Add the document to a blocklist to programmatically block future verifications completed with the same document.

When processing new verification attempts, Stripe reviews your completed verifications for duplicate identities using biometric data (for example, based on a selfie) to make sure that each identity is unique.

If we detect a duplicate selfie, we’ll share a list of verification sessions where the duplicate is detected and how many times it’s found in each session.

## Block list

The block list prevents individuals from using data for verification after you add it to the block list. All future verifications processed with matching data are programmatically marked as ‘unverified‘.

We support adding block list items of the following types:

- Document: matches against the combination of the type of the document, the document number, and the document country.

- Selfie: matches against the facial mapping of the selfie image uploaded during verification.

If you believe there are any mistakes with the block list outcome, you can manually overturn Stripe’s automated decision by overriding the status.

[overriding the status](#actions)

From the Identity Dashboard, find the VerificationSession containing the data you want to add to the block list. Navigate to the overflow menu ​​() in the top right, then select Add to list.

[Identity Dashboard](https://dashboard.stripe.com/identity)

On the block list item details page, you can click Disable in the top right. After you confirm your decision in a modal, it disables the item, and future verifications that have data that match are no longer programmatically unverified.

If you wish to re-enable a block list item, you can visit the VerificationSession that initially created it and create a new item with the same data.

By default, if you redact a VerificationSession the associated list items are deleted as well.

If you want to delete an individual list item, you can click Delete in the top right corner of the block list item details page. After you confirm your decision in a modal, the item is permanently disabled and the underlying data is redacted.

## Identity reports

In this report, you can see usage and verification rates over time, including how users progress through the different stages of the verification funnel. This data is reported from your live verification sessions and doesn’t include test mode sessions.

To access Identity reports from your Stripe Dashboard, navigate to More > Reports, then select Identity. Generate a report by selecting a date range. The earliest date you can choose is when you began using Identity.

[Identity reports](https://dashboard.stripe.com/identity/overview)

[Stripe Dashboard](https://dashboard.stripe.com/)

Stripe calculates the reporting metrics for VerificationSessions in a number of ways:

[VerificationSessions](/identity/verification-sessions)

- Verifications created: The total number of verifications created, including those that are abandoned, canceled, redacted, or otherwise unfinished.

- Verifications started: The number of verifications that a user visited and then started the verification process for.

- Verification submitted: The number of verifications that were completed and submitted by a user. You’re charged for every submitted verification, regardless of the outcome.

- Verifications successful: The number of verifications that were verified successfully after submission.

- Completion rate: The rate at which started verifications were completed and submitted by a user. Stripe divides the number of submitted verifications by the number of started verifications.

- Verification rate: The rate at which submitted verifications were verified successfully. Stripe divides the number of verified verifications by the number of submitted verifications.

Verification sessions can have multiple attempts (in case the user is unverified after an initial attempt). Each attempt generates a new VerificationReport, and Stripe calculates a number of verification report metrics:

[VerificationReport](/api/identity/verification_reports)

- Verification reports created: The number of verification attempts that were completed and submitted.

- Verification reports successful: The number of verification attempts that were verified successfully after submission.

## Best practices

Use the following best practices to get the most out of reviews and perform them efficiently:

- Focus on verifications where human judgment or manual review adds valuable insight to the determination of whether the customer’s identity is verified.Our systems can make determinations on identity verification on the majority of verification sessions, but human judgment can improve accuracy for some cases.

Focus on verifications where human judgment or manual review adds valuable insight to the determination of whether the customer’s identity is verified.

Our systems can make determinations on identity verification on the majority of verification sessions, but human judgment can improve accuracy for some cases.

- Use insights and context from your business to make an informed decision.Use the data in the Insights section to see how Stripe made the decision on the document or face image. Combining Insights, knowledge about your business, and human judgment can help you make an informed choice about when to trust or ignore the risk signals that Identity indicates.

Use insights and context from your business to make an informed decision.

Use the data in the Insights section to see how Stripe made the decision on the document or face image. Combining Insights, knowledge about your business, and human judgment can help you make an informed choice about when to trust or ignore the risk signals that Identity indicates.

[Insights](/identity/insights)

- Apply what reviewers learn to develop fraud prevention strategies.As reviewers sort through your verifications, they develop intuitions for fraud prevention that you can translate into updates to your integration with Identity.

Apply what reviewers learn to develop fraud prevention strategies.

As reviewers sort through your verifications, they develop intuitions for fraud prevention that you can translate into updates to your integration with Identity.

- Customize the process by presenting data unique to your business at review time.Pass along any additional customer information as metadata so that all relevant information is in the Dashboard at the time of review.

Customize the process by presenting data unique to your business at review time.

Pass along any additional customer information as metadata so that all relevant information is in the Dashboard at the time of review.

- Don’t slow down your customer.A review implies some amount of time between verification completion and enabling the capabilities within your business for the customer. If your business has an inherent delay of this type (for example, Identity is a part of a more long form review process), taking the time to review a verification doesn’t change the customer experience. If you don’t have a built-in delay, adding a review process could slow down customers—consider the impact on them before you implement a review process. For example, build out workflows for handling situations when the verification status changes for a customer after they’ve already been verified.

Don’t slow down your customer.

A review implies some amount of time between verification completion and enabling the capabilities within your business for the customer. If your business has an inherent delay of this type (for example, Identity is a part of a more long form review process), taking the time to review a verification doesn’t change the customer experience. If you don’t have a built-in delay, adding a review process could slow down customers—consider the impact on them before you implement a review process. For example, build out workflows for handling situations when the verification status changes for a customer after they’ve already been verified.

- Implement customer support workflows.Prepare to handle customer requests regarding their verification status and offer a non-biometric method for identity verification if they request it.

Implement customer support workflows.

Prepare to handle customer requests regarding their verification status and offer a non-biometric method for identity verification if they request it.

## See also

- Insights

[Insights](/identity/insights)

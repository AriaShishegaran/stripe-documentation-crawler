# Reviews

While Stripe’s automated systems work to prevent fraud on your account, you can use reviews to provide an extra layer of fraud protection by giving payments a manual inspection.

For example, you might want to review transactions that:

- Have an elevated risk of fraud according to Stripe’s fraud protection system

[elevated risk](/radar/risk-evaluation#elevated-risk)

- Were made from outside your country

- Are greater than a certain amount

- Use an email address from an unusual domain

The review queue of Stripe Radar for Fraud Teams allows you to examine unusual payments, without having to look at each payment individually. You can create a targeted list of payments to review with criteria that you specify, and review them in the Dashboard.

## Reviewing payments

The Dashboard review queue is a prioritized list of completed or to-be-captured payments that might need further investigation. You can review payments in two key ways: the list view allows you to scan a list of reviews without seeing details about a payment, but the detailed view provides much more context about it. You can also customize the detailed view with your own data.

[review queue](https://dashboard.stripe.com/radar/reviews)

[list view](#list-view)

[detailed view](#detailed-view)

Payments placed into review have typically already been successfully processed, unless you use a process of capturing a payment later. You can approve a payment as-is, refund it, or refund it and mark it as fraudulent.

[process of capturing a payment later](/payments/place-a-hold-on-a-payment-method)

The list view contains information to help you quickly get a sense for each payment’s possible risk of fraud.

The manual review queue in the Dashboard.

The list view highlights:

- The risk level Stripe has assigned after evaluating the payment

- Customer name

[Customer](/api/customers)

- Payment method information

- Customer information

- Amount, date, and time of the payment

- Device

- The device IP address

You can also use the J and K keys to move between payments when viewing them in more detail.

If you need to view further information about a payment before making a decision (such as any metadata), select the payment within the review queue to view the entire payment detail page. You can navigate between payments to review using the Previous and Next buttons.

[metadata](#best-practices)

The Stripe Radar machine learning system evaluates hundreds of signals when scoring a charge. The risk insights section on the payment page identifies some of the most relevant signals, along with some key data points that can help assess fraud on a payment. The related payments section shows other payments made to your business that use the same email address, IP address, or card number as the payment you’re currently reviewing.

[risk insights](/radar/reviews/risk-insights)

[related payments](/radar/reviews/risk-insights#related-payments)

## Actions

After you review a completed payment, you can remove it from the review queue by taking one of the following actions:

- Approve: Closes the review with no changes made to the payment. You can still refund and, optionally, report fraud on an approved payment.

- If you capture payments later, there is also a Capture button. You can capture a payment before or after approval.

[capture payments later](/payments/place-a-hold-on-a-payment-method)

- Refund: Refunds the payment without reporting it to Stripe as fraudulent. A completed refund is permanent, you can’t undo it—you must process a new payment. If you capture payments later, this button changes to Cancel. You can read more about this review process here.

[this review process here](/radar/reviews/auth-and-capture)

- Refund and report fraud: Refunds the payment and also reports it to Stripe as fraudulent, for instance to save dispute fees. This adds the associated card fingerprint and customer email to your block lists and further increases the effectiveness of our fraud prevention.

[save dispute fees](/disputes/prevention/best-practices#consider-proactively-refunding-suspicious-payments)

[block lists](/radar/lists#default-lists)

If a customer disputes a payment that’s currently in your review queue, the review is automatically closed.

[disputes](/disputes)

With Stripe Radar for Fraud Teams, you can create rules that automatically place payments in review based on your unique business needs. This gives you the opportunity to identify payments that might require more investigation before you can make an informed decision.

[rules](/radar/rules#review-rules)

## Review Assignments

Anyone managing the review queue can assign themselves to reviews to avoid duplicating effort.

As a reviewer, you can see which reviews other people are working on and assign or remove yourself from reviews. You can also filter the review queue to see reviews you own or reviews that are currently unassigned.

You can only change review assignments for yourself, not for other team members.

In the list view, use quick actions or the overflow menu to assign yourself to a review.

To assign yourself to a review in the list view, hover over a review and click on the person icon or the Assign to me button in the overflow menu. In the detail view, click the Assign to me button at the top right.

[list view](/radar/reviews#list-view)

[detail view](/radar/reviews#detailed-view)

If a review is assigned to another team member, you can still take action on it or assign it to yourself. You can find a complete history of assignment changes in the timeline of the review.

The timeline in the detail view displays a history of assignment changes.

## Best practices

Use the following best practices to get the most out of reviews and perform them efficiently.

- Focus time on payments where human judgment can add valuable insight to the decisionAutomated systems can make decisions on the majority of payments but human decision making can significantly improve accuracy when identifying fraud in some cases. Because not every case would benefit from human involvement, make sure that you choose transactions where the benefit is clear.

Focus time on payments where human judgment can add valuable insight to the decision

Automated systems can make decisions on the majority of payments but human decision making can significantly improve accuracy when identifying fraud in some cases. Because not every case would benefit from human involvement, make sure that you choose transactions where the benefit is clear.

- Use risk insights and related payments to make an informed decisionUse the data in the risk insights section to see how Stripe Radar came up with a score for a charge. Combining the reasons for a score, knowledge about your business, and human judgement can help you make an informed choice about when to trust or ignore the score assigned by Radar.

Use risk insights and related payments to make an informed decision

Use the data in the risk insights section to see how Stripe Radar came up with a score for a charge. Combining the reasons for a score, knowledge about your business, and human judgement can help you make an informed choice about when to trust or ignore the score assigned by Radar.

[risk insights](/radar/reviews/risk-insights)

- Leverage the insights from reviewers to develop hypotheses for fraud prevention strategiesAs reviewers sort through your transactions, they develop intuitions for fraud prevention that you can translate into better rules. Collect insights from reviewers to test custom rules on your account.

Leverage the insights from reviewers to develop hypotheses for fraud prevention strategies

As reviewers sort through your transactions, they develop intuitions for fraud prevention that you can translate into better rules. Collect insights from reviewers to test custom rules on your account.

[test custom rules on your account](/radar/testing#rules)

- Customize the process by presenting data unique to your business at review timePass along any additional customer or order information as metadata so that all relevant information is in the Dashboard at the time of review. Some examples of useful metadata include:More information about the order and its shipping informationGoogle Maps and Street View links to the customer’s shipping address so the reviewer can see if the address might be a drop-shipping or freight-forwarding service

Customize the process by presenting data unique to your business at review time

Pass along any additional customer or order information as metadata so that all relevant information is in the Dashboard at the time of review. Some examples of useful metadata include:

- More information about the order and its shipping information

- Google Maps and Street View links to the customer’s shipping address so the reviewer can see if the address might be a drop-shipping or freight-forwarding service

[Google Maps](https://maps.google.com)

- Don’t slow down your customerA review implies some amount of time between order placement and delivery. If your business has an inherent delay of this type (for example, you’re shipping physical goods), taking the time to review a transaction doesn’t change the customer experience. If you don’t have a built-in delay between orders and fulfillment with your business, adding a review process could slow down orders and create a bottleneck for good customers. Consider the impact on customers before you implement a review process.

Don’t slow down your customer

A review implies some amount of time between order placement and delivery. If your business has an inherent delay of this type (for example, you’re shipping physical goods), taking the time to review a transaction doesn’t change the customer experience. If you don’t have a built-in delay between orders and fulfillment with your business, adding a review process could slow down orders and create a bottleneck for good customers. Consider the impact on customers before you implement a review process.

## See also

- Rules

[Rules](/radar/rules)

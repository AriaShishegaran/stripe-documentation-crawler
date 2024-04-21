htmlResponding to disputes | Stripe Documentation[Skip to content](#main-content)Responding to disputes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fresponding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fresponding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)# Responding to disputes

Learn how to effectively respond to disputes.When an account owner files a dispute against a payment, their bank alerts Stripe and Stripe notifies you through the following channels:

- Email
- Stripe Dashboard
- An API`charge.dispute.created`event (if your integration is set up to receive[webhooks](/webhooks))
- Push notification (if you’ve subscribed)

Each of the dispute notification channels provides a link to the dispute’s details page in your Dashboard, where you can learn more about the reason for the dispute and take appropriate action.

You can see a detailed list of all disputed payments on the Disputes tab of the Payments page in your Dashboard. To review or respond to a dispute, open its details page by selecting it in the list.

NoteWhen you receive a dispute notification, take action to resolve it before the deadline. If you don’t respond, you automatically lose the dispute and can’t retrieve the disputed funds.

[Review the dispute category](#review-reasons)When you get a dispute, the corresponding category or reason appears in your Dashboard and as the value for the reason attribute of the dispute object.

Each dispute category specifies different response requirements and recommendations to make it effective in addressing the root claim from the cardholder, so your first step is to review our response guidelines for the category of your dispute so you can collect the best set of evidence to counter the dispute claim.

### Inquiries

Inquiries appear as disputed payments in the Dashboard, but they actually represent a pre-dispute stage that’s typically issued when an account owner doesn’t recognize a transaction on their account. Respond in this stage to resolve any questions and prevent a formal dispute escalation, which saves you time, fees, and your rating with the card networks. For more information, see Inquiries.

NoteIf an inquiry escalates to a chargeback, you must submit another response for the dispute.

### Fraudulent Disputes

Visa CE 3.0 Eligibility![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For fraudulent disputes with the Visa 10.4 (Card absent fraud) code, Stripe automatically evaluates your transaction history to determine eligibility with Visa Compelling Evidence 3.0. If your dispute is eligible, we notify you in the Dashboard and in the dispute email. In these cases, we encourage submitting evidence because this eligibility typically translates to a significantly higher likelihood of overturning the dispute in your favor.

Liability Shift![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For fraudulent disputes that might be covered by the liability shift rule, Stripe automatically provides most of the evidence, such as  the Electronic Commerce Indicator (ECI) from 3D Secure.

[Understand the complaint](#understand)When possible, the Dispute details page provides you with a copy of the bank’s submission to Stripe based on the account owner’s claim. These are actual documents attached by card networks and can provide additional information about the disputed transaction, such as a text description from the account owner describing the specific complaint. When responding to the dispute, make sure to properly address the issue described in these files.

If the dispute is still open and the bank has provided these files, select Review the claim details under Step 1 of the checklist modal in the Dashboard to view them.

The Dispute details page might also provide you with a way to email the account owner. We recommend contacting them, as it might give you insight to better understand the complaint and help you decide how to proceed. Be sure to keep a record of all communication with your customer during this process, as it provides evidence to submit with your response.

[Decide to accept or challenge the dispute](#decide)### Handle disputes through Stripe

Always address a formally disputed payment through this process. The issuing bank has already refunded the account owner, and it’s the only way you can attempt to retrieve the disputed funds.

When you have a clear picture of the dispute details, decide whether to accept or challenge the dispute. Consider the following questions in your determination:

- Is the account owner’s claim valid?
- If not, do I have the evidence required to disprove the claim?
- Can I convince the account owner to withdraw their dispute if I resolve their complaint amicably, for example, by offering a store credit or a replacement item?
- Is the dispute[CE 3.0 Eligible](#visa-ce-30-eligibility)? If so, consider responding because Stripe provides most of the required evidence from your transaction history.
- Might the dispute be covered by the[liability shift](#liability-shift)rule? If so, consider responding with evidence on top of what Stripe automatically provides, such as the[3D Secure](/payments/3d-secure)outcome.

When you’ve decided how to respond, select the corresponding button on the Dispute details page in your Dashboard:

- Accept disputesubmits a response to the issuing bank affirming that you agree to refund the customer for the disputed payment.
- Counter disputeopens a form that guides you through the submission process, prompts you for evidence that is relevant to the dispute type and your response type, and allows you to easily upload supporting files.

See Responding to disputes using the API if you prefer to handle disputes programmatically.

[Submit evidence through the Dashboard](#respond)Prepare your response carefullyYou have only one opportunity to submit your response. Stripe immediately forwards your response and all supporting files to the issuing bank. You can’t edit the response or submit additional files, so make sure you’ve assembled all your evidence before you submit.

1. Open the dispute response form: Click Counter dispute to open Stripe’s dispute response form.


2. Tell us about the dispute: In the first page of the form, tell us why you believe the dispute is in error and the product type of the original purchase. This information along with the dispute category helps Stripe recommend the most relevant evidence to support your challenge on the next page of the form. For example, if your counter to a customer’s claim that they canceled a subscription for an online service is that the customer agreed to a minimum term, it doesn’t make sense to ask you for shipping and tracking details. When your integration supports it, Stripe automatically captures the product type based on the original payment.


3. Assemble your evidence: The second page of the form has a dynamic set of sections representing the most relevant details you can provide for your individual case.

In the Supporting Files: section, use the File Upload tool to attach evidence that matches the checklist of evidence types relevant to your dispute type and counter argument. For each uploaded file, specify which type of evidence it satisfies. You can only submit one file per type of evidence, so if you have several files representing one type of evidence, combine them into a single, multi-page file.

Consider the following guidelines to make sure your supporting files are effective:

  - Consult the evidence recommendations for your specific dispute category.


  - For fraudulent disputes in particular, if your dispute is Visa CE 3.0 eligible, look for the Required for CE 3.0 badge throughout the response form. In most cases, Stripe pre-populates these fields with the required data from your transaction history.

    - If the field is pre-populated, don’t edit it because you might affect eligibility
    - If the field is empty, add the requested information, such as the product description

If your dispute may be covered by the liability shift rule, we populate 3D Secure information such as the Electronic Commerce Indicator (ECI) automatically for you.


  - Organize each piece of evidence according to the evidence type it satisfies - be as succinct as possible.


  - Combine items of the same evidence type into a single file.


  - Limit your evidence file size to the combined maximum of 4.5 MB.


  - Limit your Mastercard evidence file length to the combined maximum of 19 pages.


  - Banks evaluating the dispute won’t review any external content, so don’t include:

    - Audio or video files
    - Requests to call or email for more information
    - Links to click for further information (for example, file downloads or links to tracking information)




4. Background evidence: The other sections of the second page vary depending on the dispute type and your answers in the first page. When your integration supports it, Stripe automatically captures the data for these sections and pre-populates both the API evidence object attributes and the form fields in the Dashboard. But if any of these fields aren’t pre-populated, include as much information as you can before you submit your response. These sections can include:

  - Shipping details
  - Refund policy details
  - Customer details
  - Product details

The more information your integration collects and passes to Stripe when your customer makes a payment, the better your ability to prevent disputes and fraud from occurring, and challenge them effectively when they do.


5. Submit evidence: Click the checkbox to acknowledge your understanding that your response is final. After you submit it, Stripe automatically puts the evidence you provide into a format accepted by the issuing bank and submits it for consideration. At this point, you can’t amend what you’ve submitted or provide any additional information, so make sure to include every relevant detail.



NoteIn some cases, you might have multiple disputes associated with a single payment. If this occurs, consider responding to each dispute individually.

[Check the dispute status](#status)After you submit a response, the status of the dispute changes to under_review. When the issuer informs Stripe of its decision, we inform you of the outcome by email, in the charge.dispute.closed webhook event, and by updating the dispute status in the Dashboard and the Dispute API object to one of the following:

- won indicates that the bank decided in your favor and overturned the dispute. In this case, the issuing bank returns the debited chargeback amount to Stripe, and Stripe passes this amount back to you. For businesses in Mexico, the dispute fee might also be returned. Otherwise, the dispute fee isn’t returned.


- lost indicates that the bank decided in the account owner’s favor and upheld the dispute. In this case, the refund is permanent and the dispute fee isn’t returned.

In some cases, the bank provides additional details about the dispute decision. Select View issuing bank response under Relevant documents in the Dispute details to view them.



## See also

- [Preventing disputes and fraud](/disputes/prevention)
- [Dispute monitoring programs](/disputes/monitoring-programs)
- [Calculating dispute rates](/disputes/measuring)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Review the dispute category](#review-reasons)[Understand the complaint](#understand)[Decide to accept or challenge the dispute](#decide)[Submit evidence through the Dashboard](#respond)[Check the dispute status](#status)[See also](#see-also)Related Guides[How disputes work](/docs/disputes/how-disputes-work)[Dispute categories](/docs/disputes/categories)[Dispute withdrawals](/docs/disputes/withdrawing)[Preventing disputes and fraud](/docs/disputes/prevention)Products Used[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
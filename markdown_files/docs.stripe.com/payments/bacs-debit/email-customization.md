htmlBacs Direct Debit email notification requirements | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Femail-customization)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Femail-customization)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Bacs Direct Debit email notification requirements

Design and send your own Bacs Direct Debit notification emails.Bacs Direct Debit requires that you notify your customers when payment details are initially collected and two days before a payment is to be collected. There are three types of Bacs Direct Debit email notifications you need to send in different scenarios:

EmailDescriptionConfirmation of signupSent when payment details are initially collected and payment is to be collected more than one month laterAdvanced noticeSent two days before payment is to be collected, for every payment *Confirmation of signup incorporating Advanced noticeSent when payment details are initially collected if the first payment is to be collected within one month of collecting the mandate* If you are charging a recurring amount where both the charge amount and schedule is unchanging then only one advanced notice email is required and it must be sent before the first payment. This is often a reason why users choose to send their own Bacs email notifications: to reduce the overall number of emails they send their customers.

## Approval process

To send your own Bacs Direct Debit notification emails, follow these steps:

1. If you have not already opted to do so, you first need to customize your Business Display Name in the[Bacs Direct Debit settings](https://dashboard.stripe.com/settings/payments#bacs_debit).
2. [Contact us](https://support.stripe.com/contact)with screenshots of your email designs for approval. This document lists out the requirements and gives examples to follow when designing your emails.
3. Turn off Stripe emails in the[Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails).

## Confirmation of signup

Bacs Direct Debit requires that the following information be included on a Confirmation of signup email notification:

- A heading advising confirmation of the setup of a Direct Debit Instruction
- Wording advising the payer to check the details contained in the email
- The payer’s account name
- The last 4 numbers of the payer’s account number with the leading digits masked
- The payer’s bank sort code
- Your customized Business Display Name
- Your contact telephone number and email address
- Advice of right to cancel
- The[mandate reference](/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
- The unedited[Stripe Direct Debit Guarantee](https://stripe.com/legal/bacs-direct-debit-guarantee), including the Direct Debit logo

The Confirmation of signup email must be sent as soon as you have collected payment details from your customer. Send this email when you receive the checkout.session.completed event for a payment method of type bacs_debit.

The following example Confirmation of signup email for a fictional company, named Rocket Rides, can be used as a reference for creating your own email:

![](https://b.stripecdn.com/docs-statics-srv/assets/bacs-customized-mandate-confirmation.b05c81230fef01460f71ab1a529f7238.png)

## Advanced notice

Bacs Direct Debit requires that the following information be included on an Advanced notice email notification:

- The total amount of the Direct Debit to be debited from the payer’s account
- The Direct Debit due date (day, month, and year) — this will be two business days after the PaymentIntent is created in Stripe
- The Frequency of Direct Debit collection — only required when charging an unchanging, recurring amount and you will not be sending an advanced notice email for each charge
- The[mandate reference](/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
- Your customized Business Display Name
- Your contact telephone number and email address

The Advanced notice email must be sent two days before you charge your customer. Send this email when you receive a payment_intent.processing event with a payment method of type bacs_debit. If you are collecting a mandate and payment at the same time, and have opted not to send the combined Confirmation of signup incorporating an Advanced notice email, then you must wait until the mandate is accepted to send the Advanced notice email. A mandate is accepted when you receive a mandate.updated event with a payment_method_details.type set to bacs_debit and payment_method_details.bacs_debit.network_status updated from pending to accepted.

The following example Advanced notice email for a fictional company, named Rocket Rides, can be used as a reference for creating your own email:

![](https://b.stripecdn.com/docs-statics-srv/assets/bacs-customized-debit-initiated.531bf6868a65fee83ddd62b0519914e3.png)

## Confirmation of signup incorporating an Advanced notice

The Confirmation of signup and Advanced notice email notifications can only be sent as a single email when the first payment will be collected within one month of the mandate being collected.

Bacs Direct Debit requires that the following information be included on an Confirmation of signup email notification that incorporates an advanced notice:

- A heading advising confirmation of the setup of a Direct Debit Instruction and the future payment schedule
- Wording advising the payer to check the details contained in the email
- The payer’s account name
- The last 4 numbers of the payer’s account number with the leading digits masked
- The payer’s bank sort code
- Your customized Business Display Name
- Your contact telephone number and email address
- Advice of right to cancel
- The[mandate reference](/api/mandates/object#mandate_object-payment_method_details-bacs_debit-reference)
- The unedited[Stripe Direct Debit Guarantee](https://stripe.com/legal/bacs-direct-debit-guarantee), including the Direct Debit logo
- The total amount of the Direct Debit to be debited from the payer’s account
- The Direct Debit due date (day, month, and year) — this will be two business days after the PaymentIntent is created in Stripe
- The Frequency of Direct Debit collection — only required when charging an unchanging, recurring amount and you will not be sending an advanced notice email for each charge

The Confirmation of signup email incorporating Advanced notice must be sent as soon as you have collected payment details from your customer. Send this email when you receive the checkout.session.completed event for a payment method of type bacs_debit.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Approval process](#approval-process)[Confirmation of signup](#confirmation-of-signup)[Advanced notice](#advanced-notice)[Confirmation of signup incorporating an Advanced notice](#confirmation-of-signup-incorporating-an-advanced-notice)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
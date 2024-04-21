htmlIssuing regulated customer notices | Stripe Documentation[Skip to content](#main-content)Customer communications[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcompliance-us%2Fissuing-regulated-customer-notices)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcompliance-us%2Fissuing-regulated-customer-notices)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)[Product and marketing compliance guidance (US)](/docs/issuing/compliance-us)# Issuing regulated customer notices

Learn about sending regulatory notifications to your customers.To comply with applicable laws, Issuing platforms must send customer communications upon certain trigger events. This guide shows you how Stripe helps you stay compliant by sending properly formatted notices when required.

Stripe offers a no-code solution to send regulated emails on your behalf. We recommend this option because it helps you stay compliant automatically.

Let Stripe send regulated emails on your behalfSend regulated emails yourselfStripe monitors events requiring a customer notice, and sends an email on your behalf to the connected account.

[Preview and send test emails](#preview-and-send-test-emails)You can preview our email templates and send test emails to make sure your branding and email addresses are working as expected.

From Emails, click Preview and customize to view the Issuing notice email templates, then click Send test email. Issuing notices only appear on this page for US Issuing platforms.

[Confirm your branding settings](#confirm-branding-settings)All connected accounts that receive Issuing notices see your business name, icon, and branding colors in the notice emails.

To manage these brand settings, go to Connect Settings and verify the content under Branding is correct.

[Confirm your support email and set up your email domain](#confirm-support-email-and-set-up-email-domain)When Stripe sends an email on your behalf, we use your support email for the reply-to address. You can configure this in your Public details settings.

By default, Stripe sends Issuing notices from card-issuing-notices@stripe.com, using your business name as the display name (for example, “Rocket Rides” card-issuing-notices@stripe.com). You can send emails from your own email domain, but you can’t change the local address (for example,  card-issuing-notices@yourcustomdomain.com).

[Review connected account details](#review-connected-account-details)Stripe sends notices to the connected account’s email saved with Stripe. If the connected account has a primary user with log-in access to the Stripe Dashboard, we’ll email that individual. If not, we send it to the account email address (if available) and if that’s not available, we send it to the representative’s email address.

To view notices sent by Stripe to a connected account, go to the account’s Activity page in your Dashboard and look for the section Emails to this account.

## Events that require a customer notice

The trigger events outlined below require a customer notice.

Events monitored by StripeOther events (not monitored by Stripe)Stripe monitors for most events requiring a notice. We either send a notice to the customer on your behalf, or (for platforms sending their own notices) require you to email your customers when we inform you of the event through the Account Notice API.

### Disputes

You must send regulated notices when you submit a dispute, and again when the result of the dispute is determined by the network (the dispute is either won or lost).

### Involuntary account closures

Only Stripe can disable inactive connected accounts and disable accounts that violate our terms of service. Stripe sends emails on your behalf for both of these events. If you’re sending emails yourself, Stripe informs you of both events. We recommend that you send a notice for inactivity closures, and we require that you send a notice for terms of service closures.

If the customer requests an account closure, you don’t need to send a notice (and Stripe won’t send one on your behalf).

### Issuing applications rejected for failure to verify identity

You must notify a connected account when it remains unverified within 29 days of completing an application for the card_issuing capability. Stripe monitors completed applications (once the account has submitted all required information for Issuing and accepted the Issuing terms of service) and generates a notice if the capability remains inactive after 29 days. In test mode, Stripe generates the notice 1 hour after completion to help you reproduce this scenario.

### Charge Card credit underwriting decisions

Stripe monitors Charge Card underwriting decisions, and you must send regulated notices for any negative impact to the user’s credit account. This includes rejected applications, rejected requests for a credit limit increase, reductions in a credit limit, or the closure of a credit line. If your platform hasn’t been approved to use Stripe’s Charge Card product, these templates don’t apply.

[Issuing Notice email templates](#issuing-notice-email-templates)Stripe uses the templates below to send emails to your users relevant to events that trigger them. You can preview each template from Communication Settings by clicking Preview and customize. Customize your platform name and logo at your Connect Branding settings

If you’ve configured your custom email domain, Stripe automatically removes the italicized text in each template. This text is included when the email is sent from card-issuing-notices@stripe.com.

### Dispute submitted

### Dispute lost

### Dispute won

### Account closed by Stripe for Inactivity

### Account closed by Stripe for Terms of Service violation

### Spend Card application rejected for failure to verify identity

### Additional templates for Charge Card platforms

### Equal Credit Opportunity Act disclosures

In the templates above, <Bank specific ECOA footer> is replaced with the appropriate equal credit opportunity act disclosure for your platform’s bank sponsor.

Celtic BankCross River BankOn behalf of Celtic Bank

Notice: The federal Equal Credit Opportunity Act prohibits creditors from discriminating against credit applicants on the basis of race, color, religion, national origin, sex, marital status, age (provided the applicant has the capacity to enter into a binding contract); because all or part of the applicant’s income derives from any public assistance program; or because the applicant has in good faith exercised any right under the Consumer Credit Protection Act.

The Federal agency that administers compliance with this law concerning Celtic Bank is Division of Depositor and Consumer Protection, National Center for Consumer and Depositor Assistance, Federal Deposit Insurance Corporation, 1100 Walnut Street, Box #11, Kansas City, MO 64106

<Your platform name> is located at <Your platform address>

If an account has cards provided by multiple banks (not common), then account closure templates will show the <Bank specific ECOA footer> for all applicable bank sponsors.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Preview and send test emails](#preview-and-send-test-emails)[Confirm your branding settings](#confirm-branding-settings)[Confirm your support email and set up your email domain](#confirm-support-email-and-set-up-email-domain)[Review connected account details](#review-connected-account-details)[Events that require a customer notice](#events-that-require-a-customer-notice)[Issuing Notice email templates](#issuing-notice-email-templates)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
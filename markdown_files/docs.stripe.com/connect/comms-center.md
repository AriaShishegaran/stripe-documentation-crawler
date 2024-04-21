htmlComms Center | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcomms-center)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcomms-center)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Comms Center

Collect and send communications to connected accounts.## Overview

Platforms that want to update the emails Stripe has on file for connected accounts can update them using the Comms Center collection flow.

## Collecting emails

After hitting Get Started you see the main page for collection and validation.

![Comms Center Getting Started](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-get-started.0342e9ed411102b9c81f3bfd3b075010.png)

### 1. Download a template with all of your connected accounts that are eligible for receiving communications.

![Comms Center Download Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-download-emails.0f98ff258879870ce5a83603524c33ac.png)

You get a template CSV like this:

Emails.csv`Account ID,Business Name,First Name,Last Name,Email Address (please add or replace),User has claimed primary user email address
acct_123abc,Connected Account A,John,Doe,,✔
acct_456def,Connected Account B,,,,✗`### 2. Add the email addresses you want to add to the business within Stripe

For example, a filled out CSV might look like this:

Emails_Updated.csv`Account ID,Business Name,First Name,Last Name,Email Address (please add or replace),User has claimed primary user email address
acct_123abc,Connected Account A,John,Doe,email-a@email.com,✔
acct_456def,Connected Account B,,,email-b@email.com,✗`### 3. Upload the file with your changes

The filename doesn’t matter. Only the Account ID and Email Address (please add or replace) fields matter here, the rest are only for validating your changes.

![Comms Center Upload Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-upload-emails.9ec27a2b1c9e46fd2d342f2b2c5ed923.png)

### 4. Wait for validation to complete and verify the account changes are correct.

![Comms Center Validation Step](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-validation.09e86d5773685dea8a7ce28578abaaff.png)

### 5. Confirm your changes

After confirming, you see the completion state. Updates can take some time, depending on how many emails you’ve uploaded. We send email updates to any webhooks you’ve configured.

![Comms Center Confirmed](https://b.stripecdn.com/docs-statics-srv/assets/comms-center-confirmed.b5a1286831c481edc0055551ad4c5f6d.png)

## Important usage notes

- Comms Center can only currently handle CSVs with 500,000 rows. If you have more than that, break up your CSV into multiple files.
- If you get validation errors, make sure your headers on your CSV match the expected headers.The required columns are`Account ID`which has the`acct_`tokens and`Email Address (please add or replace)`which has the desired email.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Overview](#overview)[Collecting emails](#collecting-emails)[Important usage notes](#important-usage-notes)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
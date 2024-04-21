htmlImport data into Stripe | Stripe Documentation[Skip to content](#main-content)Import and manage data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fimport-external-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fimport-external-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Import data into StripeBeta

Automatically import and map external data from other sources with no-code connectors.Import external data into Stripe with Data Management. Use the Dashboard to automatically upload data from other sources into Stripe. You can integrate with the Data Management API or set up recurring CSV imports with a data connector, like Amazon S3. You can also manually upload a CSV file as a one-time import.

With Data Management, you can:

- Integrate with the Data Management API or set up recurring CSV imports with a data connector, like Amazon S3. You can also manually upload a CSV file as a one-time import.
- Create data templates to automatically map your CSV files to common objects.
- View the processing status of your CSV Import Sets.
- Get detailed information on CSV file processing after completion.
- Download and resolve CSV Import Set errors.

Interested in getting early access to Data Management?Access to Data Management is currently limited to Revenue Recognition and Reconciliation users. If you’re using Revenue Recognition or Reconciliation and would like to automatically import your external data into Stripe, enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon to understand your data requirements in more detail.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
htmlStripe Apps CLI reference | Stripe Documentation[Skip to content](#main-content)CLI[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fcli)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fcli)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Stripe Apps CLI reference

Install the Stripe Apps command line interface and use it to manage your app.The Stripe Apps CLI helps you create, develop, configure, and upload your Stripe app using the terminal.

## Before you begin

1. [Log in to the Stripe Dashboard](https://dashboard.stripe.com/)using your existing Stripe account, or by creating a new one.
2. [Install the Stripe CLI](/stripe-cli).
3. Log in to the CLI using the same account you logged into the Stripe Dashboard with.Command Line`stripe login`
4. Verify that you’re using CLI version 1.8.11 or newer.Command Line`stripe version
# expected output: stripe version 1.8.11`

## Install the CLI plugin

To install the Stripe Apps CLI plugin, run:

Command Line`stripe plugin install apps`## Upgrade the CLI plugin

To get the latest version of the Stripe Apps CLI plugin, run:

Command Line`stripe plugin upgrade apps`## Command overview

CommandDescription`create`Create a new Stripe app.`start`Start a development server for viewing your app in the Stripe Dashboard. Use the`--manifest`flag to[load an extended manifest file](/stripe-apps/reference/app-manifest#extended-manifest).`add`Add a building block for developing your app.`remove`Remove a building block from your`stripe-app.json`file.`grant`Grant configuration access to your app.`revoke`Revoke configuration access to your app.`set`Set a configuration value within the app manifest.`upload`Upload your app to be submitted for review.`version`Print the version of Stripe Apps CLI plugin.## See also

- [App manifest reference](/stripe-apps/reference/app-manifest)
- [Permissions reference](/stripe-apps/reference/permissions)
- [How UI extensions work](/stripe-apps/how-ui-extensions-work)
- [Upload and install your Stripe App](/stripe-apps/upload-install-app)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Install the CLI plugin](#install-cli-plugin)[Upgrade the CLI plugin](#upgrade-the-cli)[Command overview](#command-overview)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
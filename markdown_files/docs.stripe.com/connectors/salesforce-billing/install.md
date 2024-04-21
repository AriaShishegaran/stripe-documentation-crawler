htmlInstalling Stripe for Salesforce Billing | Stripe Documentation[Skip to content](#main-content)Installation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-billing%2Finstall)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-billing%2Finstall)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce Billing](/docs/connectors/salesforce-billing)# Installing Stripe for Salesforce Billing

Learn how to install Stripe for Salesforce Billing including the prerequisites.## Before you begin

Before you can install and configure the Stripe Connector for Salesforce Billing managed package, you have to install the Salesforce CPQ and Salesforce Billing managed packages. The package install links for both apps are available in the Salesforce Quote-to-Cash install website, and the configuration instructions for each package are in the following sections.

## Install Salesforce CPQ

To install the Salesforce CPQ package, you must apply the Salesforce CPQ License permission set license to the user that will install the package in your organization.

Navigate to the Salesforce Quote-to-Cash website, scroll down to the Salesforce CPQ package installation links, and select the most recent release. If you’re installing into a sandbox environment, click the Sandbox link. If you’re installing into a production environment, click the Production link. You might be prompted to log into your Salesforce organization if you haven’t logged in previously.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-cpq-install.86a97352d2e50c5bcda9e98e4f246a0c.png)

The Salesforce CPQ installation links

Next, make sure that Install for All Users is selected and click Install.

![](https://b.stripecdn.com/docs-statics-srv/assets/Salesforce-install-for-all-users.075e59fd13a25231252072473b753228.png)

Salesforce CPQ install for all users

You’ll be asked to approve access to and from third-party websites.  Check the Grant Access checkbox and click Continue.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-approve-third-party.34f5ae314d715d1bfeff38016e9034ac.png)

Approving third-party access for Salesforce CPQ

If successful, you’ll receive an email telling you Salesforce CPQ is installed. After you receive the email, navigate to Setup > Apps > Packaging > Installed Packages and click Configure on Salesforce CPQ.

![](https://b.stripecdn.com/docs-statics-srv/assets/installed-packages.f9d8b71b58f90255c31e6bacbb744081.png)

Salesforce installed packages

Click the Pricing and Calculation tab and click Authorize new calculation service.

![](https://b.stripecdn.com/docs-statics-srv/assets/pricing-and-calculation-tab.629f4b041efc6393f90591126cd07a81.png)

Salesforce CPQ pricing and calculation configuration

As an optional but recommended step, click the Order tab, then check the Allow Multiple Orders checkbox and set the Default Order Start Date to Quote Start Date. After setting those fields, click Save.

![](https://b.stripecdn.com/docs-statics-srv/assets/order-tab.e9a9057b47ff2a654985d3481931b26a.png)

Salesforce CPQ order configuration

For more information, see Salesforce documentation on Install Salesforce Billing.

## Install Salesforce Billing

Navigate to the Salesforce Quote-to-Cash website, scroll down to the Salesforce Billing package installation links, and select the most recent release. If you’re installing it into a sandbox environment, click the Sandbox link, and if you’re installing it into a production environment, click the Production link. You may be prompted to log into your Salesforce organization if you haven’t done so previously.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-billing-install.d3e00d0fefdc3a86240d5d92e351b4f3.png)

The Salesforce Billing installation links

Make sure Install for All Users is selected, then click Install.

![](https://b.stripecdn.com/docs-statics-srv/assets/Salesforce-install-for-all-users.075e59fd13a25231252072473b753228.png)

Salesforce Billing install for all users

You’ll receive an email telling you Salesforce Billing is installed.  To verify, navigate to Setup > Apps > Packaging > Installed Packages and make sure the package is installed.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-billing-installed-package.7161b4f6380a235ad5c05b715b451687.png)

Salesforce installed packages

## Install Stripe Connector for Salesforce Billing

After you’ve installed both prerequisite packages, you can install the Stripe Connector for Salesforce CPQ & Billing managed package. Use the links below to install the package into your Salesforce organization or contact your Stripe representative to request the latest version:

Sandbox

Production

You may be prompted to log into your Salesforce org if you haven’t done so previously.

Make sure Install for Admins Only is selected, then click Install.

![](https://b.stripecdn.com/docs-statics-srv/assets/stripe-salesforce-admins-only.ce050e830280859a49789029a91a0942.png)

The Stripe for Salesforce Billing installation process

You’ll be asked to approve access to and from third-party websites.  Check the Grant Access checkbox and click Continue.

![](https://b.stripecdn.com/docs-statics-srv/assets/stripe-salesforce-third-party-access.3812aa661f1a6193c160878339cdcc8b.png)

Grant third-party access to Stripe

You’ll receive an email telling you Stripe for Salesforce Billing is installed. To verify, navigate to Setup > Apps > Packaging > Installed Packages and make sure the package is installed.

![](https://b.stripecdn.com/docs-statics-srv/assets/stripe-salesforce-installed-packages.36cc041c350eef6ecc1ed6d451e31f8f.png)

Salesforce installed packages list

## Next steps

- [Configure Stripe for Salesforce Billing](/connectors/salesforce-billing/configuration)
- [ACH with Stripe for Salesforce Billing](/connectors/salesforce-billing/ach)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Install Salesforce CPQ](#install-salesforce-cpq)[Install Salesforce Billing](#install-salesforce-billing)[Install Stripe Connector for Salesforce Billing](#install-stripe-connector-for-salesforce-billing)[See also](#next-steps)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
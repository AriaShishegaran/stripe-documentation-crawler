htmlStripe Shell | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-shell%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-shell%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)
[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Stripe Shell# Stripe Shell

Manage your Stripe resources in test mode from the Stripe docs site.Stripe Shell is an interactive, authenticated, browser-based shell for managing your Stripe resources in test mode. It securely authenticates access anywhere within the Stripe docs site. Just login to the Stripe docs site and launch the Stripe Shell with a keyboard shortcut.

## Start with a guide

[Get started with the Stripe ShellLearn how to launch the Stripe Shell and get started with a YouTube video from Developer Advocacy.](/docs/stripe-shell/launch)[Keyboard shortcuts in the Stripe ShellLearn about the keyboard shortcuts available for the Stripe Shell.](/docs/stripe-shell/keyboard-shortcuts)## Key features

### Use your favorite pre-installed tools

Manage your Stripe resources with the Stripe CLI pre-loaded with autocomplete. No more hunting around for commands—start typing stripe and hit the space bar on your keyboard then click a supported command.

### Use the Stripe Shell to learn new products

Launch the Stripe Shell from the Stripe docs site to easily try out different combinations of Stripe API requests before writing a line of code.

### Execute Stripe CLI snippets directly in Stripe docs

Run any supported Stripe CLI command directly within the Stripe docs site. When you click the green play button next to any supported CLI command, the Stripe Shell runs the request and returns an immediate response in the terminal window.

### Use the Stripe CLI for local development

While the Stripe Shell can’t test a webhooks integration on your local server, it’s still possible to use the Stripe CLI to forward and trigger webhook events locally. To learn more, see Test a webhooks integration with the Stripe CLI.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Start with a guide](#start-with-a-guide)[Key features](#key-features)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
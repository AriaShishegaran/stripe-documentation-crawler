htmlGet started with the Stripe Shell | Stripe Documentation[Skip to content](#main-content)Get started[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-shell%2Flaunch)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-shell%2Flaunch)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)
[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Stripe Shell# Get started with the Stripe Shell

Get started with the Stripe Shell on any page in the Stripe docs site.This page describes how to launch the Stripe Shell terminal window from any page on the Stripe docs site and how to get started.

## Initial setup

1. To begin, you need a Stripe account. If you don’t already have one,[follow these instructions](https://dashboard.stripe.com/register).
2. ClickSign into authenticate with your Stripe account’s APIsecret keyfor[test mode](/test-mode).

[Listen for events](#listen)1. Press the`Control`+`Backtick`(on Windows, Linux or macOS) keys on your keyboard to launch the Stripe Shell.
2. Click thestripe listencommand to listen for[events](/webhooks#events-overview), or type the command and press theEnterkey on your keyboard.

Command Line`stripe listen`This launches a Stripe Shell session inside a new frame at the bottom of the site and displays a command-line terminal.

[Run your first request](#first)1. Press the`Alt`+`Shift`+`D`(on Windows, Linux) or`Command`+`D`(on macOS) keys on your keyboard to open a new pane.
2. Click the greenplaybutton to run the command, or copy and paste the command and press the`Enter`key on your keyboard.
3. Copy the Stripe resource identifier (in`id`) in the response for subsequent requests.

Command Line`stripe products create \
--name="Introductory offer (Monthly)" \
--description="$0.99 per month"`This creates a product with a name and description.

[Get started with a video](#get-started)Watch this video to learn all of the different ways to use the Stripe Shell.

Loading video content## Next steps

- [Keyboard shortcuts in the Stripe Shell](/stripe-shell/keyboard-shortcuts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Initial setup](#initial-setup)[Listen for events](#listen)[Run your first request](#first)[Get started with a video](#get-started)[Next steps](#next-steps)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
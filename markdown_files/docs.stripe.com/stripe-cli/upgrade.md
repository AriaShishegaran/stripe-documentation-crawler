htmlUpgrade the Stripe CLI | Stripe Documentation[Skip to content](#main-content)Upgrade[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Fupgrade)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Fupgrade)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)
[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Stripe CLI# Upgrade the Stripe CLI

Learn how to upgrade the CLI.Take advantage of the latest features of the Stripe CLI.

## Homebrew

To upgrade the Stripe CLI with homebrew, run:

Command Line`brew upgrade stripe/stripe-cli/stripe`## Scoop

To upgrade the Stripe CLI with Scoop, run:

Command Line`scoop update stripe`## macOS

To upgrade the Stripe CLI on macOS without homebrew:

1. Download the latest`mac-os`tar.gz file of your cpu architecture type from[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
2. Unzip the file:`tar -xvf stripe_[X.X.X]_mac-os_[ARCH_TYPE].tar.gz`.

Optionally, install the binary in a location where you can execute it globally (for example, /usr/local/bin).

## Linux

To upgrade the Stripe CLI on Linux without a package manager:

1. Download the latest`linux`tar.gz file from[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
2. Unzip the file:`tar -xvf stripe_X.X.X_linux_x86_64.tar.gz`.
3. Move`./stripe`to your execution path.

## Windows

To upgrade the Stripe CLI on Windows without Scoop:

1. Download the latest`windows`zip file from[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
2. Unzip the`stripe_X.X.X_windows_x86_64.zip`file.
3. Add the path to the unzipped`stripe.exe`file to your`Path`environment variable. To learn how to update environment variables, see the[Microsoft PowerShell documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3#saving-changes-to-environment-variables).

NoteWindows anti-virus scanners occasionally flag the Stripe CLI as unsafe. This is very likely a false positive. For more information, see issue #692 in the GitHub repository.

## Docker

The Stripe CLI is also available as a Docker image. To install the latest version, run:

Command Line`docker run --rm -it stripe/stripe-cli:latest`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Homebrew](#homebrew)[Scoop](#scoop)[macOS](#macos)[Linux](#linux)[Windows](#windows)[Docker](#docker)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
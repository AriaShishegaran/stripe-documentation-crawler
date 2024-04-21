htmlEnable autocompletion for the Stripe CLI | Stripe Documentation[Skip to content](#main-content)Autocompletion[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Fautocomplete)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Fautocomplete)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)
[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Stripe CLI# Enable autocompletion for the Stripe CLI

Enable autocompletion so that the Stripe CLI automatically completes your commands.Use the stripe completion command to enable autocompletion so that the Stripe CLI automatically completes your commands. After you enable autocomplete, you can type a command and press the tab key on your keyboard to view available commands and flags.

## Setup with ZSH on macOS and Linux

Open a new ZSH shell and run the following commands:

Command Line`stripe completion
mkdir -p ~/.stripe
mv stripe-completion.zsh ~/.stripe`Add the following lines to your .zshrc file:

Command Line`# The next lines enables shell command completion for Stripe
fpath=(~/.stripe $fpath)
autoload -Uz compinit && compinit -i`## Setup with Bash on macOS and Linux

Follow the instructions in bash-completion to set up bash completions.

Open a new Bash shell and run the following commands:

Command Line`stripe completion
mkdir -p ~/.stripe
mv stripe-completion.bash ~/.stripe`Add the following lines to your .bashrc file:

Command Line`# The next line enables shell command completion for Stripe
source ~/.stripe/stripe-completion.bash`## Windows

Windows autocompletion is currently not supported.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Setup with ZSH on macOS and Linux](#setup-with-zsh-on-macos-and-linux)[Setup with Bash on macOS and Linux](#setup-with-bash-on-macos-and-linux)[Windows](#windows)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
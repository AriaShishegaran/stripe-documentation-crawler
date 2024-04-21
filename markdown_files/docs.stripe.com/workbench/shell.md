htmlShell and API Explorer | Stripe Documentation[Skip to content](#main-content)Shell and API Explorer[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench%2Fshell)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench%2Fshell)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)
[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Workbench](/docs/workbench)# Shell and API ExplorerBeta

Use a command-line interface to manage your integration and explore APIs.Shell is a command-line interface within Workbench that provides many of the same commands built into the Stripe CLI. When using Workbench, a minimal Shell is always available at the bottom of the pane, or use the Shell tab to launch a full-screen session.

Use the following Shell features to help you manage and debug your Stripe integration:

- Autocompletion: Shell provides tab completion for API requests and CLI commands.
- API Explorer:Use the built-in API Explorer to visually explore API resources and build API calls from Shell.

NoteShell runs in the browser, so it has some limitations when compared to the Stripe CLI, which can receive and trigger webhook events on your local machine with a local event listener. See Test a webhooks integration with the Stripe CLI to learn more.

## Initial setup

Sign in to the Dashboard. From the Developers menu, click Workbench. Switch to the Shell tab.

Common mistakeShell is read-only in live mode. Switch to test mode to run API requests that create, modify, or delete API objects.

[Listen for events](#listen)1. From the command-line prompt, type`stripe listen`to listen for[webhook events](/webhooks#events-overview), then pressEnteron your keyboard to run the command.

Command Line`stripe listen`This listens to incoming events for your Stripe account.

[Run your first API request](#first)1. ClickNew paneto open a new session in a pane alongside your existing session.
2. Copy the command, paste it into the command-line prompt, then pressEnteron your keyboard.
3. Copy the object identifier (in`id`) from the response for subsequent requests.

Command Line`stripe products create \
--name="Introductory offer (Monthly)" \
--description="$0.99 per month"`This creates a product with a name and description.

[Use the API Explorer](#explorer)1. ClickAPI Explorerto show the interactive API Explorer on the right.
2. Choose the`Products`resource and the`Update`method. The API Explorer shows all the required and optional parameters for the Products resource.
3. Paste the object identifier from the previous step into the`Value`for the`id`path argument. When you provide the API Explorer with an existing object’s identifier, it loads the properties of the existing product.
4. Update the optional parameter`description`to 1.99 USD per month. The API Explorer automatically populates Shell with the equivalent API command to update the product’s description. PressEnterto run the command and update the product.
5. ClickPrint SDK codeto see the equivalent code snippet in the language of your choice.

## Available commands

Shell provides multiple commands in addition to the stripe command (see the Stripe CLI reference).

CommandPurpose`cd`Navigates to other documentation pages`clear`Clears all prior text from the shell`ls`Lists Dashboard pages relative to the current one`pwd`Prints the current page slug and title`shortcuts`Displays keyboard shortcuts that you can use with Shell`stripe`Available Stripe CLI commands (see the[complete reference](/cli))`whoami`Displays logged in merchant detailsWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Initial setup](#initial-setup)[Listen for events](#listen)[Run your first API request](#first)[Use the API Explorer](#explorer)[Available commands](#available-commands)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
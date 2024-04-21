htmlStripe CLI | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-cli%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)
[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Stripe CLI# Stripe CLI

Manage your Stripe resources in test mode directly from the command line.The Stripe CLI is a developer tool to help you build, test, and manage your integration with Stripe directly from the command line. With the Stripe CLI, it’s easy to perform many common tasks like calling Stripe APIs, testing your webhooks integration, and creating an application.

## Start with a guide

[Get started with the Stripe CLIInstall the Stripe CLI on macOS, Windows, and Linux and get started with a YouTube video from Developer Advocacy.](/docs/stripe-cli)[Enable autocompletion for the Stripe CLIEnable autocompletion so that the Stripe CLI automatically completes your commands.](/docs/stripe-cli/autocomplete)[Stripe CLI keys and permissionsLearn about Stripe CLI keys, where they’re stored locally, and where to find their permissions.](/docs/stripe-cli/keys)[Upgrade the Stripe CLITake advantage of the latest features of the Stripe CLI.](/docs/stripe-cli/upgrade)[Reference guidesUse these reference guides to explore the CLI and Stripe APIs.](/docs/stripe-cli/reference)## Log into Stripe to authenticate requests

Log in and authenticate your Stripe user account to generate a set of restricted keys. To learn more, see Stripe CLI keys and permissions.

Command Line`stripe login`Press the Enter key on your keyboard to complete the authentication process in your browser.

Output`Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1 (^C to quit)`## Specify an API version while running requests

When you call Stripe APIs in the CLI, it uses your default API version in all requests. To find your default version in the Developers Dashboard, see the API keys page. To try out different API versions in the CLI, use the following flags:

FlagDescriptionExample`–stripe-version 2024-04-10`Use the`--stripe-version`flag in any CLI request to specify an API version.`stripe products create --name=“My Product” --stripe-version 2024-04-10``--latest`Use the`--latest`flag in any CLI request to specify the latest API version.`stripe products create --name="My Product" --latest`You can also view a list of API versions.

## Stream request logs

Use the stripe logs tail command to stream API request logs. Keep this window open. If you have an error in your API calls, this terminal returns the API error message and a reason for the error.

Command Line`stripe logs tail`## Forward events to your local webhook endpoint

Use the --forward-to flag to send all Stripe events in test mode to your local webhook endpoint. To disable HTTPS certificate verification, use the --skip-verify flag.

Command Line`stripe listen --forward-to localhost:4242/stripe_webhooks`Output`Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)`To forward specific events in a comma separated list, use the --events flag.

Command Line`stripe listen --events payment_intent.created,customer.created,payment_intent.succeeded,charge.succeeded,checkout.session.completed,charge.failed \
  --forward-to localhost:4242/webhook`If you’ve already registered your endpoint in Stripe, you can use the --load-from-webhooks-api and --forward-to flags.

Command Line`stripe listen --load-from-webhooks-api --forward-to localhost:5000`This command forwards events sent to your Stripe-registered public webhook endpoint to your local webhook endpoint. It loads your registered endpoint, parses the path and its registered events, then appends the path to your local webhook endpoint in the --forward-to path. If you’re checking webhook signatures, use the {{WEBHOOK_SIGNING_SECRET}} from the initial output of the listen command.

## List all available events

Use the --help flag to list all possible events that can occur for an event category. For example, to list all possible events for the prebuilt checkout page for Stripe Checkout:

Command Line`stripe trigger checkout --help`## Create a one-time product and price

1. Make a single API request to[Create a product](/api/products/create).

Command Line`stripe products create \
--name="My First Product" \
--description="Created with the Stripe CLI"`1. Look for the product identifier (in`id`) in the response object. Save it for the next step.

If everything worked, the command-line displays the following response.

`{
  "id": "prod_LTenIrmp8Q67sa",
  "object": "product",`See all 25 lines1. Call[Create a price](/api/prices/create)to attach a price of 30 USD. Swap the placeholder in`product`with your product identifier (for example,`prod_LTenIrmp8Q67sa`).

Command Line`stripe prices create \
  --unit-amount=3000 \
  --currency=usd \
  --product={{PRODUCT_ID}}`If everything worked, the command-line displays the following response.

`{
  "id": "price_1KzlAMJJDeE9fu01WMJJr79o",
  "object": "price",`See all 20 lines## Trigger a webhook event while testing

1. Trigger the`checkout.session.completed`event to create the API objects that result from a checkout session successfully completing.

Command Line`stripe trigger checkout.session.completed`Your stripe listen terminal displays the following output:

Command Line`Setting up fixture for: checkout_session
Running fixture for: checkout_session
Setting up fixture for: payment_page
Running fixture for: payment_page
Setting up fixture for: payment_method
Running fixture for: payment_method
Setting up fixture for: payment_page_confirm
Running fixture for: payment_page_confirm
Trigger succeeded!`1. Trigger the`charge.failed`event to create the API objects that result from a failed charge attempt.

Command Line`stripe trigger charge.failed`Your stripe listen terminal displays the following output:

Command Line`Setting up fixture for: charge
Running fixture for: charge
Trigger succeeded!`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Start with a guide](#start-with-a-guide)[Log into Stripe to authenticate requests](#log-into-stripe-to-authenticate-requests)[Specify an API version while running requests](#specify-an-api-version-while-running-requests)[Stream request logs](#stream-request-logs)[Forward events to your local webhook endpoint](#forward-events-to-your-local-webhook-endpoint)[List all available events](#list-all-available-events)[Create a one-time product and price](#create-a-one-time-product-and-price)[Trigger a webhook event while testing](#trigger-a-webhook-event-while-testing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
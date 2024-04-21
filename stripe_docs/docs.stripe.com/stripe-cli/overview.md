# Stripe CLI

The Stripe CLI is a developer tool to help you build, test, and manage your integration with Stripe directly from the command line. With the Stripe CLI, it’s easy to perform many common tasks like calling Stripe APIs, testing your webhooks integration, and creating an application.

## Start with a guide

[Get started with the Stripe CLIInstall the Stripe CLI on macOS, Windows, and Linux and get started with a YouTube video from Developer Advocacy.](/docs/stripe-cli)

Install the Stripe CLI on macOS, Windows, and Linux and get started with a YouTube video from Developer Advocacy.

[Enable autocompletion for the Stripe CLIEnable autocompletion so that the Stripe CLI automatically completes your commands.](/docs/stripe-cli/autocomplete)

Enable autocompletion so that the Stripe CLI automatically completes your commands.

[Stripe CLI keys and permissionsLearn about Stripe CLI keys, where they’re stored locally, and where to find their permissions.](/docs/stripe-cli/keys)

Learn about Stripe CLI keys, where they’re stored locally, and where to find their permissions.

[Upgrade the Stripe CLITake advantage of the latest features of the Stripe CLI.](/docs/stripe-cli/upgrade)

Take advantage of the latest features of the Stripe CLI.

[Reference guidesUse these reference guides to explore the CLI and Stripe APIs.](/docs/stripe-cli/reference)

Use these reference guides to explore the CLI and Stripe APIs.

## Log into Stripe to authenticate requests

Log in and authenticate your Stripe user account to generate a set of restricted keys. To learn more, see Stripe CLI keys and permissions.

[Stripe user account](/get-started/account/activate)

[Stripe CLI keys and permissions](/stripe-cli/keys)

Press the Enter key on your keyboard to complete the authentication process in your browser.

[https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1](https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1)

## Specify an API version while running requests

When you call Stripe APIs in the CLI, it uses your default API version in all requests. To find your default version in the Developers Dashboard, see the API keys page. To try out different API versions in the CLI, use the following flags:

[API keys](https://dashboard.stripe.com/test/apikeys)

You can also view a list of API versions.

[view a list of API versions](/upgrades#api-versions)

## Stream request logs

Use the stripe logs tail command to stream API request logs. Keep this window open. If you have an error in your API calls, this terminal returns the API error message and a reason for the error.

## Forward events to your local webhook endpoint

Use the --forward-to flag to send all Stripe events in test mode to your local webhook endpoint. To disable HTTPS certificate verification, use the --skip-verify flag.

[Stripe events](/cli/trigger#trigger-event)

To forward specific events in a comma separated list, use the --events flag.

If you’ve already registered your endpoint in Stripe, you can use the --load-from-webhooks-api and --forward-to flags.

[registered your endpoint in Stripe](/webhooks#register-webhook)

This command forwards events sent to your Stripe-registered public webhook endpoint to your local webhook endpoint. It loads your registered endpoint, parses the path and its registered events, then appends the path to your local webhook endpoint in the --forward-to path. If you’re checking webhook signatures, use the {{WEBHOOK_SIGNING_SECRET}} from the initial output of the listen command.

## List all available events

Use the --help flag to list all possible events that can occur for an event category. For example, to list all possible events for the prebuilt checkout page for Stripe Checkout:

[--help](/cli/help)

[prebuilt checkout page](/checkout/quickstart)

[Stripe Checkout](/payments/checkout)

## Create a one-time product and price

- Make a single API request to Create a product.

[Create a product](/api/products/create)

- Look for the product identifier (in id) in the response object. Save it for the next step.

If everything worked, the command-line displays the following response.

- Call Create a price to attach a price of 30 USD. Swap the placeholder in product with your product identifier (for example, prod_LTenIrmp8Q67sa).

[Create a price](/api/prices/create)

If everything worked, the command-line displays the following response.

## Trigger a webhook event while testing

- Trigger the checkout.session.completed event to create the API objects that result from a checkout session successfully completing.

Your stripe listen terminal displays the following output:

- Trigger the charge.failed event to create the API objects that result from a failed charge attempt.

Your stripe listen terminal displays the following output:

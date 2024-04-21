# Shell and API ExplorerBeta

Shell is a command-line interface within Workbench that provides many of the same commands built into the Stripe CLI. When using Workbench, a minimal Shell is always available at the bottom of the pane, or use the Shell tab to launch a full-screen session.

[Stripe CLI](/stripe-cli)

Use the following Shell features to help you manage and debug your Stripe integration:

- Autocompletion: Shell provides tab completion for API requests and CLI commands.

- API Explorer: Use the built-in API Explorer to visually explore API resources and build API calls from Shell.

Shell runs in the browser, so it has some limitations when compared to the Stripe CLI, which can receive and trigger webhook events on your local machine with a local event listener. See Test a webhooks integration with the Stripe CLI to learn more.

[Stripe CLI](/stripe-cli)

[Test a webhooks integration with the Stripe CLI](/webhooks#test-webhook)

## Initial setup

Sign in to the Dashboard. From the Developers menu, click Workbench. Switch to the Shell tab.

[Dashboard](https://dashboard.stripe.com/)

Shell is read-only in live mode. Switch to test mode to run API requests that create, modify, or delete API objects.

[test mode](/test-mode)

[Listen for events](#listen)

## Listen for events

- From the command-line prompt, type stripe listen to listen for webhook events, then press Enter on your keyboard to run the command.

[webhook events](/webhooks#events-overview)

This listens to incoming events for your Stripe account.

[Run your first API request](#first)

## Run your first API request

- Click New pane to open a new session in a pane alongside your existing session.

- Copy the command, paste it into the command-line prompt, then press Enter on your keyboard.

- Copy the object identifier (in id) from the response for subsequent requests.

This creates a product with a name and description.

[Use the API Explorer](#explorer)

## Use the API Explorer

- Click API Explorer to show the interactive API Explorer on the right.

- Choose the Products resource and the Update method. The API Explorer shows all the required and optional parameters for the Products resource.

- Paste the object identifier from the previous step into the Value for the id path argument. When you provide the API Explorer with an existing object’s identifier, it loads the properties of the existing product.

- Update the optional parameter description to 1.99 USD per month. The API Explorer automatically populates Shell with the equivalent API command to update the product’s description. Press Enter to run the command and update the product.

- Click Print SDK code to see the equivalent code snippet in the language of your choice.

## Available commands

Shell provides multiple commands in addition to the stripe command (see the Stripe CLI reference).

[Stripe CLI reference](/cli)

[complete reference](/cli)

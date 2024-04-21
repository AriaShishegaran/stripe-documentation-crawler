# Stripe for Visual Studio Code

Stripe’s extension for Visual Studio Code lets you generate sample code, view API request logs, forward events to your application, and use Stripe within your editor.

[extension](https://marketplace.visualstudio.com/items?itemName=Stripe.vscode-stripe)

[Visual Studio Code](https://code.visualstudio.com/)

A new Stripe panel in the activity bar provides access to code snippets for several languages, adds debug configurations, and extends the command palette with common developer workflows.

[debug configurations](https://code.visualstudio.com/docs/editor/debugging#_redirect-inputoutput-tofrom-the-debug-target)

[command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)

With Stripe for VS Code, you can:

- Get started quickly with a Stripe Sample.

[Get started quickly with a Stripe Sample.](#samples)

- Forward Stripe webhook events to your local application.

[Forward Stripe webhook events to your local application.](#webhooks)

- Stream request logs in real-time.

[Stream request logs in real-time.](#monitor-logs)

- Trigger new events while testing.

[Trigger new events while testing.](#webhooks)

- Generate snippets for common scenarios.

[Generate snippets for common scenarios.](#snippets)

- Verify your source code doesn’t expose API keys.

[Verify your source code doesn’t expose API keys.](#linter)

- Quickly jump to the API reference.

[Quickly jump to the API reference.](#api-reference)

- Easily access the Stripe Dashboard.

[Easily access the Stripe Dashboard.](#dashboard-access)

## Install Stripe for VS Code

As a prerequisite, ensure you have the Stripe CLI installed.

[Stripe CLI](/stripe-cli#install)

You can find the Stripe VS Code extension in the Visual Studio Marketplace. Click Install to add the extension to your editor.

[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Stripe.vscode-stripe)

## Features

Stripe Samples are built by Stripe, and provide all of the client and server code you need for common integration scenarios, such as creating a subscription with Stripe Billing.

[Stripe Samples](https://github.com/stripe-samples)

The Start with a Stripe Sample button allows you to browse through the catalog and select the right language for your integration. The extension clones and opens the Sample in a new workspace, automatically populating your API keys in the .env file of the Sample.

You can listen for incoming webhook events and forward them to your to your local machine in one of two ways:

- Click Forward webhook events to your local machine in the Events section.

- Run the command Stripe: Forward webhook events to your local machine from the command palette.

[command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)

Then, enter the localhost URL that you want to forward events to. If you’re using Connect, you can set a different URL for events from your Connect applications. If your localhost URLs use HTTPS, you can skip SSL certificate verification.

You can use the Trigger new event button to test your webhook integration with events from the Stripe API.

You can only trigger events in test mode.

You can stream events created by members of your account in real time with the Start streaming events button. Clicking on an event entry under Recent events opens event details directly inside your editor.

If you’d like to resend an event, you can right click an event entry under Recent events or run a Stripe CLI command: stripe events resend <event>.

[Stripe CLI](/cli/events/resend)

When forwarding events to your local machine, you may find yourself entering the same URLs over and over. To fix this, you can create a debug configuration to save your forwarding setup, allowing you to start forwarding to your URLs with a single button.

[debug configuration](https://code.visualstudio.com/docs/editor/debugging#_redirect-inputoutput-tofrom-the-debug-target)

Place the following configuration in a launch.json file, which VS Code uses to track debugging setup details. Then, select the configuration in the Run view. After selecting your configuration, press F5 to quickly start forwarding events.

[launch.json](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)

[http://localhost:3000](http://localhost:3000)

[http://localhost:3000](http://localhost:3000)

You can specify the forwardTo and forwardConnectTo parameters; these are the URLs on your local machine that you want to receive your account’s events and Connect events, respectively. The events parameter accepts an optional list to specify which events to receive. If you’re using HTTPS URLs, the skipVerify parameter accepts a Boolean to skip verifying SSL certificates.

You can launch your local application and forward webhook events simultaneously using a compound configuration.

[compound configuration](https://code.visualstudio.com/docs/editor/debugging#_compound-launch-configurations)

[http://localhost:3000](http://localhost:3000)

[http://localhost:3000](http://localhost:3000)

You can stream API request logs created by members of your account in real time with the Start streaming API logs button. Clicking on a log entry under Recent logs opens log details directly inside your editor. From there, you can hover over the request ID to open the log in your Dashboard.

The extension only delivers logs for requests made in test mode.

You can quickly generate code snippets for common scenarios (for example, creating a Checkout Session and redirecting the user to the browser) or basic API requests. After generating a snippet, you can tab through it to fill in your values.

The built-in Stripe linter checks for API keys in your source code and marks them as problems if you unsafely expose them.

[API keys](/keys)

The linter treats unsafe use of test-mode keys as warnings and live-mode keys as errors.

You can hover over a resource method to reveal a link to the Stripe API reference. This is useful for identifying parameters for an API request or the shape of an API response.

[Stripe API reference](/api)

The Quick Links section includes links to quickly jump to the Dashboard to manage API keys, webhooks, and other resources.

## Settings

The following configurations can be set in your VS Code settings:

[VS Code settings](https://code.visualstudio.com/docs/getstarted/settings)

[Stripe CLI reference](/cli/login)

## Commands

The extension supports various commands to access features through the command palette. To see the full list of supported commands, open the command palette and type Stripe.

[command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)

## Contributing

Stripe VS Code is an open-source project under the MIT License. Contributions to the project are welcome. For details on how to contribute to the project, check out the vscode-stripe project on GitHub.

[vscode-stripe](https://github.com/stripe/vscode-stripe)

## Feedback

Feel free to provide feedback or submit feature requests through the project’s issue tracker.

[issue tracker](https://github.com/stripe/vscode-stripe/issues/new)

## See also

- Stripe CLI

[Stripe CLI](/stripe-cli)

- Webhooks

[Webhooks](/webhooks)

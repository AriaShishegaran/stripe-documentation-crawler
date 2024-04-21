htmlStripe for Visual Studio Code | Stripe Documentation[Skip to content](#main-content)Stripe for Visual Studio Code[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-vscode)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-vscode)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)# Stripe for Visual Studio Code

Build, test, and use Stripe inside your editor.Stripe’s extension for Visual Studio Code lets you generate sample code, view API request logs, forward events to your application, and use Stripe within your editor.

A new Stripe panel in the activity bar provides access to code snippets for several languages, adds debug configurations, and extends the command palette with common developer workflows.

With Stripe for VS Code, you can:

- [Get started quickly with a Stripe Sample.](#samples)
- [Forward Stripe webhook events to your local application.](#webhooks)
- [Stream request logs in real-time.](#monitor-logs)
- [Trigger new events while testing.](#webhooks)
- [Generate snippets for common scenarios.](#snippets)
- [Verify your source code doesn’t expose API keys.](#linter)
- [Quickly jump to the API reference.](#api-reference)
- [Easily access the Stripe Dashboard.](#dashboard-access)

## Install Stripe for VS Code

NoteAs a prerequisite, ensure you have the Stripe CLI installed.

RecommendedManualYou can find the Stripe VS Code extension in the Visual Studio Marketplace. Click Install to add the extension to your editor.

## Features

### Get started quickly with a Stripe Sample

Stripe Samples are built by Stripe, and provide all of the client and server code you need for common integration scenarios, such as creating a subscription with Stripe Billing.

The Start with a Stripe Sample button allows you to browse through the catalog and select the right language for your integration. The extension clones and opens the Sample in a new workspace, automatically populating your API keys in the .env file of the Sample.

### Trigger and forward webhook events

You can listen for incoming webhook events and forward them to your to your local machine in one of two ways:

- ClickForward webhook events to your local machinein theEventssection.
- Run the command`Stripe: Forward webhook events to your local machine`from the[command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

Then, enter the localhost URL that you want to forward events to. If you’re using Connect, you can set a different URL for events from your Connect applications. If your localhost URLs use HTTPS, you can skip SSL certificate verification.

You can use the Trigger new event button to test your webhook integration with events from the Stripe API.

CautionYou can only trigger events in test mode.

You can stream events created by members of your account in real time with the Start streaming events button. Clicking on an event entry under Recent events opens event details directly inside your editor.

NoteIf you’d like to resend an event, you can right click an event entry under Recent events or run a Stripe CLI command: stripe events resend <event>.

Stripe debug configuration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When forwarding events to your local machine, you may find yourself entering the same URLs over and over. To fix this, you can create a debug configuration to save your forwarding setup, allowing you to start forwarding to your URLs with a single button.

Place the following configuration in a launch.json file, which VS Code uses to track debugging setup details. Then, select the configuration in the Run view. After selecting your configuration, press F5 to quickly start forwarding events.

.vscode/launch.json`{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Stripe: Webhooks listen",
      "type": "stripe",
      "request": "launch",
      "command": "listen",
      "forwardTo": "http://localhost:3000",
      "forwardConnectTo": "http://localhost:3000",
      "events": ["payment_intent.succeeded", "payment_intent.canceled"],
      "skipVerify": true
    }
  ]
}`You can specify the forwardTo and forwardConnectTo parameters; these are the URLs on your local machine that you want to receive your account’s events and Connect events, respectively. The events parameter accepts an optional list to specify which events to receive. If you’re using HTTPS URLs, the skipVerify parameter accepts a Boolean to skip verifying SSL certificates.

Compound configurations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can launch your local application and forward webhook events simultaneously using a compound configuration.

.vscode/launch.json`{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Stripe: Webhooks listen",
      "type": "stripe",
      "request": "launch",
      "command": "listen",
      "forwardTo": "http://localhost:3000",
      "forwardConnectTo": "http://localhost:3000",
      "events": ["payment_intent.succeeded", "payment_intent.canceled"],
      "skipVerify": true
    },
    {
      "type": "node",
      "request": "launch",
      "name": "Node: Launch Program",
      "program": "${workspaceFolder}/examples/standalone.js",
      "skipFiles": ["<node_internals>/**"]
    }
  ],
  "compounds": [
    {
      "name": "Launch: Stripe + API",
      "configurations": ["Node: Launch Program", "Stripe: Webhooks listen"]
    }
  ]
}`### Monitor API request logs in real-time

You can stream API request logs created by members of your account in real time with the Start streaming API logs button. Clicking on a log entry under Recent logs opens log details directly inside your editor. From there, you can hover over the request ID to open the log in your Dashboard.

CautionThe extension only delivers logs for requests made in test mode.

### Code snippets for common Stripe scenarios

You can quickly generate code snippets for common scenarios (for example, creating a Checkout Session and redirecting the user to the browser) or basic API requests. After generating a snippet, you can tab through it to fill in your values.

### Verify your source code doesn’t expose API keys

The built-in Stripe linter checks for API keys in your source code and marks them as problems if you unsafely expose them.

NoteThe linter treats unsafe use of test-mode keys as warnings and live-mode keys as errors.

![](https://b.stripecdn.com/docs-statics-srv/assets/api_key_linter.99d5ec681ed1835e12ec8ff43a31df42.png)

### Access the Stripe API reference

You can hover over a resource method to reveal a link to the Stripe API reference. This is useful for identifying parameters for an API request or the shape of an API response.

![](https://b.stripecdn.com/docs-statics-srv/assets/api_reference_hover.7faf7deee997b0f54656ed4a4f842e14.png)

### Access the Stripe Dashboard

The Quick Links section includes links to quickly jump to the Dashboard to manage API keys, webhooks, and other resources.

![](https://b.stripecdn.com/docs-statics-srv/assets/quick_links_view.dd5362166ad40a383ca540bc62e71ed6.png)

## Settings

The following configurations can be set in your VS Code settings:

Setting nameDescription`stripe.cliInstallPath`Specifies the absolute install path for the Stripe CLI executable. Default: the default install path for the Stripe CLI`stripe.projectName`Specifies the project name to read from for the Stripe CLI configuration. You can define a unique configuration for individual projects, or use the global configuration by default. See the[Stripe CLI reference](/cli/login)for more details. Default:`default``stripe.telemetry.enabled`Specifies whether to enable Stripe telemetry (even if enabled still abides by the overall`telemetry.enableTelemetry`setting). Default:`true`## Commands

The extension supports various commands to access features through the command palette. To see the full list of supported commands, open the command palette and type Stripe.

![](https://b.stripecdn.com/docs-statics-srv/assets/command_palette.ee0cb66b2fbbc0c2e981e1340815e57e.png)

## Contributing

Stripe VS Code is an open-source project under the MIT License. Contributions to the project are welcome. For details on how to contribute to the project, check out the vscode-stripe project on GitHub.

## Feedback

Feel free to provide feedback or submit feature requests through the project’s issue tracker.

## See also

- [Stripe CLI](/stripe-cli)
- [Webhooks](/webhooks)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Install Stripe for VS Code](#installation)[Features](#features)[Settings](#extension-configuration)[Commands](#commands)[Contributing](#contributing)[Feedback](#feedback)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
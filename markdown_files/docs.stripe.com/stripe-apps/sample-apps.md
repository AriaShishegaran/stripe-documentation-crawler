htmlSample apps | Stripe Documentation[Skip to content](#main-content)Sample apps[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fsample-apps)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fsample-apps)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Sample apps

See working apps from design to code.Many sample apps are available on GitHub or as design files in our Figma UI toolkit. Use these as a starting point for your own app.

## Complete sample app

SuperTodo is a complete to-do list app you can download from GitHub. It demonstrates:

- A[frontend-only app](/stripe-apps/how-stripe-apps-work#frontend-only-applications)that integrates with the Stripe API
- UI components, including[List](/stripe-apps/components/list),[Tab](/stripe-apps/components/tabs), and[Button](/stripe-apps/components/button)
- Design patterns, including[Action buttons](/stripe-apps/patterns/action-buttons)and[Communicating state](/stripe-apps/patterns/communicating-state)

![Screens from the SuperTodo example app](https://b.stripecdn.com/docs-statics-srv/assets/supertodo.2647da490dc734af24defeb13356d902.png)

The SuperTodo example app shows you how to use lists, tabs, buttons, a creation screen, and a confirmation message

## Sample design files

Our Figma UI toolkit includes design examples for SuperTodo and five other sample apps. Use these to see our design patterns and UI components in action.

![All example apps side by side](https://b.stripecdn.com/docs-statics-srv/assets/app-examples.2b959be2502e11b7200649303a9096c1.png)

Example apps you can use to get started

## Minimal samples

These samples on GitHub demonstrate specific techniques. They don’t come with design files, and they might need additional features to be useful:

[Basic auth](https://github.com/stripe/stripe-apps/tree/main/examples/basic-auth)Authenticate with OAuth2[Climate](https://github.com/stripe/stripe-apps/tree/main/examples/climate)Link to[Stripe Climate](https://www.stripe.com/climate)in your app[Dropbox OAuth PKCE](https://github.com/stripe/stripe-apps/tree/main/examples/dropbox-oauth-pkce)Retrieve an OAuth token from Dropbox and set it in the[Secret Store API](/stripe-apps/store-secrets)[GitHub OAuth](https://github.com/stripe/stripe-apps/tree/main/examples/github-oauth)Authenticate with GitHub using OAuth[Messaging](https://github.com/stripe/stripe-apps/tree/main/examples/messaging)Display recent messages from a customer[Settings View](https://github.com/stripe/stripe-apps/tree/main/examples/settings-view)Save application settings in the[Secret Store API](/stripe-apps/store-secrets)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Complete sample app](#complete-sample-app)[Sample design files](#sample-design-files)[Minimal samples](#minimal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
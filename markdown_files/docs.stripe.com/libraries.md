htmlStripe SDKs | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flibraries)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flibraries)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)
[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)# Stripe SDKs

Libraries and tools for interacting with your Stripe integration.## Server-side SDKs

Stripe’s server-side helper libraries (also known as server-side SDKs) reduce the amount of work required to use Stripe’s REST APIs, starting with reducing the boilerplate code you have to write. Below are the installation instructions for these libraries in a variety of popular server-side programming languages.

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`You can access certain Stripe products and features in the beta stage with beta SDKs. The versions of these beta SDKs have the beta or b suffix, for example, 5.1.0b3 in Python and 5.1.0-beta.3 in other language SDKs. Try these beta SDKs and share feedback with us before the features reach the stable phase. To learn more about how to use the beta SDKs, read the readme file in the GitHub repository of the individual language SDKs.

## Web SDKs

Stripe provides the following web client SDKs to enable integrations with Stripe Elements, our prebuilt UI components, to create a payment form that lets you securely collect a customer’s card details without handling the sensitive data.

[React Stripe.jsReact Native](/stripe-js/react)[ES Module Stripe.jsHTML · JavaScript](/libraries/stripejs-esmodule)## Mobile device SDKs

Our mobile device helper libraries (also known as Mobile device SDKs) help you create native applications for Apple’s and Android’s devices and platforms. The React Native SDK helps you integrate Stripe into iOS and Android applications built with React Native.

[Stripe iOS SDKiOS](/libraries/ios)[Stripe Android SDKAndroid](/libraries/android)[Stripe React Native SDKReact Native](/libraries/react-native)## Community libraries

The following is a list of community-supported libraries that we know about—these libraries aren’t supported by Stripe, and we can’t speak to their accuracy or completeness. But these are open source, so feel free to fork and hack as much as you like.

[Community librariesWeb · Mobile](/libraries/community)## Stripe OpenAPI Specification

Stripe’s OpenAPI specification empowers you with a broad set of developer tooling, starting with Postman collections.

[Stripe Postman CollectionAPI](https://www.postman.com/stripedev/workspace/stripe-developers/overview)[Stripe Open API SpecificationAPI](https://github.com/stripe/openapi)## Stripe versioning

Stripe server-side SDKs use Semantic Versioning, whereas Stripe APIs are versioned by the release date. A breaking API change results in an increment in the major version number of the SDK.

[Stripe versioning and support policiesAPI · SDK](/libraries/versioning)[Set a Stripe API versionAPI](/libraries/set-version)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Server-side SDKs](#server-side-libraries)[Web SDKs](#client-side-and-ui-libraries)[Mobile device SDKs](#stripe-mobile-sdks)[Community libraries](#community-libraries)[Stripe OpenAPI Specification](#api-resources)[Stripe versioning](#versioning)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
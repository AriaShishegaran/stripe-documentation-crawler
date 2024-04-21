htmlSet up your development environment | Stripe Documentation[Skip to content](#main-content)Development environment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fquickstart)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fquickstart)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)
Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Building your integration](/docs/development/get-started)# Set up your development environment

Fast-track local development with the essential tools needed for a Stripe integration.## Quickstart by language

Stripe’s server-side helper libraries (also known as server-side SDKs) and command-line interface (CLI) allow you to interact with Stripe’s REST APIs. Start with the Stripe CLI and make Stripe API calls without writing a line of code. Use the SDKs to avoid writing boilerplate code. To start sending requests from your environment, choose a language to follow a quickstart guide.

RubyPythonGoJavaNode.jsPHP.NETIn this quickstart, you install the Stripe CLI—an essential tool that gets you command line access to your Stripe integration. You also install the Stripe Ruby server-side SDK to get access to Stripe APIs from applications written in Ruby.

## What you learn

In this quickstart, you’ll learn:

- How to call Stripe APIs without writing a line of code
- How to manage third-party dependencies using a bundler with RubyGems
- How to install the Stripe Ruby SDK v11.0.0
- How to send your first SDK request

[Set up the Stripe CLI](#setup-cli)First, create a Stripe account or sign in.

### Install

From the command-line, use an install script or download and extract a versioned archive file for your operating system to install the CLI.

homebrewaptyumScoopmacOSLinuxWindowsDockerTo install the Stripe CLI with homebrew, run:

Command Line`brew install stripe/stripe-cli/stripe`### Authenticate

Login and authenticate your Stripe user Account to generate a set of restricted keys. To learn more, see Stripe CLI keys and permissions.

Command Line`stripe login`Press the Enter key on your keyboard to complete the authentication process in your browser.

Output`Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1 (^C to quit)`### Confirm setup

Now that you’ve installed the CLI, you can make a single API request to Create a product.

Command Line`stripe products create \
--name="My First Product" \
--description="Created with the Stripe CLI"`Look for the product identifier (in id) in the response object. Save it for the next step.

If everything worked, the command-line displays the following response.

`{
  "id": "prod_LTenIrmp8Q67sa",
  "object": "product",`See all 25 linesNext, call Create a price to attach a price of 30 USD. Swap the placeholder in product with your product identifier (for example, prod_LTenIrmp8Q67sa).

Command Line`stripe prices create \
  --unit-amount=3000 \
  --currency=usd \
  --product={{PRODUCT_ID}}`If everything worked, the command-line displays the following response.

`{
  "id": "price_1KzlAMJJDeE9fu01WMJJr79o",
  "object": "price",`See all 20 lines[Manage third-party dependencies](#sdk-deps)We recommend managing third-party dependencies using the RubyGems command-line tool, which allows you to add new libraries and include them in your Ruby projects. Check whether RubyGems is installed:

### Install RubyGems

Command Line`gem --version`If you get gem: command not found, download RubyGems from their downloads page.

[Install the Ruby server-side SDK](#install-sdk)The latest version of the Stripe Ruby server-side SDK is v11.0.0. It supports Ruby versions 2.3+.

Check your Ruby version:

Command Line`ruby -v`### Install the library

Create a gem file and install the generated gem using a bundler with RubyGems.

Add the latest version of the Stripe gem to a project:

Command Line`bundle add stripe`Install the required gems from your specified sources:

Command Line`bundle install`### Installation alternatives

[Run your first SDK request](#test-install)Now that you have the Ruby SDK installed, you can create a subscription Product and attach a Price with a couple API requests. We’re using the product identifier returned in the response to create the price in this example.

NoteThis sample uses your Stripe user account’s default keys for test mode. Only you can see these values.

create_price.rb`require 'rubygems'
require 'stripe'
Stripe.api_key = "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"

starter_subscription = Stripe::Product.create(
  name: 'Starter Subscription',
  description: '$12/Month subscription',
)

starter_subscription_price = Stripe::Price.create(
  currency: 'usd',
  unit_amount: 1200,
  recurring: {interval: 'month'},
  product: starter_subscription['id'],
)

puts "Success! Here is your starter subscription product id: #{starter_subscription.id}"
puts "Success! Here is your starter subscription price id: #{starter_subscription_price.id}"`Save the file as create_price.rb. From the command line, cd to the directory containing the file you just saved and run:

Command Line`ruby create_price.rb`If everything worked, the command line shows the following response. Save these identifiers so you can use them while building your integration.

Command Line`Success! Here is your starter subscription product id: prod_0KxBDl589O8KAxCG1alJgiA6
Success! Here is your starter subscription price id: price_0KxBDm589O8KAxCGMgG7scjb`## See also

This wraps up the quickstart. See the links below for a few different ways to process a payment for the product you just created.

- [Create a payment link](/payment-links)
- [Prebuilt checkout page](/checkout/quickstart)
- [Custom payment flow](/payments/quickstart)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Quickstart by language](#quickstart-by-language)[What you learn](#what-you-learn)[Set up the Stripe CLI](#setup-cli)[Manage third-party dependencies](#sdk-deps)[Install the Ruby server-side SDK](#install-sdk)[Run your first SDK request](#test-install)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
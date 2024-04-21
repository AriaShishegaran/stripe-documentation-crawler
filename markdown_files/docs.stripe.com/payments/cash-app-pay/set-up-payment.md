htmlSet up future Cash App Pay payments | Stripe Documentation[Skip to content](#main-content)Save payment details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcash-app-pay%2Fset-up-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcash-app-pay%2Fset-up-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[Cash App Pay](/docs/payments/cash-app-pay)# Set up future Cash App Pay payments

Learn how to save Cash App Pay details and charge your customers later.WebMobilePrebuilt checkout pageDirect APIThis guide covers how to save a Cash App Pay payment details using Checkout, our fully hosted checkout page.

To create recurring payments after saving a payment method in Checkout, see Set up a subscription with Cash App Pay for more details.

[Set up StripeServer-side](#web-set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve a CustomerServer-side](#web-create-customer)To reuse a Cash App Pay payment method for future payments, attach it to a Customer.

Create a Customer object when your customer creates an account with your business, and associate the ID of the Customer object with your own internal representation of a customer. Alternatively, you can create a new Customer later, right before saving a payment method for future payments.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode description="My First Test Customer (created for API docs)"`[Create a Checkout SessionServer-side](#web-create-checkout-session)Your customer must authorize you to use their Cash App account for future payments through Stripe Checkout. This allows you to accept Cash App payments. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`Create a Checkout Session in setup mode to collect the required information. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'setup',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'cashapp'],
  customer: customer.id,
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`[Test your integrationServer-side](#web-test-integration)Mobile web app testingDesktop web app testingTo test your integration, choose Cash App Pay as the payment method and tap Pay. In test mode, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping Pay redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#web-set-up-stripe)[Create or retrieve a Customer](#web-create-customer)[Create a Checkout Session](#web-create-checkout-session)[Test your integration](#web-test-integration)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
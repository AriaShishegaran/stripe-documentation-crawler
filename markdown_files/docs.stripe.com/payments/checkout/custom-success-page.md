htmlCustomize redirect behavior with a Stripe-hosted page | Stripe Documentation[Skip to content](#main-content)Customize redirect behavior (Stripe-hosted page)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-success-page)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-success-page)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Customize redirect behavior with a Stripe-hosted page

For Stripe-hosted pages, display a confirmation page with your customer's order information.After payment succeeds, Stripe redirects your customer to a success page that you create and host on your site.

Common mistakeIf you’ve integrated with an embedded payment form, you can’t use the success_url parameter. You must use return_url. Learn more about customizing redirect behavior for integrations with the embedded form.

## Redirect customers to a success page

You can use the details from a Checkout Session to display an order confirmation page for your customer (for example, their name or payment amount) after the payment. To use the details from a Checkout Session:

1. Modify the`success_url`[parameter](/api/checkout/sessions/create#create_checkout_session-success_url)to pass the Checkout Session ID to the client side.
2. Look up the Checkout Session using the ID on your success page.
3. Use the Checkout Session to customize what’s displayed on your success page.

## Modify the success URL Server-side

Add the {CHECKOUT_SESSION_ID} template variable to the success_url when you create the Checkout Session. Note that this is a literal string and must be added exactly as you see it here. Do not substitute it with a Checkout Session ID—this happens automatically after your customer pays and is redirected to the success page.

[Ruby](#)`session = Stripe::Checkout::Session.create(
  success_url: "http://yoursite.com/order/success",
  success_url: "http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}",
  # other options...,
)`## Create the success page Server-side

Look up the Checkout Session using the ID and create a success page to display the order information. This example prints out the customer’s name:

[Ruby](#)`# This example sets up an endpoint using the Sinatra framework.
# Watch this video to get started: https://youtu.be/8aA9Enb8NVc.

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

require 'sinatra'

get '/order/success' do
  session = Stripe::Checkout::Session.retrieve(params[:session_id])
  customer = Stripe::Customer.retrieve(session.customer)

  "<html><body><h1>Thanks for your order, #{customer.name}!</h1></body></html>"
end`## Test the integration

To confirm that your redirect is working as expected:

1. Click the checkout button.
2. Fill in the customer name and other payment details.
3. ClickPay.

If it works, you’re redirected to the success page with your custom message. For example, if you used the message in the code samples, the success page displays this message: Thanks for your order, Jenny Rosen!

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Redirect customers to a success page](#success-url)[Modify the success URL](#modify-the-success-url)[Create the success page](#create-the-success-page)[Test the integration](#test-the-integration)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
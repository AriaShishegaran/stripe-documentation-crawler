htmlCreate payment links with Connect | Stripe Documentation[Skip to content](#main-content)Create payment links with Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayment-links)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayment-links)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Create payment links with Connect

With Connect, you can create payment links for connected accounts, optionally taking fees in the process.### Learn more about Connect

Don’t know much about Connect? Check out our Overview article.

You can create payment links for connected accounts, which support several approaches for collecting payments. You can use direct charges to create them directly on the connected account. Alternatively, you can create payment links on the platform with transfers to the connected account by using destination charges. You can also take an application fee on these payment links.

## Create a payment link using direct charges

To create an payment link that directly charges on a connected account, create a payment link while authenticated as the connected account. For this to work, you must also create the product and the price on the connected account.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1`When you use direct charges, the connected account is responsible for the cost of the Stripe fees, refunds, and chargebacks.

## Create a payment link using destination charges

To create a payment link that charges on the platform and creates automatic transfers to a connected account, create a payment link while providing the connected account ID as the transfer_data[destination] value.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`For this to work, you must also create the product and the price on the platform account. When using automatic transfers, the platform is the business of record.

When performing destination charges, Payment Links uses the brand settings of your platform account for the payment page. See the Customize branding section for more information.

## Create a payment link using destination charges and on_behalf_of

You can also create a destination charge with the on_behalf_of parameter set to the connected account ID (by default, it is the platform). The on_behalf_of parameter determines the settlement merchant, which affects:

- Whose statement descriptor the end user sees
- Whose address and phone number the end user sees
- The settlement currency of the charge
- The payment page branding the customer sees

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`## Fulfill orders placed through payment links

After an end user pays through a payment link you need to enable your connected accounts to handle any fulfillment necessary.

Configure a webhook endpoint in the Dashboard.

![Webhooks page in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/account_webhooks.03b71cec87ef2093fe0caa92e5bfce44.png)

Then create an HTTP endpoint on your server to monitor for completed payments. Make sure to replace the endpoint secret key (whsec_...) in the example with your key.

server.rb[Ruby](#)`# Using Sinatra.
require 'sinatra'
require 'stripe'

set :port, 4242

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in
# the Developer Dashboard
endpoint_secret = 'whsec_...'

post '/webhook' do
  payload = request.body.read
  sig_header = request.env['HTTP_STRIPE_SIGNATURE']

  event = nil

  # Verify webhook signature and extract the event.
  # See https://stripe.com/docs/webhooks#verify-events for more information.
  begin
    event = Stripe::Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  rescue JSON::ParserError => e
    # Invalid payload.
    status 400
    return
  rescue Stripe::SignatureVerificationError => e
    # Invalid Signature.
    status 400
    return
  end

  if event['type'] == 'checkout.session.completed'
    session = event['data']['object']
    connected_account_id = event['account']
    handle_completed_checkout_session(connected_account_id, session)
  end

  status 200
end

def handle_completed_checkout_session(connected_account_id, session)
  # Fulfill the purchase
  puts 'Connected account ID: ' + connected_account_id
  puts session.to_s
end`Learn more in our fulfillment guide.

[OptionalCollect application fees](#collecting-fees)[OptionalCustomize branding](#customize-branding)[OptionalIntegrate tax calculation and collection](#connect-tax)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Direct charges](#direct)[Destination charges](#destination)[Destination charges and on_behalf_of](#destination-on-behalf-of)[Fulfill orders placed through payment links](#fulfill-orders-placed-through-payment-links)Products Used[Connect](/connect)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
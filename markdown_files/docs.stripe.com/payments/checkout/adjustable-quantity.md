htmlMake line item quantities adjustable | Stripe Documentation[Skip to content](#main-content)Make line item quantities adjustable[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadjustable-quantity)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fadjustable-quantity)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Make line item quantities adjustable

Configure the Checkout Session so customers can adjust line item quantity during checkout.## Create a Checkout Session with adjustable_quantity enabled

Set adjustable_quantity on your line_items when creating a Checkout Session to enable your customers to update the quantity of an item during checkout.

You can customize the default settings for the minimum and maximum quantities allowed by setting adjustable_quantity.minimum and adjustable_quantity.maximum. By default, an item’s minimum adjustable quantity is 0 and the maximum adjustable quantity is 99. You can specify a value of up to 999999 for adjustable_quantity.maximum.

When using adjustable quantities with a line_items[].quantity value greater than 99 (the default adjustable maximum), set adjustable_quantity.maximum to be greater than or equal to that item’s quantity.

If you use adjustable quantities, change your configuration so that it uses adjustable_quantity.maximum when creating the Checkout Session to reserve inventory quantity instead of the line_items quantity.

Checkout prevents the customer from removing an item if it is the only item remaining.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][price_data][tax_behavior]"=exclusive \
  -d "line_items[0][adjustable_quantity][enabled]"=true \
  -d "line_items[0][adjustable_quantity][minimum]"=1 \
  -d "line_items[0][adjustable_quantity][maximum]"=10 \
  -d "line_items[0][quantity]"=1 \
  -d "automatic_tax[enabled]"=true \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`## Handling completed transactions

After the payment completes, you can make a request for the finalized line items and their quantities. If your customer removes a line item, it is also removed from the line items response. See the Fulfillment guide to learn how to create an event handler to handle completed Checkout Sessions.

NoteTo test your event handler, install the Stripe CLI and use stripe listen --forward-to localhost:4242/webhook to forward events to your local server.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"

require 'sinatra'

# You can find your endpoint's secret in your webhook settings
endpoint_secret = 'whsec_...'

post '/webhook' do
  event = nil

  # Verify webhook signature and extract the event
  # See https://stripe.com/docs/webhooks#verify-events for more information.
  begin
    sig_header = request.env['HTTP_STRIPE_SIGNATURE']
    payload = request.body.read
    event = Stripe::Webhook.construct_event(payload, sig_header, endpoint_secret)
  rescue JSON::ParserError => e
    # Invalid payload
    return status 400
  rescue Stripe::SignatureVerificationError => e
    # Invalid signature
    return status 400
  end

  if event['type'] == 'checkout.session.completed'
    checkout_session = event['data']['object']

    line_items = Stripe::Checkout::Session.list_line_items(checkout_session['id'], {limit: 100})

    # Fulfill the purchase...
    begin
      fulfill_order(checkout_session, line_items)
    rescue NotImplementedError => e
      return status 400
    end
  end

  status 200
end

def fulfill_order(checkout_session, line_items)
  # TODO: Remove error and implement...
  raise NotImplementedError.new(<<~MSG)
    Given the Checkout Session "#{checkout_session.id}" load your internal order from the database here.
    Then you can reconcile your order's quantities with the final line item quantity purchased. You can use `checkout_session.metadata` and `price.metadata` to store and later reference your internal order and item ids.
  MSG
end`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a Checkout Session with  enabled](#enable-adjustable-quantity)[Handling completed transactions](#handling-transactions)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
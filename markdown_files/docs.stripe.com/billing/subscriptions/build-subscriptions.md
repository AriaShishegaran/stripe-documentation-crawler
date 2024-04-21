htmlBuild a subscriptions integration | Stripe Documentation[Skip to content](#main-content)Build a subscriptions integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fbuild-subscriptions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fbuild-subscriptions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# Build a subscriptions integration

Create and manage subscriptions to accept recurring payments.WebiOSAndroidReact NativeStripe-hosted pageEmbedded formCustom flow![Checkout subscription page](https://b.stripecdn.com/docs-statics-srv/assets/checkout-subs-preview.d409ee79bf1f3280b9dfd3968b314c21.png)

Low codeCustomize logo, images, and colors.

Use prebuilt hosted forms to collect payments and manage subscriptions.

Clone a sample integration from GitHub.

For an immersive version of this guide, see the Billing integration quickstart.

View the demo to see a hosted example.

## What you’ll build

This guide describes how to sell fixed-price monthly subscriptions using Stripe Checkout.

This guide shows you how to:

- Model your business by building a product catalog
- Add a Checkout session to your site, including a button and success and cancellation pages
- Monitor subscription events and provision access to your service
- Set up the[customer portal](/customer-management)
- Add a customer portal session to your site, including a button and redirect
- Let customers manage their subscription through the portal

If you aren’t ready to code an integration, you can set up basic subscriptions manually in the Dashboard or use Payment Links to set up subscriptions without writing any code.

Learn more about designing an integration to understand the decisions and required resources in a full integration.

After you complete the integration, you can extend it to:

- [Display taxes](/payments/checkout/taxes)
- [Apply discounts](/billing/subscriptions/coupons#using-coupons-in-checkout)
- [Offer customers a free trial period](/billing/subscriptions/trials)
- [Add more payment methods](/payments/payment-methods/integration-options#low-code)
- [Integrate the hosted invoice page](/invoicing/hosted-invoice-page)
- [Use Checkout in setup mode](/payments/save-and-reuse)
- [Set up metered billing](/products-prices/pricing-models#usage-based-pricing),[pricing tiers](/products-prices/pricing-models#tiered-pricing), and[usage-based pricing](/products-prices/pricing-models#usage-based-pricing)
- [Manage prorations](/billing/subscriptions/prorations)
- [Allow customers to subscribe to multiple products](/billing/subscriptions/multiple-products)
- [Integrate entitlements to manage access to your product’s features](/billing/entitlements)

[Set up Stripe](#set-up-stripe)Install the Stripe client of your choice:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`Install the Stripe CLI (optional). The CLI provides webhook testing, and you can run it to create your products and prices.

Command Line[homebrew](#)`# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login`For additional install options, see Get started with the Stripe CLI.

[Create the pricing modelDashboard or Stripe CLI](#create-pricing-model)Create your products and their prices in the Dashboard or with the Stripe CLI.

This example uses a fixed-price service with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. (If you want to add a one-time charge for something like a setup fee, create a third product with a one-time price. To keep things simple, this example doesn’t include a one-time charge.)

In this example, each product bills at monthly intervals. The price for the Basic product is 5 USD. The price for the Premium product is 15 USD.

DashboardStripe CLIGo to the Add a product page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features

  - Price: Standard pricing | 15USD


- Basic product: Basic service with minimum features

  - Price: Standard pricing | 5USD



After you create the prices, record the price IDs so you can use them in other  steps. Price IDs look like this: price_G0FvDp6vZvdwRZ.

When you’re ready, use the Copy to live mode button at the top right of the page to clone your product from test mode to live mode.

If you offer multiple billing intervals, use Checkout to upsell customers on longer billing intervals and collect more revenue upfront.

For other pricing models, see Billing examples.

[Create a Checkout SessionClient and Server](#create-session)Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html[View full sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/index.html)`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <!-- Note: If using PHP set the action to /create-checkout-session.php -->

      <input type="hidden" name="priceId" value="price_G0FvDp6vZvdwRZ" />
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`On the backend of your application, define an endpoint that creates the session for your frontend to call. You need these values:

- The price ID of the subscription the customer is signing up for—your frontend passes this value
- Your`success_url`, a page on your website that Checkout returns your customer to after they complete the payment

You can optionally provide cancel_url, a page on your website that Checkout returns your customer to if they cancel the payment process. You can also configure a billing cycle anchor to your subscription in this call.

If you created a one-time price in step 2, pass that price ID as well. After creating a Checkout Session, redirect your customer to the URL returned in the response.

NoteYou can use lookup_keys to fetch prices rather than Price IDs. See the sample application for an example.

server.rb[Ruby](#)[View full sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/server/ruby/server.rb)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# The price ID passed from the front end.
#   price_id = params['priceId']
price_id = '{{PRICE_ID}}'

session = Stripe::Checkout::Session.create({
  success_url: 'https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}',
  cancel_url: 'https://example.com/canceled.html',
  mode: 'subscription',
  line_items: [{
    # For metered billing, do not pass quantity
    quantity: 1,
    price: price_id,
  }],
})

# Redirect to the URL returned on the session
#   redirect session.url, 303`This example customizes the success_url by appending the Session ID. For more information about this approach, see the documentation on how to Customize your success page.

From your Dashboard, enable the payment methods you want to accept from your customers. Checkout supports several payment methods.

[Provision and monitor subscriptionsServer](#provision-and-monitor)After the subscription signup succeeds, the customer returns to your website at the success_url, which initiates a checkout.session.completed webhooks. When you receive a checkout.session.completed event, you can provision the subscription. Continue to provision each month (if billing monthly) as you receive invoice.paid events. If you receive an invoice.payment_failed event, notify your customer and send them to the customer portal to update their payment method.

To determine the next step for your system’s logic, check the event type and parse the payload of each event object, such as invoice.paid. Store the subscription.id and customer.id event objects in your database for verification.

For testing purposes, you can monitor events in the Dashboard. For production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your STRIPE_WEBHOOK_SECRET key, click the webhook in the Dashboard to view it.

server.rb[Ruby](#)[View full sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/server/ruby/server.rb)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

post '/webhook' do
  webhook_secret = '{{STRIPE_WEBHOOK_SECRET}}'
  payload = request.body.read
  if !webhook_secret.empty?
    # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
    sig_header = request.env['HTTP_STRIPE_SIGNATURE']
    event = nil

    begin
      event = Stripe::Webhook.construct_event(
        payload, sig_header, webhook_secret
      )
    rescue JSON::ParserError => e
      # Invalid payload
      status 400
      return
    rescue Stripe::SignatureVerificationError => e
      # Invalid signature
      puts '⚠️  Webhook signature verification failed.'
      status 400
      return
    end
  else
    data = JSON.parse(payload, symbolize_names: true)
    event = Stripe::Event.construct_from(data)
  end
  # Get the type of webhook event sent
  event_type = event['type']
  data = event['data']
  data_object = data['object']

  case event_type
  when 'checkout.session.completed'
    # Payment is successful and the subscription is created.
    # You should provision the subscription and save the customer ID to your database.
  when 'invoice.paid'
    # Continue to provision the subscription as payments continue to be made.
    # Store the status in your database and check when a user accesses your service.
    # This approach helps you avoid hitting rate limits.
  when 'invoice.payment_failed'
    # The payment failed or the customer does not have a valid payment method.
    # The subscription becomes past_due. Notify your customer and send them to the
    # customer portal to update their payment information.
  else
    puts "Unhandled event type: \#{event.type}"
  end

  status 200
end`The minimum event types to monitor:

Event nameDescription`checkout.session.completed`Sent when a customer clicks the Pay or Subscribe button in Checkout, informing you of a new purchase.`invoice.paid`Sent each billing interval when a payment succeeds.`invoice.payment_failed`Sent each billing interval if there is an issue with your customer’s payment method.For even more events to monitor, see Subscription webhooks.

[Configure the customer portalDashboard](#configure-portal)The customer portal lets your customers directly manage their existing subscriptions and invoices.

Use the Dashboard to configure the portal. At a minimum, make sure to configure it so that customers can update their payment methods. See Integrating the customer portal for information about other settings you can configure.

[Create a portal SessionServer](#create-portal-session)Define an endpoint that creates the customer portal session for your frontend to call. Here CUSTOMER_ID refers to the customer ID created by a Checkout Session that you saved while processing the checkout.session.completed webhook. You can also set a default redirect link for the portal in the Dashboard.

Pass an optional return_url value for the page on your site to redirect your customer to after they finish managing their subscription:

server.rb[Ruby](#)[View full sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/server/ruby/server.rb)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# This is the URL to which users will be redirected after they are done
# managing their billing.
return_url = '{{DOMAIN_URL}}'
customer_id = '{{CUSTOMER_ID}}'

session = Stripe::BillingPortal::Session.create({
  customer: customer_id,
  return_url: return_url,
})

# Redirect to the URL for the session
#   redirect session.url, 303`[Send customers to the customer portalClient](#send-to-portal)On your frontend, add a button to the page at the success_url that provides a link to the customer portal:

success.html[View full sample](https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/success.html)`<html>
  <head>
    <title>Manage Billing</title>
  </head>
  <body>
    <form action="/customer-portal" method="POST">
      <!-- Note: If using PHP set the action to /customer-portal.php -->
      <button type="submit">Manage Billing</button>
    </form>
  </body>
</html>`After exiting the customer portal, the Customer returns to your website at the return_url. Continue to monitor webhooks to track the state of the Customer’s subscription.

If you configure the customer portal to allow actions such as canceling a subscription, see Integrating the customer portal for additional events to monitor.

[Test your integration](#test)### Test payment methods

Use the following table to test different payment methods and scenarios.

Payment methodScenarioHow to testBECS Direct DebitYour customer successfully pays with BECS Direct Debit.Fill out the form using the account number`900123456`and BSB`000-000`. The confirmed PaymentIntent initially transitions to`processing`, then transitions to the`succeeded`status three minutes later.BECS Direct DebitYour customer’s payment fails with an`account_closed`error code.Fill out the form using the account number`111111113`and BSB`000-000`.Credit cardThe card payment succeeds and does not require authentication.Fill out the credit card form using the credit card number`4242 4242 4242 4242`with any expiration, CVC, and postal code.Credit cardThe card payment requires[authentication](/strong-customer-authentication).Fill out the credit card form using the credit card number`4000 0025 0000 3155`with any expiration, CVC, and postal code.Credit cardThe card is declined with a decline code like`insufficient_funds`.Fill out the credit card form using the credit card number`4000 0000 0000 9995`with any expiration, CVC, and postal code.SEPA Direct DebitYour customer successfully pays with SEPA Direct Debit.Fill out the form using the account number`AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later.SEPA Direct DebitYour customer’s payment intent status transition from`processing`to`requires_payment_method`.Fill out the form using the account number`AT861904300235473202`.### Monitoring events

Set up webhooks to listen to subscription change events like upgrades and cancellations. Read the guide to learn more about subscription webhooks. You can view events in the Dashboard or with the Stripe CLI.

For more details about testing your Billing integration, read the guide.

## See also

- [Offer customers a free trial period](/billing/subscriptions/trials)
- [Apply discounts](/billing/subscriptions/coupons#using-coupons-in-checkout)
- [Manage prorations](/billing/subscriptions/prorations)
- [Integrate entitlements to manage access to your product’s features](/billing/entitlements)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).[Code quickstart](/docs/billing/quickstart)On this page[What you’ll build](#build)[Set up Stripe](#set-up-stripe)[Create the pricing model](#create-pricing-model)[Create a Checkout Session](#create-session)[Provision and monitor subscriptions](#provision-and-monitor)[Configure the customer portal](#configure-portal)[Create a portal Session](#create-portal-session)[Send customers to the customer portal](#send-to-portal)[Test your integration](#test)[See also](#see-also)Products Used[Billing](/billing)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
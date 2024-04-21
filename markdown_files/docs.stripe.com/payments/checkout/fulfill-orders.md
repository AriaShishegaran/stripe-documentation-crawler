htmlFulfill orders with Checkout | Stripe Documentation[Skip to content](#main-content)Fulfill your orders[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffulfill-orders)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffulfill-orders)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Fulfill orders with Checkout

Learn how to fulfill orders after a customer pays with Stripe Checkout or Stripe Payment Links.After you integrate Stripe Checkout or create a Stripe Payment Link to take your customers to a payment form, you need notification that you can fulfill their order after they pay.

In this guide, you’ll learn how to:

1. Receive an event notification when a customer pays you.
2. Handle the event.
3. Use[Stripe CLI](/stripe-cli)to quickly test your new event handler.
4. Optionally, handle additional payment methods.
5. Turn on your event handler in production.

[Install Stripe CLI](#install-stripe-cli)The quickest way to develop and test webhooks locally is with the Stripe CLI.

As a first step, follow the install guide for Stripe CLI.

Once you have the Stripe CLI installed and have completed the login process, you’re ready to move on to the next step.

[Create your event handlerServer-side](#create-event-handler)In this section, you’ll create a small event handler so Stripe can send you a checkout.session.completed event when a customer completes checkout.

First, create a new route for your event handler. Start by printing out the event you receive. You’ll verify that delivery is working in the next step:

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

require 'sinatra'

post '/webhook' do
  payload = request.body.read

  # For now, you only need to print out the webhook payload so you can see
  # the structure.
  puts payload.inspect

  status 200
end`### Testing

Run your server (for example, on localhost:4242). Next, set up Stripe CLI to forward events to your local server, so you can test your event handler locally:

Command Line`stripe listen --forward-to localhost:4242/webhook

Ready! Your webhook signing secret is 'whsec_<REDACTED>' (^C to quit)`Next, go through Checkout as a customer:

- Click your checkout button (you probably set this up in the[Accept a payment guide](/payments/accept-a-payment?integration=checkout))
- Fill out your payment form with test data  - Enter`4242 4242 4242 4242`as the card number
  - Enter any future date for card expiry
  - Enter any 3-digit number for CVV
  - Enter any billing postal code (`90210`)


- Click thePaybutton

You should see:

- A`checkout.session.completed`in the`stripe listen`output
- A print statement from your server’s event logs with the`checkout.session.completed`event

Now that you’ve verified event delivery, you can add a bit of security to make sure that events are only coming from Stripe.

### Verify events came from Stripe

Anyone can POST data to your event handler. Before processing an event, always verify that it came from Stripe before trusting it. The official Stripe library has built-in support for verifying webhook events, which you’ll update your event handler with:

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

require 'sinatra'

# You can find your endpoint's secret in the output of the `stripe listen`
# command you ran earlier
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

  # Print out the event so you can look at it
  puts event.inspect

  status 200
end`### Testing

Go through the testing flow from the previous step. You should still see the checkout.session.completed event being printed out successfully.

Next, try hitting the endpoint with an unsigned request:

Command Line`curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "fake": "unsigned request" }' \
  -is http://localhost:4242/webhook


HTTP/1.1 400 Bad Request
... more headers`You should get a 400 Bad Request error, because you tried to send an unsigned request to your endpoint.

Now that the basics of the event handler are set up, you can move on to fulfilling the order.

[Fulfill the orderServer-side](#fulfill)To fulfill the order, you’ll need to handle the checkout.session.completed event. Depending on which payment methods you accept (for example, cards, mobile wallets), you’ll also optionally handle a few extra events after this basic step.

Handle the`checkout.session.completed`event![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Now that you have the basic structure and security in place to make sure any event you process came from Stripe, you can handle the checkout.session.completed event. This event includes the Checkout Session object, which contains details about your customer and their payment.

When handling this event, you might also consider:

- Saving a copy of the order in your own database.
- Sending the customer a receipt email.
- Reconciling the line items and quantity purchased by the customer if using`line_item.adjustable_quantity`. If the Checkout Session has many line items you can paginate through them with the[line_items](/api/checkout/sessions/line_items).

Add code to your event handler to fulfill the order:

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

require 'sinatra'

# You can find your endpoint's secret in the output of the `stripe listen`
# command you ran earlier
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
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
    session = Stripe::Checkout::Session.retrieve({
      id: event['data']['object']['id'],
      expand: ['line_items'],
    })

    line_items = session.line_items
    fulfill_order(line_items)
  end

  status 200
end

def fulfill_order(line_items)
  # TODO: fill in with your own logic
  puts "Fulfilling order for #{line_items.inspect}"
end`Handle redirect behavior![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can configure Checkout to redirect your customers after receiving webhook events. Checkout handles these webhook-triggered redirects slightly differently depending on whether you use the embedded form or a Stripe-hosted page.

Stripe-hosted pageYour webhook endpoint redirects your customer to the`success_url`afteryou[acknowledge that you received the event](/webhooks#acknowledge-events-immediately). If your endpoint is down or the event isn’t acknowledged properly, your handler redirects the customer to the`success_url`10 seconds after a successful payment.Embedded formYour webhook endpoint redirects your customer to the`return_url`immediately. Youdo notneed to acknowledge that you received the event.Testing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Ensure that stripe listen is still running. Go through Checkout as a test user, just like in the prior steps. Your event handler should receive a checkout.session.completed event, and you should have successfully handled it.

[Handle delayed notification payment methodsServer-side](#delayed-notification)CautionThis step is only required if you plan to use any of the following payment methods: Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, SEPA Direct Debit, SOFORT, or ACH Direct Debit.

When receiving payments with a delayed notification payment method, funds aren’t immediately available. It can take multiple days for funds to process so you should delay order fulfillment until the funds are available in your account. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

You’ll need to handle the following Checkout events:

Event NameDescriptionNext steps[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)The customer has successfully authorized the debit payment bysubmitting the Checkout form.Wait for the payment to succeed or fail.[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)The customer’s payment succeeded.Fulfill the purchased goods or services.[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)The payment was declined, or failed for some other reason.Contact the customer via email and request that they place a new order.These events all include the Checkout Session object.

Update your event handler to fulfill the order:

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# You can find your endpoint's secret in the output of the `stripe listen`
# command you ran earlier
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

  case event['type']
  if event['type'] == 'checkout.session.completed'
    checkout_session = event['data']['object']

    fulfill_order(checkout_session)
  end
  when 'checkout.session.completed'
    checkout_session = event['data']['object']

    # Save an order in your database, marked as 'awaiting payment'
    create_order(checkout_session)

    # Check if the order is already paid (for example, from a card payment)
    #
    # A delayed notification payment will have an `unpaid` status, as
    # you're still waiting for funds to be transferred from the customer's
    # account.
    if checkout_session.payment_status == 'paid'
      fulfill_order(checkout_session)
    end
  when 'checkout.session.async_payment_succeeded'
    checkout_session = event['data']['object']

    # Fulfill the purchase...
    fulfill_order(checkout_session)
  when 'checkout.session.async_payment_failed'
    session = event['data']['object']

    # Send an email to the customer asking them to retry their order
    email_customer_about_failed_payment(checkout_session)
  end

  status 200
end

def fulfill_order(checkout_session)
  # TODO: fill in with your own logic
  puts "Fulfilling order for #{checkout_session.inspect}"
end

def create_order(checkout_session)
  # TODO: fill in with your own logic
  puts "Creating order for #{checkout_session.inspect}"
end

def email_customer_about_failed_payment(checkout_session)
  # TODO: fill in with your own logic
  puts "Emailing customer about payment failure for: #{checkout_session.inspect}"
end`### Testing

Ensure that stripe listen is still running. Go through Checkout as a test user, like you did in the prior steps. Your event handler should receive a checkout.session.completed event, and you should have successfully handled it.

Now that you’ve completed these steps, you’re ready to go live in production whenever you decide to do so.

[Go live in production](#go-live)After you’ve deployed your event handler endpoint to production, you need to register your live URL with Stripe. Follow the guide to register a webhook.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Install Stripe CLI](#install-stripe-cli)[Create your event handler](#create-event-handler)[Fulfill the order](#fulfill)[Handle delayed notification payment methods](#delayed-notification)[Go live in production](#go-live)Products Used[Checkout](/payments/checkout)[Payment Links](/payments/payment-links)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
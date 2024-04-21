htmlConnect webhooks | Stripe Documentation[Skip to content](#main-content)Listen for updates[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fwebhooks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fwebhooks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Connect webhooks

Learn how to use webhooks with Connect to be notified of Stripe activity.Stripe uses webhooks to notify your application when an event happens in your account. All Connect integrations should establish a webhook endpoint to listen for Connect events.

## Connect webhooks

There are a few types of webhooks:

- Accountwebhooks are for activity on your own account(for example, most requests made using your API keys and without[authenticating as another Stripe account](/connect/authentication)). This includes all types of charges, except those made directly on a connected account.
- Connectwebhooks are for activity on any connected account.All events on the connected account are sent to the Connect webhooks.This includes the important`account.updated`event for any connected account and direct charges.

When creating your webhook, ensure it is correctly configured to receive Connect webhook events. You can do this with the API by setting the connect parameter to true when creating the webhook endpoint, or through the Dashboard.

![Webhook settings in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/webhooks.ac3d6c19a5281fbbd2b85a335cd887b3.png)

For Connect webhooks, it’s important to note that while only test webhooks will be sent to your development webhook URLs, both live and test webhooks will be sent to your production webhook URLs. This is due to the fact that you can perform both live and test transactions under a production application. For this reason, we recommend you check the livemode value when receiving an event webhook to know what action, if any, should be taken.

As we state in the event object reference, each event for a connected account also contains a top-level account property. It identifies the account that the webhook is sent to and the data[object] it belongs to. Because these objects belong to other accounts, you must make the API requests as the corresponding connected account to access them.

`{
  "id": "{{EVENT_ID}}",
  "livemode": true,
  "object": "event",
  "type": "customer.created",
  "account": "{{CONNECTED_ACCOUNT_ID}}",
  "pending_webhooks": 2,
  "created": 1349654313,
  "data": {...}
}`There are several events related to accounts that Stripe recommends listening for:

Eventdata.object typeDescription`account.application.deauthorized``application`Occurs when a connected account disconnects from your platform. You can use it to trigger cleanup on your server. Available for connected accounts with access to the Stripe Dashboard, which includes[Standard accounts](/connect/standard-accounts).`account.external_account.updated`An external account, such as`card`or`bank_account`Occurs when[a bank account or debit card attached to a connected account is updated](/connect/payouts-bank-accounts), which can impact payouts. Available for connected accounts that your platform controls, which includes Custom and Express accounts, and Standard accounts with[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)enabled.`account.updated``account`Allows you to monitor changes to connected account requirements and status changes. Available for all connected accounts.`balance.available``balance`Occurs when your Stripe balance has been updated (for example, when[funds you’ve added from your bank account](/connect/add-and-pay-out-guide#add-funds)are available for transfer to your connected account).`payment_intent.succeeded``payment_intent`Occurs when a payment intent results in a successful charge. Available for all payments, including[destination](/connect/collect-then-transfer-guide#fulfillment)and[direct](/connect/enable-payment-acceptance-guide)charges.`payout.failed``payout`Occurs when[a payout fails](/connect/payouts-connected-accounts#webhooks).  When a payout fails, the external account involved will be disabled, and no automatic or manual payouts can go through until the external account is updated.`person.updated``person`If you[use the Persons API](/connect/handling-api-verification#verification-process), allows you to monitor changes to requirements and status changes for individuals. Available for connected accounts that your platform controls, which includes Custom and Express accounts, and Standard accounts with[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)enabled.Event:account.application.deauthorizedaccount.updatedperson.updatedpayment_intent.succeeded, direct chargepayment_intent.succeeded, non-direct chargebalance.availableaccount.external_account.updatedpayout.failedserver.rb[Ruby](#)`# Using Sinatra.
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

  if event['type'] == 'account.application.deauthorized'
    application = event['data']['object']
    connected_account_id = event['account']
    handle_deauthorization(connected_account_id, application)
  end

  status 200
end

def handle_deauthorization(connected_account_id, application)
  # Clean up account state.
  puts 'Connected account ID: ' + connected_account_id
  puts application.to_s
end`The events listed above are the ones we typically recommend Connect integrations listen for, but there are many other event types you may be interested in.

## Test webhooks locally

You can test webhooks locally with the Stripe CLI.

1. If you haven’t already, install the Stripe CLI on your machine.


2. Log in to your Stripe account and set up the CLI by running stripe login on the command line.


3. Allow your local host to receive a simulated event on your connected account by running stripe listen --forward-to localhost:{PORT}/webhook in one terminal window, and running stripe trigger {{EVENT_NAME}} in another.



NoteFor Connect webhooks, use --forward-connect-to with stripe listen and --stripe-account with stripe trigger.

## See also

- [Webhook documentation](/webhooks)
- [Event object reference](/api#events)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
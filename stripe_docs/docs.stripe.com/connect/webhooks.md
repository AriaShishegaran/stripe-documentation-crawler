# Connect webhooks

Stripe uses webhooks to notify your application when an event happens in your account. All Connect integrations should establish a webhook endpoint to listen for Connect events.

[webhooks](/webhooks)

[Connect](/connect)

[webhook endpoint](https://dashboard.stripe.com/account/webhooks)

## Connect webhooks

There are a few types of webhooks:

- Account webhooks are for activity on your own account (for example, most requests made using your API keys and without authenticating as another Stripe account). This includes all types of charges, except those made directly on a connected account.

[authenticating as another Stripe account](/connect/authentication)

- Connect webhooks are for activity on any connected account. All events on the connected account are sent to the Connect webhooks. This includes the important account.updated event for any connected account and direct charges.

When creating your webhook, ensure it is correctly configured to receive Connect webhook events. You can do this with the API by setting the connect parameter to true when creating the webhook endpoint, or through the Dashboard.

[connect parameter](/api/webhook_endpoints/create#create_webhook_endpoint-connect)

[through the Dashboard](https://dashboard.stripe.com/test/webhooks)

For Connect webhooks, it’s important to note that while only test webhooks will be sent to your development webhook URLs, both live and test webhooks will be sent to your production webhook URLs. This is due to the fact that you can perform both live and test transactions under a production application. For this reason, we recommend you check the livemode value when receiving an event webhook to know what action, if any, should be taken.

As we state in the event object reference, each event for a connected account also contains a top-level account property. It identifies the account that the webhook is sent to and the data[object] it belongs to. Because these objects belong to other accounts, you must make the API requests as the corresponding connected account to access them.

[event object reference](/api/events/object)

[as the corresponding connected account](/connect/authentication)

There are several events related to accounts that Stripe recommends listening for:

[Standard accounts](/connect/standard-accounts)

[a bank account or debit card attached to a connected account is updated](/connect/payouts-bank-accounts)

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

[funds you’ve added from your bank account](/connect/add-and-pay-out-guide#add-funds)

[destination](/connect/collect-then-transfer-guide#fulfillment)

[direct](/connect/enable-payment-acceptance-guide)

[a payout fails](/connect/payouts-connected-accounts#webhooks)

[use the Persons API](/connect/handling-api-verification#verification-process)

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

The events listed above are the ones we typically recommend Connect integrations listen for, but there are many other event types you may be interested in.

[many other event types](/api/events/types)

## Test webhooks locally

You can test webhooks locally with the Stripe CLI.

- If you haven’t already, install the Stripe CLI on your machine.

If you haven’t already, install the Stripe CLI on your machine.

[install the Stripe CLI](/stripe-cli#install)

- Log in to your Stripe account and set up the CLI by running stripe login on the command line.

Log in to your Stripe account and set up the CLI by running stripe login on the command line.

- Allow your local host to receive a simulated event on your connected account by running stripe listen --forward-to localhost:{PORT}/webhook in one terminal window, and running stripe trigger {{EVENT_NAME}} in another.

Allow your local host to receive a simulated event on your connected account by running stripe listen --forward-to localhost:{PORT}/webhook in one terminal window, and running stripe trigger {{EVENT_NAME}} in another.

For Connect webhooks, use --forward-connect-to with stripe listen and --stripe-account with stripe trigger.

[--forward-connect-to](/cli/listen#listen-forward-connect-to)

[--stripe-account](/cli/trigger#trigger-stripe_account)

## See also

- Webhook documentation

[Webhook documentation](/webhooks)

- Event object reference

[Event object reference](/api#events)

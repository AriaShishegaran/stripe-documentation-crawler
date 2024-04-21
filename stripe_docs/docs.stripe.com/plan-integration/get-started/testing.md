# Testing basics

Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to simplify the testing process.

[Postman collection](https://www.getpostman.com/collections/080102f58f29afa081d7)

Each Stripe account includes a test and live mode. Test mode includes a separate set of data and API keys that you can use exclusively for testing your integration; we recommend using test mode to build the integration and replace your test keys with live keys when you’re ready to go live.

[test and live mode](/keys#test-live-modes)

You’re welcome to test on as many accounts as you’d like; however, if you create a new test account, make sure to let your Stripe contact know so they can apply any custom configurations. You can open additional Stripe accounts directly from the Stripe Dashboard.

[additional Stripe accounts](/get-started/account/multiple-accounts)

[Testing use cases](#qa-testing-use-cases)

## Testing use cases

The following table contains quality assurance (QA) testing use cases:

[capturing funds for later](/payments/place-a-hold-on-a-payment-method)

[capturing funds for later](/payments/place-a-hold-on-a-payment-method)

[https://stripe.com/docs/error-codes/card-declined](https://stripe.com/docs/error-codes/card-declined)

[high risk](/radar/risk-evaluation#high-risk)

[rule](/radar/rules)

[statuses](/disputes)

[successful payout](/api/events/types#event_types-payout.paid)

[failed payout](/api/events/types#event_types-payout.failed)

[Stripe's Postman collection](#postman-collection)

## Stripe's Postman collection

Postman is a widely-used API development tool. To make integrating Stripe simpler, we provide a Payments-specific Postman collection with the tools you’ll need to test the server-side component of your integration.

[Payments-specific Postman collection](https://www.getpostman.com/collections/080102f58f29afa081d7)

To get started, you need access to the Postman app. The app is available in a browser-based version or standalone desktop version. As soon as you have either version launched, the first step is to import the collection.

To do this from the web, click the Import button on the upper left hand corner, and then Link. Paste in the link for the Payments collection. If you’re using Postman’s desktop app, click File > Import. After a successful import, you can find the collection listed under Collections.

[Payments collection](https://www.getpostman.com/collections/080102f58f29afa081d7)

The import modal

To use the collection, navigate to the collection you just imported and click Variables. Copy your testmode Stripe secret key from the Stripe Dashboard and paste it into the field titled Initial Value.  After completing this step, you’re ready to begin making requests.

[Stripe Dashboard](https://dashboard.stripe.com/test/apikeys)

Other variables are populated by scripts during the runtime of the collection.  For example, when creating a customer or price creating a charge or payment intent, a script in the collection saves that ID to be used in subsequent requests such as a refund.

[creating a customer](/api/customers/create)

[price](/api/prices/create)

Add a secret key to a Postman collection

## See also

- Stripe testing guide

[Stripe testing guide](/testing)

- Integration security guide

[Integration security guide](/security)

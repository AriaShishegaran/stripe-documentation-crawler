htmlBest practices for using Sources | Stripe Documentation[Skip to content](#main-content)Best practices[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fbest-practices)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fbest-practices)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# Best practices for using SourcesDeprecated

Best practices to accept a variety of payment methods through a single integration.WarningWe deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

The flexibility of the Sources API helps you minimize the changes required to support additional payment methods as you add them.

## Typical flow for card payments

In a typical checkout flow for card payments (excluding 3D Secure), your integration collects the card information and creates a source, and uses it to make a charge request. Because it requires no additional action from the customer and card payments provide synchronous confirmation, we can immediately confirm if the payment is successful and that the funds are guaranteed—using webhooks isn’t necessary.

## The required use of webhooks

Other payment methods may require your customer to take additional action (for example, a redirect) before a source becomes chargeable and can be used to make a charge request (for example, iDEAL). This transition generally happens asynchronously and may even occur after the customer leaves your website. For these reasons your integration must rely on webhooks to determine when a source becomes chargeable before creating a charge.

Stripe sends the following webhook events to notify you about changes to the status of the source:

EventDescriptionSuggested action`source.chargeable`A Source object becomes`chargeable`after a customer has authenticated and verified a payment.Create a Charge.`source.failed`A Source object failed to become chargeable because your customer declined to authenticate the payment.Cancel the order and (optionally) re-engage the customer in your payment flow.`source.canceled`A Source object expired and you can’t use it to create a charge.Cancel the order and (optionally) re-engage the customer in your payment flow.Similarly, when creating a charge, certain asynchronous payment methods might require days for the funds to be confirmed and the charge to succeed, requiring webhooks to know when to confirm and eventually fulfill your orders.

Stripe sends the following webhook events to notify you about changes to the status of a charge:

EventDescriptionSuggested action`charge.pending`The Charge is pending (asynchronous payments only).No action required.`charge.succeeded`The Charge succeeded and the payment is complete.Finalize the order and send a confirmation to the customer over email.`charge.failed`The Charge has failed and the payment couldn’t be completed.Cancel the order and (optionally) re-engage the customer in your payment flow.## Building a flexible integration

To ensure that your checkout process is flexible and ready to support multiple payment methods, we recommend the following approach:

### Source creation

When creating Sources, record the source ID on your internal order representation so that you can retrieve the order when you receive and process source.chargeable webhooks. Make sure to index your order objects based on this source attribute for efficient lookup.

### Charge creation

Delivery of the source.chargeable webhook charges the Source. When receiving the webhook, retrieve your internal order representation by a look-up based on the received source ID and verify that the order is awaiting a payment.

When making a charge request, use your internal order ID as an idempotency key to avoid any possible race condition. Additionally, if the source is reusable and you want to reuse it, make sure to attach it to a Customer before charging it. Refer to the Single-use or reusable and Sources & Customers guides to learn more about how to handle single-use and reusable Sources and how they interact with Customers.

Similarly to source creation, record the charge ID on your internal order representation so that you can retrieve the order when you receive and process charge.succeeded webhooks.

### Confirmation page

After your customer takes the required actions to authorize a payment (for example, they’ve followed a redirect) you should present a confirmation page that shows the state of the order. You can do this by polling the order internally.

Because webhook delivery latency isn’t guaranteed, if want to further streamline your confirmation page, you can poll for the status of the associated Source in your client-side code. When you detect that your Source has become chargeable, you can initiate a Charge creation using that Source without waiting for the source.chargeable webhook to arrive.

Be aware that some types of Sources take minutes (or even days) to become chargeable. If you decide to poll the Source, we recommend that you time out at some point and tell the customer that their order is awaiting payment confirmation, then send them a payment confirmation email asynchronously. You can see our recommended customer-facing messaging for each Source status in the table below.

Client-side polling stops if the customer leaves your page. This means that you must also integrate against the source.chargeable webhook to make sure you don’t lose track of your customer’s order.

If you’re using Stripe.js, you can use stripe.retrieveSource() to implement your own polling:

`// In order-confirmation-page.js

const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

// After some amount of time, we should stop trying to resolve the order synchronously:
const MAX_POLL_COUNT = 10;
let pollCount = 0;

const pollForSourceStatus = async () => {
  const {source} = await stripe.retrieveSource({id: SOURCE_ID, client_secret: CLIENT_SECRET})
  if (source.status === 'chargeable') {
    // Make a request to your server to charge the Source.
    // Depending on the Charge status, show your customer the relevant message.
  } else if (source.status === 'pending' && pollCount < MAX_POLL_COUNT) {
    // Try again in a second, if the Source is still `pending`:
    pollCount += 1;
    setTimeout(pollForSourceStatus, 1000);
  } else {
    // Depending on the Source status, show your customer the relevant message.
  }
};

pollForSourceStatus();`The table below contains recommendations for potential customer-facing messages you can show based on the Source’s status.

StatusCustomer-facing messagingSource is`chargeable`Your order was received and is awaiting payment confirmation.Source is`canceled`Your payment failed and your order couldn’t be processed.Source is`failed`Your payment failed and your order couldn’t be processed.Source is still`pending`after polling for a whileYour order was received and is awaiting payment confirmation.After you create a Charge (and if the user is still on your confirmation page), you can show the following messages based on the status of the Charge:

StatusCustomer-facing messagingCharge is`pending`Your order was received and is awaiting payment confirmation.Charge is`failed`Your payment failed and your order couldn’t be processed.Charge is`succeeded`Your payment is confirmed and your order is complete.### Order confirmation

Only confirm your order after you receive the charge.succeeded webhook (this may happen instantly, but it may not). Send an email to the customer at this stage because the payment confirmation can take days for asynchronous payments.

### Cancellations and failures

Listen for the source.canceled and source.failed webhooks and make sure to cancel the order associated with the source concerned. If you follow the best practices above, you should never receive a source.canceled webhook for sources that were previously chargeable (as your source.chargeable handler should have created a charge immediately, preventing the source from getting canceled). You’ll still receive source.canceled webhooks for sources that were never chargeable and remained pending, generally an indication that your customer left your checkout flow early. You can also receive a source.failed webhook whenever the Customer refused the payment or a technical failure happened at the payment scheme level.

You should also listen for the charge.failed webhooks to make sure to cancel the order associated with the received charge.

For each of these events, we recommend that you notify your customer that their order failed and to invite them to re-engage in your payment flow, if desired.

## See also

- [Supported payment methods](/sources)
- [Sources API reference](/api#sources)
- [Considerations for Stripe Connect platforms](/sources/connect)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Typical flow for card payments](#typical-flow-for-card-payments)[The required use of webhooks](#the-required-use-of-webhooks)[Building a flexible integration](#building-a-flexible-integration)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
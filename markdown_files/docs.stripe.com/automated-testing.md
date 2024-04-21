htmlAutomated testing | Stripe Documentation[Skip to content](#main-content)Automated testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fautomated-testing)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fautomated-testing)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API# Automated testing

Learn how to use automated testing in your Stripe integration.Automated testing is a common part of application development, both for server and client-side code. Frontend interfaces, like Stripe Checkout or the Payment Element, have security measures in place that prevent automated testing, and Stripe APIs are rate limited. However, you can simulate the output of our interfaces and API requests using mock data to test your application behavior and its ability to handle errors.

## Client side testing

If you want to test your application’s ability to recover from errors such as transaction declines when using the Payment Element, you can return a simulated error object by hard-coding error objects in your test code, or creating an API service that returns mock errors in an HTTP response. The error object represents what would be returned by the confirmPayment function when a card is declined.  See the following section to learn how you can generate a simulated error object.

### Generating an error object

First, use a Stripe UI element such as the Payment Element manually to produce an error object by confirming a test mode Payment Intent using one of the test card numbers for declined payments.  Log the error during the confirmation process as shown below.

client.js`const { error } = await stripe.confirmPayment({
  elements,
  confirmParams: {
    return_url: 'https://example.com'
  },
}) ;
if (error) {
  console.log(error)
}`This produces an error object logged to the browser console that resembles the one shown below.  The specifics for properties such as error_code depend on the card used and the type of error it generates.

`{
  "charge": "{{CHARGE_ID}}",
  "code": "card_declined",
  "decline_code": "generic_decline",
  "doc_url": "https://stripe.com/docs/error-codes/card-declined",
  "message": "Your card has been declined.",
  "payment_intent": {"id": "{{PAYMENT_INTENT_ID}}", …},
  "payment_method": {"id": "{{PAYMENT_METHOD_ID}}", …},
  "request_log_url": "https://dashboard.stripe.com/test/logs/req_xxxxxxx",
  "type": "card_error"
}`Modify your tests to return this error object instead of calling Stripe.js functions and the Stripe APIs.  You can use different test cards to generate errors with different error codes to make sure your application properly handles each type of error.

## Server side testing

You can use the same approach when testing server-side API calls.  You can generate Stripe API responses manually for various errors and mock the response returned in backend automated testing.

For example, to write a test to validate that your application can correctly handle an off-session payment requiring 3DS, you can generate the response by creating a Payment Intent with the Payment Method pm_card_authenticationRequired and confirm set to true.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2099 \
  -d currency=usd \
  -d payment_method=pm_card_authenticationRequired \
  -d confirm=true \
  -d off_session=true`This generates a Payment Intent with a status of requires_confirmation, and other properties associated with 3DS Authentication like next_action.

`{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
  ...
	"next_action": {
        "type": "use_stripe_sdk",
    ...
  },
  ...
  "status": "requires_confirmation",
  ...
}`Generating PaymentIntent objects that reflect different stages of the Payment lifecycle allows you to test your application’s behavior as the PaymentIntent transitions through various states. Use this approach in your automated testing to make sure your integration can successfully respond to different outcomes, such as requesting that the customer comes back on-session to authenticate a payment that requires a next action.

When to use this approachThe above examples all reference testing the behavior of your application and are suitable to use in a continuous integration test suite.  When you need to perform tests to validate the response of the Stripe API, making requests to the API in test mode is an acceptable approach. You can also use Stripe API requests to periodically validate that Stripe API responses haven’t changed—but you should perform these tests infrequently to avoid rate limits.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Client side testing](#client-side-testing)[Server side testing](#server-side-testing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
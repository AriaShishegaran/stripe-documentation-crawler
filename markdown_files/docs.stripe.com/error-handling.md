htmlError handling | Stripe Documentation[Skip to content](#main-content)Error handling[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ferror-handling)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ferror-handling)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API# Error handling

Catch and respond to declines, invalid data, network problems, and more.RubyPythonPHPJavaNode.jsGo.NETStripe offers many kinds of errors. They can reflect external events, like declined payments and network interruptions, or code problems, like invalid API calls.

To handle errors, use some or all of the techniques in the table below. No matter what technique you use, you can follow up with our recommended responses for each error type.

TechniquePurposeWhen needed[Catch exceptions](#catch-exceptions)Recover when an API call can’t continueAlways[Monitor webhooks](#monitor-webhooks)React to notifications from StripeSometimes[Get stored information about failures](#use-stored-information)Investigate past problems and support other techniquesSometimes## Catch exceptions

### Errors and HTTP

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see Low-level exception handling and the Error object.

If an immediate problem prevents an API call from continuing, the Stripe Ruby library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Ruby’s rescue keyword. Catch Stripe::StripeError or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can use its class to choose a response.

[Ruby](#)`require 'stripe'

Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    puts "A payment error occurred: #{e.error.message}"
  rescue Stripe::InvalidRequestError => e
    puts "An invalid request occurred."
  rescue Stripe::StripeError => e
    puts "Another problem occurred, maybe unrelated to Stripe."
  else
    puts "No error."
  end
end`After setting up exception handling, test it on a variety of data, including test cards, to simulate different payment outcomes.

Error to trigger:Invalid requestCard errorNo error[Ruby](#)`example_function(
  # The required parameter currency is missing,
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa',
)`console[Ruby](#)`An invalid request occurred.`## Monitor webhooks

Stripe notifies you about many kinds of problems using webhooks. This includes problems that don’t follow immediately after an API call. For example:

- You lose a dispute.
- A recurring payment fails after months of success.
- Your frontend[confirms](/api/payment_intents/confirm)a payment, but goes offline before finding out the payment fails. (The backend still receives webhook notification, even though it wasn’t the one to make the API call.)

You don’t need to handle every webhook event type. In fact, some integrations don’t handle any.

In your webhook handler, start with the basic steps from the webhook builder: get an event object and use the event type to find out what happened. Then, if the event type indicates an error, follow these extra steps:

1. Access[event.data.object](/api/events/object#event_object-data-object)to retrieve the affected object.
2. [Use stored information](#use-stored-information)on the affected object to gain context, including an error object.
3. [Use its type to choose a response](#error-types).

[Ruby](#)`require 'stripe'
require 'sinatra'
post '/webhook' do
  payload = request.body.read
  data = JSON.parse(payload, symbolize_names: true)

  # Get the event object
  event = Stripe::Event.construct_from(data)

  # Use the event type to find out what happened
  case event.type
  when 'payment_intent.payment_failed'

    # Get the object affected
    payment_intent = event.data.object

    # Use stored information to get an error object
    e = payment_intent.last_payment_error

    # Use its type to choose a response
    case e.type
    when 'card_error'
      puts "A payment error occurred: #{e.message}"
    when 'invalid_request'
      puts "An invalid request occurred."
    else
      puts "Another problem occurred, maybe unrelated to Stripe."
    end
  end

  content_type 'application/json'
  {
    status: 'success'
  }.to_json
end`To test how your integration responds to webhook events, you can trigger webhook events locally. After completing the setup steps at that link, trigger a failed payment to see the resulting error message.

Command Line`stripe trigger payment_intent.payment_failed`Output`A payment error occurred: Your card was declined.`## Get stored information about failures

Many objects store information about failures. That means that if something already went wrong, you can retrieve the object and examine it to learn more. In many cases, stored information is in the form of an error object, and you can use its type to choose a response.

For instance:

1. Retrieve a specific payment intent.
2. Check if it experienced a payment error by determining if[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)is empty.
3. If it did, log the error, including its type and the affected object.

[Ruby](#)`require 'stripe'
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

payment_intent = Stripe::PaymentIntent.retrieve('{{PAYMENT_INTENT_ID}}')
e = payment_intent.last_payment_error
if !e.nil?
  puts "PaymentIntent #{payment_intent.id} experienced a #{e.type}."
end`Here are common objects that store information about failures.

ObjectAttributeValues[Payment Intent](/api/payment_intents)`last_payment_error`[An error object](#work-with-error-objects)[Setup Intent](/api/setup_intents)`last_setup_error`[An error object](#work-with-error-objects)[Invoice](/api/invoices)`last_finalization_error`[An error object](#work-with-error-objects)[Setup Attempt](/api/setup_attempts)`setup_error`[An error object](#work-with-error-objects)[Payout](/api/payouts)`failure_code`[A payout failure code](/api/payouts/failures)[Refund](/api/refunds)`failure_reason`[A refund failure code](/api/refunds/object#refund_object-failure_reason)To test code that uses stored information about failures, you often need to simulate failed transactions. You can often do this using test cards or test bank numbers. For example:

- [Simulate a declined payment](/testing#declined-payments), for creating failed Charges, PaymentIntents, SetupIntents, and so on.
- [Simulate a failed payout](/connect/testing#account-numbers).
- [Simulate a failed refund](/testing#refunds).

## Types of error and responses

In the Stripe Ruby library, error objects belong to stripe.error.StripeError and its subclasses. Use the documentation for each class for advice on responding.

NameClass

DescriptionPayment errorStripe::CardError

An error occurred during a payment, involving one of these situations:- [Payment blocked for suspected fraud](#payment-blocked)
- [Payment declined by the issuer](#payment-declined).
- [Other payment errors](#other-payment-errors).

Invalid request errorStripe::InvalidRequestError

You made an API call with the wrong parameters, in the wrong state, or in an invalid way.

Connection errorStripe::APIConnectionError

There was a network problem between your server and Stripe.API errorStripe::APIError

Something went wrong on Stripe’s end. (These are rare.)Authentication errorStripe::AuthenticationError

Stripe can’t authenticate you with the information provided.Idempotency errorStripe::IdempotencyError

You used an[idempotency key](/api/idempotent_requests)for something unexpected, like replaying a request but passing different parameters.Permission errorStripe::PermissionError

The API key used for this request does not have the necessary permissions.Rate limit errorStripe::RateLimitError

You made too many API calls in too short a time.Signature verification errorStripe::SignatureVerificationError

You’re using[webhook](/webhooks)[signature verification](/webhooks#verify-events)and couldn’t verify that a webhook event is authentic.## Payment errors

### Non-card payment errors

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type Stripe::CardError. But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](#payment-blocked)
- [Payment declined by the issuer](#payment-declined)
- [Other payment errors](#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the error code, decline code, and charge outcome.

(To find the charge outcome from an error object, first get the Payment Intent that’s involved and the latest Charge it created. See the example below for a demonstration.)

[Ruby](#)`require 'stripe'
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end`Users on API version 2022-08-01 or older:

(To find the charge outcome from an error object, first get the Payment Intent that’s involved and the latest Charge it created. See the example below for a demonstration.)

[Ruby](#)`require 'stripe'
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end`You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](/testing#fraud-prevention)
- [Simulating declined payments and other card errors](/testing#declined-payments)

The test code below demonstrates a few possibilities.

Error to trigger:Blocked for suspected fraudDeclined by the issuerCard expiredOther card error[Ruby](#)`example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock',
)`console[Ruby](#)`Payment blocked for suspected fraud.`### Payment blocked for suspected fraud

TypeStripe::CardError

Codes`charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
charge.outcome.type == 'blocked'`Codese.error.payment_intent.charges.data[0].outcome.type == 'blocked'

ProblemStripe’s fraud prevention system,[Radar](/radar), blocked the paymentSolutions

This error can occur when your integration is working correctly. Catch it and prompt the customer for a different payment method.

To block fewer legitimate payments, try these:

- [Optimize your Radar integration](/radar/integration)to collect more detailed information.
- Use[Payment Links](/payment-links),[Checkout](/payments/checkout), or[Stripe Elements](/payments/elements)for prebuilt optimized form elements.

Radar for Fraud Teams customers have these additional options:

- To exempt a specific payment, add it to your allowlist.Radar for Fraud Teams
- To change your risk tolerance, adjust your[risk settings](/radar/risk-settings).Radar for Fraud Teams
- To change the criteria for blocking a payment, use[custom rules](/radar/rules).Radar for Fraud Teams

You can test your integration’s settings with test cards that simulate fraud. If you have custom Radar rules, follow the testing advice in the Radar documentation.

### Payment declined by the issuer

TypeStripe::CardError

Codese.error.code == "card_declined"

ProblemThe card issuer declined the payment.Solutions

This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action may be legitimate. Use the decline code to determine what next steps are appropriate. See the documentation on decline codes for appropriate responses to each code.

You can also:

- [Follow recommendations to reduce issuer declines](/declines/card#reducing-bank-declines).
- Use[Payment Links](/payment-links),[Checkout](/payments/checkout), or[Stripe Elements](/payments/elements)for prebuilt form elements that implement those recommendations.

Test how your integration handles declines with test cards that simulate successful and declined payments.

### Other payment errors

TypeStripe::CardError

ProblemAnother payment error occurred.SolutionsThis error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the[documentation on error codes](/error-codes)for appropriate responses to each code.## Invalid request errors

TypeStripe::InvalidRequestError

ProblemYou made an API call with the wrong parameters, in the wrong state, or in an invalid way.SolutionsIn most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.- Consult the[error code documentation](/error-codes)for details on the problem.
- For convenience, you can follow the link atfor documentation about the error code.
- If the error involves a specific parameter, useto determine which one.

## Connection errors

TypeStripe::APIConnectionError

ProblemThere was a network problem between your server and Stripe.Solutions

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that if failed.

To find out if it succeeded, you can:

- Retrieve the relevant object from Stripe and check its status.
- Listen for webhook notification that the operation succeeded or failed.

To make it easier to recover from connection errors, you can:

- When creating or updating an object, use an[idempotency key](/api/idempotent_requests). Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice. Repeat the request with the same idempotency key until you receive a clear success or failure. For advanced advice on this strategy, see[Low-level error handling](/error-low-level#idempotency).
- Turn on[automatic retries.](#automatic-retries)Then, Stripe generates idempotency keys for you, and repeats requests for you when it is safe to do so.

This error can mask others. It’s possible that when the connection error resolves, some other error becomes apparent. Check for errors in all of these solutions just as you would in the original request.

## API errors

TypeStripe::APIError

ProblemSomething went wrong on Stripe’s end. (These are rare.)Solutions

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

Rely on webhooks for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

To set your integration up for maximum robustness in unusual situations, see this advanced discussion of server errors.

## Authentication errors

TypeStripe::AuthenticationError

ProblemStripe can’t authenticate you with the information provided.Solutions- Use the correct[API key](/keys).
- Make sure you aren’t using a key that you[“rolled” or revoked](/keys#rolling-keys).

## Idempotency errors

TypeStripe::IdempotencyError

ProblemYou used an[idempotency key](/api/idempotent_requests)for something unexpected, like replaying a request but passing different parameters.Solutions- After you use an idempotency key, only reuse it for identical API calls.
- Use idempotency keys under the limit of 255 characters.

## Permission errors

TypeStripe::PermissionError

ProblemThe API key used for this request does not have the necessary permissions.Solutions- Are you using a[restricted API key](/keys#limit-access)for a service it doesn’t have access to?
- Are you performing an action in the Dashboard while logged in as a[user role](/get-started/account/teams/roles)that lacks permission?

## Rate limit errors

TypeStripe::RateLimitError

ProblemYou made too many API calls in too short a time.Solutions- If a single API call triggers this error, wait and try it again.
- To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on[rate limits](/rate-limits)for further advice.
- If you anticipate a large increase in traffic and want to request an increased rate limit,[contact support](https://support.stripe.com/)in advance.

## Signature verification errors

TypeStripe::SignatureVerificationError

ProblemYou’re using[webhook](/webhooks)[signature verification](/webhooks#verify-events)and couldn’t verify that a webhook event is authentic.Solutions

This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a 400 Bad Request status code.

If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on checking webhook signatures for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Catch exceptions](#catch-exceptions)[Monitor webhooks](#monitor-webhooks)[Get stored information about failures](#use-stored-information)[Types of error and responses](#error-types)[Payment errors](#payment-errors)[Payment blocked](#payment-blocked)[Payment declined](#payment-declined)[Other payment errors](#other-card-errors)[Invalid request errors](#invalid-request-errors)[Connection errors](#connection-errors)[API errors](#api-errors)[Authentication errors](#authentication-errors)[Idempotency errors](#idempotency-errors)[Permission errors](#permission-errors)[Rate limit errors](#rate-limit-errors)[Signature verification errors](#signature-verification-errors)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
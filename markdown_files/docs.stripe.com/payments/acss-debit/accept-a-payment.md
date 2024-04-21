htmlAccept a Canadian pre-authorized debit payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Facss-debit%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Facss-debit%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[Pre-authorized debit in Canada](/docs/payments/acss-debit)# Accept a Canadian pre-authorized debit payment

Build a custom payment form or use Stripe Checkout to accept payments with pre-authorized debit in Canada.Custom payment formPrebuilt Checkout pageAccepting Canadian pre-authorized debit (PAD) payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, submitting the payment to Stripe for processing and verifying your customer’s bank account.

Stripe uses this payment object, the Payment Intent, to track and handle all the states of the payment until the payment completes.

[Set up StripeServer-side](#web-set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve a CustomerServer-side](#web-create-customer)To reuse a bank account for future payments, it must be attached to a Customer.

You should create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a PaymentIntentServer-side](#web-create-payment-intent)A PaymentIntent is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through each stage.

In order to use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see PAD Mandates). The Mandate object records this agreement and authorization.

First, create a PaymentIntent on your server and specify the amount to collect and currency (usually cad). If you already have another integration using the Payment Intents API, add acss_debit to the list of payment method types for your PaymentIntent. Specify the id of the Customer.

If you want to reuse the payment method in the future, provide the setup_future_usage parameter with a value of off_session.

In order to define a payment schedule and verification method on the Mandate for this PaymentIntent, also include the following parameters:

ParameterValueRequired?`payment_method_options[acss_debit][mandate_options][payment_schedule]`The mandate payment schedule. Accepted values are`interval`,`sporadic`, or`combined`. See the[PAD Mandates](/payments/acss-debit#mandates)overview to help you select the right schedule for your business.Yes`payment_method_options[acss_debit][mandate_options][interval_description]`Text description of the interval of payment schedule. See the[PAD Mandates](/payments/acss-debit#mandates)overview to help you construct the right interval description for your business.If`payment_schedule`is specified as`interval`or`combined``payment_method_options[acss_debit][mandate_options][transaction_type]`The type of the mandate you are creating, either`personal`(if your customer is an individual) or`business`(if your customer is a business).YesCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=cad \
  -d setup_future_usage=off_session \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=acss_debit \
  -d "payment_method_options[acss_debit][mandate_options][payment_schedule]"=interval \
  -d "payment_method_options[acss_debit][mandate_options][interval_description]"="First day of every month" \
  -d "payment_method_options[acss_debit][mandate_options][transaction_type]"=personal`### Retrieve the client secret

The PaymentIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

Single-page applicationServer-side renderingRetrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

main.rb[Ruby](#)`get '/secret' do
  intent = # ... Create or retrieve the PaymentIntent
  {client_secret: intent.client_secret}.to_json
end`And then fetch the client secret with JavaScript on the client side:

`(async () => {
  const response = await fetch('/secret');
  const {client_secret: clientSecret} = await response.json();
  // Render the form using the clientSecret
})();`[Collect payment method details and submitClient-side](#web-collect-mandate-and-submit)When a customer clicks to pay with Canadian pre-authorized debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

client.js`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`Rather than sending the entire PaymentIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmAcssDebitPayment to collect bank account details and verification, confirm the mandate, and complete the payment when the user submits the form. Including the customer’s email address and the account holder’s name in the billing_details property of the payment_method parameter is required to create a PAD payment method.

`const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {paymentIntent, error} = await stripe.confirmAcssDebitPayment(
    clientSecret,
    {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
          email: email.value,
        },
      },
    }
  );

  if (error) {
    // Inform the customer that there was an error.
    console.log(error.message);
  } else {
      // Handle next step based on PaymentIntent's status.
      console.log("PaymentIntent ID: " + paymentIntent.id);
      console.log("PaymentIntent status: " + paymentIntent.status);
  }
});`Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

Notestripe.confirmAcssDebitPayment may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

StatusDescriptionNext step`processing`The bank account has been instantly verified or verification was not necessary.​​​​​​Step 6:[Confirm the PaymentIntent succeeded](#web-confirm-paymentintent-succeeded)`requires_action`Further action needed to complete bank account verification.Step 5:[Verifying bank accounts with micro-deposits](#web-verify-with-microdeposits)After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to send custom notifications if you prefer.

NoteMandate confirmation emails will not be sent to the customer’s email address when testing the integration.

If the customer chooses to close the modal without completing the verification flow, Stripe.js returns the following error:

`{
  "error": {
    "type": "validation_error",
    "code": "incomplete_payment_details",
    "message": "Please provide complete payment details."
  }
}`[Verify bank account with micro-depositsClient-side](#web-verify-with-microdeposits)Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In this case, Stripe automatically sends two micro-deposits to the customer’s bank account. These deposits take one to two business days to appear on the customer’s online statement and have statement descriptors that include ACCTVERIFY.

The result of the stripe.confirmAcssDebitPayment method call in the previous step is a PaymentIntent in the requires_action state. The PaymentIntent contains a next_action field that contains some useful information for completing the verification.

Stripe notifies your customer at the billing email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits are not verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send custom email notifications, you have to email your customer instead. To do this, you can use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.

If you are sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using Stripe.js.

`stripe.verifyMicrodepositsForPayment(clientSecret, {
  amounts: [32, 45],
});`When the bank account is successfully verified, Stripe returns the PaymentIntent object with a status of processing, and sends a payment_intent.processing webhook event.

Verification can fail for several reasons. The failure may happen synchronously as a direct error response, or asynchronously through a payment_intent.payment_failed webhook event (shown in the following examples).

Synchronous ErrorWebhook Event`{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}`Error CodeSynchronous or asynchronousMessageStatus Change`payment_method_microdeposit_failed`Synchronously, or asynchronously through webhook eventMicrodeposits failed. Please check the account, institution and transit numbers provided`status`is`requires_payment_method`, and`last_payment_error`is set.`payment_method_microdeposit_verification_amounts_mismatch`SynchronouslyThe amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.Unchanged`payment_method_microdeposit_verification_attempts_exceeded`Synchronously, and asynchronously through webhook eventExceeded number of allowed verification attempts`status`is`requires_payment_method`, and`last_payment_error`is set.`payment_method_microdeposit_verification_timeout`Asynchronously through webhook eventMicrodeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.`status`is`requires_payment_method`, and`last_payment_error`is set.[Confirm the PaymentIntent succeededServer-side](#web-confirm-paymentintent-succeeded)Canadian pre-authorized debits are a delayed notification payment method. This means that it can take up to five business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of processing. Successful completion of the payment updates the PaymentIntent status from processing to succeeded.

The following events are sent when the PaymentIntent status is updated:

EventDescriptionNext step`payment_intent.processing`The customer’s payment was submitted to Stripe successfully.Wait for the initiated payment to succeed or fail.`payment_intent.succeeded`The customer’s payment succeeded.Fulfill the goods or services that the customer purchased.`payment_intent.payment_failed`The customer’s payment was declined. This can also apply to a failed microdeposit verification.Contact the customer via email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account.We recommend using webhooks to confirm the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the Stripe Dashboard.

[Test your integration](#web-test-integration)### Receive micro-deposit verification email

In order to receive the micro-deposit verification email in test mode after collecting the bank account details and accepting a mandate, provide an email in the payment_method[billing_details][email] field in the form of {any_prefix}+test_email@{any_domain} when confirming the payment method details.

### Test account numbers

Stripe provides several test account numbers you can use to make sure your integration for manually-entered bank accounts is ready for production. All test accounts that automatically succeed or fail the payment must be verified using the test micro-deposit amounts below before they can be completed.

Institution NumberTransit NumberAccount NumberScenario`000``11000``000123456789`Succeeds the payment immediately after micro-deposits are verified.`000``11000``900123456789`Succeeds the payment with a three-minute delay after micro-deposits are verified.`000``11000``000222222227`Fails the payment immediately after micro-deposits are verified.`000``11000``900222222227`Fails the payment with a three-minute delay after micro-deposits are verified.`000``11000``000666666661`Fails to send verification micro-deposits.To mimic successful or failed bank account verifications in test mode, use these meaningful amounts for micro-deposits:

Micro-deposit ValuesScenario`32`and`45`Successfully verifies the account.Any other number combinationsFails account verification.[OptionalInstant only verificationServer-side](#web-instant-only)[OptionalMicro-deposit only verificationServer-side](#web-microdeposit-only)## See also

- [Save Canadian pre-authorized debit details for future payments](/payments/acss-debit/set-up-payment)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#web-set-up-stripe)[Create or retrieve a Customer](#web-create-customer)[Create a PaymentIntent](#web-create-payment-intent)[Collect payment method details and submit](#web-collect-mandate-and-submit)[Verify bank account with micro-deposits](#web-verify-with-microdeposits)[Confirm the PaymentIntent succeeded](#web-confirm-paymentintent-succeeded)[Test your integration](#web-test-integration)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
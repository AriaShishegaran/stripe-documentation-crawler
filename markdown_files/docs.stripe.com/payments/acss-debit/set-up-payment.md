htmlSave details for future payments with pre-authorized debit in Canada | Stripe Documentation[Skip to content](#main-content)Save bank details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Facss-debit%2Fset-up-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Facss-debit%2Fset-up-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[Pre-authorized debit in Canada](/docs/payments/acss-debit)# Save details for future payments with pre-authorized debit in Canada

Learn how to save payment method details for future Canadian pre-authorized debit payments.Custom formPrebuilt checkout pageYou can use the Setup Intents API to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a[subscription](/billing/subscriptions/creating)

### Presentment currency

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It is possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so results in a delayed payment failure that takes up to five business days.

To avoid these failures, it is safest to set up PAD bank accounts in CAD unless you are confident your customer’s account accepts USD debits.

[Set up StripeServer-side](#web-set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve a CustomerServer-side](#web-create-customer)To reuse a bank account for future payments, it must be attached to a Customer.

You should create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

Create a new Customer or retrieve an existing Customer to associate with these payment details. Include the following code on your server to create a new Customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a SetupIntentServer-side](#web-create-setup-intent)A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

In order to use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see PAD Mandates). The Mandate object records this agreement and authorization.

Create a SetupIntent on your server with payment_method_types set to acss_debit and specify the Customer’s id. In order to define a payment schedule on the Mandate for this SetupIntent, also include the following parameters:

ParameterValueRequired?`payment_method_options[acss_debit][currency]`Currency to use for future payments with this payment method. Must match the customer’s bank account currency. Accepted values are`cad`or`usd`.Yes`payment_method_options[acss_debit][mandate_options][payment_schedule]`The mandate payment schedule. Accepted values are`interval`,`sporadic`, or`combined`. See the[PAD Mandates](/payments/acss-debit#mandates)overview to help you select the right schedule for your business.Yes`payment_method_options[acss_debit][mandate_options][interval_description]`Text description of the interval of payment schedule. See the[PAD Mandates](/payments/acss-debit#mandates)overview to help you construct the right interval description for your business.If`payment_schedule`specified as`interval`or`combined``payment_method_options[acss_debit][mandate_options][transaction_type]`The type of the mandate you are creating, either`personal`(if your customer is an individual) or`business`(if your customer is a business).YesCommand Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "payment_method_types[]"=acss_debit \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_options[acss_debit][currency]"=cad \
  -d "payment_method_options[acss_debit][mandate_options][payment_schedule]"=interval \
  -d "payment_method_options[acss_debit][mandate_options][interval_description]"="First day of every month" \
  -d "payment_method_options[acss_debit][mandate_options][transaction_type]"=personal`### Retrieve the client secret

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

Single-page applicationServer-side renderingRetrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

main.rb[Ruby](#)`get '/secret' do
  intent = # ... Create or retrieve the SetupIntent
  {client_secret: intent.client_secret}.to_json
end`And then fetch the client secret with JavaScript on the client side:

`(async () => {
  const response = await fetch('/secret');
  const {client_secret: clientSecret} = await response.json();
  // Render the form using the clientSecret
})();`[Collect payment method details and mandate acknowledgementClient-side](#web-collect-mandate-and-submit)When a customer clicks to pay with Canadian pre-authorized debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

client.js`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`Rather than sending the entire PaymentIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.confirmAcssDebitSetup to collect bank account details and verification, confirm the mandate, and complete the setup when the user submits the form. Including the customer’s email address and the account holder’s name in the billing_details property of the payment_method parameter is required to create a PAD payment method.

`const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {setupIntent, error} = await stripe.confirmAcssDebitSetup(
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
      // Handle next step based on SetupIntent's status.
      console.log("SetupIntent ID: " + setupIntent.id);
      console.log("SetupIntent status: " + setupIntent.status);
  }
});`Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

Notestripe.confirmAcssDebitSetup may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

StatusDescriptionNext step`succeeded`The bank account has been instantly verified or verification was not necessary.No action needed`requires_action`Further action needed to complete bank account verification.Step 5:[Verifying bank accounts with micro-deposits](#web-verify-with-microdeposits)After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to send custom notifications if you prefer.

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

The result of the stripe.confirmAcssDebitSetup method call is a SetupIntent in the requires_action state. The SetupIntent contains a next_action field that contains some useful information for completing the verification.

Stripe notifies your customer at the billing email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits are not verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send custom email notifications, you have to email your customer instead. To do this, you can use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.

If you are sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using Stripe.js.

`stripe.verifyMicrodepositsForSetup(clientSecret, {
  amounts: [32, 45],
});`When the bank account is successfully verified, Stripe returns the SetupIntent object, with a status of succeeded, and sends a setup_intent.succeeded webhook event.

Verification can fail for several reasons. The failure may happen synchronously as a direct error response, or asynchronously through a setup_intent.payment_failed webhook event (shown in the following examples).

Synchronous ErrorWebhook Event`{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}`Error CodeSynchronous or asynchronousMessageStatus Change`payment_method_microdeposit_failed`Synchronously, or asynchronously through webhook eventMicrodeposits failed. Please check the account, institution and transit numbers provided`status`is`requires_payment_method`, and`last_setup_error`is set.`payment_method_microdeposit_verification_amounts_mismatch`SynchronouslyThe amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.Unchanged`payment_method_microdeposit_verification_attempts_exceeded`Synchronously, and asynchronously through webhook eventExceeded number of allowed verification attempts`status`is`requires_payment_method`, and`last_setup_error`is set.`payment_method_microdeposit_verification_timeout`Asynchronously through webhook eventMicrodeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.`status`is`requires_payment_method`, and`last_setup_error`is set.[Test your integration](#web-test-integration)### Receive micro-deposit verification email

In order to receive the micro-deposit verification email in test mode after collecting the bank account details and accepting a mandate, provide an email in the payment_method[billing_details][email] field in the form of {any_prefix}+test_email@{any_domain} when confirming the payment method details.

### Test account numbers

Stripe provides several test account numbers you can use to make sure your integration for manually-entered bank accounts is ready for production. All test accounts that automatically succeed or fail the payment must be verified using the test micro-deposit amounts below before they can be completed.

Institution NumberTransit NumberAccount NumberScenario`000``11000``000123456789`Succeeds the payment immediately after micro-deposits are verified.`000``11000``900123456789`Succeeds the payment with a three-minute delay after micro-deposits are verified.`000``11000``000222222227`Fails the payment immediately after micro-deposits are verified.`000``11000``900222222227`Fails the payment with a three-minute delay after micro-deposits are verified.`000``11000``000666666661`Fails to send verification micro-deposits.To mimic successful or failed bank account verifications in test mode, use these meaningful amounts for micro-deposits:

Micro-deposit ValuesScenario`32`and`45`Successfully verifies the account.Any other number combinationsFails account verification.[OptionalAccept future paymentsServer-side](#charge-later)[OptionalInstant only verificationServer-side](#web-instant-only)[OptionalMicro-deposit only verificationServer-side](#web-microdeposit-only)## See also

- [Accept a Canadian pre-authorized debit payment](/payments/acss-debit/accept-a-payment)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#web-set-up-stripe)[Create or retrieve a Customer](#web-create-customer)[Create a SetupIntent](#web-create-setup-intent)[Collect payment method details and mandate acknowledgement](#web-collect-mandate-and-submit)[Verify bank account with micro-deposits](#web-verify-with-microdeposits)[Test your integration](#web-test-integration)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
htmlSave details for future payments with ACH Direct Debit | Stripe Documentation[Skip to content](#main-content)Save bank details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Fset-up-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Fset-up-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[ACH Direct Debit](/docs/payments/ach-debit)# Save details for future payments with ACH Direct Debit

Learn how to save payment method details for future ACH Direct Debit payments.Custom payment formPrebuilt checkout pageiOSAndroidReact NativeYou can use the Setup Intents API to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a[subscription](/billing/subscriptions/creating)

NoteACH Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

[Create or retrieve a customerRecommendedServer-side](#web-create-customer)Create a Customer object when your user creates an account with your business, or retrieve an existing Customer associated with this user. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the Customer to enable Financial Connections’ return user optimization.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Create a SetupIntentServer-side](#web-create-setup-intent)A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

Create a SetupIntent on your server with payment_method_types set to us_bank_account and specify the Customer’s id.

For more information on Financial Connections fees, see pricing details.

By default, collecting bank account payment information uses Financial Connections to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the Financial Connections docs to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

NoteTo expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=balances`### Retrieve the client secret

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
})();`[Collect payment method detailsClient-side](#web-collect-details)When a customer clicks to pay with ACH Direct Debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

client.js`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`Rather than sending the entire SetupIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the Payment Method setup process. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.collectBankAccountForSetup  to collect bank account details with Financial Connections, create a PaymentMethod, and attach that PaymentMethod to the SetupIntent. Including the account holder’s name in the billing_details parameter is required to create an ACH Direct Debit PaymentMethod.

script.js`// Use the form that already exists on the web page.
const paymentMethodForm = document.getElementById('payment-method-form');
const confirmationForm = document.getElementById('confirmation-form');

paymentMethodForm.addEventListener('submit', (ev) => {
  ev.preventDefault();
  const accountHolderNameField = document.getElementById('account-holder-name-field');
  const emailField = document.getElementById('email-field');

  // Calling this method will open the instant verification dialog.
  stripe.collectBankAccountForSetup({
    clientSecret: clientSecret,
    params: {
      payment_method_type: 'us_bank_account',
      payment_method_data: {
        billing_details: {
          name: accountHolderNameField.value,
          email: emailField.value,
        },
      },
    },
    expand: ['payment_method'],
  })
  .then(({setupIntent, error}) => {
    if (error) {
      console.error(error.message);
      // PaymentMethod collection failed for some reason.
    } else if (setupIntent.status === 'requires_payment_method') {
      // Customer canceled the hosted verification modal. Present them with other
      // payment method type options.
    } else if (setupIntent.status === 'requires_confirmation') {
      // We collected an account - possibly instantly verified, but possibly
      // manually-entered. Display payment method details and mandate text
      // to the customer and confirm the intent once they accept
      // the mandate.
      confirmationForm.show();
    }
  });
});`The Financial Connections authentication flow automatically handles bank account details collection and verification. When your customer completes the authentication flow, the PaymentMethod automatically attaches to the SetupIntent, and creates a Financial Connections Account.

Common mistakeBank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.



To provide the best user experience on all devices, set the viewport minimum-scale for your page to 1 using the viewport meta tag.

`<meta name="viewport" content="width=device-width, minimum-scale=1" />`[OptionalAccess data on a Financial Connections bank accountServer-side](#access-data-on-a-financial-connections-bank-account)[Collect mandate acknowledgement and submitClient-side](#web-collect-mandate-and-submit)Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see Mandates.

When the customer accepts the mandate terms, you must confirm the SetupIntent. Use stripe.confirmUsBankAccountSetup to complete the payment when the customer submits the form.

script.js`confirmationForm.addEventListener('submit', (ev) => {
  ev.preventDefault();
  stripe.confirmUsBankAccountSetup(clientSecret)
  .then(({setupIntent, error}) => {
    if (error) {
      console.error(error.message);
      // The payment failed for some reason.
    } else if (setupIntent.status === "requires_payment_method") {
      // Confirmation failed. Attempt again with a different payment method.
    } else if (setupIntent.status === "succeeded") {
      // Confirmation succeeded! The account is now saved.
      // Display a message to customer.
    } else if (setupIntent.next_action?.type === "verify_with_microdeposits") {
      // The account needs to be verified via microdeposits.
      // Display a message to consumer with next steps (consumer waits for
      // microdeposits, then enters a statement descriptor code on a page sent to them via email).
    }
  });
});`Notestripe.confirmUsBankAccountSetup may take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

StatusDescriptionNext Steps`succeeded`The bank account has been instantly verified or verification was not necessary.No action needed`requires_action`Further action needed to complete bank account verification.Step 6:[Verifying bank accounts with microdeposits](/payments/ach-debit/accept-a-payment#web-verify-with-microdeposits)After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to send custom notifications if you prefer.

[Verify bank account with microdepositsClient-side](#web-verify-with-microdeposits)Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a descriptor_code microdeposit and might fall back to an amount microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- Descriptor code. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit`descriptor_code`that starts with SM. Your customer uses this string to verify their bank account.
- Amount. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads`ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the stripe.confirmUsBankAccountSetup method call in the previous step is a SetupIntent in the requires_action state. The SetupIntent contains a next_action field that contains some useful information for completing the verification.

`next_action: {
  type: "verify_with_microdeposits",
  verify_with_microdeposits: {
    arrival_date: 1647586800,
    hosted_verification_url: "https://payments.stripe.com/…",
    microdeposit_type: "descriptor_code"
  }
}`If you supplied a billing email, Stripe notifies your customer via this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

WarningVerification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the SetupIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

Optionally, you can send custom email notifications to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose one of the following:

- Use the Stripe-hosted verification page. To do this, use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.


- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using Stripe.js.

  - At minimum, set up the form to handle the`descriptor code`parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the`amounts`parameter, as some banks your customers use may require it.

Integrations only pass in the descriptor_code or amounts. To determine which one your integration uses, check the value for verify_with_microdeposits[microdeposit_type] in the next_action object.



`stripe.verifyMicrodepositsForSetup(clientSecret, {
  // Provide either a descriptor_code OR amounts, not both
  descriptor_code: `SMT86W`,
  amounts: [32, 45],
});`When the bank account is successfully verified, Stripe returns the SetupIntent object with a status of succeeded, and sends a setup_intent.succeeded webhook event.

Verification can fail for several reasons. The failure may happen synchronously as a direct error response, or asynchronously through a setup_intent.setup_failed webhook event (shown in the following examples).

Synchronous ErrorWebhook Event`{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}`Error CodeSynchronous or AsynchronousMessageStatus change`payment_method_microdeposit_failed`Synchronously, or asynchronously through webhook eventMicrodeposits failed. Please check the account, institution and transit numbers provided`status`is`requires_payment_method`, and`last_setup_error`is set.`payment_method_microdeposit_verification_amounts_mismatch`SynchronouslyThe amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.Unchanged`payment_method_microdeposit_verification_attempts_exceeded`Synchronously, or asynchronously through webhook eventExceeded number of allowed verification attempts`status`is`requires_payment_method`, and`last_setup_error`is set.`payment_method_microdeposit_verification_timeout`Asynchronously through webhook eventMicrodeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.`status`is`requires_payment_method`, and`last_setup_error`is set.[Test your integration](#test-integration)Learn how to test scenarios with instant verifications using Financial Connections.

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

Common mistakeYou need to activate your Stripe account before you can trigger these emails in Test mode.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

Account numberTokenRouting numberBehavior`000123456789``pm_usBankAccount_success``110000000`The payment succeeds.`000111111113``pm_usBankAccount_accountClosed``110000000`The payment fails because the account is closed.`000111111116``pm_usBankAccount_noAccount``110000000`The payment fails because no account is found.`000222222227``pm_usBankAccount_insufficientFunds``110000000`The payment fails due to insufficient funds.`000333333335``pm_usBankAccount_debitNotAuthorized``110000000`The payment fails because debits aren’t authorized.`000444444440``pm_usBankAccount_invalidCurrency``110000000`The payment fails due to invalid currency.`000666666661``pm_usBankAccount_failMicrodeposits``110000000`The payment fails to send microdeposits.`000555555559``pm_usBankAccount_dispute``110000000`The payment triggers a dispute.`000000000009``pm_usBankAccount_processing``110000000`The payment stays in processing indefinitely. Useful for testing[PaymentIntent cancellation](/api/payment_intents/cancel).Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

Microdeposit values0.01 descriptor code valuesScenario`32`and`45`SM11AASimulates verifying the account.`10`and`11`SM33CCSimulates exceeding the number of allowed verification attempts.`40`and`41`SM44DDSimulates a microdeposit timeout.[Accepting future paymentsServer-side](#web-future-payments)When the SetupIntent succeeds, it will create a new PaymentMethod attached to a Customer. These can be used to initiate future payments without having to prompt the customer for their bank account a second time.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=1099 \
  -d "currency"="usd" \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "payment_method"="{{PAYMENT_METHOD_ID}}" \
  -d "payment_method_types[]"="us_bank_account" \
  -d "confirm"="true"`[OptionalInstant only verificationServer-side](#instant-only-verification)[OptionalMicrodeposit only verificationServer-side](#microdeposit-only-verification)[OptionalUpdating the default payment methodServer-side](#update-default-payment-method)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create or retrieve a customer](#web-create-customer)[Create a SetupIntent](#web-create-setup-intent)[Collect payment method details](#web-collect-details)[Collect mandate acknowledgement and submit](#web-collect-mandate-and-submit)[Verify bank account with microdeposits](#web-verify-with-microdeposits)[Test your integration](#test-integration)[Accepting future payments](#web-future-payments)Products Used[Payments](/payments)[Elements](/payments/elements)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
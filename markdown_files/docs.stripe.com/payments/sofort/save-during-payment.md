htmlSave bank details during a Sofort payment | Stripe Documentation[Skip to content](#main-content)Save bank details during payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort%2Fsave-during-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort%2Fsave-during-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)[Sofort](/docs/payments/sofort)# Save bank details during a Sofort payment

Learn how to save your customer's IBAN bank details from a Sofort payment.WarningOur financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

CautionWe recommend that you follow the Save payment details during payment guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

### SEPA Direct Debit

See accepting SEPA Direct Debit payments to integrate without Sofort.

Sofort is a single use, delayed notification payment method that requires customers to authenticate their payment. Customers pay with Sofort by redirecting from your website to their bank’s portal to authenticate the payment. It typically takes 2 to 14 days to receive notification of success or failure.

You can use Sofort to save your customer’s IBAN bank details into a SEPA Direct Debit PaymentMethod. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription. This reduces friction for your customer as they don’t have to enter their IBAN again. You also receive their verified name and validated IBAN.

CautionTo use Sofort to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the Sofort Terms of Service and SEPA Direct Debit Terms of Service.

WebiOSAndroidReact NativeAccepting Sofort payments consists of creating a PaymentIntent object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit PaymentMethod collected from your initial Sofort PaymentIntent to create PaymentIntents for future payments.

[Set up StripeServer-side](#set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a CustomerServer-side](#create-customer)Create a Customer when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a PaymentIntentServer-side](#create-payment-intent)Create a PaymentIntent on your server and specify the amount to collect, the eur currency, the customer ID, and off_session as an argument for setup future usage. If you have an existing Payment Intents integration, add sofort to the list of payment method types.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]"=sofort \
  -d customer={{CUSTOMER_ID}} \
  -d setup_future_usage=off_session`The PaymentIntent includes the payment method ID and a client secret, which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object.

[Collect payment method details and mandate acknowledgementClient-side](#collect-payment-method-details)Create a payment form on your client to collect the required billing details from the customer.

HTML + JSReact​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace Rocket Rides with your company name.

deenesfifritnlAuthorization text templateBy providing your payment information and confirming this payment, you authorise (A)Rocket RidesReplace this with your company nameand Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you are entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.[Copy](#)​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

FieldValue`name`The full name (first and last) of the customer.`email`The customer’s email.checkout.html`<form id="payment-form">
  <div class="form-row">
    <label for="name">
      Name
    </label>
    <input id="name" name="name" required>
  </div>

  <div class="form-row">
    <label for="email">
      Email
    </label>
    <input id="email" name="email" required>
  </div>

  <button id="submit-button">Pay with Sofort</button>

  <!-- Display mandate acceptance text. -->
  <div id="mandate-acceptance">
    By providing your payment information and confirming this payment, you
    authorise (A) Rocket Rides and Stripe, our payment service provider, to
    send instructions to your bank to debit your account and (B) your bank to
    debit your account in accordance with those instructions. As part of your
    rights, you are entitled to a refund from your bank under the terms and
    conditions of your agreement with your bank. A refund must be claimed
    within 8 weeks starting from the date on which your account was debited.
    Your rights are explained in a statement that you can obtain from your
    bank. You agree to receive notifications for future debits up to 2 days
    before they occur.
  </div>
  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>`[Submit the payment to StripeClient-side](#submit-payment)Rather than sending the entire PaymentIntent object to the client, use its client secret from step 3. This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

HTML + JSReactUse stripe.confirmSofortPayment to handle the redirect away from your page and to complete the payment. Add a return_url to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

Include your customer’s name and email address in payment_method[billing_details]. They will be used when generating the SEPA Direct Debit PaymentMethod.

client.js`var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
var accountholderName = document.getElementById('name');
var accountholderEmail = document.getElementById('email');

// Redirects away from the client
const {error} = await stripe.confirmSofortPayment(
  '{{PAYMENT_INTENT_CLIENT_SECRET}}',
  {
    payment_method: {
      sofort: {
        country: "DE"
      },
      billing_details: {
        name: accountholderName.value,
        email: accountholderEmail.value,
      },
    },
    return_url: 'https://example.com/checkout/complete',
  }
);

if (error) {
  // Inform the customer that there was an error.
}`When your customer submits a payment, Stripe redirects them to the return_url and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the return_url, you can also append your own query parameters for use on the return page.

ParameterDescription`payment_intent`The unique identifier for the`PaymentIntent`.`payment_intent_client_secret`The[client secret](/api/payment_intents/object#payment_intent_object-client_secret)of the`PaymentIntent`object.When the customer is redirected back to your site, you can use the payment_intent_client_secret to query for the PaymentIntent and display the transaction status to your customer.

[Charge the SEPA Direct Debit PaymentMethod later](#charge-sepa-pm)When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by retrieving the previous PaymentIntent and expanding the latest_charge field where you will find the generated_sepa_debit ID inside of payment_method_details.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=latest_charge`The SEPA Direct Debit payment method ID is the generated_sepa_debit ID under payment_method_details in the response.

`{
  "latest_charge": {
    "payment_method_details": {
      "sofort": {
        "bank_code": "VAPE",
        "bank_name": "VAN DE PUT & CO",
        "bics": "VAPEBE22",
        "iban_last4": "7061",
        "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
        "preferred_language": "en",
        "verified_name": "Jenny Rosen"
      },
      "type": "sofort"
    },
  },
  "payment_method_options": {
    "sofort": {}`See all 32 linesCreate a PaymentIntent with the SEPA Direct Debit and Customer IDs.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "payment_method_types[]"=sepa_debit \
  -d amount=1099 \
  -d currency=eur \
  -d customer={{CUSTOMER_ID}} \
  -d payment_method={{SEPA_DEBIT_PAYMENT_METHOD_ID}} \
  -d confirm=true`[Test your integration](#test-your-integration)EmailPaymentMethodSet payment_method.billing_details.email to one of the following values to test the PaymentIntent status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, test_1_generatedSepaDebitIntentsFail@example.com results in a SEPA Direct Debit PaymentMethod that will always fail when used with a PaymentIntent.

Country:AustriaBelgiumGermanyNetherlandsSpainEmail AddressDescriptiongeneratedSepaDebitIntentsSucceedAustria@example.comThe SEPA Direct Debit PaymentIntent status transitions from`processing`to`succeeded`.generatedSepaDebitIntentsSucceedDelayedAustria@example.comThe SEPA Direct Debit PaymentIntent status transitions from`processing`to`succeeded`after three minutes.generatedSepaDebitIntentsFailAustria@example.comThe SEPA Direct Debit PaymentIntent status transitions from`processing`to`requires_payment_method`.generatedSepaDebitIntentsFailDelayedAustria@example.comThe SEPA Direct Debit PaymentIntent status transitions from`processing`to`requires_payment_method`after three minutes.generatedSepaDebitIntentsSucceedDisputedAustria@example.comThe SEPA Direct Debit PaymentIntent status transitions from`processing`to`succeeded`, but a dispute is created immediately.[Handle post-payment events](#fulfillment)As Sofort is a delayed notification payment method, the PaymentIntent’s status remains in a payment_intent.processing state for up to 14 days from its creation (also known as the cutoff date). In test mode, the PaymentIntent’s status remains in the processing state for three minutes to simulate this.

- Stripe recommends fulfilling purchases during the processing state. On average, you can expect approximately 0.2% of Sofort payment attempts to fail after entering the processing state. This only applies to Sofort payments due to its low payment failure rate and doesn’t apply to other[delayed notification](/payments/payment-methods#payment-notification)payment methods.
- You may prefer to fulfill orders only after receiving the[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)event. Stripe sends this event after the payment attempt is confirmed and the funds are guaranteed.
- If a customer doesn’t pay, Stripe sends the[payment_intent.failed](/api/events/types#event_types-payment_intent.failed)event and the PaymentIntent returns to a status of`requires_payment_method`.

Use the Dashboard, a custom webhook, or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](/payments/handling-payment-events#build-your-own-webhook)

### Prebuilt apps

Handle common business events, like automation or marketing and sales, by integrating a partner application.

[OptionalHandle the Sofort redirect manually](#handle-redirect)## See also

- [Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)
- [Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Create a Customer](#create-customer)[Create a PaymentIntent](#create-payment-intent)[Collect payment method details and mandate acknowledgement](#collect-payment-method-details)[Submit the payment to Stripe](#submit-payment)[Charge the SEPA Direct Debit PaymentMethod later](#charge-sepa-pm)[Test your integration](#test-your-integration)[Handle post-payment events](#fulfillment)[See also](#see-also)Products Used[Payments](/payments)[Elements](/payments/elements)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
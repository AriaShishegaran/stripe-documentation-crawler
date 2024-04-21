htmlSet up a subscription with ACH Direct Debit | Stripe Documentation[Skip to content](#main-content)ACH Direct Debit[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fach-debit)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fach-debit)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with ACH Direct Debit

Learn how to create and charge for a subscription with US bank account.Custom payment formPrebuilt checkout pageNoteIf you’re a new user, use the Payment Element instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see Build a subscription.

[Create a product and priceDashboard](#create-product-plan-code)Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Navigate to the[Add a product](https://dashboard.stripe.com/test/products/create)page.
2. Enter aNamefor the product.
3. Enter15for the price.
4. SelectUSDas the currency.
5. ClickSave product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create the subscriptionServer-side](#create-subscription)NoteTo create a subscription with a free trial period, see Subscription trials.

Create a subscription with the price and customer with status incomplete by providing the payment_behavior parameter with the value of default_incomplete.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "items[0][price]"="price_F52b2UdntfQsfR" \
  -d "payment_behavior"="default_incomplete" \
  -d "payment_settings[payment_method_types][]"="us_bank_account" \
  -d "expand[0]"="latest_invoice.payment_intent"`Included in the response is the subscription’s first PaymentIntent, containing the client secret, which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the client_secret to the frontend to complete payment.

[Collect payment method detailsClient-side](#collect-payment-details)When a customer clicks to pay with ACH Direct Debit, we recommend you use Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

client.js`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`Rather than sending the entire PaymentIntent object to the client, use its client secret from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use stripe.collectBankAccountForPayment  to collect bank account details with Financial Connections, create a PaymentMethod, and attach that PaymentMethod to the PaymentIntent. Including the account holder’s name in the billing_details parameter is required to create an ACH Direct Debit PaymentMethod.

script.js`// Use the form that already exists on the web page.
const paymentMethodForm = document.getElementById('payment-method-form');
const confirmationForm = document.getElementById('confirmation-form');

paymentMethodForm.addEventListener('submit', (ev) => {
  ev.preventDefault();
  const accountHolderNameField = document.getElementById('account-holder-name-field');
  const emailField = document.getElementById('email-field');

  // Calling this method will open the instant verification dialog.
  stripe.collectBankAccountForPayment({
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
  .then(({paymentIntent, error}) => {
    if (error) {
      console.error(error.message);
      // PaymentMethod collection failed for some reason.
    } else if (paymentIntent.status === 'requires_payment_method') {
      // Customer canceled the hosted verification modal. Present them with other
      // payment method type options.
    } else if (paymentIntent.status === 'requires_confirmation') {
      // We collected an account - possibly instantly verified, but possibly
      // manually-entered. Display payment method details and mandate text
      // to the customer and confirm the intent once they accept
      // the mandate.
      confirmationForm.show();
    }
  });
});`The Financial Connections authentication flow automatically handles bank account details collection and verification. When your customer completes the authentication flow, the PaymentMethod automatically attaches to the PaymentIntent, and creates a Financial Connections Account.

Common mistakeBank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.



To provide the best user experience on all devices, set the viewport minimum-scale for your page to 1 using the viewport meta tag.

`<meta name="viewport" content="width=device-width, minimum-scale=1" />`[Collect mandate acknowledgement and submitClient-side](#collect-mandate-and-submit)Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see Mandates.

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use stripe.confirmUsBankAccountPayment to complete the payment when the customer submits the form.

script.js`confirmationForm.addEventListener('submit', (ev) => {
  ev.preventDefault();
  stripe.confirmUsBankAccountPayment(clientSecret)
  .then(({paymentIntent, error}) => {
    if (error) {
      console.error(error.message);
      // The payment failed for some reason.
    } else if (paymentIntent.status === "requires_payment_method") {
      // Confirmation failed. Attempt again with a different payment method.
    } else if (paymentIntent.status === "processing") {
      // Confirmation succeeded! The account will be debited.
      // Display a message to customer.
    } else if (paymentIntent.next_action?.type === "verify_with_microdeposits") {
      // The account needs to be verified via microdeposits.
      // Display a message to consumer with next steps (consumer waits for
      // microdeposits, then enters a statement descriptor code on a page sent to them via email).
    }
  });
});`Notestripe.confirmUsBankAccountPayment may take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If the customer completes instant verification, the subscription automatically becomes active. Otherwise, see Verify bank account with microdeposits to learn how to handle microdeposit verification while the subscription remains incomplete.

[Verify bank account with microdepositsClient-side](#verify-with-microdeposits)NoteCustomers have 10 days to successfully verify microdeposits for a subscription, instead of the 23 hours normally given in the subscription lifecycle. However, this expiration can’t be later than the billing cycle date.

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a descriptor_code microdeposit and might fall back to an amount microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- Descriptor code. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit`descriptor_code`that starts with SM. Your customer uses this string to verify their bank account.
- Amount. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads`ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the stripe.confirmUsBankAccountPayment method call in the previous step is a PaymentIntent in the requires_action state. The PaymentIntent contains a next_action field that contains some useful information for completing the verification.

`next_action: {
  type: "verify_with_microdeposits",
  verify_with_microdeposits: {
    arrival_date: 1647586800,
    hosted_verification_url: "https://payments.stripe.com/…",
    microdeposit_type: "descriptor_code"
  }
}`If you supplied a billing email, Stripe notifies your customer via this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

WarningVerification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

Optionally, you can send custom email notifications to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose one of the following:

- Use the Stripe-hosted verification page. To do this, use the verify_with_microdeposits[hosted_verification_url] URL in the next_action object to direct your customer to complete the verification process.


- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using Stripe.js.

  - At minimum, set up the form to handle the`descriptor code`parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the`amounts`parameter, as some banks your customers use may require it.

Integrations only pass in the descriptor_code or amounts. To determine which one your integration uses, check the value for verify_with_microdeposits[microdeposit_type] in the next_action object.



`stripe.verifyMicrodepositsForPayment(clientSecret, {
  // Provide either a descriptor_code OR amounts, not both
  descriptor_code: 'SMT86W',
  amounts: [32, 45],
});`[Set the default payment methodServer](#default-payment-method)You now have an active subscription belonging to a customer with a payment method, but this payment method isn’t automatically used for future payments. To automatically bill this payment method in the future, use a webhook consumer to listen to the invoice.payment_succeeded event for new subscriptions and set the default payment method.

server.rb[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

if event.type == 'invoice.payment_succeeded'
  invoice = event.data.object
  if invoice['billing_reason'] == 'subscription_create'
    subscription_id = invoice['subscription']
    payment_intent_id = invoice['payment_intent']

    # Retrieve the payment intent used to pay the subscription
    payment_intent = Stripe::PaymentIntent.retrieve(payment_intent_id)

    # Set the default payment method
    Stripe::Subscription.update(
      subscription_id,
      default_payment_method: payment_intent.payment_method
    )
  end
end`[Manage subscription statusClient-side](#manage-sub-status)Assuming the initial payment succeeds, the state of the subscription is active and requires no further action. When payments fail, the status changes to the Subscription status configured in your automatic collection settings. Notify the customer upon failure and charge them with a different payment method.

[Test your integration](#test-integration)Learn how to test scenarios with instant verifications using Financial Connections.

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

Common mistakeYou need to activate your Stripe account before you can trigger these emails in Test mode.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

Account numberTokenRouting numberBehavior`000123456789``pm_usBankAccount_success``110000000`The payment succeeds.`000111111113``pm_usBankAccount_accountClosed``110000000`The payment fails because the account is closed.`000111111116``pm_usBankAccount_noAccount``110000000`The payment fails because no account is found.`000222222227``pm_usBankAccount_insufficientFunds``110000000`The payment fails due to insufficient funds.`000333333335``pm_usBankAccount_debitNotAuthorized``110000000`The payment fails because debits aren’t authorized.`000444444440``pm_usBankAccount_invalidCurrency``110000000`The payment fails due to invalid currency.`000666666661``pm_usBankAccount_failMicrodeposits``110000000`The payment fails to send microdeposits.`000555555559``pm_usBankAccount_dispute``110000000`The payment triggers a dispute.`000000000009``pm_usBankAccount_processing``110000000`The payment stays in processing indefinitely. Useful for testing[PaymentIntent cancellation](/api/payment_intents/cancel).Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

Microdeposit values0.01 descriptor code valuesScenario`32`and`45`SM11AASimulates verifying the account.`10`and`11`SM33CCSimulates exceeding the number of allowed verification attempts.`40`and`41`SM44DDSimulates a microdeposit timeout.[OptionalSetting the billing cycle](#billing-cycle)[OptionalSubscription trials](#trial-periods)[OptionalSaving payment method details for future use](#save-payment-method-for-future-subscriptions)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product and price](#create-product-plan-code)[Create the subscription](#create-subscription)[Collect payment method details](#collect-payment-details)[Collect mandate acknowledgement and submit](#collect-mandate-and-submit)[Verify bank account with microdeposits](#verify-with-microdeposits)[Set the default payment method](#default-payment-method)[Manage subscription status](#manage-sub-status)[Test your integration](#test-integration)Products Used[Billing](/billing)[Checkout](/payments/checkout)[Elements](/payments/elements)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
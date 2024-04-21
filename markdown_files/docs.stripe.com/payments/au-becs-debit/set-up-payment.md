htmlSave BECS Direct Debit details for future payments | Stripe Documentation[Skip to content](#main-content)Save bank details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit%2Fset-up-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit%2Fset-up-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[BECS Direct Debit in Australia](/docs/payments/au-becs-debit)# Save BECS Direct Debit details for future payments

Use the Setup Intents API to save payment method details for future BECS Direct Debit payments.WebiOSAndroidReact NativeUse Stripe Elements, our prebuilt UI components, to create a payment form that lets you securely collect bank details without handling the sensitive data. You can use the Setup Intents API to collect BECS Direct Debit payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- [Starting a free trial for a subscription](/billing/subscriptions/trials)

[Set up StripeServer-side](#web-set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve a CustomerServer-side](#web-create-customer)To reuse a BECS Direct Debit account for future payments, you must attach it to a Customer.

Create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of them enables you to retrieve and use the stored payment method details later.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a SetupIntentServer-side](#web-create-setup-intent)A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a SetupIntent on your server with payment_method_types set to au_becs_debit and specify the Customer’s id:

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="au_becs_debit" \
  -d "customer"="{{CUSTOMER_ID}}"`After creating a SetupIntent on your server, you can associate the SetupIntent ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you have successfully collected a payment method.

The returned SetupIntent object contains a client_secret property. Pass the client secret to the client-side application to continue with the setup process.

[Collect payment method details and mandate acknowledgmentClient-side](#web-collect-payment-method-details)You’re ready to collect payment information on the client with Stripe Elements. Elements is a set of prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. Enable it when you’re ready to accept live payments.

### Set up Stripe Elements

HTML + JSReactStripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

payment_setup.html`<head>
  <title>Payment Setup</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Elements with the following JavaScript on your payment page:

`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const elements = stripe.elements();`### Direct Debit Requests

Before you can create a BECS Direct Debit payment, your customer must agree with the Direct Debit Request Service Agreement. They do so by submitting a completed Direct Debit Request (DDR). The approval gives you a mandate to debit their account. The Mandate is a record of the permission to debit a payment method.

For online mandate acceptance, you can create a form to collect the necessary information. Serve the form over HTTPS and capture the following information:

InformationDescriptionAccount nameThe full name of the account holderBSB numberThe Bank-State-Branch number of the bank account (for example,`123-456`)Account numberThe bank account number (for example,`87654321`)When collecting a Direct Debit Request, follow our BECS Direct Debit Terms and as part of your checkout form:

- Display the exact terms of[Stripe’s DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)either inline on the form, or on a page linked from the form, and identifying it as the “DDR service agreement.”
- Make sure the accepted DDR and its accompanying[DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal)can be shared with your customer at all times, either as a printed or non-changeable electronic copy (such as email). Stripe hosts this for you.
- Display the following standard authorization text for your customer to accept the BECS DDR, where you replaceRocketship Incwith your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

NoteBy providing your bank account details, you agree to this Direct Debit Request and the Direct Debit Request service agreement, and authorize Stripe Payments Australia Pty Ltd ACN 160 180 343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of Rocketship Inc (the “Merchant”) for any amounts separately communicated to you by the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

The details of the accepted mandate are generated when setting up a PaymentMethod or confirming a PaymentIntent. At all times, you should be able to share this mandate—the accepted DDR and its accompanying DDR service agreement—with your customer, either in print or as a non-changeable electronic copy (such as email). Stripe hosts this for you under the url property of the Mandate object linked to the PaymentMethod.

### Add and configure an Australia Bank Account Element

The Australia Bank Account Element will help you collect and validate both the BSB number and the account number. It needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form. Additionally, your customer must read and accept the Direct Debit Request service agreement.

payment_setup.html[HTML](#)`<form action="/setup" method="post" id="setup-form">
  <div class="form-row inline">
    <div class="col">
      <label for="accountholder-name">
        Name
      </label>
      <input
        id="accountholder-name"
        name="accountholder-name"
        placeholder="John Smith"
        required
      />
    </div>
    <div class="col">
      <label for="email">
        Email Address
      </label>
      <input
        id="email"
        name="email"
        type="email"
        placeholder="john.smith@example.com"
        required
      />
    </div>
  </div>

  <div class="form-row">
    <!--
    Using a label with a for attribute that matches the ID of the
    Element container enables the Element to automatically gain focus
    when the customer clicks on the label.
    -->
    <label for="au-bank-account-element">
      Bank Account
    </label>
    <div id="au-bank-account-element">
      <!-- A Stripe Element will be inserted here. -->
    </div>
  </div>

  <!-- Used to display bank (branch) name associated with the entered BSB -->
  <div id="bank-name"></div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <!-- Display mandate acceptance text. -->
  <div class="col" id="mandate-acceptance">
    By providing your bank account details, you agree to this Direct Debit Request
    and the <a href="stripe.com/au-becs-dd-service-agreement/legal">Direct Debit Request service agreement</a>,
    and authorise Stripe Payments Australia Pty Ltd ACN 160 180 343
    Direct Debit User ID number 507156 (“Stripe”) to debit your account
    through the Bulk Electronic Clearing System (BECS) on behalf of
    Rocket Rides (the "Merchant") for any amounts separately
    communicated to you by the Merchant. You certify that you are either
    an account holder or an authorised signatory on the account listed above.
  </div>
  
  <!-- Add the client_secret from the SetupIntent as a data attribute -->
  <button id="submit-button" data-secret="{{CLIENT_SECRET}}">Set up BECS Direct Debit</button>

</form>`When the form loads, you can create an instance of the Australia Bank Account Element and mount it to the Element container:

`// Custom styling can be passed to options when creating an Element
const style = {
  base: {
    color: '#32325d',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    },
    ':-webkit-autofill': {
      color: '#32325d',
    },
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a',
    ':-webkit-autofill': {
      color: '#fa755a',
    },
  }
};

const options = {
    style: style,
    disabled: false,
    hideIcon: false,
    iconStyle: "default", // or "solid"
}

// Create an instance of the auBankAccount Element.
const auBankAccount = elements.create('auBankAccount', options);

// Add an instance of the auBankAccount Element into
// the `au-bank-account-element` <div>.
auBankAccount.mount('#au-bank-account-element');`[Submit the payment method details to StripeClient-side](#web-submit-payment-method)Rather than sending the entire SetupIntent object to the client, use its client secret from step 2. This is different from your API keys that authenticate Stripe API requests.

The client secret should be handled carefully because it can complete the setup. Do not log it, embed it in URLs, or expose it to anyone but the customer.

HTML + JSReactUse stripe.confirmAuBecsDebitSetup to complete the setup when the user submits the form. A successful setup returns a succeeded value for the SetupIntent’s status property. If the setup isn’t successful, inspect the returned error to determine the cause.

As customer was set, the PaymentMethod is attached to the provided Customer object after a successful setup. At this point, you can associate the ID of the Customer object with your internal representation of a customer. This allows you to use the stored PaymentMethod to collect future payments without prompting for your customer’s payment method details.

`const form = document.getElementById('setup-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  stripe.confirmAuBecsDebitSetup(
    clientSecret,
    {
      payment_method: {
        au_becs_debit: auBankAccount,
        billing_details: {
          name: accountholderName.value,
          email: email.value
        }
      }
    }
  );
});`After successfully confirming the SetupIntent, you should share the mandate URL from the Mandate object with your customer. We also recommend including the following details to your customer when you confirm their mandate has been established:

- an explicit confirmation message that indicates a Direct Debit arrangement has been set up
- the[business name](#statement-descriptors)that will appear on the customer’s bank statement whenever their account gets debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The Mandate object’s ID is accessible from the mandate on the SetupIntent object, which is sent as part of the setup_intent.succeeded event sent after confirmation, but can also be retrieved through the API.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=mandate`[Test the integration](#web-test-integration)You can test your form using the test BSB number 000-000 and one of the test account numbers below with your confirmAuBecsDebitSetup request.

BSB NumberAccount NumberDescription`000-000``000123456`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`succeeded`. The mandate status remains`active`.`000-000``900123456`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`succeeded`(with a three-minute delay). The mandate status remains`active`.`000-000``111111113`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`requires_payment_method`with an`account_closed`failure code. The mandate status becomes`inactive`at that point.`000-000``111111116`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`requires_payment_method`with a`no_account`failure code. The mandate status becomes`inactive`at that point.`000-000``222222227`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`requires_payment_method`with a`refer_to_customer`failure code. The mandate status remains`active`.`000-000``922222227`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`requires_payment_method`with a`refer_to_customer`failure code (with a three-minute delay). The mandate status remains`active`.`000-000``333333335`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`requires_payment_method`with a`debit_not_authorized`failure code. The mandate status becomes`inactive`at that point.`000-000``666666660`The PaymentIntent created with the resulting PaymentMethod transitions from`processing`to`succeeded`, but a dispute is immediately created.[OptionalValidate the Australia Bank Account ElementClient-side](#web-validate-element)[OptionalAccepting future paymentsClient-side](#web-future-payments)## See also

- [Accept a BECS Debit payment](/payments/au-becs-debit/accept-a-payment)
- [Connect platforms using the Payment Methods API](/payments/payment-methods/connect)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#web-set-up-stripe)[Create or retrieve a Customer](#web-create-customer)[Create a SetupIntent](#web-create-setup-intent)[Collect payment method details and mandate acknowledgment](#web-collect-payment-method-details)[Submit the payment method details to Stripe](#web-submit-payment-method)[Test the integration](#web-test-integration)[See also](#see-also)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
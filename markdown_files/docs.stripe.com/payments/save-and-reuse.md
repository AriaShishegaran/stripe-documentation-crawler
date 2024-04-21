htmlSet up future payments | Stripe Documentation[Skip to content](#main-content)Set up future payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsave-and-reuse)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsave-and-reuse)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)# Set up future payments

Learn how to save payment details and charge your customers later.CautionSCA regulation requires that you authenticate your customer up front if you intend to collect payments from them again in the future. If the customer never authenticated initially, their bank may decline future payments and ask for additional authentication.

WebiOSAndroidReact NativeNo-codeStripe-hosted pageEmbedded formCustom payment flowTo collect customer payment details that you can reuse later, use Checkout’s setup mode. Setup mode uses the Setup Intents API to create Payment Methods.

Check out our full, working sample on GitHub.

[Set up StripeServer-side](#set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries to access the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`To create a setup mode Session, use the mode parameter with a value of setup when creating the Session. You can optionally specify the customer parameter to automatically attach the created payment method to an existing customer. Checkout uses Dynamic payment methods by default, which requires you to pass the currency parameter when using setup mode.

Append the {CHECKOUT_SESSION_ID} template variable to the success_url to get access to the Session ID after your customer successfully completes a Checkout Session. After creating the Checkout Session, redirect your customer to the URL returned in the response.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=setup \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  --data-urlencode success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  --data-urlencode cancel_url="https://example.com/cancel"`[Retrieve the Checkout SessionServer-side](#retrieve-checkout-session)After a customer successfully completes their Checkout Session, you need to retrieve the Session object. There are two ways to do this:

- Asynchronously: Handle`checkout.session.completed`[webhooks](/webhooks), which contain aSession object. Learn more about[setting up webhooks](/webhooks).
- Synchronously: Obtain the Session ID from the`success_url`when a user redirects back to your site. Use the Session ID to[retrieve](/api/checkout/sessions/retrieve)the Session object.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`The right choice depends on your tolerance for dropoff, as customers may not always reach the success_url after a successful payment. It’s possible for them close their browser tab before the redirect occurs. Handling webhooks prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the setup_intent key, which is the ID for the SetupIntent created during the Checkout Session. A SetupIntent is an object used to set up the customer’s bank account information for future payments.

Example checkout.session.completed payload:

`{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2019-03-14",
  "created": 1561420781,
  "data": {
    "object": {
      "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
      "object": "checkout.session",
      "billing_address_collection": null,
      "cancel_url": "https://example.com/cancel",
      "client_reference_id": null,
      "customer": "",
      "customer_email": null,
      "display_items": [],
      "mode": "setup",
      "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
      "submit_type": null,
      "subscription": null,
      "success_url": "https://example.com/success"
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "checkout.session.completed"
}`Note the setup_intent ID for the next step.

[Retrieve the SetupIntentServer-side](#retrieve-setup-intent)Using the setup_intent ID, retrieve the SetupIntent object. The returned object contains a payment_method ID that you can attach to a customer in the next step.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`NoteIf you’re requesting this information synchronously from the Stripe API (as opposed to handling webhooks), you can combine the previous step with this step by expanding the SetupIntent object in the request to the /v1/checkout/session endpoint. Doing this prevents you from having to make two network requests to access the newly created PaymentMethod ID.

[Use the payment methodServer-side](#use-payment-method)If you didn’t create the Checkout Session with an existing customer, use the payment_method ID to attach the PaymentMethod to a Customer. After you attach the PaymentMethod to a customer, you can charge the PaymentMethod using a PaymentIntent.

[Disclose Stripe to your customers](#disclose-cookies)Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our privacy center.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Create a Checkout Session](#create-checkout-session)[Retrieve the Checkout Session](#retrieve-checkout-session)[Retrieve the SetupIntent](#retrieve-setup-intent)[Use the payment method](#use-payment-method)[Disclose Stripe to your customers](#disclose-cookies)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
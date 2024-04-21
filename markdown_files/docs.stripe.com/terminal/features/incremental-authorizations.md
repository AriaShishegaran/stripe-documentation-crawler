htmlIncremental authorizations | Stripe Documentation[Skip to content](#main-content)Incremental authorizations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fincremental-authorizations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fincremental-authorizations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Incremental authorizations

Increase the authorized amount before capturing a payment.Incremental authorizations allow you to increase the authorized amount on a confirmed PaymentIntent before you capture it. This is helpful if the total price changes or the customer adds goods or services and you need to update the amount on the payment.

Depending on the issuing bank, cardholders might see the amount of the original pending authorization increase in place, or they might see each increment as an additional pending authorization. After capture, the total captured amount appears as one entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- They’re only available with Visa, Mastercard, or Discover.
- Certain card brands have merchant category restrictions (see below).
- You can only increment a transaction made with the POS and reader fully online.
- You have a maximum of 10 attempts per payment.

Availability by card network and merchant category![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the Dashboard.

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

Card brandMerchant countryPayment typeMerchant categoryVisaGlobalAll card payment typesAll user categoriesMastercardGlobal*All card payment typesAll user categoriesDiscoverGlobalAll card payment typesCar rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified)DiscoverGlobalCard not presentTaxicabs and limousines* Excludes MX users and JPY transactions for JP users

### Networks with limited support (beta)

[Request incremental authorization supportServer-sideClient-side](#request-incremental-authorization-support)When you create a PaymentIntent, you can request the ability to capture increments of the payment. Set the request_incremental_authorization_support field to true and the capture_method to manual.

Server-sideiOSAndroidReact NativeCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card_present \
  -d capture_method=manual \
  -d "payment_method_options[card_present][request_incremental_authorization_support]"=true`[Confirm the PaymentIntentClient-side](#confirm-payment-intent)Check the incremental_authorization_supported field in the confirm response to determine if the PaymentIntent is eligible for incremental authorization.

You can only perform incremental authorizations on uncaptured payments after confirmation. To adjust the amount of a payment before confirmation, use the update method instead.

JavaScriptiOSAndroidReact Native`async () => {
  const result = await terminal.processPayment(paymentIntent);
  if (result.error) {
    // Placeholder for handling result.error
  } else if (result.paymentIntent) {
    // Now you're ready to increment the authorization using your backend
  }
}`[Perform an incremental authorizationServer-side](#increment-authorization)To increase the authorized amount on a payment, use the increment_authorization endpoint and provide the updated total amount to increment to, which must be greater than the original authorized amount. This attempts to authorize for the difference between the previous amount and the incremented amount. Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.

A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500`An authorization can either:

- Succeed – Returns the`PaymentIntent`with the updated amount.
- Fail – Returns a[card_declined](/error-codes#card-declined)error, and the`PaymentIntent`remains authorized to capture the original amount. Updates to other`PaymentIntent`fields (for example,[application_fee_amount](/api/payment_intents/increment_authorization#increment_authorization-application_fee_amount)) aren’t saved.

[Capture the PaymentIntentServer-side](#capture-payment-intent)To capture the authorized amount on a PaymentIntent that has prior incremental authorizations, use the capture endpoint. To increase the authorized amount and simultaneously capture that updated amount, provide an updated amount_to_capture.

Providing an amount_to_capture that’s higher than the currently authorized amount results in an automatic incremental authorization attempt.

NoteIf you’re eligible to collect on-receipt tips, using an amount_to_capture that’s higher than the currently authorized amount won’t result in an automatic incremental authorization attempt. Capture requests always succeed.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount_to_capture=2000`The possible outcomes of an incremental authorization attempt are:

- Succeed – Returns the`captured``PaymentIntent`with the updated amount.
- Fail – Returns a[card_declined](/error-codes#card-declined)error, and the`PaymentIntent`remains authorized to capture the original amount. Updates to other`PaymentIntent`fields (for example,[application_fee_amount](/api/payment_intents/capture#capture_payment_intent-application_fee_amount)) aren’t saved.

Regardless, when using amount_to_capture we recommend that you always check for potential failures.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Request incremental authorization support](#request-incremental-authorization-support)[Confirm the PaymentIntent](#confirm-payment-intent)[Perform an incremental authorization](#increment-authorization)[Capture the PaymentIntent](#capture-payment-intent)Products Used[Terminal](/terminal)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
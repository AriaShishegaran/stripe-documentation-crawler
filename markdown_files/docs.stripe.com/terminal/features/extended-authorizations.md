htmlExtended authorizations | Stripe Documentation[Skip to content](#main-content)Extended authorizations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fextended-authorizations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fextended-authorizations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Extended authorizations

Capture a confirmed Stripe Terminal payment later.Extended authorizations allow you to capture a confirmed PaymentIntent up to 31 days later, depending on the card brand and whether your business is in an eligible category. This is helpful if you need more than 48 hours between authorization and payment capture. For example, a hotel authorizes a payment in full when a guest checks in, but captures the payment when the guest checks out.

## Availability

Extended authorization is available on Visa, Mastercard, American Express and Discover. Extended authorizations are not supported on single-message payment methods like Interac and eftpos.

NoteYou can contact support if you’re unsure about the eligibility of your merchant business category. If you’re a Connect user, set the merchant category code for your connected accounts to match their businesses.

## Request extended authorization support

When you create a PaymentIntent, you can request to extend the capture window of the payment. Set the request_extended_authorization field to true and the capture_method to manual.

Server-sideiOSAndroidReact NativeCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card_present \
  -d capture_method=manual \
  -d "payment_method_options[card_present][request_extended_authorization]"=true`In the response, the capture_before field indicates the time when the authorization expires. Failure to capture the payment by this time cancels the authorization and releases the funds. When this happens, the PaymentIntent status transitions to canceled.

## Authorization validity

Every card network and card brand has a different rule for how long an authorization is valid. With Terminal, an authorization for in-person payments is valid for at least two days. Because authorization rules can change without prior notice, use the capture_before field to determine the validity window for an authorization.

NoteThe capture_before field is located on the Charge, so it is only present after the PaymentIntent is confirmed.

Card brandMerchant categoryExtended authorization validity windowVisaHotel, lodging, vehicle rental, and cruise line30 days*Mastercard(not including Maestro and Cirrus cards)All merchant categories30 daysAmerican ExpressLodging and vehicle rental30 days**DiscoverAirline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway30 days* The specific extended authorization window for Visa is 29 days and 18 hours to allow time for clearing processes.** While your validity window is extended to 30 days, you must capture the authorized funds no later than the end of the duration of your customer’s stay or rental.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Request extended authorization support](#request-extended-authorization-support)[Authorization validity](#authorization-validity)Products Used[Terminal](/terminal)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
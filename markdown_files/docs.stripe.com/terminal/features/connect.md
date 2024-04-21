htmlUse Terminal with Connect | Stripe Documentation[Skip to content](#main-content)Multiparty payments with Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Use Terminal with Connect

Integrate Stripe Terminal with your Connect platform.Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

Stripe Terminal is fully compatible with Connect, enabling your platform or marketplace to accept in-person payments.

The way Terminal creates API objects depends on whether you use direct charges or destination charges. If you use direct charges, all Terminal API objects belong to connected accounts. If you use destination charges, all Terminal API objects are created on your platform account. In both cases, use Locations to group readers as you see fit.

NoteTerminal Connect Accounts must have the card_payments capability to perform transactions.

## Direct charges

With direct charges, API objects belong to the connected account rather than the platform. The connected account is responsible for the cost of Stripe fees, refunds, and chargebacks.

In the Dashboard, you can view your Terminal data by logging in as the connected account.

### Create locations and readers Server-side

With direct charges, you must create payment objects that belong to the connected account. You must create other Terminal API objects like Locations and Readers that belong to the same connected account.

To create a Location belonging to a connected account, use the Stripe-Account header.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d display_name=HQ \
  -d "address[line1]"="1272 Valencia Street" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"=CA \
  -d "address[country]"=US \
  -d "address[postal_code]"=94110`Before you can connect your application to a smart reader, you must register the reader to a Stripe account. To register a reader to a connected account, use the Stripe-Account header.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d registration_code={{READER_REGISTRATION_CODE}} \
  --data-urlencode label="Alice's reader" \
  -d location={{LOCATION_ID}}`### Create connection tokens Server-side

NoteWhen using Connect OAuth authentication, the connected account needs to be authorized for live mode and test mode separately, using the respective application Client ID for each mode.

When creating a ConnectionToken for the Terminal SDK, set the Stripe-Account header to the connected account accepting payments. You may also provide a location parameter to control access to readers. If you provide a location, the ConnectionToken is only usable with readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/connection_tokens \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d location={{LOCATION_ID}}`### Create PaymentIntents Client-side Server-side

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent on the client or server. The JavaScript SDK only supports server-side creation.

Client-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When creating a PaymentIntent client-side for direct charges, you don’t need to specify any additional parameters for the PaymentIntent. Instead, when creating a ConnectionToken, set the Stripe-Account header to the connected account accepting payments. The iOS, Android, and React Native SDKs create the PaymentIntent on the same connected account the ConnectionToken belongs to. For more information, see Create Payment Intents Client-side.

Server-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The JavaScript SDK requires you to create the PaymentIntent on your server. For iOS or Android, you might want to create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app. For more information, see Create Payment Intents Server-side.

When creating a PaymentIntent server-side for direct charges, set the Stripe-Account header to the connected account.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card_present \
  -d capture_method=manual`## Destination charges

When using destination charges, API objects like Payment Intents and Locations belong to your platform account. Each payment creates a transfer to a connected account automatically.

In the Dashboard, you can view your Terminal data directly when logged into your platform account.

### Create locations and readers Server-side

The best way to group Reader objects by connected account is by assigning them to Locations. On your platform account, create a Location for a connected account using a display name that identifies the account.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d display_name=HQ \
  -d "address[line1]"="1272 Valencia Street" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"=CA \
  -d "address[country]"=US \
  -d "address[postal_code]"=94110`Before you can connect your application to a smart reader, you must register the reader to your platform account.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d registration_code={{READER_REGISTRATION_CODE}} \
  --data-urlencode label="Alice's reader" \
  -d location={{LOCATION_ID}}`### Create connection tokens Server-side

When creating a ConnectionToken for the Terminal SDK, use your platform account’s secret key. Don’t set the Stripe-Account header. Provide a location parameter to control access to readers. If you provide a location, the ConnectionToken is only usable with readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/connection_tokens \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d location={{LOCATION_ID}}`### Create PaymentIntents Client-side Server-side

When creating a PaymentIntent using destination charges, provide the on_behalf_of and transfer_data[destination], and application_fee_amount parameters.

The on_behalf_of parameter is the ID of the connected account that will become the settlement merchant for the payment.  For Terminal transactions, this parameter must be set in cases where the platform country isn’t the same as the Connect account country. When on_behalf_of is set, Stripe automatically:

- Settles charges in the country of the specified account, thereby minimizing declines and avoiding currency conversions.
- Uses the fee structure for the connected account’s country.
- Lists the connected account’s address and phone number on the customer’s credit card statement, as opposed to the platform’s address and phone number (only occurs if the account and platform are in different countries).

For transfer_data[destination], set the ID of the connected account that receives the transfer.

Finally, you may withhold an application fee for your platform by providing the application_fee_amount parameter.

Client-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent client-side and provide the onBehalfOf, transferDataDestination, and applicationFeeAmount parameters.

JavaScriptiOSAndroidReact NativeNoteClient-side PaymentIntent creation is possible with the iOS or Android SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a PaymentIntent server-side.

Server-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The JavaScript SDK requires you to create the PaymentIntent on your server. For iOS or Android, you want to create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app. For more information, see Create Payment Intents Server-side.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card_present \
  -d capture_method=manual \
  -d application_fee_amount=200 \
  -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`## See also

- [Cart display](/terminal/features/display)
- [Receipts](/terminal/features/receipts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Direct charges](#direct)[Destination charges](#destination)[See also](#see-also)Products Used[Terminal](/terminal)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
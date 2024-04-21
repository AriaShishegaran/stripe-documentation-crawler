htmlSet statement descriptors with Connect | Stripe Documentation[Skip to content](#main-content)Set statement descriptors[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fstatement-descriptors)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fstatement-descriptors)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Set statement descriptors with Connect

Learn how statement descriptors work for charges with Connect.Statement descriptors explain charges or payments on bank statements and include information that banks and card networks require to help customers understand their statements. Familiarize yourself with the requirements for statement descriptors.

## Set the static component for a connected account

Statement descriptors contain a static component and, optionally, a dynamic part. The static component refers to either:

- The entire statement descriptor is static ([settings.payments.statement_descriptor](/api/accounts/object#account_object-settings-payments-statement_descriptor)).
- The first half of the statement descriptor is static ([settings.card_payments.statement_descriptor_prefix](/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)) and the second half is dynamically set from the payment.

Your platform and connected accounts with the card_payments capability must have a statement descriptor and, optionally, a statement descriptor prefix. Both values must be at least 5 characters in length. For a given payment, the statement descriptor of the platform or the connected account applies depending on the charge type.

The statement descriptor is set in one of the following ways:

- With a[create or update account](/api/accounts)API call
- During Stripe-hosted or embedded onboarding
- Through the full Stripe Dashboard or Express Dashboard

Connected accounts with access to the full Stripe Dashboard or Express Dashboard can update their own statement descriptor settings.

You can prefill an account’s statement descriptor and prefix when you call the create account endpoint. During Stripe-hosted or embedded onboarding, If settings.payments.statement_descriptor or settings.card_payments.statement_descriptor_prefix isn’t set, Stripe sets them based on information provided about the account during onboarding. If sufficient information isn’t available, Stripe prompts connected accounts to set their own statement descriptors during onboarding.

After onboarding an account that doesn’t have access to the full Stripe Dashboard, you can update its settings.payments.statement_descriptor and settings.card_payments.statement_descriptor_prefix by calling the update account endpoint.

For accounts where the platform handles onboarding, you must set their statement descriptor.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=custom \
  -d country=US \
  -d business_type=company \
  -d "business_profile[name]"="Runners Club" \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "settings[payments][statement_descriptor]"="RUNNERS CLUB"`As of API version 2023-10-16, there is new logic around updating statement descriptors.

- If you update an account’s`business_profile.name`,`business_profile.url`, or the name of the company or individual and the existing statement descriptor is based on lower precedence data, Stripe automatically resets the statement descriptor to match the higher precedence value. For example, if the statement descriptor is automatically set based on the URL, then you set or update`business_profile.name`, Stripe resets the statement descriptor to match the business profile name. If the statement descriptor is automatically set based on`business_profile.name`, and you set or update the name of the company or individual, the statement descriptor doesn’t reset because`business_profile.name`has higher precedence. The precedence order is`business_profile.name`,`business_profile.url`, then the name of the company or individual.
- Any update to an account’s full statement descriptor causes Stripe to automatically set the statement descriptor prefix to a shortened version of the updated statement descriptor, even if the previous prefix is manually set.

## Statement descriptor usage

The full statement descriptor is provided to the bank or card network processing the payment. Only the first 22 characters of the full statement descriptor are sent for card payments.

The customer’s statement uses the connected account’s static component for the following charge types:

- Direct charges
- Destination charges with`on_behalf_of`
- Separate charges and transfers with`on_behalf_of`

CautionThe platform provides the static component for /v1/charges requests with on_behalf_of for API versions before 2019-02-19.

Using the static component on connected accounts requires the card_payments capability.

The customer’s statement uses the platform account’s static component for the following charge types:

- Destination charges without`on_behalf_of`
- Separate charges and transfers without`on_behalf_of`

Any additional information that’s displayed on a customer’s statement is also provided by the account that provides the static component (for example, support address or support phone number). If the connected account hasn’t provided this information, on_behalf_of charges use the platform account’s information.

If you use a dynamic suffix on a charge that uses the connected account’s static descriptor, you can set a prefix to ensure the complete statement descriptor appears as intended.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=custom \
  -d country=US \
  -d business_type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "settings[card_payments][statement_descriptor_prefix]"=RUNCLUB`The static prefix must contain between 2 and 10 characters, inclusive. Card networks receive only the first 22 characters (including the * symbol and the space that concatenates the static prefix and dynamic suffix) of the complete statement descriptor.

Set the statement_descriptor and statement_descriptor_prefix for flexibility in setting statement descriptors on charges.

If the statement descriptor is set on card charges and no prefix is set, Stripe truncates the account statement descriptor as needed to set the prefix value.

## Set a dynamic suffix for connected account charges

Dynamic suffixes are supported only for card charges by using the statement_descriptor_suffix parameter. You can read more about dynamic suffixes or see the concatenated statement descriptors (prefix* suffix) in the Dashboard.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d statement_descriptor_suffix="Custom suffix"`## Set Japanese statement descriptors

We recommend setting the static components of kanji and kana statement descriptors for Japanese connected accounts.

You can set all descriptors and their corresponding prefixes when creating a Japanese Custom connected account as follows:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=custom \
  -d country=JP \
  -d business_type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "settings[card_payments][statement_descriptor_prefix]"="example prefix" \
  -d "settings[card_payments][statement_descriptor_prefix_kanji]"="漢字プリフィックス" \
  -d "settings[card_payments][statement_descriptor_prefix_kana]"="カナプリフィックス" \
  -d "settings[payments][statement_descriptor]"="example descriptor" \
  -d "settings[payments][statement_descriptor_kanji]"="漢字明細" \
  -d "settings[payments][statement_descriptor_kana]"="カナメイサイ"`You can set dynamic kanji and kana suffixes when creating card charges with payment_method_options[card][statement_descriptor_suffix_kanji] and payment_method_options[card][statement_descriptor_suffix_kana].

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=jpy \
  -d "payment_method_types[]"=card \
  -d statement_descriptor_suffix="example descriptor" \
  -d "payment_method_options[card][statement_descriptor_suffix_kanji]"="漢字サフィックス" \
  -d "payment_method_options[card][statement_descriptor_suffix_kana]"="カナサフィックス"`See Japanese statement descriptors for more details.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set the static component for a connected account](#set-the-static-component-for-a-connected-account)[Statement descriptor usage](#statement-descriptor-usage)[Set a dynamic suffix for connected account charges](#dynamic-descriptors)[Set Japanese statement descriptors](#set-japanese-statement-descriptors)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
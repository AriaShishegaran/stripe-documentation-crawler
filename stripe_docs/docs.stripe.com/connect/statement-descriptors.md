# Set statement descriptors with Connect

Statement descriptors explain charges or payments on bank statements and include information that banks and card networks require to help customers understand their statements. Familiarize yourself with the requirements for statement descriptors.

[requirements for statement descriptors](/get-started/account/statement-descriptors)

## Set the static component for a connected account

Statement descriptors contain a static component and, optionally, a dynamic part. The static component refers to either:

- The entire statement descriptor is static (settings.payments.statement_descriptor).

[settings.payments.statement_descriptor](/api/accounts/object#account_object-settings-payments-statement_descriptor)

- The first half of the statement descriptor is static (settings.card_payments.statement_descriptor_prefix) and the second half is dynamically set from the payment.

[settings.card_payments.statement_descriptor_prefix](/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)

Your platform and connected accounts with the card_payments capability must have a statement descriptor and, optionally, a statement descriptor prefix. Both values must be at least 5 characters in length. For a given payment, the statement descriptor of the platform or the connected account applies depending on the charge type.

[the charge type](/connect/charges)

The statement descriptor is set in one of the following ways:

- With a create or update account API call

[create or update account](/api/accounts)

- During Stripe-hosted or embedded onboarding

- Through the full Stripe Dashboard or Express Dashboard

Connected accounts with access to the full Stripe Dashboard or Express Dashboard can update their own statement descriptor settings.

You can prefill an account’s statement descriptor and prefix when you call the create account endpoint. During Stripe-hosted or embedded onboarding, If settings.payments.statement_descriptor or settings.card_payments.statement_descriptor_prefix isn’t set, Stripe sets them based on information provided about the account during onboarding. If sufficient information isn’t available, Stripe prompts connected accounts to set their own statement descriptors during onboarding.

[create account](/api/accounts/create)

After onboarding an account that doesn’t have access to the full Stripe Dashboard, you can update its settings.payments.statement_descriptor and settings.card_payments.statement_descriptor_prefix by calling the update account endpoint.

[update account](/api/accounts/update)

For accounts where the platform handles onboarding, you must set their statement descriptor.

As of API version 2023-10-16, there is new logic around updating statement descriptors.

[API version 2023-10-16](/upgrades#2023-10-16)

- If you update an account’s business_profile.name, business_profile.url, or the name of the company or individual and the existing statement descriptor is based on lower precedence data, Stripe automatically resets the statement descriptor to match the higher precedence value. For example, if the statement descriptor is automatically set based on the URL, then you set or update  business_profile.name, Stripe resets the statement descriptor to match the business profile name. If the statement descriptor is automatically set based on business_profile.name, and you set or update the name of the company or individual, the statement descriptor doesn’t reset because business_profile.name has higher precedence. The precedence order is business_profile.name, business_profile.url, then the name of the company or individual.

- Any update to an account’s full statement descriptor causes Stripe to automatically set the statement descriptor prefix to a shortened version of the updated statement descriptor, even if the previous prefix is manually set.

## Statement descriptor usage

The full statement descriptor is provided to the bank or card network processing the payment. Only the first 22 characters of the full statement descriptor are sent for card payments.

The customer’s statement uses the connected account’s static component for the following charge types:

- Direct charges

- Destination charges with on_behalf_of

- Separate charges and transfers with on_behalf_of

The platform provides the static component for /v1/charges requests with on_behalf_of for API versions before 2019-02-19.

Using the static component on connected accounts requires the card_payments capability.

[card_payments](/connect/account-capabilities#card-payments)

The customer’s statement uses the platform account’s static component for the following charge types:

- Destination charges without on_behalf_of

- Separate charges and transfers without on_behalf_of

Any additional information that’s displayed on a customer’s statement is also provided by the account that provides the static component (for example, support address or support phone number). If the connected account hasn’t provided this information, on_behalf_of charges use the platform account’s information.

If you use a dynamic suffix on a charge that uses the connected account’s static descriptor, you can set a prefix to ensure the complete statement descriptor appears as intended.

The static prefix must contain between 2 and 10 characters, inclusive. Card networks receive only the first 22 characters (including the * symbol and the space that concatenates the static prefix and dynamic suffix) of the complete statement descriptor.

Set the statement_descriptor and statement_descriptor_prefix for flexibility in setting statement descriptors on charges.

If the statement descriptor is set on card charges and no prefix is set, Stripe truncates the account statement descriptor as needed to set the prefix value.

## Set a dynamic suffix for connected account charges

Dynamic suffixes are supported only for card charges by using the statement_descriptor_suffix parameter. You can read more about dynamic suffixes or see the concatenated statement descriptors (prefix* suffix) in the Dashboard.

[dynamic suffixes](/get-started/account/statement-descriptors#dynamic)

[Dashboard](https://dashboard.stripe.com/settings/public)

## Set Japanese statement descriptors

We recommend setting the static components of kanji and kana statement descriptors for Japanese connected accounts.

You can set all descriptors and their corresponding prefixes when creating a Japanese Custom connected account as follows:

You can set dynamic kanji and kana suffixes when creating card charges with payment_method_options[card][statement_descriptor_suffix_kanji] and payment_method_options[card][statement_descriptor_suffix_kana].

See Japanese statement descriptors for more details.

[Japanese statement descriptors](/get-started/account/statement-descriptors#set-japanese-statement-descriptors)

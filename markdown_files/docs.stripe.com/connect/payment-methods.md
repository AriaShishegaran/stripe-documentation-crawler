htmlAdding payment method capabilities | Stripe Documentation[Skip to content](#main-content)Payment methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Account capabilities](/docs/connect/account-capabilities)# Adding payment method capabilities

Onboard your connected accounts to accept different payment methods.This guide provides an overview for existing platforms on how to check the eligibility of connected accounts to accept different payment methods and apply capabilities to those accounts using the Dashboard.

[Navigate to the Connected Account Payment Method Settings Page](#goto-settings-page)To navigate to the settings page of the Payment methods for your connected accounts, do the following:

1. From the Dashboard, in the upper right corner, select Settings > Connect > Payment Methods.


2. Under Your connected accounts, select Edit Settings.



Result: You can now manage the types of payment methods that users of your connected account can accept.

[View eligibility](#view-eligibility)From the connected accounts Payment methods settings, navigate to the payment method you’re interested in.

Use the arrow on the left side of the payment method to expand the details of the payment method. Within this view, you can see the eligibility of each of your connected accounts to use the payment method.

NoteThis view includes connected accounts that:

- Have processed a payment in the last 90 days and are older than 30 days.
- Are less than 30 days old, regardless of their payment activity.

It excludes Standard accounts that are not controlled by a single platform.

![Eligibility details for a payment method](https://b.stripecdn.com/docs-statics-srv/assets/eligibility-results.088e99a8299c21267b07a7b1ba1bd7d6.png)

Eligibility details for a payment method

Each connected account appears in one of four different categories:

CategoryDescriptionEnabledThese businesses already have the capability for this payment method set to`active`.EligibleThese businesses have met all compliance requirements and passed any relevant MCC checks to have the payment method capability set to`active`when requested.Missing InfoThese businesses are missing some compliance plan information needed to add the payment method.IneligibleThese businesses aren’t eligible for the payment method, either due to country location or MCC.Countries you have connected accounts in that aren’t supported by the payment method appear grayed out.

[Enable payment method](#enable-payment-method)To enable the payment method for your connected accounts:

1. Apply the[capability](/connect/account-capabilities)to your connected accounts by selectingOn by defaultfrom the top-level dropdown located to the right of the payment method.
2. (Optional)Edit the setting to`Off`for any countries where you want to disable the payment method.
3. SelectReview Changesto confirm your selections.

After you review and confirm your update, Stripe converts all Eligible connected accounts to Enabled, with a capability status of active. Stripe also automatically applies the capability to new accounts as they become eligible. This could happen because a new account signs up for your platform and finishes inputting their information or because an account updates their information to become eligible for the payment method, such as updating their MCC from one that’s ineligible to one that’s eligible.

![The button to review changes](https://b.stripecdn.com/docs-statics-srv/assets/review-changes.d8ab55ad8f1d32cf8502520366aa6de8.png)

Review changes

BetaThe embedded payment method settings component allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.

[Gather required information](#gather-information)Stripe doesn’t apply an enabled payment method to any accounts in the Missing Info category. After you  update the account to provide the specific missing information for those accounts, Stripe applies the capability.

[OptionalExport list](#export-list)## See also

- [Account capabilities](/connect/account-capabilities)
- [Country availability for payment methods](/connect/payment-method-available-countries)
- [Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Navigate to the Connected Account Payment Method Settings Page](#goto-settings-page)[View eligibility](#view-eligibility)[Enable payment method](#enable-payment-method)[Gather required information](#gather-information)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
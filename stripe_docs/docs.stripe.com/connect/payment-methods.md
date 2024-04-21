# Adding payment method capabilities

This guide provides an overview for existing platforms on how to check the eligibility of connected accounts to accept different payment methods and apply capabilities to those accounts using the Dashboard.

[capabilities](/connect/account-capabilities)

[Navigate to the Connected Account Payment Method Settings Page](#goto-settings-page)

## Navigate to the Connected Account Payment Method Settings Page

To navigate to the settings page of the Payment methods for your connected accounts, do the following:

- From the Dashboard, in the upper right corner, select Settings > Connect > Payment Methods.

From the Dashboard, in the upper right corner, select Settings > Connect > Payment Methods.

[Dashboard](https://dashboard.stripe.com/dashboard)

[Settings](https://dashboard.stripe.com/settings)

[Connect](https://dashboard.stripe.com/settings/connect)

[Payment Methods](https://dashboard.stripe.com/settings/connect/payment_methods)

- Under Your connected accounts, select Edit Settings.

Under Your connected accounts, select Edit Settings.

[Your connected accounts](https://dashboard.stripe.com/settings/extensions/payment_methods)

[Edit Settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)

Result: You can now manage the types of payment methods that users of your connected account can accept.

[View eligibility](#view-eligibility)

## View eligibility

From the connected accounts Payment methods settings, navigate to the payment method you’re interested in.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Use the arrow on the left side of the payment method to expand the details of the payment method. Within this view, you can see the eligibility of each of your connected accounts to use the payment method.

This view includes connected accounts that:

- Have processed a payment in the last 90 days and are older than 30 days.

- Are less than 30 days old, regardless of their payment activity.

It excludes Standard accounts that are not controlled by a single platform.

Eligibility details for a payment method

Each connected account appears in one of four different categories:

Countries you have connected accounts in that aren’t supported by the payment method appear grayed out.

[Enable payment method](#enable-payment-method)

## Enable payment method

To enable the payment method for your connected accounts:

- Apply the capability to your connected accounts by selecting On by default from the top-level dropdown located to the right of the payment method.

[capability](/connect/account-capabilities)

- (Optional) Edit the setting to Off for any countries where you want to disable the payment method.

- Select Review Changes to confirm your selections.

After you review and confirm your update, Stripe converts all Eligible connected accounts to Enabled, with a capability status of active. Stripe also automatically applies the capability to new accounts as they become eligible. This could happen because a new account signs up for your platform and finishes inputting their information or because an account updates their information to become eligible for the payment method, such as updating their MCC from one that’s ineligible to one that’s eligible.

Review changes

The embedded payment method settings component allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.

[Request access](/connect/supported-embedded-components/payment-method-settings#request-access)

[integrate with Payment Method Configurations](/connect/supported-embedded-components/payment-method-settings#integration)

[Gather required information](#gather-information)

## Gather required information

Stripe doesn’t apply an enabled payment method to any accounts in the Missing Info category. After you  update the account to provide the specific missing information for those accounts, Stripe applies the capability.

[update](/connect/update-verified-information)

[OptionalExport list](#export-list)

## OptionalExport list

## See also

- Account capabilities

[Account capabilities](/connect/account-capabilities)

- Country availability for payment methods

[Country availability for payment methods](/connect/payment-method-available-countries)

- Upgrading to dynamic payment methods

[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

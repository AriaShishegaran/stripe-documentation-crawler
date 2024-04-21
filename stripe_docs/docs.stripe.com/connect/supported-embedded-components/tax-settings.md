# Tax settingsBeta

This Connect embedded component is in beta. Request access below.

[Request access](#request-access)

The Tax settings component allows your connected accounts to set up Stripe Tax in your platform. Connected accounts can change their head office address and preset tax code with this component. This component is suitable for software platforms, which means that your connected accounts are liable to collect taxes.

[set up Stripe Tax](/tax/set-up)

[preset tax code](/tax/products-prices-tax-codes-tax-behavior#product-tax-code)

[software platforms](/tax/connect#tax-for-software-platforms)

To calculate taxes on payments of your connected accounts you have to collect four data points of information:

- The head office address

- The type of product the connected account sells

- The address of the customer

- The registrations of the connected account with the tax authorities

The tax settings component helps you to collect the first two pieces of information of your connected accounts with minimal integration effort.

The embedded tax settings component uses the Tax Settings API to display the head office address and preset tax code to your connected accounts.

[Tax Settings API](/tax/settings-api)

[preset tax code](/tax/products-prices-tax-codes-tax-behavior#product-tax-code)

## Requirements

- Your integration must follow the software platforms guide for Tax on Connect. This means that your connected accounts are liable to collect taxes.

[software platforms guide](/tax/tax-for-platforms)

[Tax on Connect](/tax/connect)

- After integrating the Tax settings component, render the Tax registrations component to collect tax registration information of your connected accounts. This is a requirement for Tax to calculate tax in a specific location.

[Tax registrations component](/connect/supported-embedded-components/tax-registrations)

## Integrate the tax settings component

When creating an Account Session, enable tax settings by specifying tax_settings in the components parameter.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the tax settings component in the frontend:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

## Request early access  Beta

[privacy policy](https://stripe.com/privacy)

## See also

- Tax on Connect

[Tax on Connect](/tax/connect)

- Tax for software platforms

[Tax for software platforms](/tax/tax-for-platforms)

- Tax registrations component

[Tax registrations component](/connect/supported-embedded-components/tax-registrations)

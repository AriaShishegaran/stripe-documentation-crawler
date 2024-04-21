# Tax registrationsBeta

This Connect embedded component is in beta. Request access below.

[Request access](#request-access)

The Tax registrations component gives your connected accounts control over their tax compliance. Your connected accounts interact with this component by managing their tax registrations directly in your platform. This component is suitable for software platforms, which means that your connected accounts are liable to collect taxes.

[software platforms](/tax/tax-for-platforms)

If you’re a platform integrating Stripe Tax, you must collect information about the registrations with tax authorities of your connected accounts in the applicable jurisdictions. Your connected accounts need to register with their tax authorities before they add their tax registrations in your platform. To correctly calculate and collect taxes for your platform, you must collect the tax registrations of your connected accounts.

[registrations with tax authorities](/tax/registering)

The Tax registrations component uses the Tax Registrations API to display a list of tax registrations to your connected accounts. To calculate tax on their payments in a location, connected accounts need to add their tax registration with the Tax registrations component. If the connected account wish to stop calculating tax in a certain location, they can end the tax registration in the component.

[Tax Registrations API](/tax/registrations-api)

## Requirements

- Your integration must follow the software platforms guide for Tax on Connect. This means that your connected accounts are liable to collect taxes.

[software platforms guide](/tax/tax-for-platforms)

[Tax on Connect](/tax/connect)

- If you haven’t already, render the Tax settings component. You need both the Tax settings component and the Tax registrations component to provide tax compliance control to your connected accounts.

[Tax settings component](/connect/supported-embedded-components/tax-settings)

## Integrate the tax registrations component

When creating an Account Session, enable tax registrations by specifying tax_registrations in the components parameter.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the tax registrations component in the frontend:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

## Request early access  Beta

[privacy policy](https://stripe.com/privacy)

## See also

- Tax on Connect

[Tax on Connect](/tax/connect)

- Tax for software platforms

[Tax for software platforms](/tax/tax-for-platforms)

- Tax settings component

[Tax settings component](/connect/supported-embedded-components/tax-settings)

# Accounting software integrationsBeta

Let your users automatically synchronize their transactions, fees, refunds, payouts, customers, and products with their accounting software.

[Integrate with Connect embedded components](#undefined)

## Integrate with Connect embedded components

Set up Connect.js to enable the ability to add connected account dashboard functionality to your website.

[Set up Connect.js](/connect/get-started-connect-embedded-components#account-sessions)

[Select the app to integrate](#app-select)

## Select the app to integrate

Stripe supports the following accounting app integrations.

[Set up app installation](#app-install)

## Set up app installation

Render the app install embedded component for your selected accounting app. App installation grants permission for the third party app to access your users’ Stripe data, creating a connection between your platform, Stripe, and the third party app. The component has two states: uninstalled and installed. Listen to install event triggers to build your custom UX flow or make updates in your own backend.

When creating an Account Session, enable payments by specifying app_onboarding, app_install, and app_settings in the components parameter.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the app_install component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

This embedded component supports the following parameters:

[here](/stripe-apps/accounting-software-integrations#app-select)

[Set up app settings](#app-settings)

## Set up app settings

Render the app settings embedded component for your selected accounting app to enable core app functionality including connection to the accounting software account with OAuth, onboarding, settings, and configuration of the service and synchronization states of transactions. Pass the user_id (business represented on your platform) as an optional HTML attribute that third party apps can use to build a dynamic URL that redirects back to your user dashboard after OAuth.

This component supports the following optional attributes:

[Customize for Connect Destination OBO](#destination-obo)

## Customize for Connect Destination OBO

Pass required and optional transaction data to Xero or QuickBooks Sync by Acodei by updating the destination charge on the connected account using the data standardized data schema below. You must pass a customer object to the destination charge. QuickBooks Sync by Acodei also requires charge updates with refund amounts written to metadata. There are three instances that require you to update your destination charge:

[customer](/api/customers/object)

- one-time payment complete

- recurring payment complete

- payment refunded

[charges.customer](/api/charges/object#charge_object-customer)

[customer.name](/api/customers/object#customer_object-name)

[customer.email](/api/customers/object#customer_object-email)

[customer.address.<>](/api/customers/object#customer_object-address)

[charges.amount_refunded](/api/charges/object#charge_object-amount_refunded)

The following code snippet example traverses to the target destination charge and shows how to update per schema.

- Trace from the Transaction to the destination charge

- Create a customer and then update the charge with the relevant customer ID and metadata. The customer must belong to the connected account and not the platform for the data to pass and apps to synchronize.

[Direct charges](#direct-charges)

## Direct charges

The embedded accounting integrations accesses all payment, customer, and product data stored with Stripe. You can pass optional platform-specific data to the accounting software through the App using the below metadata schema.

## User billing

The Xero App is free for the platforms’ users. The QuickBooks Sync by Acodei includes free and paid tiers.

## Other integrations

If you need an integration with other accounting software or any other integration types, reach out at stripe-apps@stripe.com.

[privacy policy](https://stripe.com/privacy)

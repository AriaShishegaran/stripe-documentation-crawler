htmlAccounts and contacts | Stripe Documentation[Skip to content](#main-content)Accounts and contacts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-cpq%2Faccounts-contacts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-cpq%2Faccounts-contacts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Stripe Billing for Salesforce CPQ](/docs/connectors/salesforce-cpq/overview)# Accounts and contacts

Learn about syncing the Stripe customer objects for your corresponding Salesforce accounts.After you set up the Stripe Billing Connector for Salesforce CPQ and map your data, Stripe creates a Customer object when an order finalizes. This happens when you associate an account and a primary contact with a quote from an activated order.

If you use a parent-child hierarchy for your Salesforce accounts, make sure that only the account that represents the billing entity (customer) correlates to an activated order. Stripe Billing doesn’t currently support separate billing and provisioning entities for subscriptions.

## Field mappings for Stripe customers

When you configure the connector to create a Stripe Customer object for each Salesforce account, there isn’t a default mapping to a primary contact or order on the account. All customer fields are also optional.

The connector syncs a Salesforce account’s Name and Description fields to Stripe. To sync additional fields, you can add field mappings to customize the data that’s synced from Salesforce to Stripe.

Salesforce field (Account object)Stripe customerNotesName[Name](/api/customers/object#customer_object-name)Phone[Phone](/api/customers/object#customer_object-phone)Description[Description](/api/customers/object#customer_object-description)[Email](/api/customers/object#customer_object-email)By default, the`Account`object in Salesforce doesn’t have an email field. You can create a subscription without a payment; however, you must supply an email address for collections.Billing street[Address, line 1](/api/customers/object#customer_object-address-line1)This address might affect the customer’s tax calculation, depending on your tax configuration. If the address is incomplete or differs from the billing address on the quote or order, you must provide a custom mapping for this data.Billing city[Address, city](/api/customers/object#customer_object-address-city)Billing state[Address, state](/api/customers/object#customer_object-address-state)Billing postal code[Address, postal code](/api/customers/object#customer_object-address-postal_code)Billing country[Address, country](/api/customers/object#customer_object-address-country)Phone[Shipping, address, phone](/api/customers/object#customer_object-phone)Shipping street[Shipping, address, line 1](/api/customers/object#customer_object-shipping-address-line1)Shipping city[Shipping, address, city](/api/customers/object#customer_object-shipping-address-city)Shipping state[Shipping, address, state](/api/customers/object#customer_object-shipping-address-state)Shipping postal code[Shipping, address, postal code](/api/customers/object#customer_object-shipping-address-postal_code)Shipping country[Shipping, address, country](/api/customers/object#customer_object-shipping-address-country)## Update account data

Account and contact information sync in real time. When you create or update accounts in Salesforce, the connector creates and updates the Stripe Customer objects with the latest information from Salesforce when an order syncs. Because Salesforce is the primary source for account and contact information, any updates you make to a Customer object in Stripe aren’t synced to the corresponding account in Salesforce.

Stripe doesn’t allow merging of accounts. If you want to merge any customers in Salesforce, you must do so before you sync the account to Stripe. Customer objects synced to Stripe must have a valid ID in the Stripe ID field on the account.

## Delete accounts

Deleting accounts or account information in Salesforce won’t affect the data in Stripe. Any subscriptions in Stripe continue to bill and operate as normal. You can’t delete Salesforce accounts with active subscriptions.

Deleting a customer in Stripe is irreversible, cancels all subscriptions, and deletes any saved payment methods. The best practice is to retain the customer unless you created it accidentally.

## Merge accounts

Salesforce allows you to merge up to three Salesforce accounts. Merging deletes the dependent Salesforce accounts, and their dependent Salesforce records become the primary Salesforce account’s records.

The connector doesn’t sync these changes into Stripe. Any Stripe subscriptions that belong to the deleted Salesforce account still belong to the original Stripe customer that corresponds to the deleted Salesforce account.

NoteThe child account is the account that’s merged into the primary account.

## See also

- [Field defaults and custom mappings](/connectors/salesforce-cpq/field-mappings)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Field mappings for Stripe customers](#customer-field-mappings)[Update account data](#update-accounts)[Delete accounts](#delete-accounts)[Merge accounts](#merge-accounts)[See also](#see-also)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
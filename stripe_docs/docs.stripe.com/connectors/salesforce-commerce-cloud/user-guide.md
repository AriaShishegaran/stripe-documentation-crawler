# Stripe Salesforce Commerce Cloud Cartridge user guide

## Merchant roles and responsibilities

As soon as configurations and job schedules are set up, the functionality runs on demand—the merchant doesn’t need to perform any ongoing maintenance or other tasks.

## Business Manager

Business Manager settings and configuration notes are described in detail in the implementation guide.

[implementation guide](/connectors/salesforce-commerce-cloud/implementation-guide)

The cartridge comes with two jobs:

- Stripe - Delete Custom Objects

- Stripe - Process Webhook Notifications

Enable the Stripe - Process Webhook Notifications job for the desired site:

## Storefront functionality

When an authenticated customer selects a saved credit card on the payment page, they can see a list of their Stripe-saved payment sources as radio buttons rather than the default SiteGenesis select options.

After a customer saves their address and credit card information in their browser, they see the payment request button (Pay now).

The customer sees Pay now or an Apple Pay button, depending on what their device and browser combination supports.

## See also

- Testing

[Testing](/connectors/salesforce-commerce-cloud/testing)
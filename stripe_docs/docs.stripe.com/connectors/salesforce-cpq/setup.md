# Set up the Stripe Billing Connector for Salesforce CPQ

The Stripe Billing Connector for Salesforce CPQ syncs your products, prices, accounts, and orders from Salesforce to Stripe Billing. After you set up the connector and create data mappings, the service syncs this information from Salesforce and completes the collection and provisioning workflows in Stripe Billing.

[Install the connector](#install-connector)

## Install the connector

The connector is a managed package that you install from the Salesforce AppExchange onto your Salesforce account.

[Salesforce AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FOm4xUAD)

During the installation process, choose Install for Admins Only. Follow the prompts onscreen and approve third-party access. In Salesforce, search for Stripe Billing Connector to continue the setup process.

In the Stripe Billing Connector, follow the steps onscreen to:

- Authorize access between your Salesforce environment and Stripe account.

- Define how data maps between Salesforce and Stripe.

- Configure synchronization preferences.

[Define how data maps between Salesforce and Stripe](#data-map)

## Define how data maps between Salesforce and Stripe

Use the Define Data Mapping step to map the fields from the Salesforce objects to corresponding fields on the Stripe objects. For example, for a custom field that stores whether a price book entry is metered or licensed, specify that field to map to recurring.usage_type on the Stripe Price object.

[recurring.usage_type](/api/prices/object#price_object-recurring-usage_type)

The connector automatically maps the following Salesforce objects to the corresponding Stripe objects:

[Product](/api/products/object)

[Price](/api/prices/object)

[Customer](/api/customers/object)

[Subscription Schedule](/api/subscription_schedules/object)

[Subscription](/api/subscriptions/object)

[Subscription Item](/api/subscription_items/object)

You can also map information within Salesforce objects or to metadata fields within corresponding Stripe objects by defining field defaults and custom mappings.

[defining field defaults and custom mappings](/connectors/salesforce-cpq/field-mappings)

[Configure synchronization preferences](#preferences)

## Configure synchronization preferences

Use the Configure Sync Preferences step to specify:

- Sync record retention – The number of sync records retained in Salesforce.

- Start date – After you enable live syncing, the connector begins to sync data for activated orders to Stripe on or after this date. You can specify a date in the past.

[enable live syncing](#activate-syncing)

- Sync filters – Adds filters to determine when to sync Salesforce orders, accounts, products, and pricebook entries. By default, the connector syncs orders when Status = Activated, but you can customize this behavior for your workflows.

After setup completes and you activate live syncing for your integration, newly activated orders automatically:

[activate live syncing](#activate-syncing)

- Create or update a Customer object in Stripe for the account that corresponds to the order. The id on the Stripe customer is available as a custom field called Stripe ID on the Salesforce account.

- Create or update products and prices in Stripe for each product in the order.

- Create a subscription schedule in Stripe for the activated order.

- Create a Sync Record custom object in Salesforce to indicate the sync status and any errors that arise.

- Refunds – Use the Stripe Dashboard link on the Salesforce object to issue refunds through Stripe.

- Payment and subscription status – Use the Stripe Dashboard link to see an order’s subscription status, payment information, and related invoices.

- Taxes – Tax information isn’t synced between Salesforce and Stripe. To collect taxes on an invoice, use Stripe Tax to automatically calculate and apply taxes to the subscription or Stripe invoice for an order.

[Stripe Tax](/tax)

[Activate live syncing](#activate-syncing)

## Activate live syncing

In the final step of the post-installation flow, you can choose to enable live syncing now or later. Live syncing allows your integration to pull activated Salesforce orders into Stripe in real time. You can enable or disable live syncing of orders any time on the Sync Preferences tab of the application.

You can manually sync individual orders to test your integration, even when live syncing is disabled.

[OptionalImplement custom workflows](#custom-workflows)

## OptionalImplement custom workflows

[OptionalAdd custom fields to page layouts](#page-layouts)

## OptionalAdd custom fields to page layouts

[OptionalManage permissions](#manage-permissions)

## OptionalManage permissions

## See also

- Field defaults and custom mappings

[Field defaults and custom mappings](/connectors/salesforce-cpq/field-mappings)

- Accounts and contacts

[Accounts and contacts](/connectors/salesforce-cpq/accounts-contacts)

- Products and prices

[Products and prices](/connectors/salesforce-cpq/products-prices)

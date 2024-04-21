# Custom payment application

The Stripe Connector for NetSuite provides a way for you to reconcile Stripe payment activity from your custom or prebuilt, third-party integration to NetSuite. Using the following tools, you can customize how the connector records and reconciles payments in NetSuite:

- Stripe metadata

[Stripe metadata](/connectors/netsuite/custom-payment-application#stripe-metadata)

- Invoices for payments

[Invoices for payments](/connectors/netsuite/custom-payment-application#invoices-payments)

- Connector add-ons

[Connector add-ons](/connectors/netsuite/custom-payment-application#connector-addons)

[Stripe metadata](#stripe-metadata)

## Stripe metadata

You can use Stripe metadata to make sure your Stripe activity is properly represented in NetSuite.

Add metadata to Stripe objects to relate them to existing NetSuite records. You can add this metadata at the time of syncing, before the Stripe object syncs to NetSuite, or in conjunction with controls that modify the sync timing.

You can relate records in the following ways:

- Add netsuite_invoice_id: 12345 to a Stripe charge so that the connector applies the customer payment to NetSuite invoice with internal ID 12345.

- Add netsuite_credit_memo_id: 67890 to a Stripe refund so that the connector applies the customer refund to NetSuite credit memo with internal ID 67890.

- Add netsuite_customer_id: 101010 to a Stripe charge so that the connector creates the customer payment under NetSuite customer with internal ID 101010.

You can choose to override the default sync timing by programmatically controlling when a record syncs to NetSuite. There are two ways to override record sync timing: add records to a denylist or add records to an allowlist.

You can add metadata to temporarily stop the connector from syncing a record to NetSuite. This is helpful if your backend integration with Stripe requires adding data to a record before syncing to NetSuite.

Use a denylist to control the timing of a customer sync to NetSuite:

- Ask your implementation partner to enable the Denylist payments and refunds feature in your Stripe app settings. Consult with your implementation partner to understand all accounting and technical implications.

- Add netsuite_block_integration: true to the metadata of any Stripe object.

- To allow record syncing again, replace true with nil.

You can’t permanently add a payment or payment-related record to the denylist. After two days, the connector automatically attempts to create a bank deposit for the Stripe payout. Until you remove the payment or record from the denylist, the deposit automation fails and the payment or record can’t sync to NetSuite.

The following are examples of when you might want to use a denylist:

Example 1: You might have a customer record that your system created when a Stripe customer started the signup process and made a prepayment. Later you collect address data for that customer. The connector typically syncs the customer and payment data to NetSuite right away; however, you can delay syncing to NetSuite until you finish collecting all data for a customer.

Example 2: Your Stripe account includes Stripe Billing and an e-commerce app. You want to associate the payments from the e-commerce app with your NetSuite orders, and to automatically sync the subscription invoices and payments. To do so, add metadata to the payments from the e-commerce system. The connector syncs the Stripe Billing invoices and payments to NetSuite. The e-commerce payments without a Netsuite order or invoice ID won’t sync until the associated order or invoice is imported into your NetSuite account. After the order detail is added, you can remove the denylist metadata and add the NetSuite invoice ID to associate the records.

You can add metadata to stop the connector from syncing a record to NetSuite until it is granted permission. This is helpful if you have an e-commerce system that uses Stripe to process payments before the invoice is created in NetSuite.

Use an allowlist to control the syncing of a record to NetSuite:

- Ask your implementation partner to enable the Allowlist payments feature in your Stripe app settings. Consult with your implementation partner to understand all accounting and technical implications.

- Add netsuite_allow_integration: true to the metadata of a record.

Don’t use an allowlist if either of the following applies:

- You use Stripe Billing. In most cases, Stripe automatically generates invoices, which can create challenges with making sure invoices are added to the allowlist. Instead, you can use a denylist for payments that aren’t related to Stripe Billing.

- You don’t have a fully comprehensive custom system that accounts for every payment in your Stripe account. If a payment in your Stripe account isn’t synced to NetSuite, the deposit automation fails until the payment is synced.

Override any part of the connector’s record syncing process by adding metadata to Stripe objects to relate them to existing NetSuite records. You can add this metadata at the time of syncing, before the Stripe object syncs to NetSuite, or in conjunction with controls that modify the sync timing. This prevents the connector from creating that record in NetSuite.

For example, you have an existing system that creates customers that you want to use alongside the connector. You can pass the NetSuite customer’s internal ID to the Stripe customer to allow the connector to create a link between the two, rather than creating a new customer. You can also use the same process to link Stripe prices to existing NetSuite items.

See below for the list of metadata keys to link records and override record creation.

[metadata keys](/connectors/netsuite/custom-payment-application#metadata-keys)

Overriding any part of the connector’s record syncing process that affects accounts receivable might introduce accounting inaccuracies. Our system guarantees that the created records are accurate, but can’t guarantee the accuracy of records created by another system.

The connector uses metadata keys to link Stripe objects to existing NetSuite records. You can add this metadata at the time of syncing, before the Stripe object syncs to NetSuite, or in conjunction with controls that modify the sync timing.

Price

netsuite_service_sale_item_id

Service Sale Item

If unspecified, this is the default item type that the connector uses to create new items.

Price

netsuite_service_resale_item_id

Service Resale Item

You can use this item type in place of a Service Sale Item.

Price

netsuite_non_inventory_sale_item_id

Non Inventory Sale Item

You can use this item type in place of a Service Sale Item.

Price

netsuite_non_inventory_resale_item_id

Non Inventory Resale Item

You can use this item type in place of a Service Sale Item.

Price

netsuite_discount_item_id

Discount Item

Only applicable if the line item amount is negative.

Invoice Line Item

netsuite_discount_item_id

Discount Item

Only applicable if the line item amount is negative.

Refund

netsuite_credit_memo_id

Credit Memo

Only applicable if the refund’s charge is linked to a Stripe-created invoice.

[Invoices for payments](#invoices-payments)

## Invoices for payments

If your system uses Stripe to process payments and it creates a payment in Stripe that isn’t associated with an invoice, you can choose to allow the connector to create an invoice using information from the charge. You must enable this feature to use it. The connector then applies a customer payment to represent revenue and cash for that transaction.

This workflow doesn’t support discounts, multiple line items, and other complex integrations.

- The connector creates a NetSuite invoice for each charge in Stripe and includes the charge description in a memo on the invoice. You can choose to add data from the Stripe metadata fields to the invoice by using field mappings.

- The invoice uses a single line item to represent the revenue earned by the entire Stripe charge. By default, all payments on the Stripe account use the same NetSuite item. You can customize this.

- The connector creates a payment and applies it to the invoice. The payment is automatically reconciled to a bank deposit and fees are recorded.

- Refunds and disputes automatically represent as a credit memo and refund.

All invoices generated from charges use the same NetSuite item (Stripe Generic Line Item), by default. If charges are used to purchase multiple types of products in your app, you need to record the revenue for the different products against unique NetSuite items. This allows you to have detailed reports in NetSuite based on revenue by item, quantity of items sold, and more.

You can’t have multiple line items on an invoice from charges. The connector can’t distribute the revenue across separate items from the metadata information on the Stripe charge. If you need to use multiple line items on your NetSuite invoice, you can use a Stripe invoice to sync line-item details.

You can use metadata or a standard field on the Stripe charge to select a NetSuite item. The connector uses the Stripe metadata or field to search for a field on the NetSuite item. If the connector doesn’t find a match, it uses the Stripe Generic Line Item. Matches aren’t case sensitive.

For example, you create a Stripe charge and add the product_name metadata that includes the name of a NetSuite item. The connector searches for an item in NetSuite that matches the product_name in Stripe. If the connector finds a match, it uses that item on the invoice created for that charge.

Use invoices for payments flow:

- Ask your implementation partner to enable the Create invoices for payments feature in your Stripe app settings. Consult with your implementation partner to understand all accounting and technical implications.

- Add the following for the connector to use for matching:Add a NetSuite field on the item recordAdd the corresponding Stripe field on the Charge object

- Add a NetSuite field on the item record

- Add the corresponding Stripe field on the Charge object

For example, you can add a metadata key on a Stripe charge and itemid or displayName on the NetSuite item.

[Connector add-ons](#connector-addons)

## Connector add-ons

Contact us to learn more or to get started with connector add-ons.

[Contact us](http://stripe.com/sales)

The connector provides NetSuite add-ons (bundles) to support common use cases and allow seamless operation with core workflows. You can work with an official implementation partner to customize your integration with these add-ons, which live exclusively in NetSuite.

You can customize the add-ons by developing new workflows on top of them, or modifying existing workflows to support your business needs. For example, you might want to align the payment and reconciliation processes with your unique NetSuite setup, while still using core connector automations.

Use the Autopay add-on to automatically bill your customer’s saved payment method and pay open invoices in NetSuite. You can modify the billing details, such as cadence and parameters, to make sure the correct invoices are billed.

## See also

Deposit automation

[Deposit automation](/connectors/netsuite/deposit-automation)

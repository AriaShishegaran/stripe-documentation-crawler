# Query Billing data

Billing is made up of different components that work together to provide one-off invoices and periodic billing, with different aspects of billing data available across a number of tables. All billing-specific tables are in the Billing section of the schema, with the primary tables being subscriptions and invoices.

[invoices](/api/invoices)

To explore billing data further, you can use the additional tables that represent the components of subscriptions and invoices, such as prices, products, or coupons. In addition, the customers table is a fundamental part of billing, and contains data you might need to report on.

## Subscriptions

Each row within the subscriptions table represents data about an individual Subscription object—the same information that  the API retrieves or is available in the Stripe Dashboard. You can report on every subscription that you create on your account.

[Subscription](/api#subscription_object)

[Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions)

This table is our recommended starting point for creating reports about your current subscribers. You can join this to other related tables, allowing you to explore your data in more detail.

The following example retrieves a list of subscriptions that have been marked as unpaid, along with any available contact information for the customer.

## Customers

Data about Customer objects are contained in the customers table (this isn’t part of the Billing Tables group). It’s commonly used as part of billing-based reports and can be joined to a number of tables. It’s also useful if you’re creating charges with saved payment information.

[Customer](/api#customers)

[charges](/stripe-data/query-transactions)

The following example retrieves a list of customers with subscriptions that are currently in a trial period. It retrieves both the ID and email address for each customer.

## Products and Prices

Products describe items that your customers can purchase with a subscription. Prices are tied to products and set out the cost, billing interval, and currency. When viewing data from the subscriptions table, subscriptions.price_id can be joined to prices.id, and prices.product_id can be joined to products.id. The following example returns a list of active subscriptions along with the product name and its statement descriptor.

## Invoices

Refer to our invoices documentation to learn more about invoices, invoice items, and invoice line items.

[invoices](/invoicing/overview)

The invoices table contains data about individual Invoice objects. Each subscription generates an invoice on a recurring basis that represents the amount the customer owes. This automatically includes the amount required for the subscription, and any additional invoice items that might have been created (listed as line items).

[Invoice](/api#invoice_object)

[invoice items](/api#invoiceitems)

Invoices are comprised of individual (invoice) line items. These line items represent any subscriptions that the customer is billed for, and invoice items that have been created and applied to the invoice. To break down an invoice and analyze each of its line items, use the invoice_line_items table.

[invoice) line items](/api#invoice_line_item_object)

The  source_id column of this table contains the ID of either the subscription (for example, sub_YnEs4zcbPIkAjx6) or invoice item (for example, ii_gRFNBC853IaRQRj) that the line item corresponds to. The source_type column reflects whether the line items represent a subscription or an invoice item.

Unlike other foreign keys, the subscription column of the  invoice_line_items table isn’t always populated. If the corresponding invoice item is a subscription, this column is blank—its ID already appears in the source_id column.

Data about Invoice items is provided in the invoice_items table. Invoice items are commonly used to specify an additional amount (or deduct an amount) that’s applied on the next invoice at the beginning of the next billing cycle. For example, you would create an invoice item if you need to bill your customer for exceeding their monthly allowance, or if you need to provide a credit on the next invoice for unused service.

[Invoice items](/api#invoiceitems)

The following example retrieves all the invoices and associated charge IDs for a particular subscription.

The invoice subtotal represents the amount of all subscriptions, invoice items, and prorations on the invoice before any discount is applied. The invoice total is the amount after discounts and tax have been applied:

invoice.total = invoice.subtotal - discount + invoice.tax

There is no column to represent the discount amount on an invoice. Instead, you can calculate this by using the total, subtotal, and tax amounts:

discount = invoice.total - invoice.tax - invoice.subtotal

As subscription invoices are pre-billed, the customer pays at the start of a billing period. This is reflected in the value for a line item’s period. For instance, a customer on a monthly subscription is charged at the start of each month. If they cancel, their subscription remains active until the end of that month, at which point the subscription ends.

The period_start and period_end values of an invoice represents when invoice items might have been created–it’s not always indicative of the period of service that the customer is being billed for. For example, if a customer is billed on the 1st of each month and exceeds their monthly allowance on the 15th, you might create an invoice item for any additional costs that the customer is charged for. This invoice item is then included in the next invoice, which is created on the 1st of the next month. When the next invoice is generated, the period_start date would be the 15th of the previous month—the date the additional line item is first created.

## Coupons and discounts

A Coupon object represents an amount or percentage-off discount that can be applied to subscriptions or customers. A discount is the application of a coupon, represented by a Discount object.

[Coupon](/billing/subscriptions/coupons)

[Discount](/api#discounts)

Discounts aren’t tabulated separately. Instead, join  coupon.id  to either customers.discount_coupon_id or subscriptions.discount_coupon_id, which returns the coupon information for the discount that has been applied. For example, the following query returns a list of subscriptions where a coupon was applied to create a discount, along with the coupon’s discount amount or percentage.

## Subscription Item Change Events

The subscription_item_change_events table tracks changes to subscription items that affect Monthly Recurring Revenue (MRR). Use this table to calculate MRR for individual customers, products, plans, and to create custom metric definitions for your business models.

[Monthly Recurring Revenue (MRR)](https://support.stripe.com/questions/calculating-monthly-recurring-revenue-(mrr)-in-billing)

This table provides more up-to-date data than the source driving the MRR metrics on the Billing overview in the Stripe Dashboard. This means the data for the last and current day’s MRR here could be more accurate and could differ from what you see in the Dashboard.

This table includes two timestamp columns:

- event_timestamp: This is the UTC timestamp.

- local_event_timestamp: This timestamp is in your local timezone, typically the timezone of the person who created your Stripe account.

Here, you’ll find the subscription item’s settlement currency as a three-letter ISO currency code in lowercase. The currency must be one that Stripe supports.

[ISO currency code](https://stripe.com/docs/currencies)

[supports](https://stripe.com/docs/currencies)

The mrr_change column shows the positive or negative impact of an event on your MRR in the subscription item’s settlement currency’s minor unit (such as cents for USD).

Some user actions can create multiple events, so you could see an event with an event_type of ACTIVE_END on one item and then immediately an event with an event_type of ACTIVE_START on another item for the same subscription_id.

Other columns (product_id, price_id, customer_id, subscription_id, and subscription_item_id) hold IDs related to the subscription item change event.

Querying this table to calculate MRR involves window functions and, for those with customers in different currencies, foreign currency exchange calculations. Here’s an example for calculating daily MRR for the past two months in US dollar cents:

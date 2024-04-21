htmlQuery Billing data | Stripe Documentation[Skip to content](#main-content)Query Billing data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-billing-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-billing-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Query Billing data

Use Sigma or Data Pipeline to retrieve information about Billing.Billing is made up of different components that work together to provide one-off invoices and periodic billing, with different aspects of billing data available across a number of tables. All billing-specific tables are in the Billing section of the schema, with the primary tables being subscriptions and invoices.

To explore billing data further, you can use the additional tables that represent the components of subscriptions and invoices, such as prices, products, or coupons. In addition, the customers table is a fundamental part of billing, and contains data you might need to report on.

## Subscriptions

Each row within the subscriptions table represents data about an individual Subscription object—the same information that  the API retrieves or is available in the Stripe Dashboard. You can report on every subscription that you create on your account.

This table is our recommended starting point for creating reports about your current subscribers. You can join this to other related tables, allowing you to explore your data in more detail.

![](https://b.stripecdn.com/docs-statics-srv/assets/subscriptions.b2676e216021e4a013eb4da5f4f839ec.png)

The following example retrieves a list of subscriptions that have been marked as unpaid, along with any available contact information for the customer.

`select
  subscriptions.id,
  subscriptions.customer_id,
  customers.email
from subscriptions
inner join customers
  on customers.id = subscriptions.customer_id
where
  subscriptions.status = 'unpaid'
limit 5`idcustomer_idemailsub_LqzOzGQ5oX212ROcus_nAZA3BQyE8Gpk1ujenny.rosen@example.comsub_33VhOAKITHq4Okrcus_Z2AmpgrSn7LcrQcnoah.wilson@example.comsub_d4oPKsSgXqDspmdcus_I1I99Sssvt3B4aRjoshua.miller@example.comsub_9gcBnTuzpKoRJtbcus_q4OfSzzE8tiKoh0madison.jackson@example.comsub_66EKlUFjrHzM8fAcus_63gfKcWM8mV8PMfelijah.smith@example.com## Customers

Data about Customer objects are contained in the customers table (this isn’t part of the Billing Tables group). It’s commonly used as part of billing-based reports and can be joined to a number of tables. It’s also useful if you’re creating charges with saved payment information.

![](https://b.stripecdn.com/docs-statics-srv/assets/customers.60b1588c3375261e7f8b6ec1a4ab8302.svg)

The following example retrieves a list of customers with subscriptions that are currently in a trial period. It retrieves both the ID and email address for each customer.

`select
  customers.id,
  customers.email,
  subscriptions.price_id
from subscriptions
inner join customers
on customers.id = subscriptions.customer_id
where subscriptions.status = 'trialing'
limit 5`idemailprice_idcus_qFaaG9vvXtHvRutjenny.rosen@example.comruby-pro-522cus_kBgfw54kovVu7ORnoah.wilson@example.comruby-pro-522cus_UqGVzxlxYKeiCjvrichard.jones@example.comgold-basic-221cus_pAK8iRwBiTcpCBUmadison.jackson@example.comgold-basic-221cus_5SnJsAjAsjasovDelijah.smith@example.comsilver-pro-498## Products and Prices

Products describe items that your customers can purchase with a subscription. Prices are tied to products and set out the cost, billing interval, and currency. When viewing data from the subscriptions table, subscriptions.price_id can be joined to prices.id, and prices.product_id can be joined to products.id. The following example returns a list of active subscriptions along with the product name and its statement descriptor.

`select
  subscriptions.id,
  products.name,
  products.statement_descriptor
from subscriptions
inner join prices
  on subscriptions.price_id = prices.id
inner join products
  on prices.product_id = products.id
where
  subscriptions.status = 'active'
limit 10`idnamestatement_descriptorsub_GFZ1ReWm3RZOjC3ruby-pro-522Ruby Prosub_Qk2P0HoWcPkpuT8gold-basic-221Gold Basicsub_H0OxiRFvSNptjeisilver-pro-498Silver Prosub_c1AZqTFQDrBAt1Idiamond-mid-244Diamond Midsub_rXIHE3JjtZuV2G1ruby-standard-196Ruby Standard## Invoices

### Working with invoices

Refer to our invoices documentation to learn more about invoices, invoice items, and invoice line items.

The invoices table contains data about individual Invoice objects. Each subscription generates an invoice on a recurring basis that represents the amount the customer owes. This automatically includes the amount required for the subscription, and any additional invoice items that might have been created (listed as line items).

Invoices are comprised of individual (invoice) line items. These line items represent any subscriptions that the customer is billed for, and invoice items that have been created and applied to the invoice. To break down an invoice and analyze each of its line items, use the invoice_line_items table.

The  source_id column of this table contains the ID of either the subscription (for example, sub_HRTGzPXAdffeZl8) or invoice item (for example, ii_NYV1f2LJsdHo1z5) that the line item corresponds to. The source_type column reflects whether the line items represent a subscription or an invoice item.

Unlike other foreign keys, the subscription column of the  invoice_line_items table isn’t always populated. If the corresponding invoice item is a subscription, this column is blank—its ID already appears in the source_id column.

### Invoice items

Data about Invoice items is provided in the invoice_items table. Invoice items are commonly used to specify an additional amount (or deduct an amount) that’s applied on the next invoice at the beginning of the next billing cycle. For example, you would create an invoice item if you need to bill your customer for exceeding their monthly allowance, or if you need to provide a credit on the next invoice for unused service.

![](https://b.stripecdn.com/docs-statics-srv/assets/invoices.ed8822925c41f368821ba104bd52efb1.svg)

The following example retrieves all the invoices and associated charge IDs for a particular subscription.

`select
  id,
  charge_id,
  amount_due
from invoices
where subscription_id = 'sub_ALJXL9gBYtv6GJ'`idnamein_2Hj8ryNuChK4dmmch_HAoewWx1sToLOy71999in_MhlNwxbzitkGSJach_vosEgewhe51uDLJ1999in_emKjrncmCG9JxHh1999ch_JzwZBmqupUWFb0Gin_zQZLcigoMOutoYp1999ch_z0hDrTulDTKfYcdin_glz3P7nNh5YIdAs1999ch_TGEVMh9MjzbYzqI### Invoice totals and discounts

The invoice subtotal represents the amount of all subscriptions, invoice items, and prorations on the invoice before any discount is applied. The invoice total is the amount after discounts and tax have been applied:

invoice.total = invoice.subtotal - discount + invoice.tax

There is no column to represent the discount amount on an invoice. Instead, you can calculate this by using the total, subtotal, and tax amounts:

discount = invoice.total - invoice.tax - invoice.subtotal

### Working with invoice dates and periods

As subscription invoices are pre-billed, the customer pays at the start of a billing period. This is reflected in the value for a line item’s period. For instance, a customer on a monthly subscription is charged at the start of each month. If they cancel, their subscription remains active until the end of that month, at which point the subscription ends.

The period_start and period_end values of an invoice represents when invoice items might have been created–it’s not always indicative of the period of service that the customer is being billed for. For example, if a customer is billed on the 1st of each month and exceeds their monthly allowance on the 15th, you might create an invoice item for any additional costs that the customer is charged for. This invoice item is then included in the next invoice, which is created on the 1st of the next month. When the next invoice is generated, the period_start date would be the 15th of the previous month—the date the additional line item is first created.

## Coupons and discounts

A Coupon object represents an amount or percentage-off discount that can be applied to subscriptions or customers. A discount is the application of a coupon, represented by a Discount object.

Discounts aren’t tabulated separately. Instead, join  coupon.id  to either customers.discount_coupon_id or subscriptions.discount_coupon_id, which returns the coupon information for the discount that has been applied. For example, the following query returns a list of subscriptions where a coupon was applied to create a discount, along with the coupon’s discount amount or percentage.

`select
  coupons.id,
  coupons.amount_off,
  coupons.percent_off
from coupons
where valid = false
limit 5`idamount_offpercent_off10FF10SUMMER252510FREE1015OFF15FALL3030## Subscription Item Change Events

The subscription_item_change_events table tracks changes to subscription items that affect Monthly Recurring Revenue (MRR). Use this table to calculate MRR for individual customers, products, plans, and to create custom metric definitions for your business models.

CautionThis table provides more up-to-date data than the source driving the MRR metrics on the Billing overview in the Stripe Dashboard. This means the data for the last and current day’s MRR here could be more accurate and could differ from what you see in the Dashboard.

### local_event_timestamp and event_timestamp

This table includes two timestamp columns:

- `event_timestamp`: This is the UTC timestamp.
- `local_event_timestamp`: This timestamp is in your local timezone, typically the timezone of the person who created your Stripe account.

### currency

Here, you’ll find the subscription item’s settlement currency as a three-letter ISO currency code in lowercase. The currency must be one that Stripe supports.

### mrr_change

The mrr_change column shows the positive or negative impact of an event on your MRR in the subscription item’s settlement currency’s minor unit (such as cents for USD).

### event_type

Event typeDefinitionACTIVE_STARTThe subscription item started contributing to MRR.ACTIVE_UPGRADEThe MRR contribution of the subscription item increased (for example, the quantity increased).ACTIVE_ENDThe subscription item stopped contributing to MRR.ACTIVE_DOWNGRADEThe MRR contribution of the subscription item decreased (for example, the quantity decreased).NoteSome user actions can create multiple events, so you could see an event with an event_type of ACTIVE_END on one item and then immediately an event with an event_type of ACTIVE_START on another item for the same subscription_id.

### Other columns

Other columns (product_id, price_id, customer_id, subscription_id, and subscription_item_id) hold IDs related to the subscription item change event.

### Example query

Querying this table to calculate MRR involves window functions and, for those with customers in different currencies, foreign currency exchange calculations. Here’s an example for calculating daily MRR for the past two months in US dollar cents:

`-- the following six CTEs load the foreign currency exchange rates into a more efficient datastructure to use later.
with date_ranges as (
  SELECT
    date_col
  FROM
    UNNEST(
      sequence(date '2010-01-01', current_date, INTERVAL '1' DAY)
    ) t (date_col)
),
currencies AS (
  SELECT DISTINCT t.currency
  FROM exchange_rates_from_usd
	CROSS JOIN UNNEST (
  CAST(json_parse(buy_currency_exchange_rates) AS MAP(VARCHAR, DOUBLE))
) AS t (currency, rate)
),
dates as (
  select
    date_col as date,
    date_col + INTERVAL '1' DAY as fx_date
  from
    date_ranges
),
dates_currencies as (
  select
  	date,
    fx_date,
  	currency
  from
  	dates
  cross join
  	currencies
),
fx_rates_json as (
  select
    dates.date,
    last_value(
      exchange_rates_from_usd.buy_currency_exchange_rates
    ) ignore nulls over (
      order by
        exchange_rates_from_usd.date asc
    ) as buy_currency_exchange_rates
  from
    dates
    full outer join exchange_rates_from_usd on dates.fx_date = exchange_rates_from_usd.date
),
fx_rates as (
  select
    transform_values(
      multimap_agg(
        date_format(date, '%Y-%m-%d'),
        row(currency, rate)
      ),
      ((k, v) -> map_from_entries(v))
    ) as rates
  from
    fx_rates_json
    cross join unnest(
      map_entries(
        cast(
          json_parse(buy_currency_exchange_rates) as map(varchar, double)
        )
      )
    ) t(currency, rate)
  where
    date in (
      select
        date
      from
        dates
    )
  ),
-- this sums up the per-currency MRR changes for each day
per_day_sums as (
  select
    date(local_event_timestamp) as event_date,
    currency,
    sum(mrr_change) as mrr_change
  from
    subscription_item_change_events t
  group by 1, 2
),
per_currency_sums as (
  select
    date_format(c.date, '%Y-%m-%d') as date,
    c.currency,
    sum(mrr_change) over (
      partition by
        c.currency
      order by
        c.date asc
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as mrr
  from
    per_day_sums
  right join
  	dates_currencies c
  on c.currency = per_day_sums.currency
  and c.date = per_day_sums.event_date
)
-- this does the foreign exchange calculation and filters to the time range you want, 2 months.
select
  date,
  cast(
    sum(
      round(
        -- replace 'usd' below with the currency you want your MRR represented in
        mrr / fx_rates.rates[date][currency] * fx_rates.rates[date]['usd']
      )
    ) as bigint
  ) as mrr
from
  per_currency_sums
  cross join fx_rates
where
  -- here's where you filter to the range you want, in this case 2 months
  date >= date_format(current_date - interval '2' month, '%Y-%m-%d')
group by
  1
order by 1 desc`event_datemrr2024-04-17144025702024-04-16144109002024-04-15144034032024-04-14143725822024-04-13143659182024-04-12143276002024-04-11143467592024-04-10143634192024-04-09143517572024-04-08143334312024-04-07143192702024-04-06143167712024-04-05142401352024-04-04142501312024-04-03142534632024-04-02142476322024-04-01142476322024-03-31142143122024-03-30141876562024-03-29141468392024-03-28141526702024-03-27141526702024-03-26141310122024-03-25141243482024-03-24141168512024-03-23141151852024-03-22140976922024-03-21141043562024-03-20141135192024-03-19140976922024-03-1814088529Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Subscriptions](#subscriptions)[Customers](#customers)[Products and Prices](#products-and-prices)[Invoices](#invoices)[Coupons and discounts](#coupons-and-discounts)[Subscription Item Change Events](#subscription-item-change-events)Products Used[Billing](/billing)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
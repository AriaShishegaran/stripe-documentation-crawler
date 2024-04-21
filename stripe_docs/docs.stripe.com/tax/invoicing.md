# Automatically collect tax on invoices

On an invoice, Stripe Tax calculates sales tax, VAT, and GST. To calculate these for each line item, Stripe uses:

[invoice](/api/invoices)

- Your tax settings

[tax settings](https://dashboard.stripe.com/settings/tax)

- The customer’s tax settings and location

- The product tax code and price tax behavior

Log in or sign up for Stripe to activate Stripe Tax.

[Log in](https://dashboard.stripe.com/settings/tax)

[sign up](https://dashboard.stripe.com/register)

## Set up the customer

We use the customer’s location to determine the relevant taxes to collect. Customers outside of the US need at least a country-level address, while customers in the US require a 5-digit postal code. For Canada, we need at least the province or postal code.

You can add customer location information in the Customer details page by clicking Edit next to Details. To add a customer’s location from the Invoice Editor, click the overflow menu () next to the customer. Select Edit customer information, click Add additional details, and scroll down to Billing details.

[Invoice Editor](https://dashboard.stripe.com/invoices/create)

After you update the location, click Update customer. Stripe applies the new location to all of your customer’s future invoices unless you update it. For more information, see Determine customer locations.

[Determine customer locations](/tax/customer-locations)

## Set up line items

To calculate tax on each line item on an invoice, you need to set a tax behavior and optionally a tax code.

Customize line items in the Invoice Editor by selecting the tax behavior from the Include tax in price drop-down menu.

Customize tax settings for one-off line items

You can use both the Dashboard and the API to customize tax settings for product-based line items.

On the Products page, you can select both the tax behavior for a particular price and the optional tax code for the product. The tax behavior is per price. You can’t change the tax behavior after you select it, but you can create new prices or archive old ones. To set up a tax behavior, click Add a price (or Add another price if you already have one) and select it from the Tax behavior drop-down menu.

[Products page](https://dashboard.stripe.com/products)

To set up a tax code, select it from the Tax code drop-down menu when you create a new product or edit the details of an existing one.

Customize tax settings for one-off line items

## Enable automatic tax

After specifying a tax behavior and tax code, you can add the price to the customer as an invoice item:

Set the toggle in the Invoice Editor. In the API, you need to pass the automatic_tax field to enable or disable automatic tax calculation. Both steps are required to start calculating tax automatically.

To enable automatic tax calculation when you update an invoice, add the invoice parameter alongside automatic_tax:

## See also

- Determine customer locations

[Determine customer locations](/tax/customer-locations)

- Understand zero tax amounts

[Understand zero tax amounts](/tax/zero-tax)

- Reporting and filing

[Reporting and filing](/tax/reports)

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)

- Calculate tax in your custom checkout flow

[Calculate tax in your custom checkout flow](/tax/custom)

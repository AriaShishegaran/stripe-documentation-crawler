# Tax rates and IDs

If you’re looking for automated tax calculation where you don’t need to define the rates, use Stripe Tax.

[Stripe Tax](/tax)

After you create a tax rate, you can assign it:

[create a tax rate](/billing/taxes/tax-rates)

- On individual invoice items.

[invoice](/api/invoices)

- On the entire subtotal of the invoice.

Stripe recommends that you assign a tax rate on individual invoice items.

## Set tax rates on individual items

You can set tax rates on individual items using the Dashboard or API. You can add up to five tax rates to each line item.

[Dashboard](https://dashboard.stripe.com/invoices/create)

[API](/api/tax_rates)

If you’re creating an invoice through the Dashboard, assign tax rates to individual line items.

## Set default tax rates for the entire invoice

If you sell one type of product, or have simple tax needs, you can set a default tax rate on the invoice. Default tax rates apply to all invoice line items. For more complex use cases, you can also set an item-level tax rate that overrides the default tax rate. You can add up to five default tax rates to each invoice.

If you’re creating an invoice through the Dashboard, you can assign a default tax rate after you add an item.

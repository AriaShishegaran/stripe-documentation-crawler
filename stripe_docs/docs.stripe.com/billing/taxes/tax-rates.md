# Tax rates

Stripe allows you to define any number of tax rates and apply them to invoices, subscriptions, and one time payments when using Checkout. However, we won’t automatically set them on your behalf.

[invoices](/api/invoices)

[subscriptions](/billing/subscriptions/creating)

If you’re looking for automated tax calculation where you don’t need to define the rates, use Stripe Tax.

[Stripe Tax](/tax)

When applying tax rates, Stripe calculates the total tax amount per tax rate, and summarizes it in a table that you can export into tax summary reports.

[total tax amount](/billing/taxes/tax-rates#tax-amounts)

## Creating tax rates

If you’re working with a small number of tax rates, you can manage and create them in the Dashboard. After creating tax rates, you can apply them to invoices, subscriptions, and one-time payments or subscriptions created through Stripe Checkout.

[Dashboard](https://dashboard.stripe.com/test/tax-rates)

[invoices](/invoicing/taxes/tax-rates)

[subscriptions](/billing/taxes)

[one-time payments](/payments/checkout/taxes)

[subscriptions](/billing/taxes/collect-taxes?tax-calculation=tax-rates#adding-tax-rates-to-checkout)

Create a catalog of tax rates that meet the requirements for the jurisdictions that you do business in. For example, if you operate in Europe, you might want to create a catalog of tax rates for OSS VAT.

The following example demonstrates how you can create a tax rate through the API.

Required properties:

- The display_name appears on your customer’s invoice, and is usually a short name that describes the specific type of tax, such as Sales, VAT, or GST.

- The inclusive property determines whether the tax percentage is added to, or included in, the overall amount.

- The percentage is a number (up to 4 decimal places) that represents the tax percentage to be collected.

Optional properties:

- The optional country property is a valid two-letter ISO country code. Some countries (for example, United States) require an additional two-letter state property. Use these properties to apply dynamic tax rates based on your customer’s billing or shipping address in Checkout Sessions.

[two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm)

- The optional jurisdiction property represents the tax jurisdiction of the tax rate and can be used to differentiate between tax rates of the same percentage. jurisdiction appears on your customer’s invoice. In the Dashboard, jurisdiction appears as the Region label for the tax rate.

- You can also store additional details in the description. Your customers won’t see this property.

You can’t change the percentage, country, or state properties after you set them, and you can only set them when you create the tax rate.This ensures that existing subscriptions and invoices using tax rates aren’t affected… If you need to update these properties, create a new tax rate and archive the old object.

## Inclusive versus exclusive tax

Tax rates can either be exclusive or inclusive. An exclusive tax is not included in the invoice subtotal, whereas an inclusive tax is.

The following table illustrates a 25% tax rate modifying the total amount due, depending on whether it’s exclusive or inclusive.

## Tax exempt and reverse charge

You can set the exemption status for a Customer to either exempt or reverse.

[Customer](/api/customers)

In both cases, no tax is calculated on the invoice.

In the case where the customer is liable for the tax (that is, under the reverse-charge procedure within EU VAT), set the exemption status to reverse. The invoice and receipt PDF includes the text “Reverse charge”.

Download example reverse-charge invoice PDF

[Download example reverse-charge invoice PDF](https://stripe.com/files/docs/billing/taxes/example-reverse-charge.pdf)

If a one time payment is performed using Checkout, the exemption status is captured as customer_details in the Checkout Session object.

[customer_details](/api/checkout/sessions/object#checkout_session_object-customer_details)

If the customer is either exempt or reverse, for invoices with inclusive tax rates, the buyer pays the unit_amount price minus the tax that would’ve been paid had the user not been exempt or reverse. In other words, manual tax rates effectively calculate taxes as if the user weren’t exempt and then “backs out” the taxes.

The following table illustrates a 10% tax rate modifying the total amount due for an exempt or reverse customer. The first row is an example of “backed out” taxes.

## Using multiple tax rates

You can apply Tax rates to line items or set them as a default for all line items in an invoice. You can set up to five tax rates per line item. When you set tax rates on both a line item and the invoice, the rates for that invoice don’t apply to that line item.

For example, this invoice has two overall tax rates of 9.975% and 5%:

## Tax amounts

When you apply tax rates to an invoice, they’re aggregated into the total_tax_amounts attribute. This attribute represents the sum of all tax amounts, per tax rate, over the entire invoice.

[total_tax_amounts](/api/invoices/object#invoice_object-total_tax_amounts)

For example, here’s an invoice where two line items have two different rates:

Download example invoice PDF

[Download example invoice PDF](https://stripe.com/files/docs/billing/taxes/example-tax-amounts.pdf)

## Rounding

When determining tax amounts, you can do either of the following:

- Round at the invoice line item level to the smallest currency unit before summing individual tax amounts across the entire invoice. We refer to this as “line item level”.

[smallest currency unit](/currencies#zero-decimal)

- Sum up all individual taxable amounts unrounded per tax rate. Combine them to a subtotal, apply the tax rate on the subtotal, and then round. We refer to this as “invoice level”.

Select this configuration on the invoice settings page in the Dashboard. The rounding configuration is only available for invoices with manual tax rates. Invoices with automatic Stripe tax always sum up the tax amounts first and then round.

[invoice settings](https://dashboard.stripe.com/settings/billing/invoice)

Download example line item level rounding invoice PDF

[Download example line item level rounding invoice PDF](https://stripe.com/files/docs/billing/taxes/example-line-item-level-rounding.pdf)

## Discounts

Discounts are usually applied before tax, but this isn’t always the case.

Reading each line left-to-right, noting the formula applied (in the table header), you can trace the values as they’re applied to the final, total amount.

Stripe always applies discounts before exclusive tax.

This example shows how we apply discounts to an exclusive tax rate.

Download example discounts invoice PDF

[Download example discounts invoice PDF](https://stripe.com/files/docs/billing/taxes/example-exclusive-tax-with-discount.pdf)

When tax rates are inclusive, Stripe Tax applies discounts to the original amount first. Then, we recalculate taxes based on the remaining amount. This reduction has the side effect of reducing the tax amount due.

Download example invoice PDF

[Download example invoice PDF](https://stripe.com/files/docs/billing/taxes/example-inclusive-tax-with-discount.pdf)

In the case where you have both inclusive and exclusive tax, the two rules apply together in the following steps for every line item:

- We calculate the inclusive tax amount based on the post-discounted amount by multiplying by the inclusive tax rate.

- We calculate the exclusive tax amount by multiplying the exclusive tax rate by the post-discounted amount, less the inclusive tax amount.

- We calculate the total amount due by summing the post-discounted amount and the exclusive tax amount (calculated in step 2).

Download example invoice PDF

[Download example invoice PDF](https://stripe.com/files/docs/billing/taxes/example-inclusive-and-exclusive-tax-with-discount.pdf)

## Tax reporting and remittance

Any business collecting taxes ultimately needs to remit tax to the appropriate government.

See Tax reporting and filing to learn more.

[Tax reporting and filing](/tax/reports)

From the Dashboard’s Tax Rates list page, you can export data files required for tax reporting calculations.

[Tax Rates list](https://dashboard.stripe.com/test/tax-rates/)

Stripe Billing provides two different levels of tax report export files:

- Invoice line item tax export — A lower-level export, this includes details down to the line item level, including per-line-item tax rates, inclusive/exclusive, amounts, and so on.

- Invoice totals export — Shows the aggregate tax collected on the invoice as a whole, including adjustments for any refunds.

For remittance reporting, use the line-item tax export to sum all amounts paid for all tax rates used. To factor in any refunds you will also need to pivot against the Invoice totals export.

## Migrate to tax rates

If you’re using the deprecated tax_percent, tax_info, tax_info_verification, and business_vat_id fields, review the following options to migrate to tax rates and Customer Tax IDs for better tax collection and reporting (remittance) tools.

[Customer Tax IDs](/billing/customer/tax-ids)

Existing tax_percent uses have been automatically converted into tax rates, and your invoices and subscriptions have been updated to reference the new objects through default_tax_rates.

[tax rates](/api/tax_rates)

[default_tax_rates](/api/invoices/create#create_invoice-default_tax_rates)

This means that if you had previously been setting a tax_percent of 15% on your invoices, Stripe has created a new 15% tax rate object for you (although it lacks details such as a customer facing display name or a jurisdiction). If you continue to set the tax_percent to 15%, Stripe dynamically creates a 15% tax rate for you to aid your migration. This works exactly as it had before.

You can manage your full list of tax rates in the Dashboard’s tax rates page.

[tax rates](https://dashboard.stripe.com/tax-rates)

For new invoices or subscriptions, we recommend performing the full update to use tax rates.

[full](#full)

If you take no action, your integration continues to work as it does today. As mentioned above, existing uses of tax_percent are made to look as if they used tax rates.

As your tax rates lack a display_name and jurisdiction, tax reporting might not be very useful. Invoices and receipts render a generic name for these rates—“Tax”.

[display_name](/api/tax_rates/object#tax_rate_object-display_name)

[jurisdiction](/api/tax_rates/object#tax_rate_object-jurisdiction)

Use the Dashboard to edit pre-existing tax rates so taxes work for pre-existing invoices.

- For tax rates that have been migrated for you, edit the display_name to have a useful user-facing name. Display names are displayed to your customers on generated invoices and receipts (for example, “UST” for German VAT and “HST” for Ontario’s Harmonized Sales Tax).

[display_name](/api/tax_rates/object#tax_rate_object-display_name)

- Set the jurisdiction to store an associated tax jurisdiction (for example, “DE” for Germany or “NL Amsterdam” for the city of Amsterdam).

[jurisdiction](/api/tax_rates/object#tax_rate_object-jurisdiction)

Invoices and receipts show the display_name of tax rates. When determining how much tax to remit, you can group by jurisdiction.

We no longer recommend using the tax_percent field for new invoices, and to use tax rates instead. Apply tax rates to invoices and subscriptions. This allows you to add multiple tax rates per line item and invoice, display the correct name for tax rates and summaries on generated invoices and receipts, and improved tax reporting.

[invoices](/invoicing/taxes/tax-rates)

[subscriptions](/billing/taxes)

The Customer’s tax_info, tax_info_verification, and business_vat_id fields are deprecated in favor of Customer Tax IDs. The Tax ID object provides:

[Customer Tax IDs](/api/customers/object#customer_object-tax_ids)

[Tax ID](/api/customer_tax_ids)

- Multiple tax IDs on a Customer.

- Support for more tax ID types, such as EU VAT, NZ GST, and AU ABN.

- Automatic validation of EU VAT numbers against the European Commission’s VAT Information Exchange System (VIES) database.

[European Commission’s VAT Information Exchange System (VIES)](http://ec.europa.eu/taxation_customs/vies/)

- Automatic validation of Australian Business Numbers (ABNs) against the Australian Business Register (ABR).

[Australian Business Register (ABR)](https://abr.gov.au/)

- Associate a country with a tax ID (for example, a German EU VAT number).

See Customer Tax IDs for more information.

[Customer Tax IDs](/billing/customer/tax-ids)

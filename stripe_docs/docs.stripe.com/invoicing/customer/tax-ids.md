# Customer tax IDs

Need another tax ID type? Request additional Tax ID types by emailing stripe-tax@stripe.com.

[stripe-tax@stripe.com](mailto:stripe-tax@stripe.com?subject=Request)

Displaying a customer’s tax ID on invoice documents is a common requirement that you can satisfy by adding tax IDs to customers. A customer’s tax IDs display in the header of invoice and credit note PDFs.

[invoice](/api/invoices)

## Supported Tax ID types

Currently, Stripe supports the following Tax ID types in the following regions:

## Validation

You’re responsible for the accuracy of customer information including their tax ID number. The invoice includes the customer tax ID whether or not it’s valid.

Stripe provides automatic validation to help determine ​​if the formatting is correct when you add the ID to our system. You can see the results of the validation in the Dashboard along with other customer information, including details returned from the government databases, and the registered name and address. However, we don’t continue to validate them over time. ​​If automatic validation isn’t available, you must manually verify these IDs.

Stripe automatically validates all Australian Business Numbers (ABNs) with the Australian Business Register (ABR).

[Australian Business Register (ABR)](https://abr.gov.au/)

Stripe also automatically validates all European Value-Added-Tax (EU VAT) numbers with the European Commission’s VAT Information Exchange System (VIES). This process only validates whether or not the tax ID is valid—you still need to verify the customer’s name and address to make sure it matches the registration information.

[European Commission’s VAT Information Exchange System (VIES)](http://ec.europa.eu/taxation_customs/vies/)

VIES validation usually takes only a few seconds, but depending on the availability of various government databases, might take longer. Stripe automatically handles VIES downtime and attempts retries.

Stripe automatically validates all UK Value-Added-Tax (GB VAT) numbers with the United Kingdom’s Revenue & Customs (HMRC). This process only validates whether or not the tax ID is valid—you still need to verify the customer’s name and address to make sure it matches the registration information.

[United Kingdom’s Revenue & Customs (HMRC)](https://www.gov.uk/)

HMRC validation usually takes only a few seconds, but depending on the availability, might take longer. Stripe automatically handles HMRC downtime and attempts retries.

Use these magic tax IDs to trigger certain verification conditions in test mode. The tax ID type must be either the EU VAT Number or Australian Business Number (ABN).

Because this validation process happens asynchronously, the customer.tax_id.updated webhook notifies you of validation updates.

[customer.tax_id.updated](/api/events/types#event_types-customer.tax_id.updated)

Hover over a customer’s EU VAT number to display their VIES information.

The Dashboard displays the results of the validation within the customer details, including information returned from the government databases, and the registered name and address.

When automatic validation isn’t available, you must manually verify these IDs.

## Managing

You can manage tax IDs in the Dashboard, with the customer portal, or the Tax ID API.

[customer portal](/customer-management)

[Tax ID API](/api/customer_tax_ids)

To add a tax ID:

- Navigate to the Customers page.

[Customers](https://dashboard.stripe.com/customers)

- Click Actions > Edit information.

- Scroll down to see the Tax Status and Tax ID fields.

- Click Add another ID to add a row to the tax ID list, where you can select the ID type and value.

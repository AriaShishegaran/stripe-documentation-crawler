# Collect customer addresses

Stripe Tax requires your customer’s location to automatically calculate tax. This requirement applies even if you don’t register to collect taxes. This guide helps you decide what address information to collect from your customer and how to handle regional differences.

[register to collect taxes](/tax/registering)

## Supported address formats

Each billing and shipping address has the fields line1, line2, city, state, postal_code, and country. The tables below describe the address formats supported when calculating tax.

- line1: 27 Fredrick Ave

- city: Brothers

- state: OR

- postal_code: 97712

- country: US

Full address

A full address includes at least a line1 (street address), city, state, postal code, and country.

The address is matched to the closest address or street in the US Postal Service address database. If a match isn’t found, we use the geographical center (average location of addresses) of the 5-digit postal code as a fallback.

9-digit postal code:

- postal_code: 97712-4918

- country: US

5-digit postal code:

- postal_code: 97712

- country: US

Country and postal code

If you provided a 5-digit or 9-digit postal code, we calculate tax at the geographical center (average location of addresses) of the 5-digit postal code area. Check that this is suitable for your business.

[suitable for your business](/tax/customer-locations#us-postal-codes)

- state: OR

- country: US

Country and state

We can’t calculate tax for US customers with only an ISO country code and state code.

[country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)

[state code](https://en.wikipedia.org/wiki/ISO_3166-2)

- country: US

Country

We can’t calculate tax for US customers with only an ISO country code.

[ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)

Use one of the above address formats to ensure that we can consistently recognize your customer addresses. The country field must always be a valid ISO country code.

[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1)

## Which customer address we use

Stripe Tax uses a single address as your customer’s location when calculating tax. We choose the same address whether you’re selling a digital product, a service, or a shipped good.

We use the first viable item in the list below to determine your customer’s location:

- We use your customer’s shipping address if it’s non-empty. Using an address that isn’t precise enough to calculate tax returns a status of requires_location_inputs.

[shipping address](/api/customers/object#customer_object-shipping)

- We use your customer’s billing address if it’s non-empty. Using an address that isn’t precise enough to calculate tax returns a status of requires_location_inputs.

[billing address](/api/customers/object#customer_object-address)

- If the transaction is tied to a payment method with full billing details we use that billing address.

[billing details](/api/payment_methods/object#payment_method_object-billing_details)

- If the billing details associated with the payment method are incomplete or missing, we assemble a billing address using the information provided, combined with details of the payment method itself (for example, using the country code of the credit card issuer to determine the country if the customer doesn’t provide it).

- Otherwise, we geolocate the Customer IP address and use that location as your customer’s location. We store this geolocation result and reuse it for future transactions involving the same customer.

[IP address](/api/customers/object#customer_object-tax-ip_address)

The payment method tied to the transaction is the first one that’s set in this list:

- The Invoice default payment method

[Invoice](/api/invoices)

[default payment method](/api/invoices/object#invoice_object-default_payment_method)

- The Subscription default payment method

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

- The Customer default payment method

[default payment method](/api/customers/object#customer_object-invoice_settings-default_payment_method)



## Handling unrecognized locations

Invoice finalization fails and payment isn’t attempted for invoices with automatic_tax[enabled]=true if the customer location is unrecognized. When finalization happens during an API request, such as creating a subscription or sending an invoice, Stripe returns a customer_tax_location_invalid error. When finalization happens asynchronously, for example when a subscription renews, Stripe sends an invoice.finalization_failed webhook and the invoice remains in the draft state.

[creating a subscription](/api/subscriptions/create#create_subscription-automatic_tax-enabled)

[sending an invoice](/api/invoices/send)

[customer_tax_location_invalid](/error-codes#customer-tax-location-invalid)

[invoice.finalization_failed](/api/events/types#event_types-invoice.finalization_failed)

How you correct customer_tax_location_invalid errors depends on whether you collect a recognized customer location. If you do, keep Stripe Tax enabled. If you don’t, disable Stripe Tax for the affected invoices and subscriptions.

To collect a recognized customer location:

- Update the address of the affected customer. Provide enough location details for your customer. For example, a country and state code alone aren’t enough to calculate tax in the US.

[Update the address](/api/customers/update#update_customer-address)

- Confirm that the customer location is recognized by ensuring the value of customer.tax.automatic_tax is supported or not_collecting.

[customer.tax.automatic_tax](/api/customers/object#customer_object-tax-automatic_tax)

- Finalize the affected invoice.

[Finalize](/api/invoices/finalize)

Alternatively, to progress without a recognized customer location:

- Update the affected invoice so automatic_tax[enabled]=false.

[Update the affected invoice](/api/invoices/update#update_invoice-automatic_tax)

- Update the affected subscription so automatic_tax[enabled]=false.

[Update the affected subscription](/api/subscriptions/update#update_subscription-automatic_tax-enabled)

- Finalize the affected invoice.

[Finalize](/api/invoices/finalize)

When an invoice can’t be finalized due to an unrecognized customer location, Stripe sends an invoice.finalization_failed webhook with automatic_tax[status] = 'requires_location_inputs'. When using subscriptions, we recommend listening for subscription and invoice related events because most activity happens asynchronously.

[events](/billing/subscriptions/webhooks)

To prevent invoices failing finalization due to an unrecognized customer location:

- Before updating an existing subscription from automatic_tax[enabled]=false to automatic_tax[enabled]=true, verify that the customer has a recognized location. If the customer’s location is unrecognized, update and verify it before enabling Stripe Tax on the subscription.

[updating an existing subscription](/api/subscriptions/update#update_subscription-automatic_tax-enabled)

[customer has a recognized location](/tax/subscriptions/update#customer-locations)

- After updating a customer that has a subscription with automatic_tax[enabled]=true, verify that the value of customer.tax.automatic_tax is supported or not_collecting.

[updating a customer](/api/customers/update)

We recommend collecting a full address from your customers for the most accurate tax calculation result, and to minimize how often you can’t collect tax.

## Region-specific considerations

The complexity of taxes vary widely by region. Most countries have a single set of tax rules for the entire country. In the United States, sales tax rules and rates vary by state, with some states having hundreds of districts setting their own rates. In Canada, the type of tax and tax rate vary by province.

Stripe Tax supports calculating sales tax with only a basic 5-digit US postal code. The country field must be the ISO country code “US”. We use the point at the geographical center of the postal code area, which represents the average location of addresses within the postal code area, as your customer’s location. The tax rate at this point might differ from the tax rate at your customer’s full address. Whether a postal code alone is sufficient to identify the correct tax rates to impose varies by state.

[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1)

We recommend against relying on a postal code alone in the following states: Arizona, Colorado, Oklahoma, Alabama, Missouri, Texas, Illinois, Washington, Kansas, New Mexico, Louisiana, Arkansas, California, Alaska, South Dakota, North Dakota, Utah, Nebraska, and West Virginia.

We recommend collecting a full address in states where you’re registered to collect local sales taxes.

Because the location of an IP address could be some distance from the actual location of your customer, don’t use an IP address alone for determining how much tax to collect. Instead, use the upcoming invoice endpoint to show them an estimate of the tax they’ll pay before collecting a billing or shipping address.

[upcoming invoice](/api/invoices/upcoming#upcoming_invoice-customer_details-tax-ip_address)

In Europe, tax authorities in each country impose tax, not state or local authorities. The tax rate for the country doesn’t apply in a small number of areas, even though they’re physically located in a country that imposes tax. For example, the Italian postal code “00120” identifies Vatican City, where Italian VAT doesn’t apply.

Collect your customer’s postal code or state to enable Stripe Tax to determine when your customer is located in an excluded territory.

See the list of excluded territories supported by Stripe Tax.

[list of excluded territories](/tax/zero-tax#excluded-territories)

In order for Stripe Tax to determine the applicable tax rate and collect tax in Canada, you need to collect the customer’s province or postal code.



## See also

- Understanding zero tax

[Understanding zero tax](/tax/zero-tax)

- Available tax codes

[Available tax codes](/tax/tax-codes)

- How tax is calculated

[How tax is calculated](/tax/calculating)

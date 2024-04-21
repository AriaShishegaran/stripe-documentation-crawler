# Collect taxes for recurring payments

Stripe Tax allows you to calculate the tax to collect on your recurring payments when using Stripe Billing. You can create new subscriptions or add Stripe Tax to existing subscriptions, and examine any potential impact to the amount on your customer’s upcoming invoice. Stripe Tax is natively integrated with Stripe Billing and automatically handles tax calculation with your pricing model (for example, sub-cent, package), prorations, discounts, trials, and more. This guide assumes you’re setting up Stripe Tax and Billing for the first time.

To update existing subscriptions, reference the Update existing subscriptions guide.

[Update existing subscriptions](/tax/subscriptions/update)

Log in or sign up for Stripe to activate Stripe Tax.

[Log in](https://dashboard.stripe.com/settings/tax)

[sign up](https://dashboard.stripe.com/register)

[Update your products and prices](#product-and-price-setup)

## Update your products and prices

Stripe Tax uses information stored on the Products and Prices APIs to determine the right rates and rules to apply when calculating tax. Update the products and prices you use to include:

[Products](/api/products)

[Prices](/api/prices)

- Tax behavior: The tax behavior on a price can be either inclusive or exclusive. This determines how the buyer sees the tax. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.Setting the tax behavior explicitly on a price is optional, if you set up the default tax behavior in the Stripe Tax settings. You can override the default tax behavior setting by setting a tax behavior on a price.

Tax behavior: The tax behavior on a price can be either inclusive or exclusive. This determines how the buyer sees the tax. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

[Tax behavior](/tax/products-prices-tax-codes-tax-behavior#tax-behavior)

Setting the tax behavior explicitly on a price is optional, if you set up the default tax behavior in the Stripe Tax settings. You can override the default tax behavior setting by setting a tax behavior on a price.

[set up the default tax behavior](/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional))

[Stripe Tax settings](https://dashboard.stripe.com/login?redirect=%2Fsettings%2Ftax)

- (Optional) Tax code: A tax code is a classification of your product or service for Stripe Tax that makes sure we apply the correct tax rate to your transactions. Some examples include “Audio book,” “Gift card,” or “Software as a service.” If you don’t set the tax code, Stripe Tax uses the preset tax settings.

(Optional) Tax code: A tax code is a classification of your product or service for Stripe Tax that makes sure we apply the correct tax rate to your transactions. Some examples include “Audio book,” “Gift card,” or “Software as a service.” If you don’t set the tax code, Stripe Tax uses the preset tax settings.

[Tax code](/tax/products-prices-tax-codes-tax-behavior)

[tax settings](https://dashboard.stripe.com/login?redirect=%2Fsettings%2Ftax)

You can’t change tax_behavior after you set it to one of “exclusive” or “inclusive.” You can create a new price and archive the current one instead.

If you don’t want to create your products and prices upfront, you can pass price_data.tax_behavior and product_data.tax_code when creating subscriptions.

Learn more about Products, prices, tax codes, and tax behavior.

[Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior)

This guide uses an e-magazine as an example of a product with a recurring payment.

First, create a Price on your server with a monthly charge for a new Product named “My Product”. For tax purposes you add two extra fields:

[Price](/api/prices)

[Product](/api/products)

- tax_behavior on the Price object. Set to inclusive or exclusive. This is a required field if you’re using Stripe Tax with Subscriptions.

- tax_code on the Product object. A Stripe tax code, which maps to a product tax code. Consult our list of tax codes for more information.

[tax code](/api/tax_codes)

[list of tax codes](/tax/tax-codes)

Record the product ID for the product. It looks like this:

Use the product ID to create a price.

When price_data.tax_behavior is set to exclusive, tax is added onto the subtotal amount you specify. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays will never change, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

Record the price ID so you can use it in subsequent steps. It looks like this:

[Create a customerServer-side](#create-a-customer)

## Create a customerServer-side

When a user subscribes to your website, create a Customer on your server.

[Customer](/api/customers)

When creating a customer, you can send us a description and the payment method only. However, the more information you send us, the better the tax calculation can identify the location of your customer and tax them accordingly. We recommend populating the customer.address field. Expand the tax field to confirm the location Stripe Tax has identified for your customer.

[Expand](/api/expanding_objects)

You can either add a country and a postal code:

Or, ideally, add a complete billing address:

Or, only an IP address:

The expanded tax field indicates the computed tax location (using the address first, falling back on the given IP address) and if the customer is compatible with automatic tax calculation:

The value of automatic_tax has four possible states:

[add a new registration](/tax/registering)

[Create a subscriptionServer-side](#create-a-subscription)

## Create a subscriptionServer-side

Now that the Customer is set up for tax calculation, you can create a Subscription on your server with the customer and their selected plan. To enable automatic tax calculation on subscriptions, set the automatic_tax[enabled] parameter to true:

Setting this parameter causes all subsequent Invoices to be created with automatic tax calculations activated.

[Invoices](/api/invoices)

To inspect the results of the latest tax calculation, retrieve the latest Invoice of a Subscription. You can do this by expanding the latest_invoice field on any Subscription request, as in the examples above. You can retrieve the tax amounts from the tax and total_tax_amounts fields on the latest invoice, and also from the per-line item tax_amounts fields.

If Stripe Tax does not have enough information to determine the customer’s location, a customer_tax_location_invalid error is returned.

[customer_tax_location_invalid](/error-codes#customer-tax-location-invalid)

[Collect payment information to activate the subscriptionClient-side](#collect-payment)

## Collect payment information to activate the subscriptionClient-side

To complete payment of the first invoice and activate the subscription, use stripe.confirmCardPayment when your customer submits the form.

[invoice](/api/invoices)

The subscription automatically becomes active upon payment. See our Subscriptions with Elements guide for more details on setting up your checkout page.

[Subscriptions with Elements guide](/billing/subscriptions/build-subscriptions?ui=elements#collect-payment)

[Handling location validation](#handling-location-validation)

## Handling location validation

Stripe Tax requires a recognized customer location to calculate tax.

[recognized customer location](/tax/customer-locations)

We recommend validating a customer’s automatic_tax status before attempting to create or update a subscription or one-off draft invoice with automatic_tax[enabled]=true.

[invoice](/api/invoices)

Creating or updating a subscription or invoice behaves the following way when the customer location is unrecognized:

[customer location is unrecognized](/tax/customer-locations#handling-errors)

- Creating or updating a subscription that causes an immediate invoice and payment attempt errors with an HTTP status 400 response.

- Updating a subscription that does not cause an immediate invoice or payment attempt returns an HTTP status 200 response. However, the customer location validation happens later asynchronously when the invoice is finalized. If the customer location is invalid during invoice finalization, Stripe sends a invoice.finalization_failed webhook. If you don’t take any action, the invoice remains in a draft state, regardless of the value of auto_advance.

- Creating or updating a draft invoice (either within the short window after a subscription cycle, or for a one-off invoice) updates the invoice’s automatic_tax.status to requires_location_inputs. You can then either update the customer object to correct the address, and then update or finalize the invoice, or turn off automatic tax calculation. If you don’t take any action, the invoice remains in a draft state, regardless of the value of auto_advance.

If tax calculation fails due to an unrecognized customer location on a recurring Subscription Invoice, Stripe sends a invoice.finalization_failed webhook when attempting to finalize the invoice. Keep this in mind when updating the location details of your customer.

We recommend listening for Subscription-related events (for example, invoice finalization failures) with webhooks because most activity happens asynchronously.

[webhooks](/billing/subscriptions/webhooks)

[Previewing a price before creating a customer or subscriptionOptional](#preview-price)

## Previewing a price before creating a customer or subscriptionOptional

Stripe also provides an endpoint for previewing an upcoming invoice for a subscription. You can use this endpoint to preview the initial invoice for a new subscription:

[invoice](/api/invoices)

If you haven’t created a Customer yet, but you’ve collected your customer’s billing information, you can use the customer_details parameter in the place of a Customer ID:

When previewing the first invoice for a subscription, the subscription ID in the response won’t point to a valid subscription.

You can also use this endpoint if you have an ongoing subscription without taxes enabled and would like to preview what the upcoming invoice would look like if you were to enable automatic tax.

## See also

- Update existing subscriptions

[Update existing subscriptions](/tax/subscriptions/update)

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)

- Calculate tax in your custom checkout flow

[Calculate tax in your custom checkout flow](/tax/custom)

# Automatically collect tax on Checkout sessions

Stripe Tax automatically calculates the taxes on all purchases and subscriptions accumulated during a Checkout session. If you haven’t integrated with Checkout, you must complete the integration using the Accept a Payment guide.

[subscriptions](/billing/subscriptions/creating)

[Accept a Payment guide](/checkout/quickstart)

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

If you don’t want to create your products and prices upfront, you can pass price_data.tax_behavior and product_data.tax_code when creating Checkout sessions.

Learn more about Products, prices, tax codes, and tax behavior.

[Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior)

[Create a Checkout Session](#create-session)

## Create a Checkout Session

After updating your products and prices, you’re ready to start calculating tax on your Checkout sessions. You can create sessions for one time and recurring purchases.

A customer’s tax rates come from their location, which Checkout assesses from the customer’s address. The address that Checkout uses to calculate taxes depends on whether the customer is new or existing, and whether you collect shipping addresses during the Checkout Session:

[customer_update[address]=auto](/api/checkout/sessions/create#create_checkout_session-customer_update-address)

If you wish to ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must require collecting a shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12.

[Calculating tax for new customers](#new-customers)

## Calculating tax for new customers

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves billing address and shipping information. For tax collection purposes, Checkout uses billing and shipping addresses to determine the customer’s location.

Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Calculating tax for existing customersOptional](#existing-customers)

## Calculating tax for existing customersOptional

To calculate tax on Checkout sessions created for existing customers, you can set the automatic_tax[enabled] parameter to true when creating the session. You can either base tax calculations on the customer’s existing addresses or new addresses collected during the session:

If you’ve already collected the addresses of existing customers, you can base tax calculations on those addresses rather than the addresses collected during checkout:

- The customer address that Checkout uses for taxes: If available, Checkout uses the customer’s saved shipping address to calculate taxes. Otherwise, Checkout uses the customer’s saved billing address to calculate taxes.

The customer address that Checkout uses for taxes: If available, Checkout uses the customer’s saved shipping address to calculate taxes. Otherwise, Checkout uses the customer’s saved billing address to calculate taxes.

[shipping address](/api/customers/object#customer_object-shipping-address)

[billing address](/api/customers/object#customer_object-address)

- Customer address requirements: When using existing addresses for taxes, the customer must either have a valid shipping address or billing address saved. You can see whether or not a customer’s saved addresses are valid by checking the customer’s customer.tax.automatic_tax property. If the property is supported or not_collecting, it means the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

Customer address requirements: When using existing addresses for taxes, the customer must either have a valid shipping address or billing address saved. You can see whether or not a customer’s saved addresses are valid by checking the customer’s customer.tax.automatic_tax property. If the property is supported or not_collecting, it means the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

[shipping address](/api/customers/object#customer_object-shipping-address)

[billing address](/api/customers/object#customer_object-address)

[customer.tax.automatic_tax](/api/customers/object#customer_object-tax-automatic_tax)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

You can configure Checkout to save new billing or shipping addresses to a customer. In this case, Checkout calculates tax using the address entered during checkout.

- The address that Checkout uses for taxes: If you collect shipping addresses, Checkout uses the shipping address entered during the session to calculate taxes. Otherwise, Checkout uses the billing address entered during the session to calculate taxes.

The address that Checkout uses for taxes: If you collect shipping addresses, Checkout uses the shipping address entered during the session to calculate taxes. Otherwise, Checkout uses the billing address entered during the session to calculate taxes.

[collect shipping addresses](/api/checkout/sessions/create#create_checkout_session-shipping_address_collection)

- Where Checkout saves the addresses collected during checkout: If you collect shipping addresses, Checkout saves the shipping address entered during the session to the customer’s customer.shipping.address property. Otherwise, Checkout saves the billing address entered during the session to the customer’s customer.address property. In both cases, the address used for taxes overrides any existing addresses.

Where Checkout saves the addresses collected during checkout: If you collect shipping addresses, Checkout saves the shipping address entered during the session to the customer’s customer.shipping.address property. Otherwise, Checkout saves the billing address entered during the session to the customer’s customer.address property. In both cases, the address used for taxes overrides any existing addresses.

[collect shipping addresses](/api/checkout/sessions/create#create_checkout_session-shipping_address_collection)

[customer.shipping.address](/api/customers/object#customer_object-shipping-address)

[customer.address](/api/customers/object#customer_object-address)

If you collect shipping addresses with Checkout, set the customer_update[shipping] property to auto so that you copy the shipping information from Checkout to the customer.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

If you don’t collect shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the customer_update[address] property to auto so that you copy the newly-entered address onto the provided customer.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Check the responseOptional](#check-the-response)

## Check the responseOptional

To inspect the results of the latest tax calculation, you can read the tax amount calculated by Checkout from the total_details.amount_tax on the Checkout Session resource. Additionally, the tax outcome for each payment is available when viewing a payment in the Dashboard.

[total_details.amount_tax](/api/checkout/sessions/object#checkout_session_object-total_details)

[viewing a payment](https://dashboard.stripe.com/test/payments)

## See also

- Determining customer locations

[Determining customer locations](/tax/customer-locations)

- Checkout and tax IDs

[Checkout and tax IDs](/tax/checkout/tax-ids)

- Reporting and filing

[Reporting and filing](/tax/reports)

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)

- Calculate tax in your custom checkout flow

[Calculate tax in your custom checkout flow](/tax/custom)

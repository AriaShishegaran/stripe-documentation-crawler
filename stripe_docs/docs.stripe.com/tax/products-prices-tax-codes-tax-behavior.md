# Specify product tax codes and tax behavior

Log in or sign up for Stripe to activate Stripe Tax.

[Log in](https://dashboard.stripe.com/settings/tax)

[sign up](https://dashboard.stripe.com/register)

Stripe Tax uses product tax codes (PTCs) to associate products with their applicable tax rates, which might be lower or higher in different cities or countries. Assign each of your products a tax code to automatically apply the rate and other taxability rules.

[Assign each of your products a tax code](/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)

If a product doesn’t fit any of the specific codes, use one of the codes with “General” in its name to apply the standard rate of the jurisdiction. See our list of available tax codes.

[list of available tax codes](/tax/tax-codes)

When activating Stripe Tax you can set two types of preset tax codes: one for products and one for shipping. You can set both in the Tax settings in the Dashboard.

[Tax settings](https://dashboard.stripe.com/settings/tax)

The tax settings showing the preset tax codes, and the default shipping tax code.

The preset product tax code represents your product or service in Stripe Tax. We use the preset if you don’t explicitly specify a tax_code on your products or in product_data on your transactions. As you process payments, we also use the preset tax code to display the tax thresholds you might be approaching or have exceeded, under the Monitor tax thresholds section in your tax settings.

[products](/api/products)

If you sell multiple different product types (for example, SaaS and e-books), you could use test mode to change your preset tax code and review the impact of different product types on the Monitor tab.

The preset shipping tax code  represents the tax treatment for shipping fees when charged. We use this if you don’t explicitly specify a tax_code on a shipping rate. Stripe Tax allows you to change the default shipping treatment to Nontaxable if you don’t want to charge any tax on shipping fees. We recommend you leave the default as “Shipping” to ensure the correct tax is always charged.

To charge tax on shipping for recurring payments, you can create a Product or pass product_data for a line item called “shipping” and select the shipping tax_code.

The taxability of shipping can vary by US state and country.

## Tax behavior

You must specify a tax_behavior on a price, or a default tax behavior in the tax settings in the Dashboard, which determines how tax is presented to the buyer. This allows you to localize your checkout depending on the market. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

You can define a default tax behavior that applies to every price that has no tax behavior defined. You can setup the default tax behavior under the Stripe Tax settings.

[Stripe Tax settings](https://dashboard.stripe.com/settings/tax)

After you set the default tax behavior, all prices that don’t have a tax_behavior defined, use this setting and are ready for Stripe Tax. The options for the default tax behavior are:

- Inclusive: Inclusive tax is already included in the price. For example, a product has the price defined as 5.00 USD. The final price the customer pays is 5.00 USD.

- Exclusive: Exclusive tax is added on top of the price. For example, a product has the price defined as 5.00 USD. The tax charged on this product could be 10% and would result in a final price of 5.50 USD. (Tax rates might differ—this is only an explanatory example.)

- Inferred by currency: The tax behavior is based on the price that’s chosen for a product. For the currencies USD and CAD the tax behavior is exclusive. For all other currencies the tax behavior is inclusive. This also works with multi-currency Prices.

[multi-currency Prices](/products-prices/pricing-models#multicurrency)

To override this setting for an individual price, set a tax behavior on a price.

[set a tax behavior on a price](#setting-tax-behavior-on-a-price-(optional))

## Setting tax behavior on a price (optional)

You can set the tax behavior for a Price when creating it with the Dashboard or the API. When creating a Price in the Dashboard, you can inspect the impact of your pricing model on your revenue.

[Price](/api/prices)

You can’t change tax_behavior after it’s been set to one of “exclusive” or “inclusive”.

To create a Price with tax_behavior through the API, it might look like this:

For a multi-currency Price, use the currency_options.<currency>.tax_behavior parameter to set different tax behaviors for different currencies.

[multi-currency Price](/products-prices/pricing-models#multicurrency)

[currency_options.<currency>.tax_behavior](/api/prices/create#create_price-currency_options-tax_behavior)

In some cases, you might want to use a custom price that hasn’t been pre-configured. You can pass in price_data instead of a price ID. For example, accepting a one time payment for a custom price might look like this:

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

## Setting a tax code on a product (recommended)

When creating Products in the Dashboard you can set your tax_code in the dropdown by searching for any available tax code. If you don’t, Stripe Tax uses the preset tax code defined on the Dashboard. If a product could fit multiple codes, for example, a SaaS product used for personal or business use depending on the type of customer, we recommend creating two separate products in Stripe and assigning the appropriate code to each.

[tax code](/tax/tax-codes)

[Dashboard](https://dashboard.stripe.com/settings/tax)

To create a Product with tax_code using the API, it might look like this:

In some cases, you might want to use a custom product that hasn’t been pre-configured. You can pass in product_data instead of a product ID. For example, accepting a one time payment for a custom product might look like this:

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

## Creating a shipping rate with tax code (optional)

Checkout payment mode allows you to set shipping rates and charge tax on shipping. You can automatically calculate tax on shipping charges by setting the tax code on the shipping rate in the Dashboard or API.

[API](/api/shipping_rates)

## See also

- Checkout and Tax

[Checkout and Tax](/tax/checkout)

- Invoicing and Tax

[Invoicing and Tax](/tax/invoicing)

- Determining customer locations

[Determining customer locations](/tax/customer-locations)

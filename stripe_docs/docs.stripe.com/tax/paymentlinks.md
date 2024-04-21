# Automatically collect tax on Payment Links

Log in or sign up for Stripe to activate Stripe Tax.

[Log in](https://dashboard.stripe.com/settings/tax)

[sign up](https://dashboard.stripe.com/register)

You can use Stripe Tax with Payment Links to automatically calculate and collect tax on a payment page and share a link to it with your customers, without writing any code.

[Payment Links](https://stripe.com/payments/payment-links)

[Set up Stripe Tax](#setup)

## Set up Stripe Tax

Before collecting tax on your Payment Links, you need to configure your tax settings within the Dashboard.

[configure your tax settings](/tax/set-up)

[Dashboard](https://dashboard.stripe.com/settings/tax)

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

Learn more about Products, prices, tax codes, and tax behavior.

[Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior)

[Create a link](#create-link)

## Create a link

In the Dashboard, open the Payment Links page and click + New. Then:

[Payment Links](https://dashboard.stripe.com/payment-links)

- Select +Add a new product.

- Fill out the product details.

- Click Add product.

- Click Next.

- Click Create link.

[Enable Stripe Tax](#enable-stripe-tax)

## Enable Stripe Tax

We enable Stripe Tax automatically on all Payment Links unless you switch off the toggle at the bottom of the tax settings page. In the Payment Link configuration page, under the Advanced options section, you’ll see that Collect tax automatically is already on.

[Payment Link configuration page](https://dashboard.stripe.com/payment-links/create)

## See also

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)

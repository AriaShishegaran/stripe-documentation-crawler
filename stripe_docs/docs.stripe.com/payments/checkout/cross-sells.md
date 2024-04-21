# Cross-sells

A cross-sell is a product that you can add to an order using Checkout.

Cross-sells enable customers to optionally purchase other related products using Checkout. Cross-sells can increase your average order value and revenue.

For Checkout to offer a product as a cross-sell, the product must meet the following criteria:

- The product must be associated with only a single Price.

[Price](/api/prices/object#price_object-product)

- The currency of the cross-sell product’s price must match the currency of the other prices in the Checkout Session.

[currency](/api/prices/object#price_object-currency)

- If the cross-sell product’s price type is recurring, the Checkout Session must be in subscription mode and its recurring interval must match the recurring interval of the other prices in the Checkout Session.

[type](/api/prices/object#price_object-type)

- If you’re using subscription upsells, cross-sells only support products with non-recurring prices. For example, you can cross-sell a one-time setup fee while also upselling a monthly subscription to annual billing.

[subscription upsells](/payments/checkout/upsells)

- If you’re using automatic taxes, cross-sells only support products with prices with specified tax behavior. You can either set tax behavior for a price or set the default tax behavior for all prices under Tax Settings in the Stripe Dashboard.

[automatic taxes](/tax)

[tax behavior](/tax/products-prices-tax-codes-tax-behavior#tax-behavior)

[set tax behavior for a price](/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional))

[Tax Settings](https://dashboard.stripe.com/test/settings/tax)

## Create a cross-sell

Configure a cross-sell on the Product detail page.

You can configure a cross-sell in the Dashboard on the Product details page. Visit the Product details page for the product from which you want to cross-sell another complementary product. You’ll see a Cross-sells section with a dropdown menu containing your other Products. Select a Product with a single Price. After you configure it, all eligible Checkout Sessions cross-sell the product selected from the dropdown menu. For example, a customer purchasing a ‘Togethere Professional’ subscription would be cross-sold the ‘Professional Services: Deployment’ product.

[Dashboard](https://dashboard.stripe.com/products?active=true)

## Checkout experience

In Checkout, buyers see an option to add the cross-sell to their purchase. If buyers add the cross-sell to the Checkout Session, they can also remove it. If they remove it, the option to add the cross-sell appears again.

The quantity of cross-sell line items cannot be adjusted. The current maximum is 1.

Customer preview.

## Retrieve Checkout Session line items

After a customer adds a cross-sell, the line_items for the Checkout Session update to reflect the addition. When fulfilling your order using the checkout.session.completed webhook, make sure to retrieve the line items.

[fulfilling your order](/payments/checkout/fulfill-orders#fulfill)

[retrieve the line items](/api/checkout/sessions/line_items)

## Remove a cross-sell

To remove a cross-sell, click the x next to it. After you remove it, the product won’t be offered to any new Checkout Sessions.

Remove a cross-sell.

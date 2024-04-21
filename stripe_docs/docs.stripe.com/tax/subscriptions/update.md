# Update existing subscriptions

Stripe Tax allows you to calculate the tax to collect on your transactions. It computes the taxes and adds them to the payment automatically, based on the product and the customer location.

[Stripe Tax](/tax)

When you integrate with Stripe Tax, you need to update existing subscriptions to make sure that tax is automatically calculated going forward. This guide assumes that you have existing, active subscriptions. Otherwise, see how to automatically collect tax on new subscriptions or learn more about subscriptions.

[collect tax on new subscriptions](/billing/taxes/collect-taxes)

[about subscriptions](/billing/subscriptions/overview)

Use the following high-level steps to update your active subscriptions to Stripe Tax:

- Activate Stripe Tax if you haven’t already.

[Activate Stripe Tax](#activate)

- Check customer locations. In some cases, you might need to update the locations.

[Check customer locations](#customer-locations)

- Update products and prices with tax codes and tax behaviors.

[Update products and prices](#products-prices)

- Update subscriptions to automatically calculate taxes on future invoices.

[Update subscriptions](#subs)

[invoices](/api/invoices)

- Confirm that you’ve updated the subscriptions correctly.

[Confirm](#confirm)

We’re developing a Payment Element integration that manages tax, discounts, shipping, and currency conversion. Read the Build a checkout page guide to learn more.

[Build a checkout page](/checkout/custom-checkout)

[Activate Stripe Tax](#activate)

## Activate Stripe Tax

First, you need to activate Stripe Tax. Read the set up guide to learn how.

[set up guide](/tax/set-up)

[Check customer locations](#customer-locations)

## Check customer locations

To correctly calculate tax, we need to know the customer’s location. After activating Stripe Tax, you can check their tax location status by using the Dashboard, the API, or Dashboard exports.

To check a customer’s tax location status through the Dashboard, go to the Customers page, select the customer, and expand the customer’s details. The tax location status (automatic_tax) has four possible statuses:

[Customers page](https://dashboard.stripe.com/customers)

[customer.address](/api/customers/update#update_customer-address)

[tax obligations](/tax/monitoring)

[add an active registration](/tax/registering)

[error](/error-codes)

In case the status=unrecognized_location you need to update the customer location with an address that Stripe Tax can use. In the Dashboard, you can go into the Customers page, select the customer, and change its billing or shipping address under Details.

[an address that Stripe Tax can use](/tax/customer-locations)

[Customers page](https://dashboard.stripe.com/customers)

For more information on which customer address is valid, how they’re used, or how to handle errors, see Collect customer addresses.

[Collect customer addresses](/tax/customer-locations)

[Update products and prices](#products-prices)

## Update products and prices

Your products and prices use the default tax behavior you assigned when activating Stripe Tax. If you’d prefer to update active products and prices to calculate tax independently, set a tax_code and tax_behavior. See the full list of available tax codes and the guide for setting up tax codes and tax behavior for more information. For more information about products and prices, including how to decide whether a price should be inclusive or exclusive, see the Tax Setup FAQ.

[available tax codes](/tax/tax-codes)

[guide for setting up](/tax/products-prices-tax-codes-tax-behavior)

[products and prices](/billing/taxes/collect-taxes#product-and-price-setup)

[Tax Setup FAQ](/tax/faq#set-up)

First, update any existing products with a tax_code. If you don’t explicitly define a tax_code on your product, Stripe Tax uses the preset product tax code from your settings.

Here’s how to update a Product with a tax_code using the API:

To update a Product with a tax_code in the Dashboard, go to the Products page, select a product to edit and, in the product information page, choose the tax code from the drop-down menu.

[Products page](https://dashboard.stripe.com/products?active=true)

Next, update the tax behavior for your prices.

You can’t change tax_behavior after it’s been set to one of exclusive or inclusive. If you want to change the tax behavior of a price, you need to create a new price with the desired behavior, and archive the old price.

Here’s how to update a price with the API:

To update a price with the Dashboard, go to the products page, select the product with the price you want to update, and select additional options in the price information section. In the Include tax in price drop-down menu, select the behavior you want to associate with the price.

[products page](https://dashboard.stripe.com/products)

[Update subscriptions](#subs)

## Update subscriptions

With your customers, products, and prices updated, you’re ready to update existing subscriptions.

Stripe Tax requires a recognized customer location to calculate tax for a subscription. Therefore, an invoice for a subscription with automatic_tax[enabled]=true can’t be finalized when the customer’s location is unrecognized. Payment can’t be collected if the invoice can’t be finalized. Read more about the behavior of subscriptions when the customer’s location is unrecognized.

[recognized customer location](/tax/customer-locations)

[behavior of subscriptions when the customer’s location is unrecognized](/tax/subscriptions#handling-location-validation)

To get a list of subscriptions that need to be updated, go to the subscriptions page, click Export, select All as the Date range,  and select All columns in the Columns drop-down menu. Then you can filter by Automatic Tax Enabled column in the CSV export.

[subscriptions page](https://dashboard.stripe.com/subscriptions)

How you update the subscriptions depends on their state:

- If your subscriptions don’t have existing tax rates, you only need to enable automatic tax.

[don’t have existing tax rates](#no-tax-rates)

- If your subscriptions have existing tax rates (at either the subscription or line-item level), you need to clear out any existing tax rates and enable automatic tax. To avoid creating prorated items, you can schedule this update.

[existing tax rates](#existing-tax-rates)

- If your subscriptions have subscriptions schedules, you need to remove instances of automatic_tax[enabled]=false in the subscription schedule plans.

[subscriptions schedules](#existing-subscription-schedules)

To update subscriptions that have no tax rates configured, set automatic_tax.enabled to true.

[update subscriptions](/api/subscriptions/update)

[tax rates](/billing/taxes/tax-rates)

[automatic_tax.enabled](/api/subscriptions/update#update_subscription-automatic_tax)

Setting automatic_tax.enabled=true activates automatic tax calculations for all subsequent invoices created for that subscription.

To do this through the Dashboard, update the subscription and turn on the Calculate tax automatically option.

To update subscriptions with tax rates set at the subscription level, you need to remove the tax rates before enabling automatic_tax. When you make the update:

[tax rates](/billing/taxes/tax-rates)

[subscription level](/billing/taxes/collect-taxes?tax-calculation=tax-rates#static-configuration)

- Pass an empty string in the default_tax_rates and tax_rates fields for each subscription item. Doing this clears out tax rates set at both the subscription (default_tax_rates) and line-item (tax_rates) levels.

[default_tax_rates](/api/subscriptions/update#update_subscription-default_tax_rates)

[tax_rates](/api/subscriptions/object#subscription_object-items-data-tax_rates)

[item](/api/subscriptions/object#subscription_object-items)

- Set automatic_tax.enabled to true.

[automatic_tax.enabled](/api/subscriptions/update#update_subscription-automatic_tax)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

To make this update through the Dashboard, edit the subscription, then enable the calculate tax automatically option. The Dashboard automatically calculates tax going forward and removes any existing tax rates. If you haven’t updated your prices to set tax_behavior, the Dashboard prompts you to update any missing details before you can update the subscription.

If you need to collect tax and any of your subscriptions include a subscription schedule that sets automatic_tax[enabled]=false, you must remove this parameter. To do this, update all phases of the subscription’s schedule by removing automatic_tax[enabled]=false and setting default_settings[automatic_tax][enabled]=true.

When you update a subscription schedule, you need to pass in all current and future phases. To do this, verify the set parameters, then enable Stripe Tax in the subscription schedule.

To update the subscription schedule after you obtain it, remove the automatic_tax[enabled]=false parameter, and pass down the other phases and parameters:

If you want to avoid creating a prorated item, you can schedule the update to occur at the start of the next cycle.

You can currently only schedule subscription updates with the API:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[Confirm updates](#confirm)

## Confirm updates

To confirm that you’ve properly updated your subscriptions, retrieve the upcoming invoice of a subscription and inspect the results of its tax calculation.

[upcoming invoice](/api/invoices/upcoming)

You can retrieve the tax amounts from the tax and total_tax_amounts fields on the upcoming invoice, and from the per-line-item tax_amounts fields. The invoice has an automatic_tax field showing the status of the calculation, with one of three possible statuses:

[tax](/api/invoices/object#invoice_object-tax)

[total_tax_amounts](/api/invoices/object#invoice_object-total_tax_amounts)

[tax_amounts](/api/invoices/line_item#invoice_line_item_object-tax_amounts)

[automatic_tax](/api/invoices/object#invoice_object-automatic_tax)

[customer.address](/api/invoices/object#invoice_object-customer_address)

## See also

- Create new subscriptions with Stripe Tax

[Create new subscriptions with Stripe Tax](/tax/subscriptions)

- Setting tax codes, products, and prices

[Setting tax codes, products, and prices](/tax/products-prices-tax-codes-tax-behavior)

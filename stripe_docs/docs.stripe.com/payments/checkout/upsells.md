# Subscription upsells

## Subscription upsells

Subscription upsells give customers the option to upgrade to a longer-term plan using Checkout. Upselling customers to longer subscription intervals (for example, from monthly to yearly) can increase your average order value and cash flow.

All recurring prices that aren’t metered are eligible to use subscription upsells. For any eligible price, you can set up a subscription upsell to another price that meets the following criteria:

- Prices must reference the same Product.

[Product](/api/prices/object#price_object-product)

- Prices must have the same currency.

[currency](/api/prices/object#price_object-currency)

- Prices must be recurring type.

[type](/api/prices/object#price_object-type)

- If your prices use tax behavior, their values must be identical.

[tax behavior](/api/prices/object#price_object-tax_behavior)

- If your price uses tiers, the value for up_to in each tier must be identical.

[tiers](/api/prices/object#price_object-tiers)

- If using quantity transformation, the values for divide_by and round must be identical.

[quantity transformation](/api/prices/object#price_object-transform_quantity)

## Create a subscription upsell

Configure a subscription upsell in the Dashboard on the Price detail page (to view the details for a Price, click on a Product, then click a price that’s been added to a Product). In the Upsells section, select an upsell price from the dropdown menu. Upsells immediately apply to eligible Checkout Sessions that use that price.

Configure a subscription upsell on the Price detail page.

## Checkout experience

During checkout, customers see an option to select the upsell with savings displayed, if applicable. For a Checkout Session to be eligible for upsells, it must:

- Be a subscription mode Checkout Session

- Have only one type=recurring price in the Checkout Session

- Have a valid configuration for the upsell price

Stripe calculates savings based on the amount the user would save in one billing cycle if they chose upsell pricing. For example, a monthly subscription of 100 USD that upsells to an annual subscription of 1000 USD shows savings of 200 USD. Savings are displayed as an amount or a percentage, depending on the character length of the savings.

Users can toggle between the initial price option and the upsell price option and then checkout.

Customer preview.

## Retrieve Checkout Session line items

After a customer selects an upsell, the line_items for the Checkout Session update to reflect the upsell price. When fulfilling your order using the checkout.session.completed webhook, make sure to retrieve the line items.

[fulfilling your order](/payments/checkout/fulfill-orders#fulfill)

[retrieve the line items](/api/checkout/sessions/line_items)

## Trial behavior

If a customer selects an upsell for a Checkout Session with a trial available, the trial length won’t change.

## Coupon behavior

If a coupon is passed into the discounts array of the Checkout Session, that coupon is also applied to the upsell price if a customer selects the upsell. For example, if a monthly subscription upsells to a yearly subscription, and you pass in a 50% off coupon with a duration of four months, the discount applies to all invoices in the four month period starting when the coupon is first applied. If the upsell is selected, the 50% discount applies to the entire yearly subscription because the yearly invoice is created during the coupon’s four month period.

[discounts](/api/checkout/sessions/create#create_checkout_session-discounts)

## Remove a subscription upsell

To remove a subscription upsell, click the x below. After you remove a subscription upsell, that upsell won’t be available to any new Checkout Sessions.

Remove an upsell.

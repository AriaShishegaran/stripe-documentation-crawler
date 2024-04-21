# Flexible coupons and promotion codes

Redeem coupons to apply discounts to the subscriptions you offer. You can also use coupons to create promotion codes to share with your customers. Customers can redeem these promotion codes to apply discounts to their subscriptions.

You can use coupons and promotion codes to:

- Apply one or more discounts to every invoice, a specific invoice, or for a certain duration of time

[invoice](/api/invoices)

- Apply one or more discounts to every subscription a customer has or to specific subscriptions

- Apply one or more discounts to specific subscription items

- Reduce invoice amounts by a percentage or a flat amount

You can also define a coupon that a customer must redeem by a certain date, or that’s limited to a set number of redemptions across all of your customers.

To use discounts for one-time payments, see Add discounts for one-time payments.

[Add discounts for one-time payments](/payments/checkout/discounts)

## Coupons

To apply discounts to a customer or a customer’s charges, redeem coupons into discounts. Learn how to create and manage coupons in the following sections.

Create coupons in the Dashboard or with the API:

[API](/api/coupons/create)

- In the Dashboard, open the Products page.

[Products](https://dashboard.stripe.com/test/products?active=true)

- Click Coupons.

- Click +New.

- In the Create a coupon dialog, enter the coupon’s parameters.

- Click Create coupon.

Here are all the settings for coupons.

Percentage off or Discount amount

Indicates how much the coupon actually discounts.

If you sell in multiple currencies, a single coupon can define different discount amounts for different currencies. Multi-currency coupons follow the same rules as multi-currency prices.

[multi-currency prices](/products-prices/pricing-models#multicurrency)

[promotion codes](#promotion-codes--promotion-codes)

You can only edit the name of the coupon after creation.

To set the products that are eligible for discounts, add the relevant product in the Apply to specific product field. Any promotion codes that are associated with the coupon are also restricted to this list of eligible products.

If you configure a coupon to apply to specific products and a subscription doesn’t have any applicable products, no discount is applied when you add the coupon to the subscription.

When you make changes to a subscription, any existing discounts are applied when proration is calculated. You can’t discount proration line items further on the invoice that’s generated.

[make changes](/billing/subscriptions/change)

After you’ve created coupons, create a discount by applying them to a subscription. You can apply the coupon when you create the subscription or by updating a customer’s existing subscription.

[updating a customer’s existing subscription](/api#update_subscription)

- In the Dashboard, open the Billing page and click Subscriptions.

- Click the relevant subscription.

- Click Actions.

- Click Update subscription.

- Click Add coupon.

- Select one or more coupons from the dropdown menus and click Submit.

You can still create a subscription when a customer doesn’t have a stored payment method if no immediate payment is required after you apply coupons to it.

If you add a coupon to a customer, the coupon applies to all subscriptions for that customer, including subscriptions added later. To prevent discounting all recurring charges for a customer, add coupons to subscriptions instead of customers.

A coupon attached to a subscription takes priority over a coupon attached to a customer. If you add coupons to a subscription, any coupons attached to the customer are not automatically applied. You must add the customer coupons to the subscription if you want those to apply as well.

- In the Dashboard, open the Customers page and select the customer.

[Customers](https://dashboard.stripe.com/test/customers)

- Click Actions

- Click Apply coupon.

- Select a coupon from the dropdown menu and click Submit.

Apply coupons to subscriptions in a Checkout Session by setting the discounts parameter in the API. To create a session with an applied discount, pass the coupon ID in the coupon parameter of the discounts array. This coupon overrides any coupon on the customer.

[API](/api/checkout/sessions/create#create_checkout_session-discounts)

If you’re creating a subscription with an existing customer, any coupon associated with the customer is applied to the subscription’s invoices.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

You can delete coupons with the Dashboard or the API.

[API](/api/coupons/delete)

Deleting a coupon prevents it from being applied to future subscriptions or customers, but it doesn’t remove the discount from any subscription or customer that already has it.

- In the Dashboard, open the Products page.

[Products](https://dashboard.stripe.com/test/products?active=true)

- Click Coupons

- Click the relevant coupon.

- Click the overflow menu ().

- Click Delete coupon.

A coupon’s duration indicates how long the redeemed discount is valid for. For example, a coupon for 50% off with a duration of 4 months applies to all invoices in the 4 month period starting when the coupon is first applied. If a customer applies this coupon to a yearly subscription during the coupon’s 4 month period, the 50% discount applies to the entire yearly subscription. In a monthly subscription, the coupon applies to the first 4 months. For a weekly subscription, a 4 month coupon applies to every invoice in the first 4 months.

[discount](/api/#discounts)

If you’re configuring a coupon’s duration in the API, when you use the value repeating you must specify duration_in_months as the number of months that the coupon repeatedly applies to. If you set the duration to once, the coupon applies only to the first invoice. If you set the duration to forever, the coupon applies to all invoices indefinitely.

Redemption limits apply to the coupon across every customer. For example, if you limit the number of times a coupon can be redeemed to 50, you can apply it to your customers only 50 times. This can be one time each for 50 different customers, one customer 50 times, or multiple customers multiple times until the max of 50 times.

If you set a coupon to last forever when a customer uses it but the coupon has an expiration date, any customer given that coupon will have that coupon’s discount forever. No new customers can apply the coupon after the expiration date.

## Promotion codes

Promotion codes are customer-facing codes that you create for coupons. For example, FALLPROMO and SPRINGPROMO can both point to a single 25% off coupon. You can share promotion codes directly with your customers to use at checkout.

If you’ve implemented the customer portal and turned on promotion codes, customers can apply a discount when upgrading or downgrading their existing subscriptions in the portal.

[customer portal](/billing/subscriptions/customer-portal)

Customize controls and limits on promotion codes by specifying eligible customers, first time orders, minimum order values, expiration dates, and redemption limits.

There are some restrictions to promotion codes.

- You can’t apply a promotion code with amount restrictions on a Customer object or a Subscription Item object.

[Customer object](/api/customers/object)

[Subscription Item object](/api/subscription_items/object)

- You can’t apply a promotion code with amount restrictions on a subscription update API call.

You can create a promotion code in the Dashboard when you create a coupon.

[create a coupon](#create-coupons--create-coupons)

The Code is case-insensitive and unique across active promotion codes for any customer. For example:

- You can create multiple customer-restricted promotion codes with the same Code, but you can’t reuse that Code for a promotion code that any customer can redeem.

- If you create a promotion code that is redeemable by any customer, you can’t create another active promotion code with the same code.

- You can create a promotion code with one Code, inactivate it, and then create a new promotion code with the same Code.

[inactivate](#inactive-promotions--inactivate)

- In the Dashboard on the Create a coupon page, click the Use customer-facing coupon codes button.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

- Enter a code. This is the code that a customer enters at checkout to redeem the discount. If you don’t set a code, Stripe generates one for you.

- Select requirements for the promotion code. For example, you can restrict the coupon to only being valid on first-time orders.

When you create a promotion code, it inherits the configuration of the associated coupon.

By configuring the promotion code settings, you can customize the following:

- Which customers are eligible to use a promotion code

- How many times a customer can redeem a promotion code

- When a promotion code expires

- Set a minimum amount a promotion code can apply to

To limit a promotion code to a particular customer complete these steps:

- On the Create a coupon page, select Limit to a specific customer.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

- Select the relevant customer. If you don’t specify a customer, any customer can redeem the promotion code.

To limit a promotion code to a customer’s first order, on the Create a coupon page, select Eligible for first-time order only.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

To set an minimum amount that is eligible for a promotion code, on the Create a coupon page, select Require minimum order value and enter the minimum value.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

Because promotion code restrictions are checked at redemption time, the minimum transaction amount only applies to the initial payment for a subscription.

If the coupon supports multiple currencies, the minimum amount can be different per-currency.

To set an expiration date for a promotion code, on the Create a coupon page, select Add an expiration date and the date and time at which the promotion code expires.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

If the underlying coupon already has an expiration date set, then the promotion code’s expiration date can’t be later than the coupon’s.

For example, you might have plans to support a coupon for a year, but you only want it to be redeemable for one week after a customer receives it. To do this, set the coupon’s expiration date to one year from now, and set each the promotion code’s expiration date to one week after it is created.

To set the number of times a customer can redeem the promotion code, on the Create a coupon page, select Limit the number of times this code can be redeemed and enter the number.

[Create a coupon](https://dashboard.stripe.com/test/coupons/create)

If the underlying coupon already has a maximum number of times set, then the promotion code’s maximum redemptions can’t be greater than the coupon’s.

To deactivate a promotion code, doing the following steps:

- In the Dashboard, open the Products page.

[Products](https://dashboard.stripe.com/test/products?active=true)

- Click Coupons.

- Click the coupon whose promotion code you want to deactivate.

- In the relevant promotion code row, click the overflow menu ().

- Click Archive promotion code.

However, if the underlying coupon for a promotion code becomes invalid, all of its promotion codes become permanently inactive. Similarly, if a promotion code reaches its maximum redemption limit or its expiration date, it becomes permanently inactive. These promotion codes can’t be reactivated.

After you create a promotion code, redeem a discount by applying the promotion code to a subscription. You can apply promotion codes two ways:

- When you create a subscription

[create a subscription](/api#create_subscription)

- When you update a customer’s existing subscription

[update a customer’s existing subscription](/api#update_subscription)

- In the Dashboard, go to Billing > Subscriptions.

- Click the relevant subscription.

- Click Actions > Update subscription > Add coupon.

- Click a promotion code from the dropdown menu and click Submit.

Enable promotion codes with the API by setting the allow_promotion_codes parameter in Checkout Sessions. When allow_promotion_codes is enabled on a Checkout Session, Checkout includes a promotion code redemption box for your customers to use.

[allow_promotion_codes](/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)

Promotion code field at checkout

## Stackable coupons and promotion codes

You can add multiple coupons, promotion codes, or redeemed discounts to a customer’s list of charges. You can do this when creating a subscription or by updating a customer’s existing subscription.

[discounts](/api/#discounts)

[creating a subscription](/api#create_subscription)

[updating a customer’s existing subscription](/api#update_subscription)

We support multiple discounts on both subscriptions and subscription items.

- In the Dashboard, go to Billing > Subscriptions.

- Click the relevant subscription.

- Click Actions > Update subscription > Add coupon.

- Click coupons from the dropdown menus and click Submit.

- Click the relevant product.

- Click Add coupons.

- Click coupons from the dropdown menus and click Submit.

You can start using the new discounts parameter on any subscription. We automatically clear out the singular discount field when discounts with more than one entry is passed in an update.

There are some restrictions to using multiple discounts.

- You can set up to 20 entries in the discounts parameter.

- Each entry in discounts has to be unique.

- You can not pass in a coupon and a promotion code created from the same coupon.

- You can not pass in a coupon and a discount that is generated from the same coupon.

- Redeemed discounts must already be attached to the customer or subscription that you’re updating.

You don’t need to set discounts if you don’t intend to make changes to existing discounts.

When updating discounts, you need to pass in any previously set coupon, promotion_code or discount you want to keep on the subscription.

Pass discounts = "" to clear all discounts from the subscription. When a subscription has no discounts, the customer-level discount, if any, applies to invoices.

If you have already set more than one discount on a subscription with the new discounts parameter, you can not update the subscription with the deprecated coupon or promotion_code parameter. Similarly, you can not update a schedule’s phases with the deprecated coupon or promotion_code parameter if you have set more than one discount on a prior phase.

Updating discounts does not incur prorations or generate an invoice on its own. The new discounts are applied the next time the subscription creates an invoice.

## Alternative discount methods

Although coupons are the most common way to discount a subscription, you can also do the following:

- Add a negative customer balance to the customer.

[customer balance](/api#customer_object-balance)

- Add negative invoice items.

[invoice items](/billing/invoices/subscription#adding-draft-invoice-items)

- Add a second price that is a cheaper version of a product’s usual price.

[second price](/products-prices/manage-prices#create-price)

Of these methods, negative invoice items provide more detailed information as to what discount was created, when, and why.

## See also

- Changing subscriptions

[Changing subscriptions](/billing/subscriptions/change)

- Working with invoices

[Working with invoices](/billing/invoices/subscription)

- Coupons API

[Coupons API](/api#coupons)

- Promotion codes API

[Promotion codes API](/api#promotion_codes)

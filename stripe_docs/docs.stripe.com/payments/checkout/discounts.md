# Add discounts for one-time payments

You can use discounts in Checkout to reduce the amount charged to a customer for one-time payments. Coupons and promotion codes allow for great flexibility in how you define and use them. They can:

- Apply a discount to an entire purchase subtotal

- Apply a discount to specific products

- Reduce the total charged by a percentage or a flat amount

- Create customer-facing promotion codes on top of coupons to share directly with customers

To use coupons for discounting subscriptions with Checkout and Billing, see Discounts for subscriptions.

[subscriptions](/billing/subscriptions/creating)

[Discounts for subscriptions](/billing/subscriptions/coupons)

## Coupons

Coupons specify a fixed value discount. You can create customer-facing promotion codes that map to a single underlying coupon.

This means that the codes FALLPROMO and SPRINGPROMO can both point to one 25% off coupon.

Coupons are created in the Dashboard or with the API:

[Dashboard](https://dashboard.stripe.com/coupons)

[API](/api#coupons)

If you want to create a session with an applied discount, pass the coupon ID in the coupon parameter of the discounts array. Checkout currently supports up to one coupon or promotion code.

[coupon ID](/api/coupons/object#coupon_object-id)

[discounts](/api/checkout/sessions/create#create_checkout_session-discounts)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

## Configure a coupon

Coupons have the following parameters that you can use for one-time payments:

- id, a unique identifier for the coupon

- currency

- percent_off or amount_off

- max_redemptions

- redeem_by, the latest date at which this coupon can be applied

- applies_to, limits the products that the coupon applies to

The coupon object adds discounts to both one-time payments and subscriptions. Some coupon object parameters, like duration, only apply to subscriptions.

[subscriptions](/billing/subscriptions/coupons)

The max_redemptions and redeem_by values apply to the coupon across every application. For example, you can restrict a coupon to the first 50 usages of it, or you can make a coupon expire by a certain date.

You can limit the products that are eligible for discounts using a coupon by adding the product IDs to the applies_to hash in the Coupon object. Any promotion codes that map to this coupon only apply to the list of eligible products.

You can delete coupons in the Dashboard or the API. Deleting a coupon prevents it from being applied to future transactions or customers.

## Promotion Codes

Promotion codes are customer-facing codes created on top of coupons. You can also specify additional restrictions that control when a customer can apply the promotion. You can share these codes with customers who can enter them into Checkout to apply a discount.

To create a promotion code, specify an existing coupon and any restrictions (for example, limiting it to a specific customer). If you have a specific code to give to your customer (for example, FALL25OFF), set the code. If you leave this field blank, we’ll generate a random code for you.

[promotion code](/api/promotion_codes)

The code is case-insensitive and unique across active promotion codes for any customer. For example:

- You can create multiple customer-restricted promotion codes with the same code, but you can’t reuse that code for a promotion code redeemable by any customer.

- If you create a promotion code that is redeemable by any customer, you can’t create another active promotion code with the same code.

- You can create a promotion code with code: NEWUSER, inactivate it by passing active: false, and then create a new promotion code with code: NEWUSER.

Promotion codes can be created in the coupons section of the Dashboard or with the API:

[Dashboard](https://dashboard.stripe.com/coupons/create)

[API](/api#promotion_codes)

Enable user-redeemable promotion codes using the allow_promotion_codes parameter in a Checkout Session. This enables a field in Checkout to allow users to input promotion codes.

[allow_promotion_codes](/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

## Configure a promotion code

With Promotion Code object parameters, you can customize eligible customers, redemptions, and other limits.

To limit a promotion to a particular customer, specify a customer when creating the promotion code. If no customer is specified, the code can be redeemed by any customer.

You can also limit the promotion code to first-time customers with the first_time_transaction parameter of the restrictions attribute. If the customer isn’t defined, or if a defined customer has no prior payments or non-void invoices, it’s considered a first-time transaction.

[invoices](/api/invoices)

Sessions that don’t create Customers instead create Guest Customers in the Dashboard. Promotion codes limited to first-time customers are still accepted for these Sessions.

[Customers](/api/customers)

[Guest Customers](https://support.stripe.com/questions/guest-customer-faq)

With promotion codes, you can set a minimum transaction amount for eligible discount by configuring the minimum_amount and the minimum_amount_currency properties. Since promotion code restrictions are checked at redemption time, the minimum transaction amount only applies to the initial payment for a subscription.

You can set an expiration date on the promotion code using expires_at. If the underlying coupon already has redeem_by set, then the expiration date for the promotion code can’t be later than that of the coupon. If promotion_code[expires_at] isn’t specified, the coupon’s redeem_by automatically populates expires_at.

For example, you might have plans to support a coupon for a year, but you only want it to be redeemable for one week after a customer receives it. You would set coupon[redeem_by] to one year from now, and set each promotion_code[expires_at] to one week after it is created.

You can limit the number of redemptions by using max_redemptions, which works similarly to the coupon parameter. If the underlying coupon already has max_redemptions set, then the max_redemptions for the promotion code can’t be greater than that of the coupon.

For example, you might want a seasonal sale coupon to be redeemable by the first 50 customers, but the winter promotion can only use 20 of those redemptions. In this scenario, you would set coupon[max_redemptions]: 50 and promotion_code[max_redemptions]: 20.

You can set whether a promotion code is currently redeemable by using the active parameter. However, if the underlying coupon for a promotion code becomes invalid, all of its promotion codes become permanently inactive. Similarly, if a promotion code reaches its max_redemptions or expires_at, it becomes permanently inactive. You can’t reactivate these promotion codes.

You can delete promotions in the Dashboard or the API. Deleting a promotion prevents it from being applied to future transactions or customers.

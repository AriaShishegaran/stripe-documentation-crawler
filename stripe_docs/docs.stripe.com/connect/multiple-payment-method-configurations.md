# Multiple configurations for your Connect accounts

Use this feature if your platform is using dynamic payment methods and supports setting different types of payment methods for different types of transactions (for example, subscriptions versus one-time checkout) or for different invoice amounts (for example, invoices more than a certain dollar amount can be paid using BNPL).

[dynamic payment methods](/connect/dynamic-payment-methods)

[Create a new payment method configuration in your Dashboard](#section-1)

## Create a new payment method configuration in your Dashboard

Navigate to the Payment methods settings for your connected accounts in the Stripe Dashboard. This is where you control your platform level “parent” configurations. Your connected accounts receive a “child” configuration for each parent that they can customize within the constraints you set below.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)

You start with one parent configuration by default. To create an additional configuration, click Add new configuration, and give it a name.

[Set the platform level default state](#section-2)

## Set the platform level default state

You can apply the default setting for each payment method to your new parent configuration, and control what customizations your connected accounts can make. Use the dropdown to select the desired setting:

- On by default the payment method is on by default. Connected accounts can turn it on and off.

- Off by default the payment method is off by default. Connected accounts can turn it on and off.

- Blocked turns the payment method off for all connected accounts. Connected accounts can’t turn it on.

[Allow your connected accounts to customize](#section-3)

## Allow your connected accounts to customize

Standard Connected accounts can visit the Dashboard to turn payment methods on or off if the payment method has been set to either On by default or Off by default. Your connected accounts see the newly created child configuration in their Payment methods settings. Your connected accounts can use the dropdown menu at the top of the page to choose a configuration to edit.

If you want your connected accounts to customize their Payment methods settings from your platform dashboard instead of the Stripe Dashboard, or if you have connected accounts who don’t have  Stripe Dashboard access, you can integrate with the Payment Method Configurations API.

Use the Payment Method Configurations API with the connected account ID and child configuration ID to read the current state of a payment method for a specific connected account on that configuration.

If successful, the return list displays each payment method and includes two parameters outlining availability and display preference.

- available is the combination of capability value (active, inactive, pending, or unrequested) and display_preference value.You can use the available field to know whether or not a buyer sees this payment method at checkout time. If available is true, that payment method’s capability is active and display_preference is on. If available is false, the payment method either doesn’t have an active capability or the display_preference value is off, and buyers won’t see it at checkout time. To simplify your integration and take advantage of other features, use payment methods that you manage from the Dashboard at checkout, which automatically reads this parameter and shows the right payment methods to buyers.

available is the combination of capability value (active, inactive, pending, or unrequested) and display_preference value.

[capability](/api/capabilities/object)

You can use the available field to know whether or not a buyer sees this payment method at checkout time. If available is true, that payment method’s capability is active and display_preference is on. If available is false, the payment method either doesn’t have an active capability or the display_preference value is off, and buyers won’t see it at checkout time. To simplify your integration and take advantage of other features, use payment methods that you manage from the Dashboard at checkout, which automatically reads this parameter and shows the right payment methods to buyers.

- display_preference has three components: overridable, preference, and value.overridable is read-only, and indicates whether the connected account’s preference can override the default set above.preference is writable, and stores the connected account’s preference.value is read-only, and reflects the effective display_preference value.

display_preference has three components: overridable, preference, and value.

- overridable is read-only, and indicates whether the connected account’s preference can override the default set above.

- preference is writable, and stores the connected account’s preference.

- value is read-only, and reflects the effective display_preference value.

Only payment methods that are relevant in the connected account’s country are shown in the API response and are configurable. Check country support.

[Check country support](/payments/payment-methods/integration-options)

When a connected account owner takes action to turn on or off a payment method, you can update the display_preference preference attribute. This stores the connected account owner’s preference for that payment method and is used to determine whether buyers see the payment method.

When your connected accounts turn on payment methods with the API, Stripe intelligently ranks the payment methods based on the buyer’s location, order size, and other factors to always show the highest converting payment methods first.

[Display available payment methods on checkout](#section-4)

## Display available payment methods on checkout

Pass the parent configuration ID when rendering your checkout flow to use your new configuration. Stripe automatically looks up the child configuration for the associated connected account and uses their customized settings.

If you’re using the Payment Element and creating a PaymentIntent before rendering the Payment Element, you can pass the parent ID into your PaymentIntent.

If you’re using the Payment Element with the deferred intent creation integration path, you can pass the parent ID in to your elements session options.

[deferred intent creation integration path](/payments/accept-a-payment-deferred)

If you’re creating a Checkout session, you can pass the parent ID in to your checkout session options.

[creating a Checkout session](/api/checkout/sessions/create)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[(Optional)—Apple Pay, Google Pay, and Link](#section-5)

## (Optional)—Apple Pay, Google Pay, and Link

Some payment methods, such as Apple Pay, Google Pay and Link, aren’t included as separate payment method types on a PaymentIntent and are confirmed only when supplying card. With the Payment Method Configurations API, you can let connected account owners opt in or opt out of these specific payment methods and prevent them from showing up in the UI.

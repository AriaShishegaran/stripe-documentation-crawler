# Connect platforms using the Sources APIDeprecated

As of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[accept a payment](/payments/accept-a-payment)

We deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](/payments/payment-methods/transitioning)

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

[PaymentMethods API](/api/payment_methods)

Connect platform owners can make use of additional payment methods supported with Sources. To learn more about creating payments for connected users, and which approach is best for you, refer to our Connect payments and fees documentation.

[Connect](/connect)

[payments and fees documentation](/connect/charges)

## Creating destination charges

If you opt for destination charges, you should create Sources on your platform directly and create Charges using the appropriate destination parameter. Customers are charged by your platform, which then transfers the necessary amount to the destination account.

[destination charges](/connect/destination-charges)

[Customers](/api/customers)

With destination charges that use cards, your platform name appears on statement descriptors and the charge is attributed to the connected account. With destination charges that use alternative payment methods (APMs), your platform name appears on statement descriptors but the charge is attributed to your platform.

## Creating direct charges

If you opt for direct charges, you will need to make sure that the connected account is onboarded on the payment method you intend to use (see below). Direct charges require creating sources on connected accounts. You can do so by passing source.stripeAccount with a value of a connected account’s ID when using Stripe.js.

If you’re creating sources server-side, you can make use of authentication using the Stripe-Account header with any of our supported libraries.

[authentication using the Stripe-Account header](/connect/authentication#stripe-account-header)

Card Sources (because they are not intrinsically tied to your platform as they do not require any authentication flow) can be created on your platform and then cloned to a connected account to create direct charges there.

[flow](/sources#flow-for-customer-action)

Once you created a card Source and attached it to a Customer (see Sources and Customers for more details on how these two objects interact), you can clone that card Source on a connected account using the connected account’s ID as the Stripe-Account header:

[Sources and Customers](/sources/customers)

Card Sources are generally reusable. However, when cloning them, you can override the usage to constrain how the connected account uses them. You do so by specifying the usage as single_use when cloning the Source.

If you are creating reusable card Sources on your connected account, you should make sure to attach them to Customers before charging them. Please refer to Sources and Customers for more details on how to attach and manage Sources on Customers.

[Sources and Customers](/sources/customers)

## See also

- Supported Payment Methods

[Supported Payment Methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best Practices Using Sources

[Best Practices Using Sources](/sources/best-practices)

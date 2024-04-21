# Customize redirect behavior with an embedded form

If you have a Checkout integration that uses an embedded form, you can customize how and whether Stripe redirects your customers after they complete payment. You can have Stripe always redirect customers, only redirect for some payment methods, or completely disable redirects.

If you’ve integrated with a Stripe-hosted payment page, you can’t use the return_url parameter. You must use success_url. Learn more about customizing a success page for integrations with a Stripe-hosted page.

[customizing a success page](/payments/checkout/custom-success-page)

To set up redirects, specify the return page in the return_url parameter.

[parameter](/api/checkout/sessions/create#create_checkout_session-return_url)

You can also optionally:

- Only redirect customers if the payment method requires it (for example, a bank authorization page for a debit-based method).

[Only redirect customers if the payment method requires it](#redirect-if-required)

- Not use a return page and disable redirect-based payment methods.

[disable redirect-based payment methods](#disable-redirects)

## Redirect customers to a return page

When you create the Checkout Session, you specify the URL of the return page in the return_url parameter. Include the {CHECKOUT_SESSION_ID} template variable in the URL. When Checkout redirects a customer, it replaces the variable with the actual Checkout Session ID.

[Checkout Session](/api/checkout/sessions)

[parameter](/api/checkout/sessions/create#create_checkout_session-return_url)

When rendering your return page, retrieve the Checkout Session status using the Checkout Session ID in the URL. Handle the result according to the session status as follows:

- complete: The payment succeeded. Use the information from the Checkout Session to render a success page.

- open: The payment failed or was canceled. Remount Checkout so that your customer can try again.

## Redirect-based payment methods

During payment, some payment methods redirect the customer to an intermediate page, such as a bank authorization page. When they complete that page, Stripe redirects them to your return page.

If you don’t want to redirect customers after payments that don’t require a redirect, set redirect_on_completion to if_required. That redirects only customers who check out with redirect-based payment methods.

[redirect_on_completion](/api/checkout/sessions/object#checkout_session_object-redirect_on_completion)

For card payments, Checkout renders a default success state instead of redirecting. To use your own success state, pass an onComplete callback that destroys the Checkout instance and renders your custom success state.

[onComplete](/js/embedded_checkout/init#embedded_checkout_init-options-onComplete)

onComplete is called when the Checkout Session completes successfully, or when the checkout.session.completed webhook event is sent.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

If you don’t want to create a return page, create your Checkout Session with redirect_on_completion set to never.

[redirect_on_completion](/api/checkout/sessions/object#checkout_session_object-redirect_on_completion)

This disables redirect-based payment methods:

- If you use Dynamic payment methods, you can still manage payment methods from the Dashboard, but payment methods that require redirects aren’t eligible.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

- If you manually specify payment methods with payment_method_types, you can’t include any redirect-based payment methods.

[payment_method_types](/api/checkout/sessions/object#checkout_session_object-payment_method_types)

Setting redirect_on_completion: never removes the return_url requirement. For these sessions, Checkout renders a default success state instead of redirecting. You can use your own success state by passing an onComplete callback which destroys the Checkout instance and renders your custom success state.

[onComplete](/js/embedded_checkout/init#embedded_checkout_init-options-onComplete)

onComplete is called when the Checkout Session completes successfully, or when the checkout.session.completed webhook event is sent.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

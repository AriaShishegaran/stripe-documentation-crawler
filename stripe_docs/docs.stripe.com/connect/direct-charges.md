# Create direct charges

Create direct charges when customers transact directly with a connected account, often unaware of your platform’s existence. With direct charges:

- The payment appears as a charge on the connected account, not your platform’s account.

- The connected account’s balance increases with every charge.

- Your account balance increases with application fees from every charge.

This charge type is best suited for platforms providing software as a service. For example, Shopify provides tools for building online storefronts, and Thinkific enables educators to sell online courses.

Redirect to a Stripe-hosted payment page using Stripe Checkout. See how this integration compares to Stripe’s other integration types.

[Stripe Checkout](/payments/checkout)

[compares to Stripe’s other integration types](/payments/accept-a-payment/web/compare-integrations)

[](https://checkout.stripe.dev/)

Redirect to Stripe-hosted payment page

Try it out

[Try it out](https://checkout.stripe.dev/)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, register for a Stripe account.

[register](https://dashboard.stripe.com/register)

Use our official libraries to access the Stripe API from your application:

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)

## Create a Checkout SessionClient-sideServer-side

A Checkout Session controls what your customer sees in the payment form such as line items, the order amount, and currency. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions)

On your server, create a Checkout Session and redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

- line_items - This attribute represents items that your customer is purchasing and shows up in the Stripe-hosted checkout page.

- payment_intent_data[application_fee_amount] - This attribute specifies the amount your platform deducts from the transaction as an application fee. After the payment is processed on the connected account, the application_fee_amount is transferred to the platform. See collect fees for more information.

[collect fees](#collect-fees)

- success_url - Stripe redirects the customer to the success URL after they complete a payment and replaces the {CHECKOUT_SESSION_ID} string with the Checkout Session ID. Use this to retrieve the Checkout Session and inspect the status to decide what to show your customer. You can also append your own query parameters, which persist through the redirect process. See customize redirect behavior with a Stripe-hosted page for more information.

[customize redirect behavior with a Stripe-hosted page](/payments/checkout/custom-success-page)

- Stripe-Account - This header indicates a direct charge for your connected account. With direct charges, the connected account is responsible for Stripe fees, refunds, and chargebacks. The connected account’s branding is used in Checkout, which allows their customers to feel like they’re interacting directly with the connected account instead of your platform.

[branding](#branding)

Charges that you create directly on the connected account are reported only on that account. These charges aren’t shown in your platform’s Dashboard or exports. Direct charges are included in reports and Sigma for connected accounts that your platform controls. You can always retrieve this information using the Stripe API.

[Handle post-payment eventsServer-side](#handle-post-payment-events)

## Handle post-payment eventsServer-side

Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[Use a webhook to receive these events](/webhooks/quickstart)

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes. Some payment methods also take 2-14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

[payment methods](https://stripe.com/payments/payment-methods-guide)

Stripe recommends handling all of the following events when collecting payments with Checkout:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded or a failure status.

[Checkout Session](/api/checkout/sessions)

[PaymentIntent](/payments/payment-intents)

[status](/payments/paymentintents/lifecycle)

[Test the integration](#test-the-integration)

## Test the integration

[authentication](/strong-customer-authentication)

See Testing for additional information to test your integration.

[Testing](/testing)

[OptionalEnable additional payment methods](#enable-payment-methods)

## OptionalEnable additional payment methods

## Collect fees

Your platform can take an application fee with the following limitations:

- The value of application_fee_amount must be positive and less than the amount of the charge. The application fee collected is capped at the amount of the charge.

- There are no additional Stripe fees on the application fee itself.

- In line with Brazilian regulatory and compliance requirements, platforms based outside of Brazil, with Brazilian connected accounts cannot collect application fees through Stripe.

- The currency of application_fee_amount depends upon a few multiple currency factors.

[multiple currency](/connect/currencies)

The resulting charge’s balance transaction includes a detailed fee breakdown of both the Stripe and application fees. To provide a better reporting experience, an Application Fee is created after the fee is collected. Use the amount property on the application fee object for reporting. You can then access these objects with the Application Fees endpoint.

[balance transaction](/api#balance_transaction_retrieve)

[Application Fee](/api/application_fees/object)

[Application Fees](/api/application_fees/list)

Earned application fees are added to your available account balance on the same schedule as funds from regular Stripe charges. Application fees are viewable in the Collected fees section of the Dashboard.

[Collected fees](https://dashboard.stripe.com/connect/application_fees)

Application fees for direct charges are created asynchronously by default. If you expand the application_fee object in a charge creation request, the application fee is created synchronously as part of that request. Only expand the application_fee object if you absolutely have to, because it increases the latency of the request.

To access the application fee objects for application fees that are created asynchronously, listen for the application_fee.created webhook event.

[application_fee.created](/api/events/types#event_types-application_fee.created)

When you specify an application fee on a charge, the fee amount is transferred to your platform’s Stripe account. When processing a charge directly on the connected account, the charge amount—less the Stripe fees and application fee—is deposited into the connected account.

For example, if you make a charge of 10 USD with a 1.23 USD application fee (like in the previous example), 1.23 USD is transferred to your platform account. 8.18 USD (10 USD - 0.59 USD - 1.23 USD) is netted in the connected account (assuming standard US Stripe fees).

If you process payments in multiple currencies, read how currencies are handled in Connect.

[how currencies are handled](/connect/currencies)

## Customize branding

Your platform and connected accounts can use the Branding settings in the Dashboard to customize branding on the payments page. For direct charges, Checkout uses the brand settings of the connected account.

[Branding settings](https://dashboard.stripe.com/account/branding)

You can also use the API to update branding settings:

[update](/api/accounts/update#update_account-settings-branding)

- icon - Displayed next to the business name in the header of the Checkout page.

- logo - Used in place of the icon and business name in the header of the Checkout page.

- primary_color - Used as the background color on the Checkout page.

- secondary_color - Used as the button color on the Checkout page.

## Issue refunds

Just as platforms can create charges on connected accounts, they can also create refunds of charges on connected accounts. Create a refund using your platform’s secret key while authenticated as the connected account.

[Create a refund](/api#create_refund)

[authenticated](/connect/authentication#stripe-account-header)

Application fees are not automatically refunded when issuing a refund. Your platform must explicitly refund the application fee or the connected account—the account on which the charge was created—loses that amount. You can refund an application fee by passing a refund_application_fee value of true in the refund request:

By default, the entire charge is refunded, but you can create a partial refund by setting an amount value as a positive integer. If the refund results in the entire charge being refunded, the entire application fee is refunded. Otherwise, a proportional amount of the application fee is refunded. Alternatively, you can provide a refund_application_fee value of false and refund the application fee separately.

[refund the application fee](/api#create_fee_refund)

## See also

- Working with multiple currencies

[Working with multiple currencies](/connect/currencies)

- Statement descriptors with Connect

[Statement descriptors with Connect](/connect/statement-descriptors)

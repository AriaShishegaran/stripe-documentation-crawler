# Create destination charges

Create destination charges when customers transact with your platform for products or services provided by your connected accounts and you immediately transfer funds to your connected accounts. With this charge type:

- You create a charge on your platform’s account.

- You determine whether some or all of those funds are transferred to the connected account.

- Your account balance is debited for the cost of the Stripe fees, refunds, and chargebacks.

This charge type is most optimal for marketplaces such as Airbnb, a home rental marketplace or Lyft, a ridesharing app.

Destination charges are only supported if both your platform and the connected account are in the same country. For cross-region support, you must specify the settlement merchant to the connected account using the on_behalf_of parameter on the Payment Intent or other valid cross-border transfers scenarios.

[settlement merchant](#settlement-merchant)

[on_behalf_of](/api/payment_intents/create#create_payment_intent-on_behalf_of)

[cross-border transfers](/connect/account-capabilities#transfers-cross-border)

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

A Checkout Session controls what your customer sees in the payment form such as line items, the order amount and currency, and acceptable payment methods. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions)

On your server, create a Checkout Session and redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

- payment_intent_data[transfer_data][destination] - This parameter indicates that this is a destination charge. A destination charge means the charge is processed on the platform and then the funds are immediately and automatically transferred to the connected account’s pending balance.

- line_items - This parameter represents the items the customer is purchasing. The items are displayed in the embedded payment form.

- success_url - Stripe redirects the customer to the success URL after they complete a payment and replaces the {CHECKOUT_SESSION_ID} string with the Checkout Session ID. Use this to retrieve the Checkout Session and inspect the status to decide what to show your customer. You can also append your own query parameters, which persist through the redirect process. See customize redirect behavior with a Stripe-hosted page for more information.

[customize redirect behavior with a Stripe-hosted page](/payments/checkout/custom-success-page)

- payment_intent_data[application_fee_amount] - This parameter specifies the amount your platform plans to take from the transaction. The full charge amount is immediately transferred from the platform to the connected account that’s specified by transfer_data[destination] after the charge is captured. The application_fee_amount is then transferred back to the platform, and the Stripe fee is deducted from the platform’s amount.

When processing destination charges, Checkout uses the brand settings of your platform account. See customize branding for more information.

[customize branding](#branding)

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

You can collect fees with either an application_fee_amount or transfer_data[amount].

[application_fee_amount](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-application_fee_amount)

[transfer_data[amount]](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-transfer_data-amount)

When creating charges with an application_fee_amount, the full charge amount is immediately transferred from the platform to the transfer_data[destination] account after the charge is captured. The application_fee_amount (capped at the full amount of the charge) is then transferred back to the platform.

[https://example.com/success](https://example.com/success)

After the application fee is collected, an Application Fee object is created. You can view a list of application fees in the Dashboard, with the application fees, or in Sigma. You can also use the amount property on the application fee object for itemized fee reporting.

[Application Fee](/api/application_fees/object)

[Dashboard](https://dashboard.stripe.com/connect/application_fees)

[application fees](/api/application_fees/list)

[Sigma](/stripe-data/access-data-in-dashboard)

When using an application_fee_amount, know that:

- The application_fee_amount is capped at the total transaction amount.

- The application_fee_amount is always computed in the same currency as the transaction.

- The application fee settles in the same currency as the connected account’s settlement currency. For cross-border destination charges, this might differ from your platform’s settlement currency.

[differ from your platform’s settlement currency](/connect/currencies#application-fees-for-destination-charges-and-converting-balances)

- Your platform pays the Stripe fee after the application_fee_amount is transferred to your account.

- No additional Stripe fees are applied to the amount.

- Your platform can use built-in application fee reporting to reconcile fees collected.

[fees collected](https://dashboard.stripe.com/connect/application_fees)

- In Stripe-hosted dashboards or components such as the Payment details component, your connected account can view both the total amount and the application fee amount.

[Payment details component](/connect/supported-embedded-components/payment-details)

With the above code, the full charge amount (10.00 USD) is added to the connected account’s pending balance. The application_fee_amount (1.23 USD) is subtracted from the charge amount and is transferred to your platform. Stripe fees (0.59 USD) are subtracted from your platform account’s balance. The application fee amount minus the Stripe fees (1.23 USD - 0.59 USD = 0.64 USD) remains in your platform account’s balance.

The application_fee_amount becomes available on the platform account’s normal transfer schedule, just like funds from regular Stripe charges.

## Customize branding

Your platform uses the branding settings in the Dashboard to customize branding on the payments page. For destination charges, Checkout uses the branding settings of the platform account. For destination charges with on_behalf_of, Checkout uses the branding settings of the connected account.

[branding settings](https://dashboard.stripe.com/account/branding)

Platforms can configure the branding settings of connected accounts using the Update Account API:

[Update Account](/api/accounts/update#update_account-settings-branding)

- icon - Displayed next to the business name in the header of the Checkout page.

- logo-  Used in place of the icon and business name in the header of the Checkout page.

- primary_color - Used as the background color on the Checkout page.

- secondary_color - Used as the button color on the Checkout page.

## Specify the settlement merchant

The settlement merchant is dependent on the capabilities set on an account and how a charge is created. The settlement merchant determines whose information is used to make the charge. This includes the statement descriptor (either the platform’s or the connected account’s) that’s displayed on the customer’s credit card or bank statement for that charge.

[capabilities](/connect/account-capabilities)

Specifying the settlement merchant allows you to be more explicit about who to create charges for. For example, some platforms prefer to be the settlement merchant because the end customer interacts directly with their platform (such as on-demand platforms). However, some platforms have connected accounts that interact directly with end customers instead (such as a storefront on an e-commerce platform). In these scenarios, it might make more sense for the connected account to be the settlement merchant.

You can set the on_behalf_of parameter to the ID of a connected account to make that account the settlement merchant for the payment. When using on_behalf_of:

- Charges settle in the connected account’s country and settlement currency.

- The fee structure for the connected account’s country is used.

- The connected account’s statement descriptor is displayed on the customer’s credit card statement.

- If the connected account is in a different country than the platform, the connected account’s address and phone number are displayed on the customer’s credit card statement.

- The number of days that a pending balance is held before being paid out depends on the delay_days setting on the connected account.

[pending balance](/connect/account-balances)

[delay_days](/api/accounts/create#create_account-settings-payouts-schedule-delay_days)

If on_behalf_of is omitted, the platform is the business of record for the payment.

The on_behalf_of parameter is supported only for connected accounts with the card_payments capability. Accounts under the recipient service agreement can’t request card_payments.

[card_payments](/connect/account-capabilities#card-payments)

[recipient service agreement](/connect/service-agreement-types#recipient)

## Issue refunds

If you are using the Payment Intents API, refunds should be issued against the most recent charge that is created.

[the most recent charge that is created](/payments/payment-intents/verifying-status#identifying-charges)

Charges created on the platform account can be refunded using the platform account’s secret key. When refunding a charge that has a transfer_data[destination], by default the destination account keeps the funds that were transferred to it, leaving the platform account to cover the negative balance from the refund. To pull back the funds from the connected account to cover the refund, set the reverse_transfer parameter to true when creating the refund:

By default, the entire charge is refunded, but you can create a partial refund by setting an amount value as a positive integer.

If the refund results in the entire charge being refunded, the entire transfer is reversed. Otherwise, a proportional amount of the transfer is reversed.

When refunding a charge with an application fee, by default the platform account keeps the funds from the application fee. To push the application fee funds back to the connected account, set the refund_application_fee parameter to true when creating the refund:

[refund_application_fee](/api/refunds/create#create_refund-refund_application_fee)

Note that if you refund the application fee for a destination charge, you must also reverse the transfer. If the refund results in the entire charge being refunded, the entire application fee is refunded as well. Otherwise, a proportional amount of the application fee is refunded.

Alternatively, you can provide a refund_application_fee value of false and refund the application fee separately through the API.

[through the API](/api#create_fee_refund)

## See also

- Working with multiple currencies

[Working with multiple currencies](/connect/currencies)

- Statement descriptors with Connect

[Statement descriptors with Connect](/connect/statement-descriptors)

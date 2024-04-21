# Collect payments then pay out

This guide explains how to accept payments and move funds to the bank accounts of your service providers or sellers. For demonstration purposes, we’ll build a home-rental marketplace that connects homeowners to potential tenants. We’ll also show you how to accept payments from tenants (customers) and pay out homeowners (your platform’s users).

## Prerequisites

- Register your platform.

[Register your platform](https://dashboard.stripe.com/connect/tasklist)

- Add business details to activate your account.

[activate your account](https://dashboard.stripe.com/account/onboarding)

- Complete your platform profile.

[Complete your platform profile](https://dashboard.stripe.com/connect/settings/profile)

- Customize your brand settings. (Stripe-hosted onboarding only) Add a business name, icon, and brand color.

[Customize your brand settings](https://dashboard.stripe.com/settings/connect)

[Set up StripeServer-side](#setup)

## Set up StripeServer-side

Install Stripe’s official libraries to access the API from your application:

[Create a connected account](#create-account)

## Create a connected account

When a user (seller or service provider) signs up on your marketplace, you must create a corresponding user Account (referred to as a connected account). You can’t accept payments and move funds to the bank account of your user without a connected account. Connected accounts represent your users in the Stripe API and collect the information required to verify the user’s identity. In our home-rental example, the connected account represents the homeowner.

[Account](/api/accounts)

Use the /v1/accounts API to create an Express account and set type to express in the account creation request.

[create](/api/accounts/create)

If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

[Connect service agreement](/connect/service-agreement-types)

When testing your integration, prefill account information using test data.

[test data](/connect/testing)

You can create an account link by calling the Account Links API with the following parameters:

[Account Links](/api/account_links)

- account

- refresh_url

- return_url

- type = account_onboarding

[https://example.com/reauth](https://example.com/reauth)

[https://example.com/return](https://example.com/return)

The response to your Account Links request includes a value for the key url. Redirect to this link to send your user into the flow. URLs from the Account Links API are temporary and are single-use only, because they grant access to the connected account user’s personal information. Authenticate the user in your application before redirecting them to this URL. If you want to prefill information, you must do so before generating the account link. After you create the account link, you can’t read or write information for the connected account.

[Account Links](/api/account_links)

[Account Links](/api/account_links)

Don’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where the user is redirected to your platform. It’s important that you implement these correctly to provide the best experience for your user.

You can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but live mode only accepts HTTPS. Be sure to swap testing URLs for HTTPS URLs before going live.

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After a user is redirected to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to account.updated webhooks

- Calling the Accounts API and inspecting the returned object

[Accounts](/api/accounts)

Stripe redirects your user to the refresh_url in these cases:

- The link is expired (a few minutes went by since the link was created).

- The user already visited the URL (the user refreshed the page or clicked back or forward in the browser).

- Your platform is no longer able to access the account.

- The account has been rejected.

Your refresh_url should trigger a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

[Account Links](/api/account_links)

A user that’s redirected to your return_url might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

View your payment methods settings and enable the payment methods you want to support. Card payments, Google Pay, and Apple Pay are enabled by default but you can enable and disable payment methods as needed.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Before the payment form is displayed, Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. Payment methods that increase conversion and that are most relevant to the currency and customer’s location are prioritized. Lower priority payment methods are hidden in an overflow menu.

[Accept a payment](#accept-payment)

## Accept a payment

Use Stripe Checkout to accept payments. Checkout supports multiple payment methods and automatically shows the most relevant ones to your customer. You can accept payments with Checkout using a Stripe-hosted page or add a prebuilt embeddable payment form directly in your website. You can also create a custom flow (using Payment Element) to accept multiple payment methods with a single front-end integration.

[Stripe Checkout](https://stripe.com/payments/checkout)

A Checkout Session controls what your customer sees in the Stripe-hosted payment page such as line items, the order amount and currency, and acceptable payment methods.

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

On your server, make the following call to Stripe’s API. After creating a Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

- line_items - This argument represents the items the customer is purchasing. The items are displayed in the Stripe-hosted user interface.

- success_url - This argument redirects a user after they complete a payment.

- cancel_url  - This argument redirects a user after they click cancel.

- payment_intent_data[application_fee_amount] - This argument specifies the amount your platform plans to take from the transaction. The full charge amount is immediately transferred from the platform to the connected account that’s specified by transfer_data[destination] after the charge is captured. The application_fee_amount is then transferred back to the platform, and the Stripe fee is deducted from the platform’s amount.

- payment_intent_data[transfer_data][destination] - This argument indicates that this is a destination charge. A destination charge means the charge is processed on the platform and then the funds are immediately and automatically transferred to the connected account’s pending balance. For our home-rental example, we want to build an experience where the customer pays through the platform and the homeowner gets paid by the platform.

[destination charge](/connect/destination-charges)

Checkout uses the brand settings of your platform account for destination charges. For more information, see Customize branding.

[Customize branding](/connect/creating-a-payments-page?platform=web&ui=stripe-hosted#branding)

This Session creates a destination charge. If you need to control the timing of transfers or need to transfer funds from a single payment to multiple parties, use separate charges and transfers instead. To use separate charges, see Enable other businesses to accept payments directly.

[Enable other businesses to accept payments directly](/connect/enable-payment-acceptance-guide?platform=web)

Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[Use a webhook to receive these events](/webhooks/quickstart)

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes. Some payment methods also take 2-14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

[payment methods](https://stripe.com/payments/payment-methods-guide)

In addition to handling the checkout.session.completed event, we recommend handling two other events when collecting payments with Checkout:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[Checkout Session](/api/checkout/sessions)

[PaymentIntent](/payments/payment-intents)

[Testing](#testing)

## Testing

Test your account creation flow by creating accounts and using OAuth.

[creating accounts](/connect/testing#creating-accounts)

[using OAuth](/connect/testing#using-oauth)

[authentication](/strong-customer-authentication)

See Testing for additional information to test your integration.

[Testing](/testing)

## Disputes

As the settlement merchant on charges, your platform is responsible for disputes. Make sure you understand the best practices for responding to disputes.

[settlement merchant](/connect/destination-charges#settlement-merchant)

[best practices](/disputes/responding)

## Payouts

By default, any funds that you transfer to a connected account accumulate in the connected account’s Stripe balance and are paid out on a daily rolling basis. You can change the payout frequency by going into the connected account’s detail page, clicking the right-most button in the Balance section, and selecting Edit payout schedule.

[Stripe balance](/connect/account-balances)

[payout](/payouts)

## Refunds

To issue refunds, go to the Payments page. Select individual payments by clicking the checkbox to the left of any payments you want to refund. After you select a payment, Stripe displays a Refund button in the upper-right corner of the page. Click the Refund button to issue a refund to customers for all payments you have selected.

[Payments](https://dashboard.stripe.com/payments)

Connected accounts can’t initiate refunds for payments from the Express Dashboard. If your connected accounts use the Express Dashboard, you must process refunds for them.

[Express Dashboard](/connect/express-dashboard)

## See also

- Manage connected accounts in the Dashboard

[Manage connected accounts in the Dashboard](/connect/dashboard)

- Issue refunds

[Issue refunds](/connect/direct-charges#issue-refunds)

- Customize statement descriptors

[Customize statement descriptors](/connect/statement-descriptors)

- Work with multiple currencies

[Work with multiple currencies](/connect/currencies)

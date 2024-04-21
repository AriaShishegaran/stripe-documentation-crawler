# Enable other businesses to accept payments directly

This guide covers letting your users accept payments, moving a portion of your users’ earnings into your balance, and paying out the remainder to your users’ bank accounts. To illustrate these concepts, we’ll use an example platform that lets businesses build their own online stores.

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

Install Stripe’s official libraries so you can access the API from your application:

[Create a connected account](#create-account)

## Create a connected account

When a user (seller or service provider) signs up on your platform, create a user Account (referred to as a connected account) so you can accept payments and move funds to their bank account. Connected accounts represent your user in Stripe’s API and help facilitate the collection of onboarding requirements so Stripe can verify the user’s identity. In our store builder example, the connected account represents the business setting up their Internet store.

[Account](/api/accounts)

Use the /v1/accounts API to create a Standard account and set type to standard in the account creation request.

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

The response to your Account Links request includes a value for the key url. Redirect to this link to send your user into the flow. Account Links are temporary and are single-use only because they grant access to the connected account user’s personal information. Authenticate the user in your application before redirecting them to this URL. If you want to prefill information, you must do so before generating the account link. After you create the account link, you won’t be able to read or write information for the account.

[Account Links](/api/account_links)

Don’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where the user is redirected to your platform. It’s important that you implement these correctly to provide the best experience for your user.

You can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but live mode only accepts HTTPS. Be sure to swap testing URLs for HTTPS URLs before going live.

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After a user is redirected to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to account.updated webhooks

- Calling the Accounts API and inspecting the returned object

[Accounts](/api/accounts)

Your user is redirected to the refresh_url in these cases:

- The link is expired (a few minutes went by since the link was created)

- The user already visited the link (the user refreshed the page or clicked back or forward in the browser)

- Your platform is no longer able to access the account

- The account has been rejected

Your refresh_url should trigger a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

[Account Links](/api/account_links)

If a user is redirected to your return_url, they might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). To see if they’ve completed the onboarding process, check the state of the details_submitted parameter on their account.

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

View your payment methods settings and enable the payment methods you want to support. Card payments are enabled by default but you can enable and disable payment methods as needed. This guide assumes Bancontact, credit cards, EPS, giropay, iDEAL, Przelewy24, SEPA Direct Debit, and Sofort are enabled.

[payment methods settings](https://dashboard.stripe.com/settings/connect/payment_methods)

Before the payment form is displayed, Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. Payment methods that increase conversion and that are most relevant to the currency and customer’s location are prioritized. Lower priority payment methods are hidden in an overflow menu.

The embedded payment method settings component allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.

[Request access](/connect/supported-embedded-components/payment-method-settings#request-access)

[integrate with Payment Method Configurations](/connect/supported-embedded-components/payment-method-settings#integration)

[Accept a payment](#accept-payment)

## Accept a payment

Embed Stripe Checkout as a payment form directly on your website or redirect users to a Stripe-hosted page to accept payments. Checkout supports multiple payment methods and automatically shows the most relevant ones to your customer You can also use the Payment Element, a prebuilt UI component that is embedded as an iframe in your payment form, to accept multiple payment methods with a single frontend integration.

[Stripe Checkout](https://stripe.com/payments/checkout)

A Checkout Session controls what your customer sees in the embeddable payment form such as line items, the order amount and currency, and acceptable payment methods. When performing direct charges, Checkout uses the connected account’s branding settings. See the Customize branding section for more information.

[Customize branding](/connect/creating-a-payments-page?platform=web&ui=stripe-hosted#branding)

Unlike destination charges and separate charges and transfers, users (connected accounts) are responsible for handling disputes on direct charges—it’s not the responsibility of the platform.

On your server, make the following call to the Stripe API. After creating a Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

- line_items - This argument represents items that your customer is purchasing and that will show up in the hosted user interface.

- success_url - This argument redirects a user after they complete a payment.

- cancel_url  - This argument redirects a user after they click cancel.

- Stripe-Account - This header indicates a direct charge for your connected account. With direct charges, the connected account is responsible for Stripe fees, refunds, and chargebacks. The connected account’s branding is used in Checkout, which allows their customers to feel like they’re interacting directly with the merchant instead of your platform.

[direct charge](/connect/direct-charges)

- (Optional) payment_intent_data[application_fee_amount] - This argument specifies the amount your platform plans to take from the transaction. After the payment is processed on the connected account, the application_fee_amount is transferred to the platform and the Stripe fee is deducted from the connected account’s balance.

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

Test your account creation flow by creating accounts and using OAuth. Test your Payment methods settings for your connected accounts by logging into one of your test accounts and navigating to the Payment methods settings. Test your checkout flow with your test keys and a test account. You can use our test cards to test your payments flow and simulate various payment outcomes.

[creating accounts](/connect/testing#creating-accounts)

[using OAuth](/connect/testing#using-oauth)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[test cards](/testing)

## Payouts

By default, any charge that you create for a connected account accumulates in the connected account’s Stripe balance and is paid out on a daily rolling basis. Connected accounts can manage their own payout schedules in the Stripe Dashboard.

[Stripe balance](/connect/account-balances)

[Stripe Dashboard](https://dashboard.stripe.com/settings/payouts)

## See also

- Manage connected accounts in the Dashboard

[Manage connected accounts in the Dashboard](/connect/dashboard)

- Issue refunds

[Issue refunds](/connect/direct-charges#issue-refunds)

- Customize statement descriptors

[Customize statement descriptors](/connect/statement-descriptors)

- Work with multiple currencies

[Work with multiple currencies](/connect/currencies)

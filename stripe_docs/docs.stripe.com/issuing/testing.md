# Testing Issuing

Learn more about testing your Stripe integration.

[testing](/testing)

You can issue cards and simulate purchases using your own Stripe integration in test mode. This allows you to test your integration before you go live without having to make real purchases. You can only use these cards for testing within your Stripe account and not for external purchases.

When testing your authorization endpoint, make sure that you have set the endpoint for test mode in your Issuing settings. Toggle View test data to switch between test and live mode data and settings.

[authorization endpoint](/issuing/purchases/authorizations)

[Issuing settings](https://dashboard.stripe.com/account/issuing)

## Fund your test mode Issuing balance

Before you create test mode transactions, you must add test mode funds to the Issuing balance on your account. These aren’t real funds, and you can only use them for simulating purchases in test mode.

Issuing users in the US use “pull” funding, and use Top-ups to fund their Issuing balance. You can create test mode top-ups in the Dashboard, or with the Top-ups API. Learn more about funding Issuing balances for US users.

[Top-ups API](/api/topups/create)

[US users](/issuing/funding/balance?push-pull-preference=pull)

To top up their balance, Issuing users in the UK and Europe “push” funds using Funding Instructions. You can do this in the test mode Dashboard, or with the Funding Instructions API. Learn more about funding Issuing balances for UK and euro area users.

[Funding Instructions API](/api/funding_instructions)

[UK and euro area users](/issuing/funding/balance?push-pull-preference=push)

You can simulate a card purchase by specifying authorization details in the Dashboard.

[Create a cardDashboard](#without-code-create-card)

## Create a cardDashboard

Use the API or the Dashboard to create a cardholder and card in test mode.

[API](/issuing/cards)

[Dashboard](https://dashboard.stripe.com/issuing/cards)

[Create a test purchaseDashboard](#without-code-create-test-purchase)

## Create a test purchaseDashboard

Navigate to the Issuing Cards page in test mode, find your newly-created card, then click Create test purchase.

[Issuing Cards page](https://dashboard.stripe.com/issuing/cards)

You can select to create either an Authorization or Transaction by force capture.

[Authorization](/api/issuing/authorizations/object)

[Transaction](/api/issuing/transactions/object)

Depending on your selection, you can provide a number of properties, such as amount, business data, and so on.

Click Submit to create the purchase. If you selected authorization and have configured your synchronous webhook, you can use it to approve or decline the authorization. The browser redirects to the page for the newly-created authorization.

[synchronous webhook](/issuing/controls/real-time-authorizations)

[Create a captureDashboard](#without-code-create-test-capture)

## Create a captureDashboard

To create a test capture with an authorization in the Dashboard, enter test mode and complete the following steps:

- Navigate to the Authorizations page under Issued Cards.

[Authorizations](https://dashboard.stripe.com/issuing/authorizations)

- Click the authorization you want to capture, then click Capture.

You can capture an authorization for an amount that’s lesser, greater, or equivalent to the authorized total. You can also capture multiple times regardless of the authorization’s current state.

[capture multiple times](/issuing/purchases/transactions?issuing-capture-type=multi_capture)

Enter the amount you want to capture, then click Submit to create the capture. The browser redirects you to the Transactions page and selects the newly created transaction.

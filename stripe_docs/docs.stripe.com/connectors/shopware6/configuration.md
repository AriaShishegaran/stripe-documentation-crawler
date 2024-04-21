# Configure the Stripe Connector for Shopware 6

To use Stripe with Shopware 6, you must install and then configure the Stripe connector.

[Shopware 6](https://www.shopware.com/en/)

[install](/connectors/shopware6/installation)

## Configure the connector

Use the Shopware administration panel to configure the connector.

- In the admin panel sidebar, under Extensions, select My extensions.

In the admin panel sidebar, under Extensions, select My extensions.

- On the Apps tab, for the Stripe connector, click the overflow menu () and select Open extension.

On the Apps tab, for the Stripe connector, click the overflow menu () and select Open extension.

- Configure the Stripe Connector for Shopware 6:Connect to Stripe to accept paymentsChoose your payment formCustomize the payment formCollect your customer’s postal codeChoose how to capture funds

Configure the Stripe Connector for Shopware 6:

- Connect to Stripe to accept payments

[Connect to Stripe to accept payments](/connectors/shopware6/configuration#connect-stripe)

- Choose your payment form

[Choose your payment form](/connectors/shopware6/configuration#payment-form)

- Customize the payment form

[Customize the payment form](/connectors/shopware6/configuration#customize-payment-form)

- Collect your customer’s postal code

[Collect your customer’s postal code](/connectors/shopware6/configuration#postal-code)

- Choose how to capture funds

[Choose how to capture funds](/connectors/shopware6/configuration#capture-funds)

## Connect to Stripe to accept payments

Connect Shopware to your Stripe account to start accepting payments. When you connect to a new account, you must reactivate your preferred payment methods.

- On the Stripe Configuration page, click Connect with Stripe in Live Mode. If you want to test different app functionality without processing live payments, use Connect with Stripe in Test Mode.

On the Stripe Configuration page, click Connect with Stripe in Live Mode. If you want to test different app functionality without processing live payments, use Connect with Stripe in Test Mode.

- Provide your business information to create your Stripe account.

Provide your business information to create your Stripe account.

[create your Stripe account](https://dashboard.stripe.com/register)

- After you create your Stripe account, log in to your Stripe Dashboard.

After you create your Stripe account, log in to your Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/)

- In the Stripe Dashboard, do the following:Under Settings > Payment methods, select your Shopware account from the Select your platform drop-down.Turn on your preferred payment methods individually or by using the Turn on all button.

In the Stripe Dashboard, do the following:

- Under Settings > Payment methods, select your Shopware account from the Select your platform drop-down.

Under Settings > Payment methods, select your Shopware account from the Select your platform drop-down.

- Turn on your preferred payment methods individually or by using the Turn on all button.

Turn on your preferred payment methods individually or by using the Turn on all button.

## Choose your payment form

Configure the payment form that displays to your customers during checkout. Under Payment form settings, you can choose from the following:

- Integrated payment form–The Payment Element is an embeddable UI component that lets you accept 25+ payment methods with a single integration.

[Payment Element](/payments/payment-element)

- Redirect to Stripe–Stripe Checkout lets you redirect your customers to a Stripe-hosted, customizable checkout page to finalize payment.

[Stripe Checkout](/payments/checkout)

## Customize the payment form

You can customize the appearance of your checkout form in the Stripe Dashboard. Under Select a theme for the integrated payment form, choose one of the following: Stripe, Night, Flat, or None.

## Collect your customer’s postal code

You can specify whether or not to collect your customer’s postal code at checkout using the Never collect the postal code field. Stripe recommends collecting and verifying postal code information, which can help decrease the card decline rate.

- (Recommended) Unselect this field if you want to require a postal code at checkout. This applies to cards issued in Canada, the United Kingdom, or the United States.

(Recommended) Unselect this field if you want to require a postal code at checkout. This applies to cards issued in Canada, the United Kingdom, or the United States.

- Select this field if you don’t want to collect a postal code at checkout.

Select this field if you don’t want to collect a postal code at checkout.

## Choose how to capture funds

You can specify how you want to authorize and capture funds.

- Simultaneous authorization and capture–The issuing bank confirms that the cardholder can pay, and then transfers the funds automatically after confirmation.

Simultaneous authorization and capture–The issuing bank confirms that the cardholder can pay, and then transfers the funds automatically after confirmation.

- Separate authorization and capture–The authorization occurs first, and the capture occurs later. To capture funds, change the order’s payment status from Authorized to Paid or Partially paid in the Shopware administration panel.

Separate authorization and capture–The authorization occurs first, and the capture occurs later. To capture funds, change the order’s payment status from Authorized to Paid or Partially paid in the Shopware administration panel.

## Refunds

You can refund any order with a Paid status. To initiate a refund, select the order under Orders > Overview in the Shopware administration panel. Change the order’s payment status from Paid to Refunded.

## See also

- Overview

[Overview](/connectors/shopware6)

- Install the connector

[Install the connector](/connectors/shopware6/installation)

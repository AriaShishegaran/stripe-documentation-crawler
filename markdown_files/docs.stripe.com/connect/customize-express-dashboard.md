htmlCustomize the Express Dashboard | Stripe Documentation[Skip to content](#main-content)Customize the Express Dashboard[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcustomize-express-dashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcustomize-express-dashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Express Dashboard](/docs/connect/express-dashboard)# Customize the Express Dashboard

Learn how to customize the Express Dashboard for your users.The Express Dashboard allows a platform’s users (connected accounts) to view their available balance, see upcoming payouts, and track their earnings in real time. It displays an Activity feed, an Earnings chart, and your platform’s brand name and icon. Learn how to customize the Express Dashboard for your users in this guide.

To learn more about each feature in the Express Dashboard, see Express Dashboard.

[Add your platform's brand name and icon](#add-platform-branding)You can display your platform’s brand name and icon in the Express Dashboard.

Access your Connect settings, enter your platform’s business_name, upload your platform’s icon, and save your changes. If you already saved your brand information before reading this guide, you can skip this step.

[Set custom descriptions for charges and transfers](#set-custom-descriptions)By default, the Transactions list on the Express Dashboard displays generic descriptions for charges and transfers (for example: Payment on {YOUR_PLATFORM}).

First, determine which type of charge your platform uses. The two recommended charge types for Express connected accounts are Destination Charges and Separate Charges and Transfers.

After you determine the charge type, use the following instructions to update your integration.

### Destination charges

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to all platforms that use destination charges.

1. Find the existing transfer object you created for an account by finding the latest[charge](/api/payment_intents/object#payment_intent_object-charges)created on the[PaymentIntent](/api/payment_intents/object).
2. Use the charge object to find the[transfer](/api/charges/object#charge_object-transfer)object associated with the charge.
3. Use the transfer object to find the[destination_payment](/api/transfers/object#transfer_object-destination_payment)ID that exists on the transfer.
4. Call the[Update Charge](/api/charges/update)API to update the[description](/api/charges/update#update_charge-description)on the destination payment using the`destination_payment`ID.

NoteThe destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d description="My custom description"`This description becomes visible on the charge after you’ve written this field.

Learn more about creating destination charges on your platform.

### Separate charges and transfers

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to platforms that use separate charges and transfers.

1. Use the transfer object to find the[destination_payment](/api/transfers/object#transfer_object-destination_payment)ID that exists on the transfer.
2. Call the[Update Charge](/api/charges/update)API to update the[description](/api/charges/update#update_charge-description)on the destination payment using the`destination_payment`ID found in the previous step.

NoteThe destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d description="My custom description"`This description becomes visible on the charge after you’ve written this field.

Learn more about creating separate charges and transfers.

## See also

- [Collect payments and then pay out](/connect/collect-then-transfer-guide)(if you process payments with Stripe)
- [Pay out money](/connect/add-and-pay-out-guide)(if you add money from a bank account to pay out)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Add your platform's brand name and icon](#add-platform-branding)[Add your platform's brand name and icon](#add-platform-branding)[Set custom descriptions for charges and transfers](#set-custom-descriptions)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
htmlSCA migration guide for Connect platforms | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fconnect-platforms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fconnect-platforms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# SCA migration guide for Connect platforms

Learn how to update your Connect platform for Strong Customer Authentication (SCA).Strong Customer Authentication applies to businesses based in the European Economic Area (EEA) that accept online payments from customers located in the EEA. Many card payments require additional authentication through 3D Secure. As of September 14, 2019, transactions that don’t follow the new authentication guidelines may be declined by a customer’s bank.

You need to update your platform if you create any of the following charges:

- [Direct charges](/connect/direct-charges)on a connected account based in the EEA.
- [Destination charges](/connect/destination-charges)if the`on_behalf_of`parameter is set and specifies a connected account based in the EEA.
- [Separate charges and transfers](/connect/separate-charges-and-transfers)if your platform is based in the EEA or if the`on_behalf_of`parameter is set and specifies a connected account based in the EEA.

[Choose an SCA-ready integration](#choose-integration)You need to update your Stripe integration to meet SCA requirements. For example, SCA requires off-session payments to be authenticated when customers enter payment details, and subsequent off-session payments may require notifying the customer to return to the application to re-authenticate. Refer to the SCA migration guide to review the integration paths for Stripe Checkout, Stripe Billing, and the Payment Intents API.

Choose Stripe Checkout if it supports the features your integration requires. Checkout is a hosted payment page that can be branded by businesses, supports recurring subscriptions, and is the easiest way to provide SCA support to your connected accounts. It supports creating direct charges and destination charges for Connect.

If you want to build a custom payments experience, use the Payment Intents API as the legacy Charges API isn’t SCA-ready. The Payment Intents API supports the same set of Connect features as the Charges API.

[Examine Connect-specific changes](#examine-connect-specific-changes)### Destination charge changes

If you’re using the destination, destination[account], or destination[amount] parameters with the Charges API, note that these parameters have been replaced with transfer_data[destination] and transfer_data[amount] in both the Charges and the Payment Intents APIs. See the following table for more information.

Use caseCharges APIPayment Intents APIYour platform is the merchant of record, but you wish to create a transfer to a connected account after the payment completesNot possibleSet[transfer_data[destination]](/api/payment_intents/object#payment_intent_object-transfer_data-destination)to the connected account’s IDYou want your connected account to be the settlement merchantwithoutcreating a separate transfer after the payment completesSet`on_behalf_of`to the connected account’s IDNo changeYou want your connected account to be the settlement merchantandyou wish to create a transfer to that account after the payment completesSet`destination`or`destination[account]`to the connected account’s IDSet[transfer_data[destination]](/api/payment_intents/object#payment_intent_object-transfer_data-destination)and[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)to the connected account’s IDYou wish to collect an application feeSet`application_fee`to the amount desiredSet[application_fee_amount](/api/payment_intents/object#payment_intent_object-application_fee_amount)to the amount desiredYou wish to transfer a partial amount to your connected account after the payment completesSet`destination[amount]`to the amount to transferSet[transfer_data[amount]](/api/payment_intents/object#payment_intent_object-transfer_data)to the amount to transfer### 3D Secure and Radar rules

Stripe Checkout and the Payment Intents API triggers dynamic 3D Secure authentication based on Radar rules. With Connect, the rules you create only apply to payments created on the platform account. Payments created directly on the connected account are subject to the connected account’s rules. Configure your default rules and test your integration with 3D Secure test cards.

### SCA impact on saving payment methods

Under SCA, authentication is required when saving a card in order to collect customer permission and qualify for off-session exemptions for subsequent off-session payments. To reduce the rate of customers having to authenticate their payment method, update your integration to use the off-session API.

If you clone saved payment methods to reuse across multiple connected accounts, note that sharing a payment method with a connected account automatically shares customer permission as well. This allows the platform to make off-session payments on any of their connected accounts without requiring the customer to authenticate their payment method again.

[Determine whether connected accounts need to make changes](#connected-account-changes)In most cases, once you update your payments integration for SCA, your connected accounts don’t have to do any additional work.

If you provide your own payments API to your connected accounts in addition to or on top of Stripe’s API, your connected accounts may need to make changes to continue accepting payments on your platform. For example, if you run a subscriptions platform on Stripe in which your connected accounts pass payment information to you via your own API, and then you pass those payment details to Stripe’s API, you’ll need to ensure both APIs are SCA-ready. If this is the case for your platform, provide guidance to your connected accounts on any changes they need to make.

[Implement and test the new integration path](#implement-changes)After you have identified your integration path and determined if your connected accounts need to make changes, follow the relevant migration guides for Stripe Checkout, Stripe Billing, or the Payment Intents API.

Once implementation is complete, configure your Dynamic 3D Secure rules to test your integration using 3D Secure test cards. Make sure to test both cases when the authentication is successful and unsuccessful.

[Educate your connected accounts](#educate)Finally, inform your connected accounts about how SCA can affect them and when your platform will be SCA-ready, regardless of whether they need to make any changes.

In particular, provide them with the following information, tailored for your business:

Strong Customer Authentication (SCA) is a new European regulatory requirement to reduce fraud and make online payments more secure. Since SCA took effect September 14, 2019, online payments require additional customer authentication. Transactions that don’t adhere to the new guidelines may be declined by your customers’ banks. This regulation applies to transactions where both the business and the cardholder’s bank are located in the European Economic Area (EEA).

If you’d like, you can also send along the SCA video and guide.

### How your platform should support SCA

If you’re not migrating to an SCA-ready solution, reach out to any of your connected accounts with significant business from European customers so they can move to a new solution before experiencing declines due to SCA.

### Any actions your connected accounts need to take

If no action is required on their end, let your connected accounts know. Similarly, if action is required, provide them with instructions on the necessary changes.

### How SCA can affect their business

SCA changes the checkout flow for card payments. Payments that require authentication ask for 3D Secure (often known by its brand names, “Verified by Visa” or “Mastercard SecureCode”), which typically adds an extra step in which the cardholder must provide additional information, such as a one-time passcode or biometric ID.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Choose an SCA-ready integration](#choose-integration)[Examine Connect-specific changes](#examine-connect-specific-changes)[Determine whether connected accounts need to make changes](#connected-account-changes)[Implement and test the new integration path](#implement-changes)[Educate your connected accounts](#educate)Products Used[Payments](/payments)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
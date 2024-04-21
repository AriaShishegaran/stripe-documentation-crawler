htmlTest your SFRA integration | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce B2C Commerce](/docs/connectors/salesforce-commerce-cloud)# Test your SFRA integration

Learn about testing your SFRA integration.After you install the cartridge and integrate it according to the instructions, try to place an order on your sandbox to test the storefront functionality.

You can find a number of test credit card numbers that you can use to test a variety of scenarios. However, the test cards only work while using your test secret and publishable API keys. You can’t use real credit card numbers with your test API keys.

You should monitor and test the integration against the Stripe Dashboard before going live. Stripe functions largely the same with both test and live transactions (aside from what credit card numbers you can use) . After you’ve completed and tested your integration, change your two Stripe API keys to take your integration live.

## Checkout

1. Add a product into the cart and view the cart page or expand the mini cart.


2. Click Checkout and check out as a Guest or log into your account.


3. Fill the shipping address or select shipping address from the saved address and select the shipping method.


4. Click Next: Payment.


5. Fill in the billing address or select the billing address from the saved address, fill in the email and phone number and select the payment method as Credit card and enter test data from the Stripe docs or use the card number 4242424242424242 and any CVV and expiration date.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-billing.5b22eb5c55cfd346eb8f6875486e137c.png)


6. Click on Next: Place Order.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-confirmation.3f48225e4cccaefe1a62fdeff435646e.png)

If your test transaction was successful, the confirmation page will open.



## Checkout using the Payment Request Button

1. Make sure you have at least one saved address and one credit card in your browser (Chrome).


2. Add a product into the cart and view the cart page or expand the mini cart.


3. Click Checkout and check out as a Guest or log into your account.


4. Fill in the shipping address or select the shipping address from a saved address and select the shipping method.


5. Click on Next: Payment.


6. Click on Pay now.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-paynow-button.d007d96ba5fd7c218c217e8f0c433ef2.png)


7. When the dialog opens, fill in the payment information and click the Pay.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-paymentsheet.db72272e07c385adf33c688bffad7149.png)


8. Enter any CVC code and click Confirm.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-paymentsheet-cvc.a3e176633d118ce3c186c174193bb39e.png)


9. Clicking Confirm redirects you to the last page of the checkout. Click Place Order.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-placeorder.edd7d82e1f398e4242e780b4dd36cee6.png)

The confirmation page opens.

![](https://b.stripecdn.com/docs-statics-srv/assets/testing-order-confirmation.07971ecaf576cebf3f5099ce6acbbc4d.png)



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Checkout](#checkout)[Checkout using the Payment Request Button](#checkout-using-the-payment-request-button)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
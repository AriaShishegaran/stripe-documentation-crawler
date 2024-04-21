htmlNetSuite customer payment page | Stripe Documentation[Skip to content](#main-content)Customer payment page[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fcustomer-payment-page)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fcustomer-payment-page)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[NetSuite](/docs/connectors/netsuite/overview)# NetSuite customer payment page

Allow customers to make payments toward their NetSuite balance using Stripe.The Stripe Connector for NetSuite automatically sets the amount due on your NetSuite customer payment page to the NetSuite customer balance total. Using a Stripe payment flow, customers can modify the amount they pay, up to the outstanding balance amount. Every accepted payment includes automated payment processing, deposit automation, and fee calculation.

You can enable the payment methods available to your customers in your Stripe account.

You can also use the customer payment page to designate how you want to apply payments, based on your business needs. For example, you can automate the payment application to specific invoices using native NetSuite settings, a custom workflow, or a custom SuiteScript. An unapplied customer payment gets created and associated with the NetSuite customer.

## Save payment methods for future use

You can use the payment page to optionally save a customer’s payment method for future use. For example, a connector add-on, such as AutoPay, might use the saved payment method to charge a customer for future invoices. Stripe saves the customer’s payment method to a new or existing Customer object.

ComplianceYou’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, if you want to save a customer’s payment method for future use, you need their agreement to be billed outside of the connector’s payment flow. Getting that agreement up front allows you to save the customer’s payment details, and potentially even charge the customer for future invoices.

If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

## Customize the payment page

You can customize the look and feel of the payment page to match the design of your site. Modify the payment page color and design on the Branding settings page in the Stripe Dashboard. Modify your name and statement descriptor on the Public details page.

## Add the payment page to your communications

You can integrate the payment page into your customer communications in NetSuite. For example, you might choose to map the payment page’s unique link to a Pay Now button in your NetSuite email templates, invoice PDF templates, or manual outreach.

## Send email receipts for payments

You have two options for sending email receipts to your customers:

- Use Stripe to automatically send email receipts. The connector provides the invoice ID and NetSuite customer email. To use this option, enable Successful payments on the Customer emails settings page in the Stripe Dashboard. You can also customize your receipts.


- Use NetSuite to send email receipts for payments. You must disable email receipts in the Stripe Dashboard and then set up a workflow to send customized email receipts from NetSuite.



## Support multiple currencies and payment methods

Accept payments in the supported presentment currencies in your region. The payment page displays the currency that’s specified on the NetSuite invoice. Stripe then creates a payment based on that currency.

You can enable the payment methods you want to accept on the Payment methods page. Stripe supports many categories of payment methods based on your region and business need.

## Automate bank reconciliation

The payment page includes deposit automation, which automates the bank reconciliation process for all payments, refunds, and disputes from a Stripe payout to a NetSuite bank deposit.

## See also

- [Invoice payment page](/connectors/netsuite/invoice-payment-page)
- [Deposit automation](/connectors/netsuite/deposit-automation)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Save payment methods for future use](#save-payment-methods-for-future-use)[Customize the payment page](#customize-the-payment-page)[Add the payment page to your communications](#add-the-payment-page-to-your-communications)[Send email receipts for payments](#send-email-receipts-for-payments)[Support multiple currencies and payment methods](#support-multiple-currencies-and-payment-methods)[Automate bank reconciliation](#automate-bank-reconciliation)[See also](#see-also)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
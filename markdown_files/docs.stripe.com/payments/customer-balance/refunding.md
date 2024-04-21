htmlRefund bank transfer payments | Stripe Documentation[Skip to content](#main-content)Refunds[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Frefunding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Frefunding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)# Refund bank transfer payments

Refund payments made with bank transfers, or refund a customer’s available cash balance.You can refund customer balance payments through the Dashboard or API.

[Refund a payment to the customerDashboardAPI](#refund-customer-balance-payment-bank-account)Stripe requires customer bank account details to process the refund. In some cases, Stripe receives the customer’s bank account details when performing the transfer. Stripe emails the customer to let them know that the refund is in process.

When we can’t determine the destination bank account automatically due to unavailable or ambiguous customer bank account information, Stripe requests it by contacting the customer at the email address in the customer object you created. If you didn’t include an email address when you created the customer object, creating a refund results in an error. Update the customer object with a valid email address for the customer, and try creating the refund again. You can specify a new email address when you create a refund.

In some cases, Stripe performs additional checks before processing a refund or asking your customers for bank account information. Stripe contacts you if we require more information before finalizing the refund.

Customers have 45 days from receipt of the request to submit bank account details. After 45 days without a valid response, Stripe cancels the refund and returns the funds to the customer’s account cash balance. We recommend you then contact your customer to discuss alternative ways of returning the funds.

You can refund a payment up to 180 days after it was created.

### Creating a payment refund using the Dashboard

1. To refund a payment made with a bank transfer, navigate to the payment page and clickRefund.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-page-header.57a436368ac47f5d34cbba18c2896b69.png)

1. In the following dialog, enter the amount you want to refund, if different than the full payment amount, and any other details about the refund. Then clickRefund.

### Creating a payment refund using the API

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d payment_intent={{PAYMENT_INTENT_ID}} \
  --data-urlencode instructions_email="customeremail@example.com"`Refunds are sent to the customer’s bank account, and the customer receives a notification at their default email address. If you want to override the default email address used to contact the customer, specify the new email address using the instructions_email parameter.

The refund’s status transitions as follows:

EventRefund statusRefund is created`requires_action`Customer submits bank account details, and Stripe begins processing the refund`pending`Refund is expected to arrive in customer’s bank`succeeded`Customer’s bank returns the funds back to Stripe`requires_action`Refund is in`requires_action`45days after creation`failed`Refund is canceled from a`requires_action`state`canceled`If the customer’s bank can’t successfully complete the transfer, the funds are returned to Stripe and the refund transitions to requires_action. This can happen if the account holder’s name doesn’t match what the recipient bank has on file or if the provided bank account number has a typo. In these cases, Stripe emails the customer to inform them of the failure and to request that they resubmit their bank account details.

If your customer does not provide their bank account details within 45 days, the refund’s status transitions to failed and the charge.refund.updated event is sent. This means that Stripe is unable to process the refund, and you must return the funds to your customer outside of Stripe.

The instructions_email field on the refund is the email that the refund was sent to. While a refund is waiting for a response from the customer, details of the email sent to the customer can also be found under the next_action.display_details.email_sent field on the refund.

Each individual refund (including each partial refund) may incur a fee. Please reach out to your point of contact at Stripe to learn more about this.

[Cancel a payment refund sent to the customerDashboardAPI](#refund-customer-balance-payment-bank-account-cancel)If a bank transfer payment refund has been sent to the customer, and the customer hasn’t submitted their bank details, you can still cancel the refund.

### Canceling a payment refund using the Dashboard

1. To cancel a refund for a bank transfer payment, navigate to the payment page and clickCancel refund.

![](https://b.stripecdn.com/docs-statics-srv/assets/cancel-payment-refund.b4596e21f2ee32cf1b2bff824de8d4b7.png)

1. If the payment has multiple partial refunds in the`requires_action`state, select the correct refund from theRefunddropdown in the following dialog.
2. Confirm the cancellation by selectingCancel refundin the dialog.

### Canceling a payment refund using the API

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds/{{REFUND_ID}}/cancel \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X POST`After the payment refund has been canceled, the refund transitions from requires_action to canceled. If there are no other refunds, the payment transitions back to its original pre-refund state.

[Refund a payment to the customer's cash balanceDashboard](#refund-customer-balance-payment-customer-balance)A refund to the customer balance succeeds immediately. Refunds to the customer balance are free of charge.

### Creating a payment refund using the Dashboard

1. To refund a payment made with a bank transfer, navigate to the payment page and clickRefund.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-page-header.57a436368ac47f5d34cbba18c2896b69.png)

1. In the following dialog, selectCustomer balancein theDestinationdropdown. Selecting this option deposits the refund into the customer’s Stripe account, which allows them to use the funds for future payments on your site.

[Refund the cash balance to the customerDashboardAPI](#create-return-dashboard)You can return a customer’s cash balance directly to them. For example, you might need to do this when a customer transfers more funds than expected for a payment.

### Refund a customer’s cash balance using the Dashboard

1. Navigate to the[Customer list](https://dashboard.stripe.com/customers)page.
2. Click the customer in the list of customers.
3. Expand theCash Balancerow in thePayment methodssection.
4. ClickInitiate Refundbutton at the end of the row.

![](https://b.stripecdn.com/docs-statics-srv/assets/customer_balance_row.224a651cdaecf7e3b05c8046dc0e103a.png)

1. In the next dialog, enter the amount to refund.
2. ClickInitiate Refund.

View the status of the refund on the customer balance transactions list page.

### Refund a customer’s cash balance using the API

To refund a customer’s cash balance with the API, set the origin parameter to customer_balance and specify the customer. The customer’s default email address is used to contact them. To override it, specify the new email address using the instructions_email parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  --data-urlencode instructions_email="jenny.rosen@example.com" \
  -d origin=customer_balance`[Cancel a cash balance refund sent to the customerDashboard](#create-return-dashboard-cancel)You can only cancel un-processed refunds. After the customer submits their bank account details, you can’t cancel a refund. Currently, you must use the Stripe Dashboard to cancel a refund:

1. Navigate to the[Customer list](https://dashboard.stripe.com/customers)page.
2. Click the customer in the list of customers.
3. Expand theCash Balancerow in thePayment methodssection.
4. Click theView balance detailslink.

![](https://b.stripecdn.com/docs-statics-srv/assets/cash_balance_transactions_link.2315ea0a6110fd68d550961b570622e6.png)

1. Click the overflow menu (•••) next to the refund you want to cancel and click theCancellink

![](https://b.stripecdn.com/docs-statics-srv/assets/cancel_customer_return.2b049b51896c523d27f56eaa437db52f.png)

The refund amount is credited back to the available cash balance.

[Track state of a refund](#tracking-refunds)You can track the state of a refund through the Dashboard or API.

### When and where refund email is sent

Stripe sends an email to the email address provided in the instructions_email field on the refund. While a refund is waiting for a response from the customer, you can also check the refund’s next_action.display_details.email_sent field for details such as the sent time and the address. The sent time is also the time when the refund transitioned to the requires_action state.

### Pending refunds

If the customer has submitted their bank account details, the refund transitions to pending.

### Successful refunds

The refund transitions to succeeded when the refund is successfully paid out to the customer.

[Testing refunds](#testing-refunds)You can test refund behavior in test mode using the following test bank accounts on the bank account details collection page linked in the email sent to the customer. Bank account details outside of these test bank accounts won’t be accepted.

NoteIn test mode, refund instruction emails are only sent to email addresses linked to the Stripe account.

IBANJapanMexicoUnited KingdomUnited StatesSpecify the appropriate country code (for example, GB, IL, CR, and so on) to test IBANs for any IBAN country and any valid currency for that country. For instance, the following IBANs specify Germany with the DE prefix.

NumberType`DE89370400440532013000`Refund succeeds.DE62370400440532013001

DE89370400440532013002

DE89370400440532013003

DE89370400440532013004

DE89370400440532013005

Refund fails.

Testing Refunds Expiry![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can make an API call to simulate the expiry of a testmode refund.

Command Line`curl https://api.stripe.com/v1/test_helpers/refunds/{{REFUND_ID}}/expire \
  -X POST \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Refund a payment to the customer](#refund-customer-balance-payment-bank-account)[Cancel a payment refund sent to the customer](#refund-customer-balance-payment-bank-account-cancel)[Refund a payment to the customer's cash balance](#refund-customer-balance-payment-customer-balance)[Refund the cash balance to the customer](#create-return-dashboard)[Cancel a cash balance refund sent to the customer](#create-return-dashboard-cancel)[Track state of a refund](#tracking-refunds)[Testing refunds](#testing-refunds)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
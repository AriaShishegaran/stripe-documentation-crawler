htmlWorking with SetupIntents, PaymentMethods, and BankAccounts | Stripe Documentation[Skip to content](#main-content)Working with SetupIntents, PaymentMethods, and BankAccounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fworking-with-bankaccount-objects)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fworking-with-bankaccount-objects)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Working with SetupIntents, PaymentMethods, and BankAccounts

Learn how to set up money movements in Treasury.You can use PaymentMethod objects to save account credentials for a US-based bank account for future use. After creating the PaymentMethod, you can use the same object repeatedly to move funds into and out of a financial account. Depending on your use case, you can attach the PaymentMethod to either a Customer object or the Stripe account.

- Attach the`PaymentMethod`to a`Customer`object if you intend to use the payment method for an outbound payment to a third party.
- Attach the`PaymentMethod`to a connected account or platform account if you intend to use the payment method for an inbound transfer or outbound transfer between an external account that belongs to the same business as the Stripe account.

NoteThe Customer object defines a third-party entity that represents the owner of an external bank account.

If you previously collected customer payment details with Stripe using the BankAccounts object, you can substitute the BankAccount for a PaymentMethod in those requests. For InboundTransfers, the BankAccount status value in this case must be verified. We recommend using PaymentMethods where possible to get the full suite of features.

In some cases, banks on the receiving end of ACH money movements notify Stripe that account information (such as account number or routing number) has changed. If we receive such a notification for an account associated with a PaymentMethod or BankAccount object, we automatically update the object. See the ACH Notification of Change handling guide for more information.

## Create a SetupIntent to save us_bank_account details

SetupIntents enable you to set up a payment method to use with money movement endpoints of the Stripe API. Use SetupIntents to save customer or account credentials as a payment method and optimize them for the objects you intend to use it with. For example, when setting up a US bank account, it’s necessary to verify the bank account if you intend to debit that external account with an inbound transfer. Stripe updates the SetupIntent object throughout the setup process.

The following example demonstrates using a SetupIntent with a bank account that allows for bidirectional fund transfers. For complete details on how to set up a payment method for creating payments and bank account verification, see the Save details for future payments with ACH Direct Debit guide. When setting up payment methods for managing financial account funds with SetupIntents, the following fields are the most relevant:

- [flow_directions](/api/setup_intents/create#create_setup_intent-flow_directions): this array defines the directionality of the flows for a payment method. It’s possible values are`inbound`and`outbound`, denoting if the payment method can move funds into, out of, or both into and out of a financial account. You can also configure an existing payment method to become bidirectional.
- [attach_to_self](/api/setup_intents/create#create_setup_intent-attach_to_self): a Boolean flag to indicate whether you want to attach this payment method to the in-context`Account`object. Set this as`true`to create an account-attached payment method for managing this account’s own money movement flows like inbound transfers and outbound transfers.
- [customer](/api/setup_intents/create#create_setup_intent-confirm): ID of the`Customer`object the payment method is attached to on successful setup. You can use`Customer`-attached payment methods with outbound payments to send money to third parties and customers. You can also use them with Stripe Payments`PaymentIntents`to receive money. You must set the`attach_to_self`attribute to`false`or leave it blank when creating a customer-attached payment method.

### Permissions

To use a payment method for ‘inbound’ flow directions (such as InboundTransfers), you need permission from the user. Creating this agreement (Mandate object) up front and associating it with the payment method allows you to charge the payment method later.

Add terms to your website or app that state how you plan to debit funds from external accounts, and let users opt in. At a minimum, ensure that your terms cover the following:

- User permission for you to initiate a debit or a series of debits on their behalf
- The anticipated frequency of debits (one-time or recurring)
- How the debit amount is determined

While you need user permission with a mandate for debiting an external bank account in the US with inbound transfers, that permission isn’t needed for sending money to a bank account with outbound transfers or outbound payments.

### Creating a SetupIntent

To create a SetupIntent, you must either use an existing payment method with the payment_method parameter, or provide new credentials using the inline payment_method_data parameter.

Use POST /v1/setup_intents to create a SetupIntent.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d payment_method={{PAYMENT_METHOD_ID}}`If successful, the response returns the newly created SetupIntent object.

[JSON (commented)](#)`{
  // ID of the Customer to attach the resulting PaymentMethod to
  "customer": "{{CUSTOMER_ID}}",
  "attach_to_self": false,
  // Configure what direction of funds flows this PaymentMethod will support.
  "flow_directions": ["inbound", "outbound"],
 // US Bank Account credentials
  "payment_method_types": ["us_bank_account"],
  "payment_method_data": {
    "type": "us_bank_account",`See all 48 linesThe SetupIntent has one of the following statuses:

STATUSDESCRIPTIONNEXT STEPS`succeeded`The bank account has been instantly verified or verification isn’t necessary.No action needed.`requires_action`Further action needed to complete bank account verification.See`next_action`for further setup steps.After successfully confirming the SetupIntent, Stripe sends an email confirmation of the mandate and collected bank account details to your user. The default email references Stripe Payments, so if you use Stripe Treasury without Stripe Payments you might want to turn off Stripe emails and send custom messages instead.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
htmlCopy PAN data across Stripe accounts | Stripe Documentation[Skip to content](#main-content)Copy PAN data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations%2Fpan-copy-self-serve)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations%2Fpan-copy-self-serve)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)
Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)PAN data migrations# Copy PAN data across Stripe accounts

Securely copy sensitive primary account number data within Stripe.Stripe’s self-serve data copy service allows you to copy customer and payment data from one Stripe account to another Stripe account in the Dashboard.

A data copy involves two parties: the sender account and the recipient account.

- Sender account: The Stripe account currently storing the customer data. This is the account to copy the data from.
- Recipient account: The Stripe account where you want to store the customer data. This is the account to copy the data to.

Before beginning the copying process, the sender and the recipient must provide their account IDs to each other. If you’re the sender account, work with a user of the recipient account to share account IDs. If you’re the recipient account, work with a user of the sender account to share account IDs. Find your account ID by going to the User settings in the Dashboard while logged into your account.

## Data copying considerations

Consider the following when copying data to a new account:

- We can only copy data from one account to another. We can’t merge or move the data. After it’s complete, the copied data exists on both the destination and source accounts.


- We only copy the raw Customer objects and associated payment data objects. The supported payment methods include:

  - Cards stored as[Card](/api/cards/object)objects
  - Cards stored as[Source](/api/sources/object)objects
  - Cards stored as[Payment method](/api/payment_methods/object)objects
  - US ACH records stored as[Bank account](/api/customer_bank_accounts/object)objects


- We can’t copy Single Euro Payments Area (SEPA), BACs, or ACH records stored as payment method objects at this time.


- We can’t copy individual Charges, PaymentIntents, Invoices, Plans, Subscriptions, Coupons, Events, Logs, Guest customers, or any other Stripe objects.


- The copy operation doesn’t change customer IDs, resulting in the same IDs for customers in both the destination and source account data.


- The copy process assigns new object IDs of the same payment type to payment data. For example, the process assigns a new card object ID to all card objects and new payment method object IDs to all payment method objects. After the copy process is complete, Stripe creates and uploads a CSV mapping file to the Documents section of the recipient’s Dashboard. The mapping file is available to the recipient only. The mapping file contains the following headers:

  - `customer_id_old`
  - `source_id_old`
  - `customer_id_new`
  - `source_id_new`

Customer IDs don’t change during the copying process, so customer_id_old and customer_id_new have the same value after the copy finishes. source_id_old is the old payment method ID from the sharing account, and source_id_new is the new payment method ID from the recipient account.


- Source account data remains intact. We recommend keeping the original source account as a backup for your data.


- The recipient account must be an activated account. To activate the account, log in to the Dashboard and follow the prompts at the top-left of the home screen to activate payments.


- You can’t copy deleted customers from the sharing account to the recipient account. After you delete a Customer, there’s no way to restore that customer.


- If you delete a customer in the recipient account, a second copy doesn’t restore that customer.


- During a second copy involving the same accounts and same customers, previously-copied Customer objects aren’t duplicated. The second copy copies over brand new Stripe Customer objects or new payment methods only for previously-copied Customer objects. If you delete a customer in the account, re-copying that customer from the sharing account doesn’t restore that customer.


- The copy includes only Stripe Customer objects (cus_xxx). We can’t copy Guest (gcus_xxxx) customers—see Guest customers to learn more. Sender accounts must have Customer objects stored to process a data copy.


- Accounts can perform up to 50 copies per day. Stripe limits copies to unauthorized accounts to one copy until the recipient account authorizes the first copy request.


- If any expired cards are included in the records that you copy over to the destination account, there’s the possibility that Card Account Updater (CAU)—if turned on for the destination account—will communicate with the card networks to automatically update these cards. This can result in additional CAU fees for the destination account. To avoid the possibility of CAU fees related to a self-serve copy, the destination account team must work with the source account team to make sure that no expired cards are included in the copy data set.



## Full or partial copy

You can perform a full or partial copy. A full copy sends all customers from the sender account. A partial copy sends a subset of customers from the sender account.

A partial copy entails sending a subset of customers from the sender account to the recipient account. There are two ways to complete a partial copy:

- Select customers in the Dashboard: Recommended for copies of less than 15 customers
- Upload a CSV file with a list of customer IDs: Recommended for copies of more than 15 customers

Full copyPartial copy with customer selectionPartial copy with CSV uploadYou need to complete three steps for a full data copy:

1. The sender shares their customer data with the recipient.
2. The recipient authorizes and accepts the customer data from the sender.
3. The copying process finishes.

## Share customer data with the recipient

1. The sender logs into their[Stripe account](https://dashboard.stripe.com/login)and navigates to the[Customers](https://dashboard.stripe.com/customers)page.
2. They clickCopy customers.
3. In theCopy Methodfield, they clickCopy all customers.
4. They enter the account ID (`acct_xxxx`) of the recipient account and clickContinue.If they haven’t previously shared customers with this recipient account, they receive a message stating that the recipient needs to authorize your request before the copy occurs.
5. They clickConfirm.
6. After successfully sharing the data with the recipient, the sender can see the pending copy request at the top of their Customers page.

## Authorize and accept customer data from the sender

The recipient logs into their Stripe account and navigates to the Customers page, where they see a banner at the top advising that the sender wants to share their data. The recipient clicks Authorize and Accept.

## The copying process finishes

After the sender completes the previous steps, the copy begins processing. The sender and recipient can see the in-progress copy banner at the top of the Customers page in the Dashboard.

Most data copies finish within 72 hours, after the sender shares the customer data with the recipient and the recipient authorizes and accepts the customer data from the sender. Copies of fewer than 10,000 customers typically complete within a couple of hours.

When the copying process is complete, the sender and recipient can see the completed copy banner at the top of the Customers page in the Dashboard. The recipient has the option to download the mapping file.

## Copy into or out of a Connect account

If the sender account is a Connect account without access to the Stripe Dashboard, reach out to your contact at the Platform to let them know you need a data copy. The Platform account owner or Data Migration Specialist needs to follow these steps:

Partial copy with customer selection isn’t available for Connect accounts.

Full copyPartial copy with CSV upload1. The Platform account owner or Data Migration Specialist logs into their Stripe account and navigates to the[Connect](https://dashboard.stripe.com/connect/accounts/overview)page.
2. The sender locates and selects the correct Connect account where the customers are stored.
3. They navigate to the Customers section within the Connect account.
4. They clickCopy customers.
5. In theCopy Methodfield, they clickCopy all customers.
6. They enter the account ID (format: acct_xxxx) of the recipient account and clickContinue. If they haven’t previously shared customers with this recipient account, they receive a message stating that the recipient needs to authorize your request before the copy occurs.
7. They clickConfirm.  After successfully sharing the data with the recipient, they can see the pending copy request at the top of the Customers page within the Connect account.
8. The recipient follows standard steps for authorizing and accepting customer data.

If the recipient account is a Connect account that doesn’t have access to the Stripe Dashboard, reach out to your contact at the Platform to let them know you need a data copy.

The Platform account owner, Admin, or Data Migration Specialist need to authorize and accept customer data from the sender after the sender shares it.

To authorize the data, the recipient logs into the Platform Stripe account, navigates to the Connect page, locates the Connect account where the customers were shared, and clicks Authorize and Accept on the banner in the Customers section.

If your customers are stored in a Platform account that you don’t own, inform your contact at the Platform that you need a data copy. Direct them to follow the steps to share your customers with the recipient account. Platform accounts typically store customers for several unrelated Connected accounts. Make sure the Platform account shares only your customers, by following the steps to do a partial copy.

## Status page

If you’re an account owner or data migration specialist, you can view in-progress and completed copies by going to the Customers page and selecting Copy customers then Status page. You can toggle between Shared data and Received data.

For all other roles, you can view in-progress and complete copies on the copy status page.

### Shared

On the Shared tab, you can see copies where your account was the sender account, sharing your customers to other accounts.

In progress copies are copies that are currently processing or where the sender account has initiated the copy, but the recipient hasn’t authorized and accepted it. For Pending copies, the recipient needs to authorize and accept the copy to proceed. Most In progress copies finish within 72 hours. Copies of fewer than 10,000 customers typically complete within a couple of hours.

Previously shared copies are copies that were successful or canceled from your account to another.

### Received

On the Received tab, you can see copies where your account was the recipient account, receiving customers from other accounts.

In progress copies are copies that are currently processing or where the sender account has initiated the copy, but you as the recipient haven’t authorized and accepted it. For Pending copies, you need to authorize and accept the copy to proceed. Most In progress copies in this state finish within 72 hours. Copies of fewer than 10,000 customers typically complete within a couple of hours.

Previously shared with you copies are copies that were successful or canceled from another account to your account.

Sharing permissions are the accounts that have previously shared their customers with you. For any future copies from these accounts to yours, the sender account still needs to share customer data with you, and you still need to accept the data. Authorized accounts see your business name when they enter your account ID during the sharing step.

View all navigates to the Authorized accounts page, which shows the accounts authorized to send you their data. You still need to accept the data copy requests from these accounts, but these accounts now have the ability to see your business name when they enter your account ID during the sharing step. You can revoke permission from any accounts in this list, which prevents them from seeing your business name during the sharing process. When revoked, future copy requests must be authorized and accepted. Only account owners, admins, and data migration specialists can add and revoke authorized accounts.

## Permissions restrictions

Only the account owner or a Data Migration Specialist can perform actions from the sender account. Only the account owner, an account admin, or a Data Migration Specialist can perform actions from the recipient account.

Learn how to add a team member as a Data Migration Specialist.

## India account considerations

Data copies aren’t permitted between India Stripe accounts and accounts outside of India. There are regulations in India that require local storage of certain payments data. As part of our continued investment in India and to meet these requirements, we’re updating our systems and have reviewed the data migrations we offer to Stripe users. The data storage requirements prevent us from proceeding with the data copy you’ve requested. If you attempt to complete a copy between an India Stripe account and an account outside of India, you receive an error message that says copying isn’t permissible.

NoteTokenized cards aren’t copied.

## Get Stripe support

If you run into issues or have any questions when completing the data copy, contact the Data Migration Team with this intake form. You must be logged in to your Stripe account before clicking this link.

In the intake form, for migration type, select Tell us about your other data migration use case, and fill out the form accordingly. If you’ve already initiated a data copy, provide the migration request ID associated with the copy request. The migration request ID is in the pending banner or the status page.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Data copying considerations](#data-considerations)[Full or partial copy](#full-or-partial)[Share customer data with the recipient](#share-customer-data-with-the-recipient)[Authorize and accept customer data from the sender](#authorize-and-accept-customer-data-from-the-sender)[The copying process finishes](#the-copying-process-finishes)[Copy into or out of a Connect account](#copy-into-or-out-of-a-connect-account)[Status page](#status-page)[Permissions restrictions](#permissions-restrictions)[India account considerations](#india-account-considerations)[Get Stripe support](#get-stripe-support)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
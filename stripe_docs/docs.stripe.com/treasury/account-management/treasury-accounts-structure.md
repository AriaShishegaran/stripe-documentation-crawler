# Stripe Treasury accounts structure

Understanding the technical components of Stripe Treasury is important for you to develop an optimized financial service for the sellers and service providers on your platform. A crucial first step in that understanding is to learn the different account types involved with a Treasury integration.

## Account types

Your platform must have Stripe Connect to use Treasury. In its most basic form, a Connect integration includes a platform account with many connected accounts, each owned by a seller or service provider that uses the platform. Both the platform account and its connected accounts are Account objects in the Stripe API. There are different types of connected accounts, but Treasury only supports the Custom connected account type. You can learn more about account types in the Choose your account type guide for Connect. For more information on using connected accounts with Treasury, see the Working with connected accounts guide.

[Connect](/connect)

[Account](/api/accounts)

[Choose your account type](/connect/accounts)

[Working with connected accounts](/treasury/account-management/connected-accounts)

A Connect platform with connected accounts

Stripe Treasury introduces another type of account to the Stripe ecosystem: financial accounts. When you onboard your platform to Treasury, Stripe automatically creates and assigns a FinancialAccount object to your platform account. As the platform, you request the treasury capability when requesting the capabilities you need for your connected accounts. After you request it, Stripe updates the connected account’s Account object to include additional requirements in its requirements hash. You can create financial accounts for your connected accounts, but until you gather the requirements from your connected account owners, the financial accounts aren’t accessible. For more information on using Treasury financial accounts, see the Working with financial accounts guide.

[requirements hash](/api/accounts/object#account_object-requirements)

[Working with financial accounts](/treasury/account-management/financial-accounts)

## Account balances

Each account in Stripe Connect (both platform and connected accounts) has an account balance that tracks pending and available funds for that account. With Stripe Treasury, each of these accounts can also have a financial account, which has a balance of its own. Treasury provides you the tools to transfer funds between the platform account and financial account, but their respective balances always remain separate. However, funds can’t be transferred from a platform end-user’s financial account to their connected account. For more information on platform and connected account balances, see the Understanding Connect account balances guide. For more information on financial account balances, see the Working with balances and transactions guide.

[account balance](/connect/account-balances)

[Understanding Connect account balances](/connect/account-balances)

[Working with balances and transactions](/treasury/account-management/working-with-balances-and-transactions)

Flow of funds between accounts

## Flow of funds between accounts

Although the payments balance and financial account balances are separate, Treasury supports the flow of funds between the two. Treasury also enables you to transfer funds from your platform financial account to the financial accounts attached to your platform’s connected accounts. You can use Payouts to send funds from your payment balance to your financial account or to the financial accounts attached to your platform’s connected accounts. To move money between two financial accounts, Treasury introduces OutboundPayment objects to facilitate this movement.

[Payouts](/api/payouts)

[OutboundPayment](/api/treasury/outbound_payments)

Transfers affect funds on the Stripe Account Balance, so if you want to move funds between two financial accounts, you must use OutboundPayments.

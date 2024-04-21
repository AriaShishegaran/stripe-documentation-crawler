# Embedded Finance integration guide

Check out our introductory guide to using BaaS for SaaS Platforms.

[BaaS for SaaS Platforms](https://stripe.com/guides/introduction-to-banking-as-a-service)

Build a US embedded financial services offering using Stripe Issuing and Treasury. Use Issuing to create cards, and Treasury to store balances and fund card spend.

[Issuing](/issuing/how-issuing-works)

[Treasury](/treasury)

By the end of this guide, you’ll know how to:

- Create verified connected accounts representing your business customers with relevant Issuing and Treasury capabilities

- Create financial accounts that you can use as a wallet for your business customers and add funds to using an external bank account

- Create virtual cards for your business customers and use these cards to spend funds from a wallet

## Before you begin

- Sign up for a Stripe account.

[Stripe account](https://dashboard.stripe.com/register)

- Activate Issuing and Treasury in test mode from the Dashboard. For more information, see API access to Issuing and Treasury.

[Activate Issuing and Treasury in test mode](https://dashboard.stripe.com/setup/treasury/activate?a=1)

[API access to Issuing and Treasury](/treasury/access)

- Configure your Connect platform branding settings for your business and add an icon.

[Connect platform branding settings](https://dashboard.stripe.com/settings/connect)

[Create connected accounts](#set-up-connect)

## Create connected accounts

Create a connected account to represent a business customer of your platform.  For example, if your product is a SaaS platform for restaurants, each restaurant would be represented as a connected account

Issuing and Treasury only support custom Connect account types. If you’re an existing platform on standard or express account types, you need to migrate to custom Connect.

[account types](/connect/accounts)

The following request creates a new US-based custom connected account and requests the requisite capabilities:

The user’s account information appears in the response:

Note the connected account’s id. You’ll provide this value to authenticate as the connected account by passing it into requests in the Stripe-Account header.

[authenticate](/connect/authentication)

If a connected account already exists, you can add the requisite capabilities by specifying the connected account id in the API request:

Choose one of the following onboarding options:

Stripe-hosted onboarding is a web form hosted by Stripe with your brand’s name, color, and icon. Stripe-hosted onboarding uses the Accounts API to read the requirements and generate an onboarding form with robust data validation and is localized for all Stripe-supported countries.

[Stripe-hosted onboarding](/connect/custom/hosted-onboarding)

[Accounts API](/api/accounts)

Before using Connect Onboarding, you must provide the name, color, and icon of your brand in the Branding section of your Connect settings page.

[Connect settings page](https://dashboard.stripe.com/test/settings/connect)

You can use hosted onboarding to allow users to link an external_account (which is required for payouts) by enabling it through your Connect Onboarding settings.

[Connect Onboarding settings](https://dashboard.stripe.com/settings/connect)

To create a link for the user to onboard to a connected account, use the Account Links API.

[Account Links API](/api/account_links/create)

For security reasons, don’t email, text, or send account link URLs directly to your user. We recommend that you distribute the account link URL from within your platform’s application, where their account is authenticated.

The response you receive includes the url parameter containing the link for your user to onboard to your platform.

[https://connect.stripe.com/setup/s/…](https://connect.stripe.com/setup/s/…)

At this point, Stripe has created and verified the connected account with active relevant capabilities to use Issuing and Treasury.

To learn more, see:

- Set up an Issuing and Connect integration

[Set up an Issuing and Connect integration](/issuing/connect)

- Stripe hosted onboarding for Custom accounts

[Stripe hosted onboarding for Custom accounts](/connect/custom/hosted-onboarding)

- Using Connect with Custom accounts

[Using Connect with Custom accounts](/connect/custom-accounts)

- Identify verification for Custom accounts

[Identify verification for Custom accounts](/connect/identity-verification)

[Create financial accounts and add funds](#create-financial-accounts-add-funds)

## Create financial accounts and add funds

After you enable Treasury on your platform, add FinancialAccount objects to your platform architecture to enable the efficient storing, sending, and receiving of funds. Stripe attaches a financial account to your platform account after enablement, and lets you provision an individual financial account for each eligible connected account on your platform.

[FinancialAccount](/api/treasury/financial_accounts)

[platform architecture](/treasury/account-management/treasury-accounts-structure)

In the Stripe API, FinancialAccount objects serve as the source and destination of money movement API requests. You request Features through the API to assign to FinancialAccounts that provide additional functionality for the financial accounts on your platform.

A financial account operates a distinct balance of funds from the connected account payments balance of the account it’s linked to. For example, the owner of a connected account on your platform might have a 100 USD connected account balance and a 200 USD financial account balance. In this scenario, the connected account owner has a sum of 300 USD spread between their financial account and connected account balances. These two balances remain separate, but the API provides the ability to move money from the connected account balance to the financial account balance.

[balance of funds](/treasury/account-management/working-with-balances-and-transactions)

The multiple financial account beta feature enables you to open multiple financial accounts for a single connected account. Contact treasury-support@stripe.com to access test mode for this feature and join the wait list.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

After Stripe adds the treasury capability to an account and it’s marked active, you can create a FinancialAccount object for the connected account. To do this, call FinancialAccounts and request the Features you want to provide:

The response, when you request features on financial account creation, indicates their status in the active_features, pending_features, and restricted_features parameters:

Activation might be instantaneous for some features (for example, card_issuing). However, other features, like financial_addresses.aba, activate asynchronously, might stay pending for up to 30 minutes while Stripe communicates with external systems. After all of the relevant features are active, you get confirmation on the treasury.financial_account.features_status_updated webhook listener.  See Available features for more information on financial account features.

[activate asynchronously](https://tripe.com/docs/treasury/account-management/financial-account-features#webhooks)

[Available features](/treasury/account-management/financial-account-features#available-features)

To let your customers transfer money to and from an external account, create a SetupIntent with the required parameters and attach it to self to denote that the external account is owned by your customer:

The API response includes a unique identifier for the payment_method that’s used to reference this bank account when making ACH transfers:

Before you can use a bank account, it must be verified using microdeposits (which we focus on here) or the faster financial connections option. The SetupIntent response from the previous step includes a hosted_verification_url which you must present to your customer for them to input the associated descriptor code of the microdeposit. Use the value SM11AA to verify the bank account, or test a variety of other cases by using the test account numbers Stripe provides.

[financial connections](/financial-connections)

[test account numbers](/payments/ach-debit/set-up-payment?platform=web&payment-ui=stripe-hosted#test-account-numbers)

Microdeposit verification

Using the embedded Financial account component in your application, you can enable your Connected Accounts to transfer funds into the Financial account.

[Financial account component](/connect/supported-embedded-components/financial-account)

When creating an Account Session, enable the financial account component by specifying financial_account in the components parameter. You can enable or disable individual features of the financial account component by specifying the features parameter under financial_account.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the financial account component in the frontend:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

From here, users can click Move money to initiate a transfer.

At this point, the connected account has a FinancialAccount that has been loaded with funds received from an InboundTransfer that you can spend using cards or OutboundPayments like ACH or wires.

To learn more, see:

- Getting permissions for InboundTransfers

[Getting permissions for InboundTransfers](/treasury/moving-money/working-with-bankaccount-objects#permissions)

- Working with Treasury financial accounts

[Working with Treasury financial accounts](/treasury/account-management/financial-accounts)

- Using Treasury to move money

[Using Treasury to move money](/treasury/examples/moving-money#microdeposits)

- Requesting features on a Financial Account

[Requesting features on a Financial Account](/treasury/account-management/financial-account-features#available-features)

- Working with SetupIntents, PaymentMethods, and BankAccounts

[Working with SetupIntents, PaymentMethods, and BankAccounts](/treasury/moving-money/working-with-bankaccount-objects)

- Moving money with Treasury using InboundTransfer objects

[Moving money with Treasury using InboundTransfer objects](/treasury/moving-money/financial-accounts/into/inbound-transfers)

- Moving money with Treasury using ReceivedCredit objects

[Moving money with Treasury using ReceivedCredit objects](/treasury/moving-money/financial-accounts/into/received-credits)

[Create cardholders and cards](#create-cardholders-cards)

## Create cardholders and cards

The Cardholder is the individual (that is, employee or contractor) that’s authorized by your business customer to use card funding by the FinancialAccount. The Cardholder object includes relevant details, such as a name to display on cards and a billing address, which is usually the business address of the connected account or your platform.

[Cardholder](/api/issuing/cardholder/object)

[name](/api/issuing/cardholders/object#issuing_cardholder_object-name)

[billing](/api/issuing/cardholders/object#issuing_cardholder_object-billing)

Use the embedded Issuing cards list component to enable your connected accounts to create a Card for a Cardholder and associate it with the Financial Account.

[Issuing cards list component](/connect/supported-embedded-components/issuing-cards-list)

[Card](/api/issuing/cards/object)

When creating an Account Session, enable the Issuing cards list component by specifying issuing_cards_list in the components parameter. You can enable or disable individual features of the Issuing cards list component by specifying the features parameter under issuing_cards_list.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the Issuing cards list component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

From here, users can click Create card to begin creating a new Cardholder and Card. The user can also activate the card during creation, or do so afterwards.

At this point, there’s an active card attached to a cardholder and financial account. See the Issuing page for the connected account to view the card and cardholder information.

[Issuing page](https://dashboard.stripe.com/issuing/overview)

To learn more, see:

- Virtual cards with Issuing

[Virtual cards with Issuing](/issuing/cards/virtual)

- Physical cards

[Physical cards](/issuing/cards/physical)

- Using the Dashboard for Issuing with Connect

[Using the Dashboard for Issuing with Connect](/issuing/connect#using-dashboard-issuing)

- Create cards with the API

[Create cards with the API](/issuing/cards)

- Testing physical card shipment

[Testing physical card shipment](/issuing/cards/physical/testing)

[Use the card](#use-card)

## Use the card

To observe the impact of card activity on the financial account, generate a test authorization. You can do this in the Issuing page of the Dashboard for the connected account, or with the following call to the Authorization API:

[Authorization API](/api/issuing/authorizations)

After approval, Stripe creates an Authorization in a pending state while it waits for capture. Note the authorization id that you’ll use to capture the funds:

[capture](/issuing/purchases/transactions)

You can use retrieve the balance details of the financial account and see the impact of the authorization:

The API response is a FinancialAccount object with a balance hash that details the funds and their availability:

The response indicates 190 USD is currently available for use with an additional 10 USD held in outbound_pending from the pending authorization. You can now simulate capture of the authorization with the API.

Capture the funds using the following code:

After the authorization is captured, Stripe creates an Issuing Transaction, the status of the authorization is set to closed, and a ReceivedDebit webhook is created with these details. Retrieving the balance details of the financial account again shows the outbound_pending is now 0 USD while the available cash is remains 190 USD:

[Transaction](/issuing/purchases/transactions)

## See also

- Handling real-time auth webhooks

[Handling real-time auth webhooks](/issuing/controls/real-time-authorizations)

- Spending controls

[Spending controls](/issuing/controls/spending-controls)

- Issuing authorizations

[Issuing authorizations](/issuing/purchases/authorizations)

- Issuing transactions

[Issuing transactions](/issuing/purchases/transactions)

- Testing Issuing

[Testing Issuing](/issuing/testing)

- Working with Stripe Issuing cards and Treasury

[Working with Stripe Issuing cards and Treasury](/treasury/account-management/issuing-cards)

- Manage transaction fraud

[Manage transaction fraud](/issuing/manage-fraud)

- Issue regulated customer notices

[Issue regulated customer notices](/issuing/compliance-us/issuing-regulated-customer-notices)

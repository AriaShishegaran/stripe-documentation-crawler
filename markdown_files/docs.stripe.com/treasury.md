htmlOverview of Stripe Treasury | Stripe Documentation[Skip to content](#main-content)Overview of Stripe Treasury[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Banking as a service](/docs/financial-services)# Overview of Stripe Treasury

Learn about the Stripe Treasury API.Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe’s API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.

Fill out the Treasury form to get access to test mode.

Businesses serving US-based commercial businesses are immediately granted access to test mode after completing the form. All other businesses will gain access after a member of the Stripe team reviews your information and confirms supportability. See our Treasury requirements guide for more information on which businesses can use Treasury.

## Building blocks for financial services

Stripe Treasury provides the modular components you need to build a full-featured, scalable financial product for your customers.

Create accountsStore fundsMove moneyAttach payment cardsOnboard users, verify their identity, and provision Treasury financial accounts with one of our bank partners in minutes.

- ID verification
- [KYC](https://en.wikipedia.org/wiki/Know_your_customer)checks
- Sanctions screening

We’ve partnered with trusted banks, including Evolve Bank & Trust and Goldman Sachs, to provide the banking-as-a-service infrastructure for you to build new financial service offerings.

## Treasury use cases

Here are some use cases commonly addressed with Stripe Treasury:

- Spend management— Build a spend management product for your customers to store funds on your platform and manage spending with branded cards.
- Store and spend account— CreateFDICinsurance-eligible accounts that allow businesses to store funds, earn yield, deposit checks, and pay contractors and vendors withACHandwire transfers.
- Programmatic money movement— Facilitate fast and efficient money movement for your platform’s businesses to other businesses on your platform or to third-party accounts.

## Treasury account architecture

With Stripe Connect, you onboard customers to your platform with connected accounts. For each of these connected accounts, you create a financial account that offers a range of benefits to your platform’s users. The following diagram illustrates an overview of a platform with Stripe Treasury integration.

Treasury account architecture

### Connected accounts

Connected accounts are sellers or service providers that use a platform. For example, as a digital storefront platform owner, you provide an e-commerce framework that businesses can leverage to easily establish their online stores. Each digital store owner that uses the storefront platform to collect payments is a connected account.

There are three types of connected accounts on Stripe: Standard, Custom, and Express. The current version of Treasury supports only Custom connected accounts. To learn how to create Custom accounts, see Create a Custom account. To learn more about the types of connected accounts, see Choose your account type.

### Financial accounts

Using Treasury endpoints of the Stripe API, you can create financial accounts and attach them to connected accounts in a one to one relationship (unless you are enrolled in the Multi  FA beta). Treasury financial accounts have routing numbers because they’re backed by US banking partners, and balances are eligible for FDIC pass-through insurance. You can fund the financial accounts of your platform’s connected accounts, as well as move money between them. The sellers and service providers (connected accounts) on your platform can also fund their Treasury financial accounts using a bank external to Stripe. If your platform uses Stripe Issuing, you can provide payment cards linked to the financial account balance of your connected accounts.

## Sample integration

Follow our two-part sample integration to see how Treasury works.

[Using Treasury to set up financial accounts and cardsSetting up a financial account with Treasury and issuing cards.](/treasury/examples/financial-accounts)[Using Treasury to move moneyUsing SetupIntent, PaymentMethods, and verifying bank accounts with Stripe Treasury.](/treasury/examples/moving-money)Stripe Treasury is provided in the US by Stripe Payments Company, licensed money transmitter, with funds held at Stripe’s bank partners, Members FDIC. Card and other credit products are provided by Celtic Bank, Member FDIC and serviced by Stripe, Inc. and its affiliate Stripe Servicing, Inc.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Building blocks for financial services](#building-blocks-for-financial-services)[Treasury use cases](#treasury-use-cases)[Treasury account architecture](#treasury-account-architecture)[Sample integration](#sample-integration)Products Used[Treasury](/treasury)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
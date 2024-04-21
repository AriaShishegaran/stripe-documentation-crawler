# Overview of Stripe Treasury

Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe’s API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.

[Stripe Treasury](https://stripe.com/treasury)

[Stripe Issuing](/issuing)

Fill out the Treasury form to get access to test mode.

[Treasury form](https://go.stripe.global/treasury-inquiry)

Businesses serving US-based commercial businesses are immediately granted access to test mode after completing the form. All other businesses will gain access after a member of the Stripe team reviews your information and confirms supportability. See our Treasury requirements guide for more information on which businesses can use Treasury.

[Treasury requirements](/treasury/requirements)

## Building blocks for financial services

Stripe Treasury provides the modular components you need to build a full-featured, scalable financial product for your customers.

Onboard users, verify their identity, and provision Treasury financial accounts with one of our bank partners in minutes.

- ID verification

- KYC checks

[KYC](https://en.wikipedia.org/wiki/Know_your_customer)

- Sanctions screening

We’ve partnered with trusted banks, including Evolve Bank & Trust and Goldman Sachs, to provide the banking-as-a-service infrastructure for you to build new financial service offerings.

## Treasury use cases

Here are some use cases commonly addressed with Stripe Treasury:

- Spend management — Build a spend management product for your customers to store funds on your platform and manage spending with branded cards.

- Store and spend account — Create FDIC insurance-eligible accounts that allow businesses to store funds, earn yield, deposit checks, and pay contractors and vendors with ACH and wire transfers.

- Programmatic money movement — Facilitate fast and efficient money movement for your platform’s businesses to other businesses on your platform or to third-party accounts.

## Treasury account architecture

With Stripe Connect, you onboard customers to your platform with connected accounts. For each of these connected accounts, you create a financial account that offers a range of benefits to your platform’s users. The following diagram illustrates an overview of a platform with Stripe Treasury integration.

[Connect](/connect)

Treasury account architecture

Connected accounts are sellers or service providers that use a platform. For example, as a digital storefront platform owner, you provide an e-commerce framework that businesses can leverage to easily establish their online stores. Each digital store owner that uses the storefront platform to collect payments is a connected account.

There are three types of connected accounts on Stripe: Standard, Custom, and Express. The current version of Treasury supports only Custom connected accounts. To learn how to create Custom accounts, see Create a Custom account. To learn more about the types of connected accounts, see Choose your account type.

[Create a Custom account](/connect/custom-accounts#create)

[Choose your account type](/connect/accounts)

Using Treasury endpoints of the Stripe API, you can create financial accounts and attach them to connected accounts in a one to one relationship (unless you are enrolled in the Multi  FA beta). Treasury financial accounts have routing numbers because they’re backed by US banking partners, and balances are eligible for FDIC pass-through insurance. You can fund the financial accounts of your platform’s connected accounts, as well as move money between them. The sellers and service providers (connected accounts) on your platform can also fund their Treasury financial accounts using a bank external to Stripe. If your platform uses Stripe Issuing, you can provide payment cards linked to the financial account balance of your connected accounts.

[Stripe API](/api)

[Multi  FA beta](/treasury/account-management/financial-accounts#create-a-financialaccount)

## Sample integration

Follow our two-part sample integration to see how Treasury works.

[Using Treasury to set up financial accounts and cardsSetting up a financial account with Treasury and issuing cards.](/treasury/examples/financial-accounts)

Setting up a financial account with Treasury and issuing cards.

[Using Treasury to move moneyUsing SetupIntent, PaymentMethods, and verifying bank accounts with Stripe Treasury.](/treasury/examples/moving-money)

Using SetupIntent, PaymentMethods, and verifying bank accounts with Stripe Treasury.

Stripe Treasury is provided in the US by Stripe Payments Company, licensed money transmitter, with funds held at Stripe’s bank partners, Members FDIC. Card and other credit products are provided by Celtic Bank, Member FDIC and serviced by Stripe, Inc. and its affiliate Stripe Servicing, Inc.

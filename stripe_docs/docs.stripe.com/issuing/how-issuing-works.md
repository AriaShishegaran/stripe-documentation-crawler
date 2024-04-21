# How Issuing works

Stripe Issuing is part of Stripe’s banking-as-a-service APIs that allows you to create, manage, and scale a commercial card program for your users without setup fees. You can get started quickly and programmatically control every detail of your program, from card design to approving transactions in real time. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to open loop wallets to offer their users additional money movement functionalities.

[Stripe Issuing](https://stripe.com/issuing)

[Stripe Treasury](/treasury)

Contact sales to start the process and determine your eligibility to use Issuing. If you’re interested in using Treasury with your Issuing integration, fill out the Treasury form instead.

[Contact sales](https://stripe.com/contact/sales)

[Treasury form](https://go.stripe.global/treasury-inquiry)

Issuing is currently available in the US, UK, and many European Economic Area (EEA) countries. Cards can be provided to individuals who reside in the same country where business is established. If your business is established in Europe, you can provide cards to individuals residing in EEA countries (this doesn’t include the UK). Read more about global issuing and see a full list of supported countries.

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[global issuing](/issuing/global)

A common use case for Issuing is spend management, which enables customers to store funds on your platform and manage spending with branded cards.

## Building blocks for financial offerings

Stripe Issuing provides the tools and components needed to build a full-featured financial offering for your customers.

- Identity verificationReduce riskPerform KYC checksRun sanctions screening

[Identity verification](/connect/identity-verification)

- Reduce risk

- Perform KYC checks

- Run sanctions screening

We’ve partnered with multiple trusted banks to provide the banking-as-a-service infrastructure for you to build new financial service offerings.

We also partner with both Mastercard and Visa card networks so you can choose the network on which you want to issue cards. You can also issue cards on both networks.

## Issuing architecture

With Stripe Connect, you onboard customers to your platform with connected accounts. For each of these connected accounts, you can create accountholders and provide cards to authorized users. The following diagram demonstrates a platform with a Stripe Issuing integration using an Issuing balance and a Treasury balance:

[Connect](/connect)

Connected accounts are businesses, sellers, or service providers that use a platform. For example, as an expense management platform, you provide software that small businesses can use to manage and control their business spend. Each digital store owner that uses the storefront platform to collect payments is a connected account.

There are three types of connected accounts on Stripe: Standard, Custom, and Express. The current version of Issuing only supports Custom connected accounts. Learn how to create Custom accounts and about the types of connected accounts.

[create Custom accounts](/connect/custom-accounts#create)

[types of connected accounts](/connect/accounts)

An Issuing balance is a funding source attached to a Custom connected account that provides the funds for spending with the associated card account. Funds can be added to the connected account’s Issuing balance either by transferring from the connected account’s Stripe account balance, or through a top up from an external bank account. Funds can also be paid out from the Issuing balance to an external bank account.

Connected accounts can also use a Stripe Treasury account to fund cards for a full banking-as-a-service solution.

## See also

- Learn how to set up Issuing as a Connect platform

[Learn how to set up Issuing as a Connect platform](/issuing/connect)

- Review compliance requirements pertaining to Issuing

[Review compliance requirements pertaining to Issuing](/issuing/compliance-us)

- Review best practices and tools for testing an Issuing integration

[Review best practices and tools for testing an Issuing integration](/issuing/testing)

- Learn about setting card rules to control spending

[Learn about setting card rules to control spending](/issuing/controls/spending-controls)

- Learn about fraud controls and tools offered through Stripe Issuing

[Learn about fraud controls and tools offered through Stripe Issuing](/issuing/manage-fraud)

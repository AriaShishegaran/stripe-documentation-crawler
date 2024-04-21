# Choose your account type

When using Connect, you must create an account (known as a connected account) for each user that receives money on your platform. You create these accounts when a user signs up for your platform. The type of account you choose for your user determines the Stripe integration you need to build (from Stripe-hosted to completely custom) and the operational responsibilities (such as chargebacks, user support, etc). Connect supports the following account types that are each designed for different use cases:

[Connect](/connect)

- Standard

[Standard](/connect/standard-accounts)

- Express

[Express](/connect/express-accounts)

- Custom

[Custom](/connect/custom-accounts)

## Account types

You must consider several factors when choosing an account type. Integration effort and user experience are especially important because they can affect engineering resource expenditure and conversion rates. You can’t change a connected account’s type after creation.

Extensions building on Connect must use OAuth to connect to Standard accounts.

[Extensions](/building-extensions)

Stripe recommends you use Express or Standard accounts to minimize integration effort. If you want more control over the user experience, Express or Custom accounts might meet your needs better. To know the account type recommended for your business, refer to your platform profile.

[platform profile](https://dashboard.stripe.com/connect/settings/profile)

There’s an additional cost for using Express or Custom accounts.

[Platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

User refers to the person with the connected account (that is, the person being paid for providing goods or services through your platform). With Standard accounts, the user is responsible for fraud and disputes when using direct charges, but this may vary operationally for destination charges.

[direct charges](/connect/charges#types)

[destination charges](/connect/charges#types)

## Express accounts

With Express accounts, Stripe handles the onboarding and identity verification processes. The platform has the ability to specify charge types and set the connected account’s payout settings programmatically. The platform is responsible for handling disputes and refunds, which is similar to a Custom account.

[charge types](/connect/charges)

[payout settings](/connect/payouts-connected-accounts)

Although your user has interactions with Stripe, they primarily interact with your platform, particularly for the core payment processing functionality. For Express account holders, Stripe provides an Express Dashboard (a lighter version of the Dashboard) that allows them to manage their personal information and see payouts to their bank.

[payouts](/payouts)

Use Express accounts when you:

- Want to get started quickly (letting Stripe handle account onboarding, management, and identity verification)

- Want to use destination charges or separate charges and transfers

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- Want significant control over your user’s experience

Examples of platforms that would use Express accounts include, but are not limited to: a home-rental marketplace like Airbnb, or a ride-hailing service like Lyft.

[home-rental marketplace](/connect/collect-then-transfer-guide)

Global compliance requirements do evolve and change over time. With Express, Stripe proactively collects information when requirements change. For best practices on how to communicate to your users when this happens, visit the guide for Express accounts.

[guide for Express accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-standard-or-express-connected-accounts)

Select one of the available countries when you create an Express account. You can’t change the country of your Express account after you create the account.

Some countries are available only when using cross-border payouts.

[cross-border payouts](/connect/cross-border-payouts)

To know when Express accounts are available in your country, contact Stripe.

[contact Stripe](mailto:connect@stripe.com)

## Standard accounts

A Standard Stripe account is a conventional Stripe account where the account holder (that is, your platform’s user) has a relationship with Stripe, is able to log in to the Dashboard, and can process charges on their own.

[Dashboard](https://dashboard.stripe.com/)

Use Standard accounts when you:

- Want to get started quickly and don’t need a lot of control over your user’s experience

- Want to use direct charges

[direct charges](/connect/direct-charges)

- Have users that are familiar with running online businesses or might already have a Stripe account

- Prefer that Stripe handles direct communication with the user for account issues (for example, to request more information for identity verification purposes)

Examples of platforms that would use Standard accounts include, but are not limited to: a store builder like Shopify, or a software as a service like Invoice2go.

[store builder](/connect/enable-payment-acceptance-guide)

Global compliance requirements do evolve and change over time. With Standard, Stripe proactively collects information when requirements change. For best practices on how to communicate to your users when this happens, visit the guide for Standard accounts.

[guide for Standard accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-standard-or-express-connected-accounts)

You can’t change the country of your Standard account after you create the account.

## Custom accounts

A Custom Stripe account is almost completely invisible to the account holder. You—the platform—are responsible for all interactions with your user, including collecting any information Stripe needs. You have the ability to change all of the account’s settings, including the payout bank or debit card account, programmatically.

[settings](/connect/updating-service-agreements)

[bank or debit card account](/connect/payouts-connected-accounts)

Custom account holders don’t have access to the Dashboard, and Stripe doesn’t contact them directly.

Use Custom accounts when you:

- Want complete control over your user’s experience

- Can build the significant infrastructure required to collect user information, create a user dashboard, and handle support

- Want to handle all communication with your users, rather than having your users contact Stripe directly

Creating and managing Custom accounts requires a larger integration effort than the other account types. To learn more, see Using Connect with Custom accounts.

[Using Connect with Custom accounts](/connect/custom-accounts)

Global compliance requirements do evolve and change over time. For best practices on how to communicate to your users when requirements change, see the guide for Custom accounts.

[guide for Custom accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-custom-connected-accounts)

If you decide to use Custom accounts, Stripe recommends you use Connect Onboarding for Custom accounts to collect onboarding and verification information from your users. This would decrease your integration effort and eliminate the need to update your onboarding form when requirements change over time.

[Connect Onboarding for Custom accounts](/connect/custom/hosted-onboarding)

Select one of the available countries when you create an Custom account. You can’t change the country of your Custom account after you create account.

Some countries are available only when using cross-border payouts.

[cross-border payouts](/connect/cross-border-payouts)

To know when Custom accounts are available in your country, contact Stripe.

[contact Stripe](mailto:connect@stripe.com)

## See also

- Express Accounts

[Express Accounts](/connect/express-accounts)

- Standard Accounts

[Standard Accounts](/connect/standard-accounts)

- Custom Accounts

[Custom Accounts](/connect/custom-accounts)

- Account capabilities

[Account capabilities](/connect/account-capabilities)

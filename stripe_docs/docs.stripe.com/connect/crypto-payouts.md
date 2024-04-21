# Crypto payoutsBeta

Access to Crypto payouts is currently limited to beta users. If you’re interested in trying it out, fill out the interest form and select Paying out third parties in crypto.

[interest form](https://stripe.com/use-cases/crypto#request-invite)

[account types](https://stripe.com/docs/connect/accounts)

Crypto payouts enable your platform to pay out in crypto, starting with USDC. You can use crypto payouts with your existing integration to avoid managing crypto yourself—your platform’s funds can remain in fiat currency, and Stripe handles converting to crypto and then paying it out.

## Supported countries

Crypto payouts enable platforms in the US to pay out to connected accounts in the following countries:

Crypto payouts aren’t currently available in New York or Hawaii.

## Before you begin

- Activated US Platform: Your Platform must be in the US and activated. You can activate it by registering your platform, activating your account, and completing the platform profile.

[registering your platform](https://dashboard.stripe.com/connect/tasklist)

[activating your account](https://dashboard.stripe.com/account/onboarding)

[completing the platform profile](https://dashboard.stripe.com/connect/settings/profile)

- Individual recipients: Recipients paid in crypto must be individuals or sole proprietors. Paying companies and non-profits in crypto isn’t currently supported.

- Express Dashboard access: To pay an individual in crypto, create a connected account for them with access to the Express Dashboard. They can link a crypto wallet and choose their preferred currency in this Dashboard.

[Express Dashboard](/connect/express-dashboard)

- Pay with the Transfers API: You must use the Transfers API within your integration to pay in crypto. Transfers to connected accounts with linked crypto wallets are converted from fiat to USDC, enabling you to pay in USDC while your platform balance stays in fiat. If you haven’t built an integration yet, you can pay in crypto using a no-code or programmatic integration.

[Transfers API](/api/transfers)

[no-code](/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=dashboard)

[programmatic integration](/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=api)

## Paying out in crypto with Connect

Sellers, freelancers, content creators, and service providers around the world are increasingly looking to be paid directly in crypto. Being paid in crypto helps them access international platforms that otherwise could not support them, or because they regularly use crypto and often convert funds from fiat. With crypto payouts, you can now support these users without writing a single line of code.

When you opt in to crypto payouts and provide your users access to the Express Dashboard, your users can link a crypto wallet with their account and set their default currency to USDC. Your users can link a crypto wallet using the Express Dashboard.

When a user links a crypto wallet, they immediately see a new USDC balance on their connected account. The USDC balance works like any other local currency balance. You can Transfer funds into the balance and the funds are paid out to their linked crypto wallet instead of their bank account. When you create Transfers in USD, they automatically convert to the preferred currency of your recipients. This simplifies your integration and enables you to have a unified integration across fiat and crypto payouts.

[Transfers](/api/transfers)

Connected account users can view account information, such as their crypto account balance and upcoming payouts, using the Express Dashboard. Stripe handles all compliance requirements, and generates tax forms for recipients paid in crypto.

After Stripe approves your use case, your users can link a crypto wallet to their account and set USDC as their preferred currency. For any user with a default currency set to USDC, Stripe automatically converts Transfers to USDC.

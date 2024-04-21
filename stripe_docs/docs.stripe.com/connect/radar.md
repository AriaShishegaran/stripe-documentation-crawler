# Use Radar with Connect

Stripe Radar uses machine learning to identify fraudulent payments in real time. When you use Radar with connected accounts, it checks only external charges. It doesn’t check fund transfers between Stripe accounts.

[Stripe Radar](/radar)

Charges in a Connect integration fall into two categories:

[Charges in a Connect integration](/connect/charges#types)

- Direct charges: Paid directly to a connected account; Stripe applies only the collecting account’s Radar configuration and rules

- Transferred charges (for example, destination charges or separate charges and transfers): Paid to the platform account and transferred to a connected account; Stripe applies only the platform account’s Radar configuration and rules

## Radar fees

Stripe charges Radar fees based on the rate for the account that collected the payment. For payments collected by the platform account and transferred to a connected account, you can pass Radar fees to the connected account by reducing the transferred amount.

## Radar configuration for a connected account

The Dashboard you use to configure Radar for a connected account depends on the connected account type. The following table shows which Dashboard to use for each account type.

## Radar behavior

Radar behavior for connected account payments depends on the charge category and connected account type. The following table describes each scenario.

## Radar for Fraud Teams

If you have Radar for Fraud Teams, you can customize your rules to include destination charge attributes. You can either use the destination attribute in the supported rule attributes, or use custom metadata on the destination account.

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

[customize your rules](/radar/rules#request-3d-secure)

[destination charge](/connect/destination-charges)

[supported rule attributes](/radar/rules/supported-attributes)

[metadata on the destination account](/radar/rules/reference#metadata-attributes)

## See also

- Choose your connected account type

[Choose your connected account type](/connect/accounts)

- Radar documentation

[Radar documentation](/radar)

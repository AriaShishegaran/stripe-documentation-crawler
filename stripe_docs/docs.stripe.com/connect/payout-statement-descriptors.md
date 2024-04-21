# Payout statement descriptors

The statement descriptor used for Connect payouts varies according to the properties of the connected account and the conditions of the payout. There is a precedence order used for manual and automatic payouts.

[manual](#manual-payouts)

[automatic](#automatic-payouts)

Connected accounts can have a customized statement descriptor stored on the Account object at settings.payout.statement_descriptor.

[settings.payout.statement_descriptor](/api/accounts/object#account_object-settings-payouts-statement_descriptor)

## Default statement descriptor

Connect platforms can configure a platform wide default statement descriptor in their Connect settings, which is also used under certain criteria. Even when the precedence order falls to it, the default statement descriptor configured in your platform’s Connect settings only applies to a connected account’s payout under certain criteria.

[Connect settings](https://dashboard.stripe.com/settings/connect/payouts/statement-descriptor)

[Connect settings](https://dashboard.stripe.com/settings/connect/payouts/statement-descriptor)

- The connected account is Custom or Express, or you have platform controls for it.

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

- The connected account doesn’t have access to the Stripe API. Connected accounts only have access to the Stripe API if they can access the Stripe Dashboard.

- The connected account isn’t restricted from using the read_write OAuth scope. Connected accounts can use the read_write OAuth scope if they have access to the Stripe Dashboard and aren’t explicitly restricted from using it with platform controls.

Unless both of these criteria apply, the statement descriptor defaults to STRIPE. However, this default might be subject to other external factors, such as which bank processed the payout.

## Precedence order

The precedence order for the statement descriptor is different for manual and automatic payouts.

- The statement_descriptor set on the Payout object.

[statement_descriptor](/api/payouts/object#payout_object-statement_descriptor)

- The settings.payout.statement_descriptor from the connected account, if your platform and the connected account were created on or after October 9th, 2023.

[settings.payout.statement_descriptor](/api/accounts/object#account_object-settings-payouts-statement_descriptor)

- Your platform’s default statement descriptor, if it’s applicable to the connected account.

- If no other conditions are met, the statement descriptor might default to STRIPE.

- The settings.payout.statement_descriptor from the connected account, if your platform and the connected account were created on or after October 9th, 2023.

[settings.payout.statement_descriptor](/api/accounts/object#account_object-settings-payouts-statement_descriptor)

- Your platform’s default statement descriptor, if it’s applicable to the connected account.

- If no other conditions are met, the statement descriptor might default to STRIPE.
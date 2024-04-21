# Alternative Currency Payouts for Connect marketplaces and platforms

Are you a direct Stripe Dashboard user looking to pay yourself out in non-primary currencies? See Alternative Currency Payouts for Direct users.

[Alternative Currency Payouts for Direct users](/payouts/alternative-currencies)

Alternative Currency Payouts allow your connected accounts to maintain balances and make payouts domestically in currencies other than their primary currency, or make payouts non-domestically in the account’s local currency. Connected accounts can hold and payout funds in up to 18 supported currencies needed to pay suppliers, process refunds, and so on, without having to re-convert funds.

## Enable Alternative Currency Payouts

[account types](https://stripe.com/docs/connect/accounts)

Enable Alternative Currency Payouts in the Connect payouts settings of the Dashboard. Your account must be in a supported region to access these settings.

[Connect payouts settings](https://dashboard.stripe.com/settings/connect/payouts)

After you enable Alternative Currency Payouts, your users can access all alternative currencies that are supported in their region. For a full list of supported currencies, see supported alternative currencies.

[supported alternative currencies](/payouts/alternative-currencies#alternative-currency-payouts-fees)

Connected accounts must be in the same region as your platform to use Alternative Currency Payouts. For example, both you and your connected account could be in Australia, or if you’re in Europe, your connected account could be in any European country.

You can prevent new connected accounts from using Alternative Currency Payouts by disabling it with the same settings in the Dashboard. However, this doesn’t disable it for connected accounts that are already using it. To disable Alternative Currency Payouts for connected accounts that are already using it, use the Delete external bank accounts API to remove the connected account’s external accounts that are in an alternative currency or offshore.

[Delete external bank accounts API](/api/external_account_bank_accounts/delete)

## Add external accounts

After you enable Alternative Currency Payouts, your connected accounts can start using it by adding an alternative currency external account.

If your connected account has access to the Express Dashboard, you can send them a Login Link to update their payout methods to add an alternative currency external account.

[Login Link](/api/account/create_login_link)

After your connected account has an external account in an alternative currency, charges presented in that currency accrue towards the alternative currency’s balance. Your connected accounts can pay out their alternative currency balances in the same way as a primary currency balance. However, each supported currency is subject to a payout minimum and fee, as described in the following section.

To learn more about processing charges in multiple currencies with Connect, see Working with multiple currencies.

[Working with multiple currencies](/connect/currencies)

## Pricing

Stripe charges platforms a 1% fee for all Alternative Currency Payouts made by their users. Each currency has a minimum fee. For a full list of fees, see the supported alternative currencies table.

[supported alternative currencies table](/payouts/alternative-currencies#alternative-currency-payouts-fees)

Stripe deducts your connected accounts’ Alternative Currency Payouts fees from your platform balance in the alternative currency. For example, if your connected account makes an alternative currency payout in USD, we charge the fee to your platform balance in USD when possible. If your platform account doesn’t support the payout currency, Stripe converts the fee to your default currency and deducts it from your primary balance. See conversion on Stripe fees for more details.

[conversion on Stripe fees](/currencies/conversions#conversion-stripe-fees)

## Request early access

Use the following form to request updates on beta features as we expand Alternative Currency Payouts features and regional support.

[privacy policy](https://stripe.com/privacy)

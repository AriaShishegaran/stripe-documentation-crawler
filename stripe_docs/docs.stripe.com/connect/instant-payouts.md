# Instant Payouts for Connect marketplaces and platforms

Are you a Stripe Dashboard user looking to request Instant Payouts for your account? See Instant Payouts for Stripe Dashboard users.

[Instant Payouts for Stripe Dashboard users](/payouts/instant-payouts)

With Instant Payouts, Connect platforms and marketplaces can allow their users to access their balances immediately following a successful charge. Instant Payouts are available at any day or time, including weekends and holidays, and funds typically settle in the associated bank account within 30 minutes.

You can use Instant Payouts to:

- Attract and retain new users

- Realize additional revenue by assessing a fee

[assessing a fee](#monetization-and-fees)

Funds acquired from card payments are available for Instant Payouts as soon as the charge is complete. ACH or bank debits are only available for Instant Payouts after the payment has settled.

## Eligible connected accounts

Instant Payouts are only available to connected accounts in the same country as the platform and must be in the local currency. For example, an Instant Payout to a Canadian business must be through a Canadian platform and must be in CAD.

To receive Instant Payouts, a user must have an eligible External Account. Eligible accounts vary by country.

[check supported banks](/payouts/instant-payouts-banks)

[check supported banks](/payouts/instant-payouts-banks)

[check supported banks](/payouts/instant-payouts-banks)

You can verify Instant Payout eligibility for your user by calling the External Accounts API with the Connected Account ID. The response returns the account’s 10 most recently active External Accounts, and those with instant in the available_payout_methods parameter are eligible for Instant Payouts. You can paginate through the results if you need to review more than the default display of 10.

[External Accounts API](/api/external_account_bank_accounts/list)

If your user doesn’t have an External Account eligible for Instant Payouts, you can prompt them to add an eligible account through the Account API.

[Account API](/api/accounts/update#update_account-external_account)

## Monetization and fees

[account types](https://stripe.com/docs/connect/accounts)

Some marketplaces and platforms choose to monetize Instant Payouts, offering the convenience for a fee. If you monetize Instant Payouts, Stripe supports two methods of fee collection: Application Fees and account debits

With Application Fees, Stripe collects the fee you determine and initiates the Instant Payout synchronously. Stripe recommends applying an application fee because it’s a single, seamless transaction:

[Application Fees](/api/application_fees)

- Users can’t pay out more than their available balance

- Fees can be refunded through the API or the Dashboard

- Monetization options include fixed or variable fees with minimums and maximums

- Fees are paired to your Instant Payouts revenue with the Payout Object, helping with reporting and reconciliation. You can view your collected fees in the Payments tab on the Dashboard

[Payout Object](/api/payouts/object)

[Payments tab](https://dashboard.stripe.com/connect/application_fees)

To use Application Fees, set your pricing structure using the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/connect/payouts/instant-payouts)

Application Fees for Instant Payouts rely on the Balance API net-of-fees  field. Turning this on without using the new field could break your API integration.

[Balance API net-of-fees](/api/balance/balance_object#balance_object-instant_available-net_available)

You can directly debit your connected account’s Stripe balance and credit your platform account’s Stripe balance to collect fees. After the Instant Payout, call the Charge API, specifying the connected account ID as the source parameter. Consider the following limitations when using account debits to collect Instant Payout fees:

[directly debit](/connect/account-debits)

[Charge API](/api#create_charge)

- You must get legally binding consent from your connected accounts.

- Account debits carry an additional cost.

[additional cost](https://stripe.com/connect/pricing)

- Debiting an account can’t make the connected account balance become negative unless you have reserves enabled (on by default for all new platforms created after January 31, 2017) and have a bank account in the same currency as the debit.

[reserves enabled](/connect/account-balances#understanding-connected-reserve-balances)

- If the connected account has already paid out their available balance in full, you might be delayed in collecting the fee.

- Reconciliation requires maintaining an internal database of debits and related payouts.

## Initiate an Instant Payout

You can initiate Instant Payouts either manually on your users’ behalf or you can use the Stripe APIs to compose user interfaces to allow your users to initiate an Instant Payout. In circumstances where you initiate Instant Payouts on your users’ behalf, you may only do so in accordance with instructions and authorizations given by your users.

- Call retrieve balance, expanding instant_available-net_available.

[retrieve balance](/api/balance/balance_retrieve)

[instant_available-net_available](/api/balance/balance_object#balance_object-instant_available-net_available)

The property instant_available.net_available is the connected account’s instant balance net of platform fees for each instantly available destination. You must use this field if you’re monetizing with Application Fees. This amount is calculated from the platform’s Application Fee pricing structure set in the Dashboard.

[Application Fees](#application-fees)

The property instant_available.amount is the connected account’s gross balance, not including any platform fees.

The following example shows a platform setting 2% pricing for any USD Instant Payout:

Funds from card charges are available immediately, but funds from bank debits (such as ACH) aren’t available immediately.

Key considerations:

- net_available only appears when included as an expanded parameter.

[expanded parameter](/expand)

- net_available only appears for connected accounts. You’ll receive an error expanding this for your platform.

- A hash in net_available only appears for instantly-available external accounts. External accounts that aren’t valid instant payouts destinations won’t appear.

- External accounts can have different net_available balances based on external account properties and platform-set pricing rules.

- Call create payout with method=instant. Use the amount field corresponding with your monetization strategy, either instant_available.amount or instant_available.net_available[0].amount. Use the destination from the balance endpoint to pay out to an intended external account.

[create payout](/api/payouts/create)

Instant payouts to ineligible external accounts will fail, so confirm eligibility before surfacing the capability to your connected accounts.

[confirm eligibility](#external-account-eligibility)

- View your application fee that was created by the payout.

[application fee](/api/application_fee/retrieve)

## Eligibility and daily volume limits

Your account has a maximum amount it can pay out instantly per day across all connected accounts. Your users can’t initiate Instant Payouts after you reach your daily limit. Daily limits reset at midnight US Central Time (CT).

## Pricing

Irrespective of your monetization decisions, Stripe charges marketplaces and platforms a 1% fee for all Instant Payouts. Each Instant Payout transaction has a minimum and maximum amount dependent on the currency. These fees are assessed as part of your overall Connect fees.

## Manage risk and eligibility

When platforms and marketplaces are liable for losses, you’re liable for uncovered negative balances due to refunds or disputes.

Stripe recommends setting risk parameters to protect your platform from unintended losses. We provide a number of best practices for managing fraud and risk, such as setting trust thresholds like the following:

[best practices for managing fraud and risk](/connect/risk-management/best-practices#fraud)

- Minimum processing volume

- Days active

- Chargeback rate

Stripe has tools to help manage eligibility– if you’re interested, contact us.

[contact us](https://support.stripe.com/?contact=true)

## Marketing

Your marketing of Instant Payouts to Connected Accounts must clearly and conspicuously disclose any fees you intend to apply for Instant Payouts.

Make sure your marketing is consistent with Stripe’s marketing of the product, which states that: “You can request Instant Payouts 24/7, including weekends and holidays, and funds typically appear in the associated bank account within 30 minutes”. Some Instant Payouts might not settle within 30 minutes, and instead might take longer to be credited to the relevant bank account.

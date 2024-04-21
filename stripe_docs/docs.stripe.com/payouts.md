# Receive payouts

For more information, see our Payouts FAQ and pricing guide.

[Payouts FAQ](https://support.stripe.com/questions/payouts-faq)

[pricing guide](https://www.stripe.com/pricing)

You receive funds when Stripe (or your platform) makes payouts to your bank account. Payout availability varies depending on your industry and country of operation. When you start processing live payments, Stripe typically schedules your initial payout for 7-14 days after you successfully receive your first payment. Your first payout might take longer, depending on your industry risk level and country of operation. Subsequent payouts follow your account’s payout schedule.

[payout schedule](#payout-schedule)

You can see a comprehensive list of your payouts and the expected dates of deposit into your bank account in the Dashboard. If you’re a Connect platform, see Connect payouts.

[Dashboard](https://dashboard.stripe.com/test/payouts)

[Connect](/connect)

[Connect payouts](/connect/payouts-connected-accounts)

## Add or update your bank account

You can update your account details or add a new bank account using the Payout settings in the Dashboard. Based on your bank’s location, Stripe might require different kinds of account details to activate your bank account. To modify your banking information, click the Edit button next to the desired bank account.

[Payout settings](https://dashboard.stripe.com/account/payouts)

Use the following table to see the required bank details for specific countries:

You have the flexibility to link various types of bank accounts for your Stripe payouts. Supported options include traditional accounts offered by established financial institutions, including checking and savings accounts. Additionally, Stripe lets you use virtual bank accounts such as N26, Revolut, Wise, and others. If you’re eligible, you can also use a debit card for instant payouts.

[instant payouts](#instant-payouts)

While Stripe supports non-standard bank accounts, you might see higher payout failures for these accounts.

In most cases, bank accounts must be located in the country where the settlement currency is the official currency. For example, SEK bank accounts must be based in Sweden. Stripe also enables you to settle and pay out to banks in select alternative currencies, or pay out to non-domestic bank accounts in the local currency, for a fee. To learn more about presenting and settling in alternative currencies, see Alternative currencies.

[Alternative currencies](/payouts/alternative-currencies)

At times, Stripe supports international currencies that don’t incur a fee. See the following table for the list of supported free currencies per country:

Acquiring fees, where applicable, are based on the settlement currency, and you can find these acquiring fees listed out by currency on your country’s pricing page.

In some countries, Stripe users can add extra bank accounts to enable settlements and payouts in additional currencies. You can add one bank account per supported settlement currency. If you use multiple bank accounts, you must select a default settlement currency, which you can change at any time.

Charges that are presented in any enabled settlement currency settle without currency conversion. However, payments presented in a currency that you haven’t configured an additional bank account for automatically convert to your default currency.

[presented](/currencies#presentment-currencies)

[currency conversion](/currencies/conversions)

For example, consider a Stripe user in the United Kingdom who has added both GBP and USD bank accounts, with GBP selected as the default settlement currency. USD payments (where USD is the presentment currency) are automatically paid out to the USD bank account without conversion, whereas payments in all other currencies are converted into GBP.

You can manage your bank accounts and default settlement currency by visiting Bank accounts and scheduling in the Dashboard.

[Bank accounts and scheduling](https://dashboard.stripe.com/account/payouts)

## Payout schedule

All payments and payouts are processed according to UTC time except for Asia-Pacific (APAC) markets. As a result, the processed date might not be the same as your local time zone.

[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)

[except for Asia-Pacific (APAC) markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts)

Your payout schedule refers to how often Stripe sends money to your bank account.

In supported countries, your default payout schedule is daily automatic. You can change this in the Dashboard to weekly automatic, monthly automatic, or manual payouts. When selecting a weekly or monthly schedule, you can specify the day of the week or month that you want payouts to arrive in your bank account.

[Dashboard](https://dashboard.stripe.com/account/payouts)

When you select a payout schedule, it doesn’t change how long it takes your pending balance to become available. However, it allows you to control when your payouts occur. For example, if your account operates on a daily payout schedule with a 3 business day payout speed, Stripe pays out funds daily from transactions captured 3 business days earlier.

[payout speed](#payout-speed)

Certain countries have restrictions on payout schedules:

- In Brazil and India, payouts are always automatic and daily.

- In Japan, daily payouts aren’t available. Default payout schedule is set to weekly (Friday).

If you’re using Cross-border payouts, these payout schedule restrictions don’t apply.

[Cross-border payouts](/connect/cross-border-payouts)

If you turn off automatic payouts in the Dashboard, you must manually send funds to your bank account. You can do this either in the Dashboard or by creating payouts using the API. Manual payouts are available in all regions except Brazil and India, where payouts are always automatic and daily.

[Dashboard](https://dashboard.stripe.com/settings/payouts)

[creating payouts](/api#create_payout)

## Payout speed

While payout schedule refers to the cadence your funds are paid out on (for example, day of the week), payout speed refers to the amount of time it takes for your funds to become available. The payout speed varies per country and is typically expressed as T+X days. Some payment processors might start “T” from their internal settlement time, meaning when the funds land in their bank accounts.

In Stripe, “T” refers to the transaction time, which indicates the time of the original payment confirmation or capture, and the counting starts earlier. If your Stripe account is in a country with a T+3 standard payout speed and you use a manual payout schedule, your Stripe balance is available for payout within three business days of capturing a payment. However, if you use a daily automatic payout schedule with a T+3 speed, Stripe pays out funds daily from transactions captured 3 business days earlier.

Most banks deposit payouts into your bank account as soon as they receive them, though some might take a few extra days to make them available. The type of business and the country you’re in can also affect payout timing.

Stripe offers accelerated payout speeds for users and connected accounts where Stripe manages credit and fraud risk in Europe, the UK, Mexico, and Canada. With accelerated payout speeds, funds are available within 3 business days.

Users become eligible for accelerated payout speeds after meeting certain criteria based on risk and history with Stripe. When you’re eligible, you can choose to opt in or out of accelerated payout speeds in the Dashboard by updating your Payout settings. You remain at the starting 7 calendar day payout speed until you meet the eligibility criteria. You can configure accounts where you manage fraud and dispute liability separately. Some high risk industries might not be eligible.

[Payout settings](https://dashboard.stripe.com/settings/payouts)

[configure accounts](/connect/manage-payout-schedule)

As the platform, you can set delay_days on your connected accounts. The delay applies as a business day or calendar day delay based on the country of the connected account. The following table shows which countries apply the delay by business or calendar day.

[delay_days](/connect/manage-payout-schedule#delay_days)

1 Delays for Pix, Boleto, debit, and prepaid payouts in Brazil apply in business days.

2 Delays for PayNow in Singapore apply in business days.

Use the following table to determine your country’s payout speed. High-risk businesses have a payout speed of 14 calendar days.

## Minimum payout amounts

The minimum payout amount depends on the lowest amount we can support with our banking partners. For example, if you’re located in the US and you have less than 1 cent (0.01 of 1 dollar) USD in your Stripe account, you must wait until you accept more payments and increase your balance before you can receive a payout. If your available account balance is less than the minimum payout amount, it remains in your Stripe account until your balance increases.

If you’re in a supported country, you can use alternative currency payouts to send a payout to your local bank accounts in a foreign currency. For example, a French user can now receive a USD payout in their French bank account instead of having to pay for multiple currency exchanges.

[alternative currency payouts](/payouts/alternative-currencies)

Minimum payout amounts are typically one base unit of the local currency. See the following collapsed table for a list of countries and their minimum payout amounts:

Cross-border minimum payout amounts are typically one base unit of the local currency in the recipient country’s currency. See the following collapsed table for a list of countries and their cross-border minimum payout amounts:

## Negative payouts

Each payout reflects your available account balance at the time it was created. In some cases, you might have a negative account balance. For example, if you receive 100 USD in payments but refund 200 USD of prior payments, your account balance would be -100 USD. If you don’t receive further payments to balance out the negative amount, Stripe creates a payout that debits your bank account.

Your bank account must support both credit and debit transactions so that Stripe can perform any required payouts.

## Payout failures

If your bank account can’t receive a payout for any reason, your bank sends the funds back to us. This returns an error with the reason for the failure. It can take up to 5 additional business days for your bank to return the payout and inform us that it failed. If this happens, you’re notified by email and in the Dashboard. To make sure that your bank account details are correct, you need to re-enter them if a payout fails. After you re-enter your bank account details, Stripe attempts to perform the payout again at the next scheduled payout interval.

[reason for the failure](/api/payouts/failures)

[Dashboard](https://dashboard.stripe.com/test/payouts)

When a payout fails, it’s possible that its state initially shows as paid but then changes to failed (within 5 business days).

Make sure that the bank account information you provide is correct because Stripe sends the funds using the account information you enter. Therefore, if you provide incorrect information (for example, a mistyped account number or an incorrect routing number), Stripe might send payouts to the wrong bank account and might not be able to recover the funds.

Any fees or losses that you incur due to incorrect information fall under your responsibility. If your banking details are correct and the payout failure is for other reasons, contact your bank. After you resolve any issues with your bank, you can reactivate the payouts by clicking Resume Payouts. If you don’t receive a payout from Stripe after clicking Resume Payouts, and haven’t received a failure notification within a reasonable time frame, please contact us.

[contact us](https://support.stripe.com/contact)

## Instant Payouts

With Instant Payouts, you can instantly send funds to a supported debit card or bank account. You can request Instant Payouts any time, including weekends and holidays, and funds usually appear in the associated bank account within 30 minutes. New Stripe users aren’t immediately eligible for Instant Payouts. You can check your eligibility in the Dashboard.

[Instant Payouts](/payouts/instant-payouts)

[eligibility](/payouts/instant-payouts#eligibility-and-daily-volume-limits)

[Dashboard](https://dashboard.stripe.com/payouts/instant_payouts_eligibility)

## Payout fees

Stripe’s fee structure includes payouts, which means Stripe won’t charge you anything additional to initiate payouts. One exception is if you want to settle your payments and receive a payout to a domestic bank in an alternative currency. However, Stripe supports some international currencies without an additional fee. This support depends on your bank account’s location and the currency that you want your payout denominated in. To learn more about various payout currencies and their associated fees, see Alternative currencies.

[Alternative currencies](/payouts/alternative-currencies)

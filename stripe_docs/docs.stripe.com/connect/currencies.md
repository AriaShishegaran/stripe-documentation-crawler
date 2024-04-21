# Working with multiple currencies

Stripe supports processing charges in 135+ currencies. This allows you to present prices in a customer’s native currency and avoid conversion costs for customers.

[135+ currencies](/currencies)

The currencies you can use are determined by the country of the Stripe account where the charge is made.

[Direct charges](/connect/direct-charges)

[Destination charges](/connect/destination-charges)

[Destination charges](/connect/destination-charges)

[Separate charges and transfers](/connect/separate-charges-and-transfers)

[Separate charges and transfers](/connect/separate-charges-and-transfers)

## Currency conversions

Another way to avoid currency conversions when performing separate charges and transfers is to use the on_behalf_of parameter.

[on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

A currency conversion occurs if the presentment currency differs from the settlement currency.

The presentment currency is the currency that’s used for charges. The settlement currency is the currency that you can receive payouts in, depending on the charge type and applicable currency conversion. See the supported presentment currencies and the supported settlement currencies.

[payouts](/payouts)

[supported presentment currencies](/currencies)

[supported settlement currencies](/connect/payouts-connected-accounts#supported-settlement)

Depending on bank account or debit card availability, the following occurs when paying out a balance:

[balance](/connect/account-balances)

If you regularly charge in multiple currencies, you might be able to establish multiple bank accounts to have multiple settlement currencies.

[multiple bank accounts](/payouts#multiple-bank-accounts)

Currency conversions use the current exchange rates provided by our service providers, with an additional conversion fee applied by Stripe. There are online resources for conversion calculation that can help you estimate current market rates. However, these numbers can fluctuate and might not reflect Stripe’s rates at the time a payment is processed.

[Currency conversions](/currencies/conversions)

[conversion calculation](https://dashboard.stripe.com/currency_conversion)

## Application fees for direct charges

Although direct charges are in the connected account’s default currency, your platform receives the application fees for direct charges in your platform’s default currency.

[application fees](/api#application_fees)

[direct charges](/connect/direct-charges)

If your platform doesn’t use application fees and retains a portion of the charges instead, those funds are paid out (and converted or not) the same way as other charges on the platform account.

## Application fees for destination charges and converting balances

Application fees collected using the application_fee_amount parameter aren’t converted again for destination charges; platforms always receive application fees in the connected account’s settlement currency. Use the transfer_data[amount] parameter to transfer less of the transaction amount and collect fees in the platform’s default settlement currency.

[destination charges](/connect/destination-charges)

If you create charges on the platform using the destination or on_behalf_of parameters, you might accumulate balances in multiple currencies. If you don’t have bank accounts for these other currencies, Stripe provides a way to pay out balances in non-default currencies to your platform’s default bank account.

These currency conversions are created as manual payouts with currency set as the currency of the source balance:

As long as there are sufficient funds in the balance for the specified currency, Stripe automatically converts the funds to the default bank account’s currency.

## Example scenarios

The following examples illustrate how to work with multiple currencies in Connect:

[Connect](/connect)

Direct charges are always converted to the connected account’s default currency from the presentment currency. The application fee is converted to the platform’s default currency.

[Direct charges](/connect/direct-charges)

[presentment currency](/currencies#presentment-currencies)

[application fee](/connect/direct-charges#collect-fees)

For example, you accept a charge for a connected account in USD. The connected account settles in EUR. The funds sent to the connected account are converted to EUR and the application fee is converted back to your platform in USD from EUR.

When processing destination charges without on_behalf_of, Stripe first converts them from the presentment currency to the platform’s default currency. The funds sent to the connected account are then converted to the connected account’s default currency.

[destination charges](/connect/destination-charges)

[presentment currency](/currencies#presentment-currencies)

- If an application_fee_amount is used, the application fee is collected after the conversion to the connected account’s default currency. The fee remains in that currency when added to the platform.

[application fee](/connect/destination-charges?fee-type=application-fee#collect-fees)

- If transfer_data[amount] is used, the fee is collected after the first currency conversion and remains in the platform’s default currency.

This charge flow is subject to Stripe’s regional and cross-border policies.

[cross-border policies](/connect/cross-border-payouts)

For example, you accept a destination charge for a connected account in EUR. The connected account settles in GBP, and your platform settles in USD. The charge is converted from EUR to USD and the funds sent to the connected account are converted to GBP.

- If application_fee_amount is used, the application fee amount is converted from EUR to GBP and taken from the amount that settles on the connected account.

- If transfer_data[amount] is used, the fee is retained in USD after converting from the initial presentment currency.

When processing destination charges with on_behalf_of, Stripe first converts them from the presentment currency to the connected account’s default currency. The application fee remains in the connected account’s currency, regardless of whether application_fee_amount or transfer_data[amount] is used.

[destination charges](/connect/destination-charges)

[presentment currency](/currencies#presentment-currencies)

[application fee](/connect/destination-charges?fee-type=application-fee#collect-fees)

For example, the connected account accepts a charge in USD but settles in EUR. The charge is converted to EUR and sent to the connected account in EUR. The fee is collected in EUR regardless of whether application_fee_amount or transfer_data[amount] is used.

Separate charges are converted to the platform’s default currency from the presentment currency and the platform later transfers the funds to the connected account. The application_fee_amount and transfer_data[amount] parameters are not used to collect fees, since the platform can choose the appropriate amount to send at transfer time.

[Separate charges](/connect/separate-charges-and-transfers)

[presentment currency](/currencies#presentment-currencies)

This charge flow is subject to Stripe’s regional and cross-border policies.

[cross-border policies](/connect/cross-border-payouts)

Separate charges are converted to the connected account’s default currency from the presentment currency and the platform later transfers the funds to the connected account. The application_fee_amount and transfer_data[amount] parameters are not used to collect fees, since the platform can choose the appropriate amount to send at transfer time.

[Separate charges](/connect/separate-charges-and-transfers)

[presentment currency](/currencies#presentment-currencies)

This charge flow is subject to Stripe’s regional and cross-border policies.

[cross-border policies](/connect/cross-border-payouts)

## See also

- Creating charges

[Creating charges](/connect/charges)

- Creating direct charges

[Creating direct charges](/connect/direct-charges)

- Using subscriptions

[Using subscriptions](/connect/subscriptions)

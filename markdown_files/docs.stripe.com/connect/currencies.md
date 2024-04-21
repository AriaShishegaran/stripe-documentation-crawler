htmlWorking with multiple currencies | Stripe Documentation[Skip to content](#main-content)Handle multiple currencies[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcurrencies)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcurrencies)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Working with multiple currencies

Support processing charges in multiple currencies with Connect.Stripe supports processing charges in 135+ currencies. This allows you to present prices in a customer’s native currency and avoid conversion costs for customers.

The currencies you can use are determined by the country of the Stripe account where the charge is made.

Charge typeCurrency determined by[Direct charges](/connect/direct-charges)Country of the connected account[Destination charges](/connect/destination-charges)Country of the platform account[Destination charges](/connect/destination-charges)using`on_behalf_of`Country of the connected account[Separate charges and transfers](/connect/separate-charges-and-transfers)Country of the platform account[Separate charges and transfers](/connect/separate-charges-and-transfers)using`on_behalf_of`at charge timeCountry of the connected account## Currency conversions

### Using on_behalf_of

Another way to avoid currency conversions when performing separate charges and transfers is to use the on_behalf_of parameter.

A currency conversion occurs if the presentment currency differs from the settlement currency.

The presentment currency is the currency that’s used for charges. The settlement currency is the currency that you can receive payouts in, depending on the charge type and applicable currency conversion. See the supported presentment currencies and the supported settlement currencies.

Depending on bank account or debit card availability, the following occurs when paying out a balance:

Bank account or debit card availabilityConversion actionAvailable for the currencyNo conversionMultiple bank accounts or debit cards available for the currencyNo conversion–Stripe uses the bank account or debit card set as`default_for_currency`Not available for the currencyStripe converts the payout balance based on the Stripe account’s default currencyIf you regularly charge in multiple currencies, you might be able to establish multiple bank accounts to have multiple settlement currencies.

Currency conversions use the current exchange rates provided by our service providers, with an additional conversion fee applied by Stripe. There are online resources for conversion calculation that can help you estimate current market rates. However, these numbers can fluctuate and might not reflect Stripe’s rates at the time a payment is processed.

## Application fees for direct charges

Although direct charges are in the connected account’s default currency, your platform receives the application fees for direct charges in your platform’s default currency.

Bank account or debit card availabilityConversion actionAvailable for the settlement currencyNo conversionNot available for the settlement currencyStripe converts the application fee based on the platform account’s default currencyIf your platform doesn’t use application fees and retains a portion of the charges instead, those funds are paid out (and converted or not) the same way as other charges on the platform account.

## Application fees for destination charges and converting balances

Application fees collected using the application_fee_amount parameter aren’t converted again for destination charges; platforms always receive application fees in the connected account’s settlement currency. Use the transfer_data[amount] parameter to transfer less of the transaction amount and collect fees in the platform’s default settlement currency.

If you create charges on the platform using the destination or on_behalf_of parameters, you might accumulate balances in multiple currencies. If you don’t have bank accounts for these other currencies, Stripe provides a way to pay out balances in non-default currencies to your platform’s default bank account.

These currency conversions are created as manual payouts with currency set as the currency of the source balance:

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=xaf`As long as there are sufficient funds in the balance for the specified currency, Stripe automatically converts the funds to the default bank account’s currency.

## Example scenarios

The following examples illustrate how to work with multiple currencies in Connect:

### Direct charges

Direct charges are always converted to the connected account’s default currency from the presentment currency. The application fee is converted to the platform’s default currency.

For example, you accept a charge for a connected account in USD. The connected account settles in EUR. The funds sent to the connected account are converted to EUR and the application fee is converted back to your platform in USD from EUR.

### Destination charges without on_behalf_of

When processing destination charges without on_behalf_of, Stripe first converts them from the presentment currency to the platform’s default currency. The funds sent to the connected account are then converted to the connected account’s default currency.

- If an`application_fee_amount`is used, the[application fee](/connect/destination-charges?fee-type=application-fee#collect-fees)is collected after the conversion to the connected account’s default currency. The fee remains in that currency when added to the platform.
- If`transfer_data[amount]`is used, the fee is collected after the first currency conversion and remains in the platform’s default currency.

NoteThis charge flow is subject to Stripe’s regional and cross-border policies.

For example, you accept a destination charge for a connected account in EUR. The connected account settles in GBP, and your platform settles in USD. The charge is converted from EUR to USD and the funds sent to the connected account are converted to GBP.

- If`application_fee_amount`is used, the application fee amount is converted from EUR to GBP and taken from the amount that settles on the connected account.
- If`transfer_data[amount]`is used, the fee is retained in USD after converting from the initial presentment currency.

### Destination charges with on_behalf_of

When processing destination charges with on_behalf_of, Stripe first converts them from the presentment currency to the connected account’s default currency. The application fee remains in the connected account’s currency, regardless of whether application_fee_amount or transfer_data[amount] is used.

For example, the connected account accepts a charge in USD but settles in EUR. The charge is converted to EUR and sent to the connected account in EUR. The fee is collected in EUR regardless of whether application_fee_amount or transfer_data[amount] is used.

### Separate charges and transfers without on_behalf_of

Separate charges are converted to the platform’s default currency from the presentment currency and the platform later transfers the funds to the connected account. The application_fee_amount and transfer_data[amount] parameters are not used to collect fees, since the platform can choose the appropriate amount to send at transfer time.

NoteThis charge flow is subject to Stripe’s regional and cross-border policies.

### Separate charges and transfers with on_behalf_of

Separate charges are converted to the connected account’s default currency from the presentment currency and the platform later transfers the funds to the connected account. The application_fee_amount and transfer_data[amount] parameters are not used to collect fees, since the platform can choose the appropriate amount to send at transfer time.

NoteThis charge flow is subject to Stripe’s regional and cross-border policies.

## See also

- [Creating charges](/connect/charges)
- [Creating direct charges](/connect/direct-charges)
- [Using subscriptions](/connect/subscriptions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Currency conversions](#currency-conversions)[Application fees for direct charges](#application-fees-for-direct-charges)[Application fees for destination charges and converting balances](#application-fees-for-destination-charges-and-converting-balances)[Example scenarios](#example-scenarios)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
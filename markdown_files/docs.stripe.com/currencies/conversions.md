htmlCurrency conversions | Stripe Documentation[Skip to content](#main-content)Currency conversions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcurrencies%2Fconversions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcurrencies%2Fconversions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)
[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[About Stripe payments](/docs/payments/online-payments)[Currencies](/docs/currencies)# Currency conversions

Learn more about how Stripe handles currency conversions for you.### Using Connect

Connect platforms have additional considerations with respect to currency conversions.

Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer’s native currency. Doing so can improve sales and help customers avoid conversion costs. In order to present prices in your customer’s currency, you need to specify the presentment currency when creating a PaymentIntent or a charge.

Payments automatically convert to your default settlement currency. Stripe uses the exchange rate at the time of the charge to protect your earnings from rate fluctuations between the payment and your anticipated payouts.

In certain countries, Stripe might support settlement in additional currencies. If you have liquidity needs in additional currencies, you can enable settlement in those currencies and add a bank account in the payout settings of your dashboard.

NoteCheckout and Payment Links automatically convert this price to an international customer’s local currency based on their location. Learn more about Adaptive Pricing.

## Calculating foreign exchange rates

When Stripe provides currency conversion services for transactions, Stripe generally applies the mid-market rate based on pricing data sourced from third-party service providers. Mid-market rate is the average between the buy and the sell price of a currency. Currency conversion on Stripe is subject to fees as detailed on our pricing page.

In certain circumstances, Stripe might apply the rate at which we source the currency owed to you. For example, this can happen if a new exchange rate is mandated by a government or if there is a large discrepancy in rates between our service providers. Stripe does so to mitigate exchange rate risk to you and to Stripe. Rarely, Stripe may take other actions to mitigate risk. If we do so, we’ll provide additional notice to you.

You can check the current rate for currency conversions on Stripe using our estimation page. You can also see the actual exchange rate applied in a transaction through the API or in your Dashboard. Note that the estimation page shows the baseline exchange rate and excludes the Stripe fees for currency conversion which is incremental to this rate.

## Conversions on disputes and refunds

If a currency-converted payment is disputed or refunded, the amount you received is converted back to the presentment currency at the current exchange rate. Exchange rates fluctuate with the market, so the rate used during the payment often differs from the rate used when a dispute or refund occurs. The amount deducted from your merchant balance depends on the current rate and this amount might be more or less than the original payment. The customer is always refunded the exact amount they paid and in the currency they paid in, regardless of any rate fluctuations.

For example, if your settlement currency is EUR and you process a 60 USD payment at a rate of 0.88 EUR per 1 USD, the converted amount is 52.80 EUR (excluding the Stripe fee). If the rate is 0.86 EUR per 1 USD at the time of refund, the amount deducted from your account balance is only 51.60 EUR.

## Countries with foreign exchange control

Remittance to or from countries with foreign exchange control (including, but not limited to, Brazil) is carried out exclusively through authorized channels, pursuant to the legislation applicable in those countries.

## Additional settlement currencies

In some countries, additional currencies might be enabled for settlement. If you have liquidity needs in additional currencies, you can enable or disable these on the payout settings of your dashboard. If there are multiple bank accounts available for a given currency, Stripe uses the one set as default_for_currency for settlement and payouts.

If you have accumulated a balance in a currency without an associated bank account, a conversion occurs if you create a manual payout in that currency.

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=xaf`As long as there are sufficient funds in the balance for the specified currency, Stripe automatically converts the funds to the default bank account’s currency.

NoteIf you enable a currency as a settlement currency by mistake, you can pay out funds in your default currency using a manual payout, then disable the accidental settlement currency so you don’t continue to accrue funds in that currency.

## Conversions on Stripe fees

If you incur a Stripe fee in a currency for which you don’t have a linked bank account, we automatically convert that fee to your default settlement currency at the time the fee is incurred before charging you. This conversion uses the baseline exchange rate and does not incur any additional fees. For example, if you’re a Stripe Billing user whose default currency is USD, you might incur the 0.5% variable fee when you present in a non-USD currency. If you have a subscriber to whom you present in EUR for their monthly subscription of 100 EUR, we convert that 0.50 EUR Stripe Billing fee to USD at the baseline rate at the time of the charge at no additional conversion cost to you.

## See also

- [Payouts](/payouts)
- [Alternative currency payouts](/payouts/alternative-currencies)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Calculating foreign exchange rates](#foreign-exchange-rates)[Conversions on disputes and refunds](#conversions-disputes-refunds)[Countries with foreign exchange control](#countries-with-foreign-exchange-control)[Additional settlement currencies](#additional-settlement-currencies)[Conversions on Stripe fees](#conversion-stripe-fees)[See also](#see-also)Products Used[Payments](/payments)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
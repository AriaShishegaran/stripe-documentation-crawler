# Automatically convert to local currencies

Adaptive Pricing is available to businesses in the following regions and settlement currencies:

- United States (USD)

- Canada (CAD)

- United Kingdom (GBP)

- European Union (EUR)

Presenting customers with prices in their local currencies and popular local payment methods can help increase conversion and revenue.

Enable Adaptive Pricing for Checkout and Payment Links to let customers see your non-recurring prices in their local currency, along with the price in the original currency, the Stripe-provided exchange rate, and supported local payment methods.

## Enable Adaptive Pricing

Enable Adaptive Pricing in your payment settings. You can enable Adaptive Pricing in test mode and live mode. Disabling Adaptive Pricing doesn’t affect Checkout Sessions that have already been converted.

[payment settings](https://dashboard.stripe.com/settings/adaptive-pricing)

Enabling Adaptive Pricing can affect some parts of your integration, like webhook handling and reporting. Review your integration to make sure it can handle webhooks and PaymentIntent objects with local currencies.

[webhooks](#webhooks-reporting)

- Use the currency_conversion hash on the Checkout Session object to determine what your customer would have paid in the default currency.

[currency_conversion](/api/checkout/sessions/object#checkout_session_object-currency_conversion)

- Use the BalanceTransactions API to determine how much you receive after fees.

[BalanceTransactions API](/api/balance_transactions)

[Supported currencies](#supported-currencies)

## Supported currencies

Automatically convert prices from USD, CAD, GBP, or EUR to the local currencies of customers in the following markets:

- Austria

- Australia

- Belgium

- Brazil

- Bulgaria

- Canada

- China

- Croatia

- Cyprus

- Czech Republic

- Denmark

- Estonia

- Finland

- France

- Germany

- Greece

- Hong Kong

- Hungary

- India

- Ireland

- Italy

- Japan

- Latvia

- Lithuania

- Luxembourg

- Malta

- Mexico

- Netherlands

- Norway

- Poland

- Portugal

- Romania

- Singapore

- Slovakia

- Slovenia

- Spain

- Sweden

- Switzerland

- United Kingdom

- United States

[Local payment methods](#local-payment-methods)

## Local payment methods

Checkout and Payment Links present customers with popular payment methods compatible with their local currencies.

For example, for customers located in the Netherlands, Checkout and Payment Links convert prices to Euros and also present popular Dutch payment methods like iDEAL.

You can configure which payment methods you accept in your payment methods settings.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[Restrictions](#restrictions)

## Restrictions

Adaptive Pricing requires the currency for your prices to be the same as your default settlement currency (in USD, CAD, EUR, or GBP). Prices automatically convert during checkout. This applies to prices you create and reference with a price ID and prices you create inline with price_data when you create a Checkout Session.

[currency for your prices](/api/checkout/sessions/object#checkout_session_object-currency)

[prices](/products-prices/manage-prices#prices-create)

[price_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data)

Adaptive Pricing does not apply for Checkout Sessions that:

- Contain manually defined multi-currency prices.

[multi-currency prices](/payments/checkout/multi-currency-prices)

- Are in subscription mode.

- Use Connect parameters like application_fee_amount, on_behalf_of, and transfer_data.

- Use capture_method as manual.

[capture_method](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)

- Set the currency value on creation.

[currency](/api/checkout/sessions/create#create_checkout_session-currency)

In Sessions that aren’t supported by Adaptive Pricing, Checkout presents prices in the original currency that you’ve set your prices in.

[Exchange rate](#exchange-rate)

## Exchange rate

Stripe uses the mid-market exchange rate and applies a margin to guarantee the rate for the duration of the Checkout Session (up to 24 hours) through settlement. If the exchange rate changes by more than 2% in that time, Stripe might use the updated exchange rate to calculate your payout.

Learn more about how Stripe handles currency conversions.

[currency conversions](/currencies/conversions)

[Refunds](#refunds)

## Refunds

Stripe pays out refunds in the currency your customer pays in using the latest Stripe-provided exchange rate. This means that you might pay more or less to cover the refund depending on how the exchange rate changes.

We ignore Stripe fees in this example for simplicity. Suppose:

- You’re a US business that uses Checkout to sell a product for 100 USD and have activated Adaptive Pricing.

- A customer in Canada views your Checkout page, sees the localized price of 137 CAD at an exchange rate of 1.37 CAD per 1 USD, and completes the purchase.

- Stripe processes the payment, converting the 137 CAD to 100 USD to pay you in your settlement currency.

- Later, when the exchange rate has changed to 1.40 CAD per 1 USD, you issue a full refund to the customer.

- Stripe deducts 97.86 USD from your account, exchanging it at 1.40 CAD per 1 USD to pay out the 137 CAD refund.

Learn more about how Stripe helps you manage refunds.

[refunds](/refunds)

[Fees](#fees)

## Fees

Our standard transaction fees apply to automatically converted transactions:

- Cards or payment methods fee

- International cards or payment methods fee (if applicable)

- Currency conversion fee

See our pricing page for more details about these fees.

[pricing page](https://stripe.com/pricing)

[Webhooks and reporting](#webhooks-reporting)

## Webhooks and reporting

Depending on the user-selected currency, both the Checkout Session and the underlying PaymentIntent objects update automatically to reflect the selected currency and amount. After a user pays in local currency, the Checkout Session object’s currency and total amount is in local currency and contains a currency_conversion hash to reflect what the user would have paid in the default currency. Learn more about what’s deposited in your account after fees.

[deposited in your account after fees](/api/balance_transactions)

The checkout.session.completed webhook event contains a currency_conversion hash that includes the amount_total and amount_subtotal in the source_currency. The amounts reflect what your customer would have paid in the source currency.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[Testing](#testing)

## Testing

To test local currency presentment for Checkout, Payment Links, and the pricing table, pass in a location-formatted customer email that includes a suffix in a +location_XX format in the local part of the email. XX must be a valid two-letter ISO country code.

[pricing table](/payments/checkout/pricing-table)

[two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm)

For example, to test currency presentment for a customer in France, pass in an email like test+location_FR@example.com.

When you visit the URL for a Checkout Session, Payment Link, or pricing table created with a location-formatted email, you see the same currency as a customer does in the specified country.

When you create a Checkout Session, pass the location-formatted email as customer_email.

[customer_email](/api/checkout/sessions/object#checkout_session_object-customer_email)

You can also create a Customer and specify their email that contains the +location_XX suffix.

[Customer](/api/customers/create)

When it’s possible to present the customer’s local currency in Checkout, the Checkout Session object changes. Fields like currency, payment_method_types, and amount_total reflect the local currency and price.

[Checkout Session](/api/checkout/sessions/object)

For Payment Links, pass the location-formatted email as the prefilled_email URL parameter to test currency presentment for customers in different countries.

[URL parameter](/payment-links/customize#customize-checkout-with-url-parameters)

For the pricing table, pass the location-formatted email as the customer-email attribute to test currency presentment for customers in different countries.

[customer-email](/payments/checkout/pricing-table#customer-email)

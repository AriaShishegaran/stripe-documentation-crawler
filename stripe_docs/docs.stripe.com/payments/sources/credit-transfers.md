# Credit transfers (Sources)

Stripe doesn’t recommend using the deprecated Sources API. Use the PaymentIntents and PaymentMethods APIs to integrate with Bank Transfers. Get started accepting Bank Transfer Payments.

[Sources API](/api/sources)

[PaymentIntents](/api/payment_intents)

[PaymentMethods](/api/payment_methods)

[accepting Bank Transfer Payments](/payments/bank-transfers)

Bank transfers let customers send money to you directly from their bank account. Bank transfers are often used by:

- Software or services businesses accepting large, one-off payments from other businesses.

- Businesses that want a low-cost alternative to cards for large one-time consumer payments, like car or auction purchases.

Bank transfers might not be a good fit for your business if:

- You accept many low value transactions. Customers have to initiate bank transfers through their bank account, and can send the wrong amount.

- You need payments to be completed at a specific time. It might take a customer hours or even days to send payment through their bank and bank transfers have varying speeds by market

- You frequently send refunds. Most bank transfer methods don’t support refunds directly. To refund a transaction, Stripe contacts the customer to find the best way to refund them. The customer might not always respond.

## Payment experience

At checkout, you instruct the customer to send funds to an account number provided by Stripe (known as a “virtual account number”). The customer initiates the transfer from their bank’s site, app, ATM, or in-person branch.

Some bank transfer methods let you control the amount the customer sends, or reuse virtual account numbers.

## Product support

[Multibanco (beta)](/sources/multibanco)

## Additional bank transfer methods

Stripe is expanding support for bank transfers to the PaymentIntents API, including automatic reconciliation and refunds. You can read more on Bank Transfer Payments.

[Bank Transfer Payments](/payments/bank-transfers)

- JPY bank transfers in Japan

- GBP bank transfers in the UK

- EUR bank transfers in SEPA countries

- MXN bank transfers in Mexico

- USD bank transfers in the US

Please contact us if you’re interested in joining one of these betas or would like to request another bank transfer method.

[contact us](https://support.stripe.com/contact)

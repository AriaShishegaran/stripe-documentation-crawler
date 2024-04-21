# Revenue Recognition with one-time payments

With one-time payments created in the Dashboard or through the Charges or Payment Intents APIs, Stripe has data on the transaction amount and payment time, but no explicit service period data. By default, Revenue Recognition immediately recognizes the revenue from one-time payments, but you can override this behavior by importing a custom service period.

[importing](/revenue-recognition/data-import)

This example is for a one time payment of 10 USD.

The journal entries generated might look like the following:

This nets out to leave the following end state:

To incorporate a fulfillment schedule into your revenue recognition reports, you must first import the data.

[import the data](/revenue-recognition/data-import)

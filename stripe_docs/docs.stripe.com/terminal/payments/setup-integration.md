# Set up your integration

Server-driven integrations use the Stripe API instead of a Terminal SDK to connect to WisePOS E or Stripe Reader S700 smart readers and collect in-person payments. This allows you to:

[WisePOS E or Stripe Reader S700 smart readers](/terminal/smart-readers)

- Use Terminal even if your infrastructure doesn’t support iOS, Android, or JavaScript SDKs

- Build a Terminal integration that’s powered by your custom middleware or cloud-based infrastructure

- Integrate any device including a .NET-based point of sale to Terminal

- Improve reader network connections using an internet connection instead of the local area network

- Make curl requests to prototype an integration

Server-driven integration doesn’t support:

- Stripe Terminal Bluetooth readers

[Stripe Terminal Bluetooth readers](/terminal/bluetooth-readers)

- Collect payments while offline

[Collect payments while offline](/terminal/features/operate-offline/collect-payments)

You can start your server-driven integration with the following components:

- Your point of sale application: The operator-facing UI that employees see when creating a transaction.

- Your backend infrastructure: Mediates requests from your point of sale application and makes requests to the Stripe API during the transaction.

- The Stripe API: Receives requests and forwards them to a smart reader, such as the BBPOS WisePOS E reader or Stripe Reader S700. Stripe also sends webhooks to your backend infrastructure with the payment status.

[BBPOS WisePOS E reader](/terminal/payments/setup-reader/bbpos-wisepos-e)

[Stripe Reader S700](/terminal/readers/stripe-reader-s700)

[webhooks](/webhooks)

- A BBPOS WisePOS E reader, Stripe Reader S700, or simulated reader: Prompts the cardholder for payment and communicates with Stripe and our financial infrastructure to process the payment. You can create a simulated reader if you don’t yet have a physical reader.

## See also

- Connect to a reader

[Connect to a reader](/terminal/payments/connect-reader)

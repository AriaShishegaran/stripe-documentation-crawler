# Connect to a reader

If you haven’t chosen a reader yet, compare the available Terminal readers and choose one that best suits your needs.

[Terminal readers](/terminal/payments/setup-reader)

Stripe provides a simulated server-driven reader so you can develop and test your app and simulate Terminal payments, without connecting to physical hardware.

## Create a simulated reader

To create a simulated reader use the  designated registration code (simulated-wpe or simulated-s700) when registering the reader. This registration code creates a simulated WisePOS E or Stripe S700 reader object in test mode only. You can register the simulated reader using the Stripe API:

[registration code](/terminal/payments/connect-reader?terminal-sdk-platform=server-driven&reader-type=smart#register-reader)

This returns a reader object representing your simulated reader:

[reader](/api/terminal/readers)

## Query your simulated reader

The simulated reader behaves like a real reader. You can retrieve its information from the reader endpoint:

[reader endpoint](/api/terminal/readers/retrieve)

## Next steps

You’ve connected your application to the reader. Next, collect your first Stripe Terminal payment.

- Collect payments

[Collect payments](/terminal/payments/collect-payment)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

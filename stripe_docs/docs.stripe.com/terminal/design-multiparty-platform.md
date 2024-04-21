# Design a multiparty platform

Stripe Terminal is fully compatible with Stripe Connect, enabling your platform or marketplace to accept in-person payments. If you aren’t familiar with Stripe Connect, we recommend going through the Connect overview.

[Stripe Connect](/connect)

[Connect overview](/connect/overview)

There are two options for integrating Terminal with Connect, depending on the account type you choose for your platform’s connected accounts. To decide which option best suits your business’s needs, refer to the following table:

[the account type you choose](/connect/accounts)

[the Terminal hardware ordering dashboard and APIs](/terminal/fleet/placing-orders)

[charge types](/connect/charges#types)

- Destination charges

[Destination charges](/connect/destination-charges)

- Separate charges/transfers

[Separate charges/transfers](/connect/separate-charges-and-transfers)

- Direct charges

[Direct charges](/connect/direct-charges)

## Express or Custom Connect

In a Connect integration with Express or Custom accounts, all API resources belong to the platform account. As needed, you can associate Terminal objects like Readers and Locations with a particular connected account by including them in the metadata object on these resources.

[Readers](/api/terminal/readers)

[Locations](/api/terminal/locations)

[metadata](/api/metadata)

When processing payments, you specify the connected account as the destination for the funds using the on_behalf_of, transfer_data[destination], and application_fee_amount parameters. This creates a transfer to the connected account automatically and establishes the connected account as the merchant of record.

## Standard Connect

In a Connect integration with Standard accounts, all API resources belong to individual connected accounts. When making API requests such as for creating locations, readers, and payments, you pass the connected account ID in the Stripe-Account header. This tells Stripe that the request is effectively being made by the connected account.

When processing payments, you also pass the connected account’s ID in the Stripe-Account header, which creates the charge directly on the connected account.

## Next steps

- Build a sample integration

[Build a sample integration](/terminal/quickstart)

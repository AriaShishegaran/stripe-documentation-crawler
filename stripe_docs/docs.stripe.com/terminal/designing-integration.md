# Design an integration

59 USD

Reader instructions

[Reader instructions](/terminal/payments/setup-reader/stripe-m2)

Product sheet

[Product sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/m2_product_sheet.pdf)

Order readers and accessories

[Order readers and accessories](https://dashboard.stripe.com/terminal/shop)

## M2 reader features

- Miniature reader

- Optional dock for countertop or mount for mobile roaming

- Contactless, chip, and swipe payments

Not a coder? Find a Stripe partner who supports Terminal.

[Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal)

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:

You can build a working example of an integration like this using the Terminal Quickstart.

[Terminal Quickstart](/terminal/quickstart)

## Organize readers and locations

Before you connect a reader to a Terminal integration, you must create one or more Locations, either in the Dashboard or using the API. Then, when you connect to your reader, specify one of those locations.

[Locations](/api/terminal/locations)

[in the Dashboard](https://dashboard.stripe.com/terminal/locations)

[using the API](/terminal/fleet/locations#create-location)

[connect to your reader](/terminal/payments/connect-reader)

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations may use addresses that represent a primary place of business.

## Prototyping

When you first begin writing your application, you can test it with a simulated reader and simulated cards. The Terminal Quickstart demonstrates an app at this stage of development.

[Terminal Quickstart](/terminal/quickstart)

When you’re ready to work with actual hardware, follow these steps:

- Order an M2 reader and physical test cards.

[Order an M2 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)

- Connect to the reader using Bluetooth or USB.

[using Bluetooth](/terminal/payments/connect-reader?reader-type=bluetooth)

[USB](/terminal/payments/connect-reader?reader-type=usb)

- Test your logic with physical test cards.

[Test your logic with physical test cards](/terminal/references/testing#physical-test-cards)

## Next steps

- Set up your integration to start writing code.

[Set up your integration](/terminal/payments/setup-integration)

- See Terminal Quickstart for a full code example.

[Terminal Quickstart](/terminal/quickstart)

- Order readers, accessories, and test cards when you’re ready to work with physical hardware.

[Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop)

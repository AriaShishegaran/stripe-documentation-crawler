htmlBulk order physical cards | Stripe Documentation[Skip to content](#main-content)Bulk ordering[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fbulk)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fbulk)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)[Physical cards](/docs/issuing/cards/physical)# Bulk order physical cards

Order a large quantity of cards and ship them to one destination.Stripe supports bulk ordering: you can order a large number of physical cards and have them shipped to a single destination.

This guide describes how bulk card ordering works and how to place a bulk order for physical cards.

## Order types

The table below provides an overview of the order types.

OrderCards per orderUse caseWhat shipsShippingFastest fulfillmentIndividual1 card onlyShip a single card directly to a cardholder.The physical card is attached to a carrier which is then put into an envelope.[Normal shipping options](/issuing/cards/physical/standard#shipping-your-cards)2 to 3 business daysBulkUnlimitedShip fewer than 10,000 cards to a single recipient.Only the physical cards. No carriers or envelopes.[Normal shipping options](/issuing/cards/physical/standard#shipping-your-cards)2 to 3 business days## PCI compliance

Before placing a bulk order, you must verify PCI compliance throughout the supply chain.

The recipient of a bulk order must meet all applicable PCI certification requirements. For certain specific issuing use cases, Stripe can grant an exception to allow your company to receive your own bulk shipments.

Confirm with your account team that your bulk order recipient adheres to the appropriate PCI standards required to take possession of the cards.

## Bulk card orders

Stripe groups all cards with the same shipping destination that are ordered on the same day into one bulk order and ships them out together.

### Create a bulk-issued card

To indicate that a card is part of a bulk order, set the shipping.type property to bulk in your create card API call.

There’s no limit to the quantity of cards in a bulk order. If the quantity exceeds a few thousand, the shipment is split across multiple boxes. Each box has its own tracking number.

### Track bulk orders

Upon shipment of each box, Stripe updates the tracking number on the corresponding Card object. You can listen for the issuing_card.updated webhook to receive notifications when the tracking numbers are assigned.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Order types](#order-types)[PCI compliance](#pci-compliance)[Bulk card orders](#bulk-card-orders)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
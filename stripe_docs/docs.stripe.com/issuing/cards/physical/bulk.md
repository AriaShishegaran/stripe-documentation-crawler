# Bulk order physical cards

Stripe supports bulk ordering: you can order a large number of physical cards and have them shipped to a single destination.

This guide describes how bulk card ordering works and how to place a bulk order for physical cards.

## Order types

The table below provides an overview of the order types.

[Normal shipping options](/issuing/cards/physical/standard#shipping-your-cards)

[Normal shipping options](/issuing/cards/physical/standard#shipping-your-cards)

## PCI compliance

Before placing a bulk order, you must verify PCI compliance throughout the supply chain.

The recipient of a bulk order must meet all applicable PCI certification requirements. For certain specific issuing use cases, Stripe can grant an exception to allow your company to receive your own bulk shipments.

Confirm with your account team that your bulk order recipient adheres to the appropriate PCI standards required to take possession of the cards.

## Bulk card orders

Stripe groups all cards with the same shipping destination that are ordered on the same day into one bulk order and ships them out together.

To indicate that a card is part of a bulk order, set the shipping.type property to bulk in your create card API call.

[shipping.type](/api/issuing/cards/create#create_issuing_card-shipping-type)

[create card API call](/api/issuing/cards/create)

There’s no limit to the quantity of cards in a bulk order. If the quantity exceeds a few thousand, the shipment is split across multiple boxes. Each box has its own tracking number.

Upon shipment of each box, Stripe updates the tracking number on the corresponding Card object. You can listen for the issuing_card.updated webhook to receive notifications when the tracking numbers are assigned.

[Card](/api/issuing/cards/object)

[issuing_card.updated](/api/events/types#event_types-issuing_card.updated)

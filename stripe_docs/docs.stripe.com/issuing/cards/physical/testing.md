# Testing physical card shipment

Refer to the Issuing testing documentation to learn more about funding your test mode Issuing balance.

[Issuing testing](/testing)

A physical card starts off with its shipping status as pending by default. As it progresses through fulfillment, subsequent possible values include: shipped, delivered, returned, failure, and canceled.

Refer to the following diagram to see how the status transitions for physical card shipping:

In test mode, you can update a card’s shipping state yourself to test out the different values. You can only use cards created in test mode for testing within your Stripe account and not for external purchases. No cards are actually shipped in test mode.

You can simulate shipping a card by updating its shipping status in the Dashboard.

[Create a cardDashboard](#without-code-create-card)

## Create a cardDashboard

Use the Dashboard to create a cardholder and physical card in test mode.

[Dashboard](https://dashboard.stripe.com/issuing/cards)

[Ship the cardDashboard](#without-code-ship-card)

## Ship the cardDashboard

- In the Dashboard, first make sure you’re viewing test data.

- Go to the Issuing Cards page and find your newly-created card.

[Issuing Cards page](https://dashboard.stripe.com/issuing/cards)

- Scroll to the Card details section.

- Click Update shipping status and select the shipping action you want to simulate (for example, Ship).

- Click Submit to apply your update and refresh the page.

# Embed Issuing card management into your websiteBeta

Issuing embedded components are in private beta. Email issuing-embedded-components@stripe.com to request access.

[issuing-embedded-components@stripe.com](mailto:issuing-embedded-components@stripe.com)

Give your connected accounts access to Issuing card management functionality on your website by using Connect embedded components. Connect embedded components allow you to create complex integrations with Stripe products that require minimal coding and configuration out of the box.

[Connect embedded components](/connect/get-started-connect-embedded-components)

Stripe offers two different components for Issuing card management:

- Issuing Card component

- Issuing Cards List component

These components are for admin users of connected accounts, who can access sensitive card and cardholder data of the entire connected account. These components shouldn’t be used to render UI for individual cardholders in any circumstance.

## Quickstart

Issuing Connect embedded components requires access to Issuing and Connect.

[Issuing and Connect](/issuing/connect)

To learn how embedded components work, see the Connect embedded components guide. The corresponding embedded components quickstart can help you set up your environment.

[Connect embedded components](/connect/get-started-connect-embedded-components)

[embedded components quickstart](/connect/connect-embedded-components/quickstart)

To embed Issuing card management into your website:

- Follow the steps to create a connected account with Issuing capabilities.

[create a connected account with Issuing capabilities](/issuing/connect#create-connected-accounts-with-issuing-capabilities)

- Create a cardholder and cards for that connected account.

[Create a cardholder and cards](/issuing/connect/cardholders-and-cards)

- Create an AccountSession with issuing_card: {enabled: true} or issuing_cards_list: {enabled: true}.

[Create an AccountSession](/connect/connect-embedded-components/quickstart#server-endpoint)

- Add the issuing-card or issuing-cards-list component to the DOM.

[Add the issuing-card or issuing-cards-list component to the DOM](/connect/connect-embedded-components/quickstart#embedded-component)

[Issuing Card component](#issuing-card-component)

## Issuing Card component

The Issuing Card component allows an admin to view individual card details. From this view, they can activate, deactivate (freeze), or cancel cards. If you implement sensitive data display, they can also view card numbers (PANs) and CVVs or CVCs for virtual cards.

[sensitive data display](#sensitive-data-display)

This embedded component supports the following parameters:

[Card](/api/issuing/cards/object#issuing_card_object-id)

[sensitive data display](#sensitive-data-display)

[Issuing Cards List component](#issuing-cards-list-component)

## Issuing Cards List component

The Issuing Cards List component allows an admin to view all the cards on a connected account. They can filter cards by cardholder, creation date, and card type.

When the admin clicks on a row in the table, they see a view of the selected card where they can activate, deactivate (freeze), or cancel the card. If you implement sensitive data display, they can also view card numbers (PANs) and CVC or CVVs for virtual cards.

[sensitive data display](#sensitive-data-display)

This embedded component supports the following parameters:

[sensitive data display](#sensitive-data-display)

[Sensitive data display](#sensitive-data-display)

## Sensitive data display

Issuing Connect embedded components integrate with Issuing Elements to provide a PCI-compliant way for you to allow your admins to view card numbers (PANs) and CVV or CVCs for virtual cards. The sensitive data renders inside Stripe-hosted iframes and never touches your servers.

[Issuing Elements](/issuing/elements)

The components can use an ephemeral key to securely retrieve card information from the Stripe API without publicly exposing your secret keys.

To enable this functionality you must:

- Set up an ephemeral key exchange on your server.

- Pass an asynchronous callback to the components.

Stripe generates a nonce from the Card ID in the Issuing Card or Issuing Cards List component when a card is selected or loaded. Stripe then calls your callback function which returns an ephemeral key, and then renders a Show numbers button if the ephemeral key is valid.

[Card ID](/api/issuing/cards/object#issuing_card_object-id)

Your server-side endpoint needs to accept a Card ID and a nonce. It can then create an ephemeral key using Stripe.

[Card ID](/api/issuing/cards/object#issuing_card_object-id)

Here’s how you might implement an ephemeral key creation endpoint in web application frameworks across various languages:

[https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)

You must define an asynchronous function that accepts a named argument with property issuingCard which is a Card ID and additionally, a nonce property. This function must return an Object with properties issuingCard, nonce, and ephemeralKeySecret which are retrieved from the endpoint you set up in the previous step.

[Card](/api/issuing/cards/object#issuing_card_object-id)

Here’s how you might implement this callback:

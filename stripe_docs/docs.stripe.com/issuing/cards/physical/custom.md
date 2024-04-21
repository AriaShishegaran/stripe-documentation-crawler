# How custom physical cards work

You can design custom cards with Stripe that showcase your brand to your end users.

You can choose from various options, but before designing your card, it’s important to understand how they’re created and what key elements make up a card. This helps inform the choices available and requirements that need to be followed. Reach out to your account representative to learn more about custom card pricing.

[How to create custom physical cards](#how-cards-are-created)

## How to create custom physical cards

The following table describes the different stages needed to get a card from the design file to live and in your hands. This is what you should expect at every step of the process:

After your custom bundle is ready for use, Stripe creates a physical bundle object on your behalf. You can also list all of your physical bundles.

[list all of your physical bundles](/api/issuing/physical_bundles/list)

A personalization design is how you control the appearance of your physical cards in the API. It consists of a physical bundle, and a logo and carrier text if your bundle supports it.

We also provide a number of features to help manage personalization designs, including:

- Setting default designs to use when you issue a card

- Using lookup keys to use many designs without having to change code

- Using Connect to manage personalization designs across many accounts

See managing personalization designs to learn more.

[managing personalization designs](/issuing/cards/physical/personalization-designs)

After you have a personalization design, you can start creating physical cards with that design. Include the ID of the personalization_design you want to use when creating the card. If the design has already been approved, cards you create with it are fulfilled right away. If the design is in review, the cards are fulfilled when the design is approved.

[creating the card](/api/issuing/cards/create#create_issuing_card-personalization_design)

If you have any design set as default, any card you create without specifying a design uses that default. See default personalization designs to learn more.

[default personalization designs](/issuing/cards/physical/personalization-designs#set-a-default-personalization-design)

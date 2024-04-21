# Create standard cards

Standard cards are a quick way to launch your card program, allowing you to showcase your business branding without any lead times.

For our custom card product, see how custom cards work.

[how custom cards work](/issuing/cards/physical/custom)

## Introduction to personalization designs

Every physical card that you create is linked to a specific personalization design, which governs the aesthetic features of your physical cards. Stripe recommends you create a personalization design to set up your card branding before creating physical cards. Personalization designs are composed of:

- Card bundle: Specifies the card’s tangible aspects, including its color and the type of chip embedded. For standard cards you can select between black and white card bundles.

- Card logo: Your brand’s logo displayed on the card that you can upload. If you don’t upload any branding, your physical cards have your business name printed on them. If you’re a platform user issuing on behalf of your connected accounts, their physical cards have your platform’s business name printed on them.

A standard card design with the “Rocket Rides” card logo

- Carrier letter text: Custom text on the card’s carrier material. Cards are attached to a tri-fold carrier, which provides a space to include essential information for cardholders and to further showcase your brand identity.

A standard carrier letter with custom carrier text

## Create a personalization design

You can manage personalization designs with the Stripe Dashboard or through the Personalization Design API. For more detailed guidance on managing personalization designs, see managing personalization designs.

[Personalization Design API](/api/issuing/personalization_designs)

[managing personalization designs](/issuing/cards/physical/personalization-designs)

- Visit the Designs tab in the Issuing Dashboard.

[Designs](https://dashboard.stripe.com/issuing/personalization-designs)

- Click New design on the upper right and select the Standard physical bundle type along with your bundle selection.

- Follow the steps to upload your card logo and set your carrier text.

- Review your personalization design. You can also optionally set this design as your account default here.

[default](/issuing/cards/physical/personalization-designs#set-a-default-personalization-design)

- Click Submit to send your design for review.

## Design review

Stripe reviews all personalization designs to make sure they comply with the guidelines set by our partner networks.

We approve almost all designs, but we might reject yours if it contains:

- The name of another legal entity

- A reference to a different network (for example, MasterCard, if you’re issuing on Visa)

- The name of a geographic location

- A reference to non-fiat currency (for example, cryptocurrency)

- Advertising or promotional language

- Inappropriate text or imagery

You can still create cards with an unapproved personalization design, but such cards aren’t fulfilled until the design has been approved.

See personalization design review to learn more.

[personalization design review](/issuing/cards/physical/personalization-designs#personalization-design-review)

## Create a card

After you have a personalization design, you can start creating physical cards with that design. Include the ID of the personalization_design you want to use when creating the card. If the design has already been approved, cards you create with it are fulfilled right away. If the design is in review, the cards are fulfilled when the design is approved.

[creating the card](/api/issuing/cards/create#create_issuing_card-personalization_design)

If you have any design set as the default, any card you create without specifying a design uses that default. See default personalization designs to learn more. Any physical cards you create without specifying any branding will have your business logo printed on them. If you’re a platform user issuing on behalf of your connected accounts, their physical cards have your platform’s business name printed on them.

[default personalization designs](/issuing/cards/physical/personalization-designs#set-a-default-personalization-design)

Some physical bundles support printing a second line. This is typically used for a business name.

The full set of valid characters for the second line are alphanumeric characters and / -&:().'. There’s a 24 character limit.

## Shipping your cards

The following table reflects prices for shipments originating from the UK:

- Use the shipping service parameter to set the delivery service.

- Use the shipping type parameter to set your shipment packaging.Individual: Each card is affixed to a letter and is shipped in a standard sized envelope addressed to the recipient.Bulk: All cards ordered to the same shipping address and shipment recipient name on a given day are batched together into a single box and are shipped without letters or envelopes.

- Individual: Each card is affixed to a letter and is shipped in a standard sized envelope addressed to the recipient.

- Bulk: All cards ordered to the same shipping address and shipment recipient name on a given day are batched together into a single box and are shipped without letters or envelopes.

Expect arrival times of up to 10 business days for large orders (over 5,000 cards). Estimated arrival times are dependent on the courier service. Estimates are subject to shipping and customs delays that are outside the control of Stripe or our card manufacturing partners.

Card orders have tracking numbers where indicated. You can ship card orders to any non-restricted country. After your card order ships, we deduct associated card fees directly from your Stripe balance. You can see all of your account’s card fees in the Dashboard.

[tracking numbers](/api/issuing/cards/object#issuing_card_object-shipping-tracking_number)

[any non-restricted country](/issuing/cards/physical/standard#shipping_country_restrictions)

[Dashboard](https://dashboard.stripe.com/test/balance)

1Estimated arrival time for priority shipments within the UK is 2-3 business days for individual shipments and 3-4 business days for bulk shipments.

Here are some recommendations to ensure that your cards are successfully delivered to your cardholders:

- Business name inclusion: When ordering individual cards to an office location, ensure you enter the business name as part of either line 1 or line 2 of the address. This doesn’t automatically pull through when ordering a card and should be entered alongside all other key address information.

- Apartment numbers: Provide apartment numbers to residential locations where known.

- EORI numbers for EU shipments: For shipments to the EU, provide an EORI reference number wherever possible. This helps your shipment clear customs. If you’re ordering a bulk shipment, this is a mandatory requirement. You can apply for EORI numbers through your local country’s customs. See the API reference if you need an EORI number.

[EORI number](/api/issuing/cards/object#issuing_card_object-shipping-customs-eori_number)

- Consignee phone number: Ensure that you provide a local phone number when placing your card order with DHL Standard. In the event of any delivery issues DHL will contact you directly. If this field is empty, we will provide them with the phone number provided when the cardholder was initially created. See the API docs for receiver phone number.

[receiver phone number](/api/issuing/cards/object#issuing_card_object-shipping-phone_number)

- If you have multiple cards being ordered to the same location, you can opt for bulk shipment with tracking included. Please note these cards will arrive without carriers/envelopes and are packaged in one box together.

## Cancelling cards

You can cancel a card at any time to make it inactive and unusable—but we still ship and bill for canceled cards.

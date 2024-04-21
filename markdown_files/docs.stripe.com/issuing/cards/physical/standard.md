htmlCreate standard cards | Stripe Documentation[Skip to content](#main-content)Create standard cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fstandard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fstandard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)[Physical cards](/docs/issuing/cards/physical)# Create standard cards

Create standard cards with Issuing.Standard cards are a quick way to launch your card program, allowing you to showcase your business branding without any lead times.

For our custom card product, see how custom cards work.

### Legacy card branding settings

## Introduction to personalization designs

Every physical card that you create is linked to a specific personalization design, which governs the aesthetic features of your physical cards. Stripe recommends you create a personalization design to set up your card branding before creating physical cards. Personalization designs are composed of:

- Card bundle: Specifies the card’s tangible aspects, including its color and the type of chip embedded. For standard cards you can select between black and white card bundles.
- Card logo: Your brand’s logo displayed on the card that you can upload. If you don’t upload any branding, your physical cards have your business name printed on them. If you’re a platform user issuing on behalf of your connected accounts, their physical cards have your platform’s business name printed on them.

![Standard design front and back](https://b.stripecdn.com/docs-statics-srv/assets/card_design-eur.93a25604bb8bbbf8ef2bef3de7bcb1f8.png)

A standard card design with the “Rocket Rides” card logo

- Carrier letter text: Custom text on the card’s carrier material. Cardsare attached to a tri-fold carrier, which provides a space to include essential information for cardholders and to further showcase your brand identity.

![Standard card carrier](https://b.stripecdn.com/docs-statics-srv/assets/carrier_design-eur.5aa4e44f1a83f1532393c3a168156295.png)

A standard carrier letter with custom carrier text

## Create a personalization design

You can manage personalization designs with the Stripe Dashboard or through the Personalization Design API. For more detailed guidance on managing personalization designs, see managing personalization designs.

DashboardAPI1. Visit the[Designs](https://dashboard.stripe.com/issuing/personalization-designs)tab in the Issuing Dashboard.

![Personalization designs](https://b.stripecdn.com/docs-statics-srv/assets/issuing_personalization_designs_tab.8005cf6843cfad8a17067f2cb7eef4e3.png)

1. ClickNew designon the upper right and select theStandardphysical bundle type along with your bundle selection.

![Personalization design create](https://b.stripecdn.com/docs-statics-srv/assets/personalization_design_create.b72ce7b9da304477e2c8ef84993a5599.png)

1. Follow the steps to upload yourcard logoand set yourcarrier text.
2. Review your personalization design. You can also optionally set this design as your account[default](/issuing/cards/physical/personalization-designs#set-a-default-personalization-design)here.
3. ClickSubmitto send your design for review.

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

## Create a card

After you have a personalization design, you can start creating physical cards with that design. Include the ID of the personalization_design you want to use when creating the card. If the design has already been approved, cards you create with it are fulfilled right away. If the design is in review, the cards are fulfilled when the design is approved.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder={{CARDHOLDER_ID}} \
  -d currency=usd \
  -d type=physical \
  -d personalization_design=ipcd_OhggKRta0zu2Te`If you have any design set as the default, any card you create without specifying a design uses that default. See default personalization designs to learn more. Any physical cards you create without specifying any branding will have your business logo printed on them. If you’re a platform user issuing on behalf of your connected accounts, their physical cards have your platform’s business name printed on them.

Some physical bundles support printing a second line. This is typically used for a business name.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder={{CARDHOLDER_ID}} \
  -d currency=usd \
  -d type=physical \
  -d second_line="My Business Name"`The full set of valid characters for the second line are alphanumeric characters and / -&:().'. There’s a 24 character limit.

## Shipping your cards

United StatesEurope (UK merchants)Europe (EU merchants)The following table reflects prices for shipments originating from the UK:

- Use the shipping`service`parameter to set the delivery service.
- Use the shipping`type`parameter to set your shipment packaging.  - Individual: Each card is affixed to a letter and is shipped in a standard sized envelope addressed to the recipient.
  - Bulk: All cards ordered to the same shipping address and shipment recipient name on a given day are batched together into a single box and are shipped without letters or envelopes.



Expect arrival times of up to 10 business days for large orders (over 5,000 cards). Estimated arrival times are dependent on the courier service. Estimates are subject to shipping and customs delays that are outside the control of Stripe or our card manufacturing partners.

Card orders have tracking numbers where indicated. You can ship card orders to any non-restricted country. After your card order ships, we deduct associated card fees directly from your Stripe balance. You can see all of your account’s card fees in the Dashboard.

DestinationServiceEstimated arrival timeTrackingIndividual costBulk costWithin UKStandard3-4 business days1.25 EURExpress3-4 business days7.50 EURPriority2-4 business days120 EUR18 EUROutside of UKStandard6-9 business days2 EURExpress5-8 business days9.50 EURPriority3-4 business days18 EUR18 EUR1Estimated arrival time for priority shipments within the UK is 2-3 business days for individual shipments and 3-4 business days for bulk shipments.

### General ordering best practices

Here are some recommendations to ensure that your cards are successfully delivered to your cardholders:

- Business name inclusion:When ordering individual cards to an office location, ensure you enter the business name as part of either line 1 or line 2 of the address. This doesn’t automatically pull through when ordering a card and should be entered alongside all other key address information.
- Apartment numbers:Provide apartment numbers to residential locations where known.
- EORI numbers for EU shipments:For shipments to the EU, provide an EORI reference number wherever possible. This helps your shipment clear customs. If you’re ordering a bulk shipment, this is a mandatory requirement. You can apply for EORI numbers through your local country’s customs. See the API reference if you need an[EORI number](/api/issuing/cards/object#issuing_card_object-shipping-customs-eori_number).
- Consignee phone number:Ensure that you provide a local phone number when placing your card order with DHL Standard. In the event of any delivery issues DHL will contact you directly. If this field is empty, we will provide them with the phone number provided when the cardholder was initially created. See the API docs for[receiver phone number](/api/issuing/cards/object#issuing_card_object-shipping-phone_number).
- If you have multiple cards being ordered to the same location, you can opt for bulkshipment with tracking included. Please note these cards will arrive without carriers/envelopes and are packaged in one box together.

### Shipping country restrictions

## Cancelling cards

You can cancel a card at any time to make it inactive and unusable—but we still ship and bill for canceled cards.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Introduction to personalization designs](#introduction-to-personalization-designs)[Create a personalization design](#create-a-personalization-design)[Design review](#design-review)[Create a card](#create-a-card)[Shipping your cards](#shipping-your-cards)[Cancelling cards](#cancelling-cards)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
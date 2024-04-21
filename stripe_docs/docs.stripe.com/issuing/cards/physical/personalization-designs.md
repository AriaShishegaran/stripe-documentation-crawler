# Manage personalization designs

## Personalization designs

A personalization design is a logical grouping of all the design attributes required to personalize and ship a card. It includes both a physical bundle and any other elements needed to complete personalization on a card:

[personalization design](/api/issuing/cards/physical/personalization_designs)

- A physical bundle is a set of physical goods in inventory that are personalized and shipped when you issue a card. See Standard cards or Custom cards to learn more. You can also view all of your physical bundles

[physical bundle](/api/issuing/cards/physical/physical_bundles)

[Standard cards](/issuing/cards/physical/standard)

[Custom cards](/issuing/cards/physical/custom)

[view all of your physical bundles](/api/issuing/physical_bundles/list)

- Some bundles support or require other design attributes, such as card logos and carrier text.

A card logo is an image printed onto the card, which you provide to Stripe as a file upload. Stripe only prints card logos in one color, so for the highest quality print we require that card logo images are purely binary containing a black logo on a white background with no grayscale. To upload a logo, use the File API with purpose set to issuing_logo.

[File API](/api/files/create)

Carrier text is a set of content, which you provide as separate pieces of text, printed onto a carrier letter template. When creating a personalization design, you need to specify both the physical bundle to use, as well as a card logo and carrier text if the bundle requires it.

Stripe must review and approve your design (and the underlying physical bundle) before fulfilling any cards made with that design. See Personalization design review to learn more.

[Personalization design review](/issuing/cards/physical/personalization-designs#personalization-design-review)

There is no limit to the number of personalization designs you can create. This gives you the flexibility to express any number of combinations of a physical bundle, card logo, and carrier text to best suit your use case.

## Personalization design review

If your personalization design includes a logo or carrier text, Stripe must review it to make sure they comply with the guidelines set by our partner networks. A design’s status field indicates whether it’s under review, active, or rejected. Cards created with personalization designs in review wait for fulfillment until the personalization design clears review. A personalization design can’t leave the review state if its physical bundle hasn’t been approved yet.

After approval, the personalization design status advances to active. After becoming active, any cards with fulfillment waiting on the personalization design may be fulfilled. Any cards created with a personalization design that is already active may be fulfilled immediately. Note that other reviews, such as cardholder watchlist screening, may also prevent a card from being fulfilled immediately.

You can only set/update the physical_bundle, card_logo, and carrier_text attributes when first creating the personalization design, or after the personalization design has been rejected.

When a personalization design is rejected, you’re notified with a webhook if configured. The personalization design object identifies which part of the design violated design guidelines and reason(s) for the rejection in the rejection_reasons attribute.

You can update the relevant design attributes to address the rejection. Any updates returns the personalization design to the review state, which prevents any further updates to those attributes.

[update the relevant design attributes](/api/issuing/personalization_designs/update)

Stripe provides webhook events for personalization design updates to help you integrate personalization design management into your own platform.

See webhooks to learn more.

[webhooks](/webhooks)

Stripe drives all status changes to a personalization design. However, we provide several test mode helpers so you can test your integration by triggering status changes yourself in test mode:

- Activate a test mode design

[Activate a test mode design](/api/issuing/personalization_designs/activate_testmode)

- Deactivate a test mode design

[Deactivate a test mode design](/api/issuing/personalization_designs/deactivate_testmode)

- Reject a test mode design

[Reject a test mode design](/api/issuing/personalization_designs/reject_testmode)

## Set a default personalization design

To help streamline your integration, you can set a default personalization design so that you don’t need to explicitly specify a personalization design for every card you create.

When creating or updating a personalization design, set the is_default preference to true. The is_default preference for the previous default design is automatically set to false, as there can only be one default.

After you have a default set, any cards you create without specifying a personalization design automatically use the default. Trying to create a card without specifying a personalization design when you don’t have any defaults set results in an error.

You can always override the default personalization design when creating a card by specifying the personalization_design parameter.

## Change personalization designs without deploying code using lookup keys

Some businesses built on Stripe Issuing offer multiple card products to their cardholders. The personalization design representing the card product can change over time. If you hardcode your personalization designs and you want to change them, the process often requires you to deploy new code. You can use lookup keys to remove the need to deploy new code when you want to change personalization designs.

[lookup keys](/api/issuing/personalization_designs/create#create_issuing_personalization_design-lookup_key)

To use lookup keys with personalization designs, you can assign a unique lookup key by passing the lookup_key parameter when creating or updating a personalization design. Instead of hardcoding a personalization design ID, you hardcode the lookup key value and query for the matching personalization design using the personalization design list endpoint.

[personalization design list endpoint](/api/issuing/personalization_designs/list#list_issuing_personalization_designs-lookup_keys)

To improve performance, you might want to cache and/or only reload the personalization design occasionally. When it’s time to change the personalization design for a card product, you can create or update a new personalization design using the existing value for lookup_key while setting transfer_lookup_key to true.

## Manage personalization designs using Connect

When using Connect, personalization designs can be managed at both the platform and connected account levels, just as described above. However, Connect also grants you some ways to streamline your integration even further, by giving connected accounts access to resources at the platform level.

Each of your connected accounts can access personalization designs and physical bundles created at the platform level. This means that you can:

- Issue cards from a connected account with a personalization design created on the platform.

- Create a personalization design on a connected account using a physical bundle available within the platform’s account. This allows you to create these resources on your platform account, and share them across all of your connected accounts. We recommend managing as much as possible at the platform level, unless there are any items that should explicitly be hidden from a connected account, or will only ever be used for specific connected accounts.

Each of your connected accounts can set their own default personalization design. You can also set a default personalization design at the platform level. If set, the platform default is used when you issue a card for a connected account without specifying a design, and that connected account doesn’t have a default.

[set a default personalization design](/api/issuing/personalization_designs/create#create_issuing_personalization_design-preferences-is_default)

If you want issued cards to use the platform default, you can unset the default personalization design for the connected account.

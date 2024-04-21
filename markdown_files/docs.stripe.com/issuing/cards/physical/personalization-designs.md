htmlManage personalization designs | Stripe Documentation[Skip to content](#main-content)Personalization designs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fpersonalization-designs)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fpersonalization-designs)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Manage personalization designs

Learn how to prepare and use personalization designs for creating physical cards.## Personalization designs

A personalization design is a logical grouping of all the design attributes required to personalize and ship a card. It includes both a physical bundle and any other elements needed to complete personalization on a card:

- A[physical bundle](/api/issuing/cards/physical/physical_bundles)is a set of physical goods in inventory that are personalized and shipped when you issue a card. See[Standard cards](/issuing/cards/physical/standard)or[Custom cards](/issuing/cards/physical/custom)to learn more. You can also[view all of your physical bundles](/api/issuing/physical_bundles/list)
- Some bundles support or require other design attributes, such as card logos and carrier text.

A card logo is an image printed onto the card, which you provide to Stripe as a file upload. Stripe only prints card logos in one color, so for the highest quality print we require that card logo images are purely binary containing a black logo on a white background with no grayscale. To upload a logo, use the File API with purpose set to issuing_logo.

Command Line`curl https://files.stripe.com/v1/files \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -F "file"="@/path/to/a/file.jpg" \
  -F "purpose"="issuing_logo"`Carrier text is a set of content, which you provide as separate pieces of text, printed onto a carrier letter template. When creating a personalization design, you need to specify both the physical bundle to use, as well as a card logo and carrier text if the bundle requires it.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/personalization_designs \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d physical_bundle=ics_Kc3MX9PPsUFFMp \
  -d card_logo={{FILE_ID}} \
  -d "carrrier_text[header_title]"=Hello`Stripe must review and approve your design (and the underlying physical bundle) before fulfilling any cards made with that design. See Personalization design review to learn more.

There is no limit to the number of personalization designs you can create. This gives you the flexibility to express any number of combinations of a physical bundle, card logo, and carrier text to best suit your use case.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder={{CARDHOLDER_ID}} \
  -d currency=usd \
  -d type=physical \
  -d personalization_design=ipcd_OhggKRta0zu2Te`## Personalization design review

If your personalization design includes a logo or carrier text, Stripe must review it to make sure they comply with the guidelines set by our partner networks. A design’s status field indicates whether it’s under review, active, or rejected. Cards created with personalization designs in review wait for fulfillment until the personalization design clears review. A personalization design can’t leave the review state if its physical bundle hasn’t been approved yet.

After approval, the personalization design status advances to active. After becoming active, any cards with fulfillment waiting on the personalization design may be fulfilled. Any cards created with a personalization design that is already active may be fulfilled immediately. Note that other reviews, such as cardholder watchlist screening, may also prevent a card from being fulfilled immediately.

You can only set/update the physical_bundle, card_logo, and carrier_text attributes when first creating the personalization design, or after the personalization design has been rejected.

### Handle design rejection

When a personalization design is rejected, you’re notified with a webhook if configured. The personalization design object identifies which part of the design violated design guidelines and reason(s) for the rejection in the rejection_reasons attribute.

Rejection reasonExplanationnon_binary_imageThe image isn’t binary - it contains colors, including grayscale, other than black and white. You can use image manipulation software to threshold the image into binary form.network_nameThe image or text improperly uses the name of a credit card network.other_entityThe image or text improperly uses the name of another entity.geographic_locationThe image or text contains the name of a geographic location.non_fiat_currencyThe image or text contains a reference to non-fiat currency.promotional_materialThe image or text contains advertising, promotional material, or a tagline.inappropriateThe image or text contains inappropriate content.otherThe image or text was flagged for some other reason. See Stripe Support to contact us about how to remediate the rejection.You can update the relevant design attributes to address the rejection. Any updates returns the personalization design to the review state, which prevents any further updates to those attributes.

### Handle status changes programmatically

Stripe provides webhook events for personalization design updates to help you integrate personalization design management into your own platform.

Webhook eventTriggerissuing_personalization_design.updatedOccurs whenever you or Stripe updates a personalization design.issuing_personalization_design.activatedOccurs whenever Stripe activates the bundle for a personalization design and design review approves the design.issuing_personalization_design.rejectedOccurs whenever a personalization design rejects a personalization design.issuing_personalization_design.deactivatedOccurs whenever Stripe deactivates the bundle for a personalization design.See webhooks to learn more.

### Test status changes

Stripe drives all status changes to a personalization design. However, we provide several test mode helpers so you can test your integration by triggering status changes yourself in test mode:

- [Activate a test mode design](/api/issuing/personalization_designs/activate_testmode)
- [Deactivate a test mode design](/api/issuing/personalization_designs/deactivate_testmode)
- [Reject a test mode design](/api/issuing/personalization_designs/reject_testmode)

## Set a default personalization design

To help streamline your integration, you can set a default personalization design so that you don’t need to explicitly specify a personalization design for every card you create.

When creating or updating a personalization design, set the is_default preference to true. The is_default preference for the previous default design is automatically set to false, as there can only be one default.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/personalization_designs/ipcd_OhggKRta0zu2Te \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "preferences[is_default]"=true`After you have a default set, any cards you create without specifying a personalization design automatically use the default. Trying to create a card without specifying a personalization design when you don’t have any defaults set results in an error.

You can always override the default personalization design when creating a card by specifying the personalization_design parameter.

## Change personalization designs without deploying code using lookup keys

Some businesses built on Stripe Issuing offer multiple card products to their cardholders. The personalization design representing the card product can change over time. If you hardcode your personalization designs and you want to change them, the process often requires you to deploy new code. You can use lookup keys to remove the need to deploy new code when you want to change personalization designs.

To use lookup keys with personalization designs, you can assign a unique lookup key by passing the lookup_key parameter when creating or updating a personalization design. Instead of hardcoding a personalization design ID, you hardcode the lookup key value and query for the matching personalization design using the personalization design list endpoint.

To improve performance, you might want to cache and/or only reload the personalization design occasionally. When it’s time to change the personalization design for a card product, you can create or update a new personalization design using the existing value for lookup_key while setting transfer_lookup_key to true.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/personalization_designs \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d physical_bundle=ics_Kc3MX9PPsUFFMp \
  -d card_logo={{FILE_ID}} \
  -d "carrrier_text[header_title]"=Hello \
  -d lookup_key="My lookup key" \
  -d transfer_lookup_key=true`## Manage personalization designs using Connect

When using Connect, personalization designs can be managed at both the platform and connected account levels, just as described above. However, Connect also grants you some ways to streamline your integration even further, by giving connected accounts access to resources at the platform level.

### Personalization designs and physical bundles

Each of your connected accounts can access personalization designs and physical bundles created at the platform level. This means that you can:

- Issue cards from a connected account with a personalization design created on the platform.
- Create a personalization design on a connected account using a physical bundle available within the platform’s account. This allows you to create these resources on your platform account, and share them across all of your connected accounts. We recommend managing as much as possible at the platform level, unless there are any items that should explicitly be hidden from a connected account, or will only ever be used for specific connected accounts.

### Default personalization designs

Each of your connected accounts can set their own default personalization design. You can also set a default personalization design at the platform level. If set, the platform default is used when you issue a card for a connected account without specifying a design, and that connected account doesn’t have a default.

If you want issued cards to use the platform default, you can unset the default personalization design for the connected account.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Personalization designs](#personalization-designs)[Personalization design review](#personalization-design-review)[Set a default personalization design](#set-a-default-personalization-design)[Change personalization designs without deploying code using lookup keys](#change-personalization-designs-without-deploying-code-using-lookup-keys)[Manage personalization designs using Connect](#manage-personalization-designs-using-connect)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
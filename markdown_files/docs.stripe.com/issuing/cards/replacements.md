htmlReplacement cards | Stripe Documentation[Skip to content](#main-content)Replacement cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Freplacements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Freplacements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Replacement cards

Learn how to replace cards that are expired, damaged, lost, or stolen.You can replace cards that are expired, damaged, lost, or stolen. The process differs slightly for each kind of card replacement.

- Card expired: The card has reached its expiration date and is no longer valid.
- Card damaged: The cardholder requests a new card for a reason other than lost or stolen (for example, a physical card’s chip no longer reads properly).
- Card lost/stolen: The card is reported lost or stolen and a new card number, expiry, security code are issued.

Depending on the scenario, the replacement card might have a different card number, expiry, or security code from the original:

ScenarioNew card numberNew security codeNew expiryCard expiredNoYesYesCard damagedNoYesYesCard lost/stolenYesYesYes## Replacements for expired or damaged cards

Physical cards can get damaged, and both physical cards and virtual cards expire, but you can create replacement cards that have the same card number. The cardholder can continue to use the original card before the replacement card is activated, as long as the card isn’t too damaged or already expired. Activating the replacement card cancels the original card if it isn’t already canceled.

To create a replacement card for an expired or damaged card, create a Card with replacement_for using the expired or damaged Card ID and replacement_reason set to expired or damaged.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
  -d currency=usd \
  -d type=virtual \
  -d replacement_for=ic_1LL8wgLUVt6Jcs5dgLLfwcAE \
  -d replacement_reason=expired`## Replacements for lost or stolen cards

Lost or stolen cards get new card numbers for security reasons. We need to cancel the original cards before we can create the replacement card.

To create a replacement card for a lost or stolen card:

1. Cancel the lost or stolen card by using the update card endpoint to set its status to canceled and its cancellation_reason to lost or stolen.


2. Create a Card with replacement_for using the lost or stolen Card ID and replacement_reason set to lost or stolen.



Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/ic_1CoYuRKEl2ztzE5GIEDjQiUI \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d status=canceled \
  -d cancellation_reason=lost`Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
  -d currency=usd \
  -d type=virtual \
  -d replacement_for=ic_1CoYuRKEl2ztzE5GIEDjQiUI \
  -d replacement_reason=lost`## All replacements

All replacement cards have renewed expiration dates and new security codes. Authorizations made on the original cards are migrated to the replacements, but might still clear on the original cards. Like the originals, replacement cards must be activated before use.

## Card-on-file updating

For many of our card programs, Stripe automatically updates the card details on file with acquiring merchants, even when a card is completely reissued. This feature offers several benefits, including saving your cardholders the hassle of manually re-entering card details when their cards expire.

### Card expired

Updating the payment details for a card that has been replaced due to expiration ensures that recurring payments and stored payment details continue to function smoothly. This provides cardholders with a seamless experience even when their cards expire.

### Card lost or stolen

By default, Stripe updates merchants with the new card number, expiry, and security code of a replacement card, even when the card is lost or stolen.

If you prefer not to provide these details to acquiring merchants, cancel the lost or stolen card and issue a new one without specifying the replacement_for card. This prevents the replacement card from being explicitly tied to the card that’s been lost or stolen.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Replacements for expired or damaged cards](#replacements-for-expired-or-damaged-cards)[Replacements for lost or stolen cards](#replacements-for-lost-or-stolen-cards)[All replacements](#all-replacements)[Card-on-file updating](#card-on-file-updating)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
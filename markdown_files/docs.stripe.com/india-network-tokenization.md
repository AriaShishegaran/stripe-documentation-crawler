htmlIndia network tokenization | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Findia-network-tokenization)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Findia-network-tokenization)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# India network tokenization

Learn how the Reserve Bank of India (RBI) card on file tokenization guidelines affect you and how to use Stripe Managed Customer Consent collection.The Reserve Bank of India (RBI) issued a directive to the issuing banks and card networks for the non-storage of card credentials by Payment Aggregators, Payment Gateways, and Merchants in the India payments ecosystem. The RBI mandates card on file (CoF) tokenization through the card networks. This means:

- To store an India-issued customer card for future use for domestic India merchants, Stripe must tokenize the card with the card network (Visa/Mastercard).
- Customers must provide explicit consent to allow the tokenization and storage of the card on Stripe’s system.
- For users who don’t want to build their own custom checkout flow for collecting customer consent, Stripe provides a Stripe-managed customer consent flow by default.

Merchants, Payment Aggregators (PAs), Payment Gateways (PGs), and acquiring banks can no longer store customer card information. Network tokenization and issuer tokenization is the only applicable way forward for the industry and the RBI.

## Regulatory requirements

You must adhere to these requirements to implement tokenization:

- Scope a Token to a Merchant, Customer Card, and Token Requestor.
- Take explicit user consent and Additional Factor of Authentication before generating a Token.
- As the Merchant, you’re required to give the customer an option to de-register their Token from the Merchant platform.
- During transactions, make available to a Merchant only the last 4 digits of the customer card, Issuer Bank name, and card network (visible on the Stripe Dashboard for payments).

NoteThis applies only to India domestic merchants for domestic transactions. International merchants on Stripe aren’t contracted with Stripe India or bound by these requirements. Cards won’t be automatically tokenized.

## Tokenize customer cards

Tokenization minimally impacts the end customer. To convert their cards into a token, a customer must give you consent during payment for a transaction. This applies to new and saved card consent flows.

You can use Stripe Managed Customer Consent to collect customer consent on your behalf. Stripe will automatically prompt the customer for consent before proceeding to 3D Secure authentication.

If you want to create a custom consent flow, you can opt out of Stripe Managed Customer Consent. To do so, navigate to Card Storage Consent under Compliance in the Dashboard.

If you opt out, you must collect customer consent and only save card details for future use on the Customer object if the cardholder gives consent in your checkout consent flow.

![](https://b.stripecdn.com/docs-statics-srv/assets/customer-consent-modal.f76e495163cda39ce68fc98fb900b99c.png)

Stripe Managed Consent Collection Experience

![](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-toggle.519b55eff7a68a73d02a4ec549343209.png)

Opting out of Stripe Managed Consent Collection

Customers who have tokenized their cards will see only the last 4 digits of their saved cards.

## Collect card information for customers that opt out of tokenization

Customers who choose not to tokenize their cards must enter their 16 digit card number, expiry, and CVC for all card transactions.

If you have a direct API integration and don’t currently collect CVC in your checkout flow, you must add it to your integration to continue accepting payments. When you’re collecting payment method details, populate the CVC field.

## More information

For more details on the updated requirements to have a compliant integration with Stripe, see Saving cards in India.

Contact us at support.stripe.com if you have any questions or need help with understanding how to comply with the regulations.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Regulatory requirements](#regulatory-requirements)[Tokenize customer cards](#tokenize-customer-cards)[Collect card information for customers that opt out of tokenization](#collect-card-information-for-customers-that-opt-out-of-tokenization)[More information](#more-information)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
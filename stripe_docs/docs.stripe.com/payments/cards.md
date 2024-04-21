# Cards

Cards are linked to a debit or credit account at a bank. To complete a payment online, customers enter their card information at checkout. Cards are enabled by default and are supported by all Stripe products. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

[Cards are enabled](/payments/payment-methods/integration-options#low-code)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

## The payment flow

A customer initiates a card payment at checkout by entering their credit card information. Depending on their card network and country location, customers have some card functionalities like additional security verification steps.

Cards can act as the funding source for other Stripe payment products and methods like Link and wallets. For instance, customers can leverage Link to save their card payment data for fast checkout with any merchant that has Link enabled.

[Link](/payments/link)

[wallets](/payments/wallets)

With wallets, customers can store their card details in a digital wallet. From your end, their payment method is managed using a wallet, but for the customer, the transaction shows up in their card history as a charge from their digital wallet provider.

[digital wallet](/payments/payment-methods)

## Supported card brands

Stripe supports several card brands, from large global networks like Visa and Mastercard to local networks like Cartes Bancaires in France or Interac in Canada. When you integrate Stripe, you can begin accepting a diversity of card brands without any additional configurations, including:

- American Express

- China UnionPay (CUP)

- Discover & Diners Club

- eftpos Australia

- Japan Credit Bureau (JCB)

- Mastercard

- Visa

Some card brands require additional configuration, such as Cartes Bancaires and Interac.

[Cartes Bancaires](/payments/cartes-bancaires)

[Interac](/terminal/payments/regional?integration-country=CA#interac-payments)

The following table describes some of the different features and restrictions of each card brand online, including limitations on countries where Stripe users can accept the brand (Stripe Account Country), countries where most cardholders of the brand are located (Customer Country) and support for key features like 3D Secure Authentication, and Wallets (like Apple Pay and Google Pay).

[Wallets](/payments/wallets)

Other payment scenarios like setting up future payments, saving a card or placing a hold are supported across all card brands.

[future payments](/payments/save-and-reuse)

[saving a card](/payments/save-during-payment)

[placing a hold](/payments/place-a-hold-on-a-payment-method)

Stripe supports processing payments in 135+ currencies, but some card brand networks have limitations on supported currencies that charges can be made with.

[135+ currencies](/currencies)

[supported currencies](/currencies#presentment-currencies)

[SEPA](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)

1 For more information, see American Express card support for India-based businesses.

[American Express card support for India-based businesses](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses)

You can disallow the use of specific card brands in the following ways:

- If you use Stripe Radar, set up a rule to reject the desired brands.

[set up a rule](/radar/rules)

- Add custom client-side code that checks the brand of a card.

[brand](/api/cards/object#card_object-brand)

- Use the Payment Element to filter cards by brand.

[filter cards by brand](/payments/customize-payment-methods#filter-card-brands)

## Geographic considerations

Stripe, along with other platforms, offer a solid infrastructure that handles secure payments and complies with specific regulations from different regions. This becomes particularly important with the roll-out of Strong Customer Authentication (SCA) rules in regulated markets like Europe and India, wherein additional verification steps are usually necessary.

It’s essential to ensure your Stripe integration is lined up with SCA rules and 3D Secure (3DS) criteria. Moreover, adjusting your approach to suit regional nuances—like installment payments and card brand preferences—is vital for seamless, compliant, and user-centered transactions.

Some banks, especially in regulated regions like Europe and India, might prompt the customer to authenticate a purchase (for example, by texting the customer a code to enter on the bank’s website). This authentication step is part of Strong Customer Authentication (SCA) Requirements. Making sure that your integration meets SCA requirements for 3DS can sometimes require extra steps.

[Strong Customer Authentication](/strong-customer-authentication)

SCA, a rule in effect as of September 14, 2019, as part of PSD2 regulation in Europe, requires changes to how your European customers authenticate online payments. Card payments require a different user experience, namely 3DS, to meet SCA requirements.

[SCA](/strong-customer-authentication)

[3DS](/payments/3d-secure)

Stripe supports 3DS by default in Stripe Checkout, Payment Links, and a Hosted Invoice Page. You can configure your integration to use 3DS with Subscriptions and Connect with the following:

[Connect](/connect)

- Payment Intents API

[Payment Intents API](/payments/payment-intents)

- Setup Intents API

[Setup Intents API](/api/setup_intents)

- Elements

- Mobile SDKs

Some regions have card brands that support installment payments - which are managed by the card issuer and not by creating Subscriptions or using SetupIntents with Stripe.

If you want to create recurring payments and your region or card network doesn’t support Messes sin interesses or  Installments in Brazil, see how to set up future payments or Subscriptions.

[Messes sin interesses](/payments/mx-installments)

[set up future payments](/payments/save-and-reuse)

[Subscriptions](/billing/subscriptions/overview)

The European Union requires businesses to allow their customers the option to pick which card brand processes their transaction because cards in the EU might have both a local network, like Cartes Bancaires, and an affiliated card network, like Visa or Mastercard. You can enable this choice using Elements or Payments APIs so that customers can choose which card brand processes their payment.

[customers can choose which card brand](/co-badged-cards-compliance)

The Reserve Bank of India (RBI) has specific regulations for online transactions that apply to Stripe accounts in India. Stripe Support includes a consolidated list of important resources, for many payment methods in the India FAQs.

[India FAQs](https://support.stripe.com/questions/india-faq)

## See also

- Integrate card payment methods

[Integrate card payment methods](/payments/payment-methods/integration-options)

- Understand card updates and change default payment methods

[Understand card updates and change default payment methods](/payments/cards/overview#card-updates)

- Customize the way PaymentElements handle cards

[Customize the way PaymentElements handle cards](/payments/customize-payment-methods)

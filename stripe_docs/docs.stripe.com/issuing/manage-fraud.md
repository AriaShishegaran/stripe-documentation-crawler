# Manage fraud with Stripe Issuing controls and tools

As a payment facilitation product, Issuing inherently incurs potential fraud risks and liabilities for both businesses and issuers. Because of this, you need to understand your responsibility for losses and how to best manage this risk as part of using our platform. This document provides guidance on the types of fraud, identifies who’s liable when fraud occurs, and outlines the resources available from Stripe to assist you in monitoring for and preventing fraud.

# Fraud in Issuing

Payments has three primary types of fraud:

- Transaction fraud: The unauthorized use of a payment card to fraudulently obtain money or property

- Business fraud: A person creates a fraudulent account (often with a stolen identity) to commit fraud.

- Account takeover (ATO) fraud: A legitimate account owner’s login is compromised by an unauthorized third party who takes actions on their account.

While business fraud and ATO fraud can occur in Issuing, transaction fraud often poses a greater risk. This guide focuses on transaction fraud and the tools available to help you combat it.

# Transaction fraud

On Stripe Issuing, we see transaction fraud in the form of unauthorized charges on a Stripe-issued card. Transaction fraud can occur at any point in a cardholder’s lifecycle. Purchases at legitimate businesses are also subject to transaction fraud. An issued card can be compromised by:

- Physical theft

- Being lost by the cardholder

- Compromised credentials through tactics such as:PhishingSpywareNon-secure checkoutsExternal breaches

- Phishing

- Spyware

- Non-secure checkouts

- External breaches

## Loss liability

Loss liability stems from an issue with a transaction that results in a financial loss for one party. Liability usually arises from either transaction fraud or a business not fulfilling its obligations on a purchase.

Loss liability is assigned to either the merchant (the provider of the service or goods being purchased), you as the Stripe Issuing user, or (in rare cases) the cardholder. This means that when loss liability is allocated to the “issuer,” you’re accountable unless an exception applies.

Stripe Issuing allows you to design your fraud monitoring system, and make your own business logic and transaction decisions. Although Stripe might offer assistance with transaction fraud prevention, you’re still responsible for all losses where the Issuer is deemed liable. So you need to build sufficient controls to monitor, manage, and prevent fraud.

## Liability assignment

In many cases, the business owns liability for fraudulent transactions. There are, however, a few factors that might result in the liability shifting to you, the Stripe Issuing user.

- Card-present Transactions If the card or a mobile wallet such as Apple Pay and Google Pay is present for the transaction, the issuer is generally liable for fraud, with a few exceptions:

Card-present Transactions If the card or a mobile wallet such as Apple Pay and Google Pay is present for the transaction, the issuer is generally liable for fraud, with a few exceptions:

- Cards and wallets need to be electronically read wherever available, that is, by using the contact or contactless chip interface or swiping the magnetic stripe. For manually entered card numbers, such as with mail order or telephone orders, liability is with the business.

Cards and wallets need to be electronically read wherever available, that is, by using the contact or contactless chip interface or swiping the magnetic stripe. For manually entered card numbers, such as with mail order or telephone orders, liability is with the business.

- If a chip-enabled card is used at a terminal that only supports magnetic stripe payments, liability shifts to the merchant.However, if the terminal used by the merchant generally supports chip transactions, but the magnetic stripe is used for a given transaction, liability remains with you, as the issuing user.

If a chip-enabled card is used at a terminal that only supports magnetic stripe payments, liability shifts to the merchant.

- However, if the terminal used by the merchant generally supports chip transactions, but the magnetic stripe is used for a given transaction, liability remains with you, as the issuing user.

- Card-not-present transactions If the card is not present for the transaction (that is, online commerce), liability is determined primarily by 3DS.

Card-not-present transactions If the card is not present for the transaction (that is, online commerce), liability is determined primarily by 3DS.

3DS 3DS is an additional layer of authentication that a merchant can request on authorizations it believes to be high risk (and thus likely to result in the issuer being responsible for fraud liability in the event of a dispute). This additional layer of verification (usually through a form of multi-factor authentication such as a one-time passcode) triggers a “liability shift” where fraud liability shifts from the merchant to the issuer, regardless of the circumstance.

[3DS](/issuing/3d-secure)

When 3DS is requested by a business for a specific card authorization, the cardholder might need to complete additional authentication to complete the transaction. However, whether the authentication is triggered depends on whether you’ve enrolled the card in 3DS and whether there are any exemptions or “frictionless” flows, which automatically bypass any configured 3DS requests. 3DS enrollment isn’t required in the US and is turned off by default; accordingly, US issuers don’t consistently enroll their cards because they don’t want any unnecessary friction for their cardholders. In the context of Stripe Issuing, when a merchant triggers 3DS, fraud liability usually automatically shifts to you, as the Stripe Issuing user, regardless of whether you have 3DS enabled on your cards. Accordingly, having 3DS enabled helps you reduce the risk of financial liability for fraudulent transactions. To learn more, you can read about 3DS for Stripe Issuing.

[read about 3DS for Stripe Issuing](/issuing/3d-secure)

## Digital Wallet Usage

Regardless of 3DS considerations, the use of a Stripe Issuing card in an Apple Pay or Google Pay wallet for a card-not-present transaction also shifts liability to the issuer.

# Transaction fraud controls and tools

Given the risk that liability transaction fraud can create, you need to  take proactive measures to monitor for and prevent it. The following are controls and tools that you can add to your Stripe Issuing program. We recommend using as many controls and tools as possible to limit your program’s transaction fraud risk.

[3D Secure](/issuing/3d-secure)

[Spending controls](/issuing/controls/spending-controls)

[Real-time webhook](/issuing/controls/real-time-authorizations)

[Verification Data](/api/issuing/authorizations/object#issuing_authorization_object-verification_data)

[Token Management](/issuing/controls/token-management)

[Card management](/api/issuing/cards/object#issuing_card_object-status)

[Disputes](/issuing/purchases/disputes)

## Proactive fraud protection controls

3D Secure (3DS) is an additional layer of authentication used by merchants to make sure an online purchase is from a legitimate cardholder. 3DS is used for online transactions and only works if the merchant requests it and you have it enabled for your Issuing program. The additional 3DS step occurs at checkout where the cardholder is shown an authentication page and is prompted to enter a verification code sent to their phone or email.

We recommend enabling 3DS to reduce fraud loss exposure for online transactions. Learn more about 3DS and how to enable it.

[3DS and how to enable it](/issuing/3d-secure)

Spending controls can block specific geographies, merchant IDs, merchant categories (for example, casinos) or set spending limits such as 100 USD per authorization or 3000 USD per month (for example). Spending controls can apply to either a card or a cardholder. The controls are particularly effective when a card or cardholder has an expected spending pattern. Stripe recommends implementing a combination of spending limits and merchant category controls on your cards and cardholders to help limit your exposure in case an unauthorized use is attempted. Learn more about spending controls and how to configure them.

[spending controls and how to configure them](/issuing/controls/spending-controls)

## Real-time fraud protection controls

You can approve or decline authorization requests in real-time based on the data available to you at the point of authorization. This gives you control over authorization outcomes and enables you to implement your own fraud-prevention logic. Use Stripe’s real-time webhook to target a specific fraud pattern while minimizing the impact on other spending behaviors. For example, you can use authorization data on the location of the authorization to block specific geographies, currencies, and merchants. Learn more about the real-time webhook and how it works.

[real-time webhook and how it works](/issuing/controls/real-time-authorizations)

By default, Stripe offers several automatic controls to help reduce your fraud exposure without changing loss liability. Among other considerations, Stripe attempts to block authorizations that:

- Appear to be card testing.

- We estimate to be extremely high risk based on our own risk modeling.

These defenses usually impact a very small subset (less than 0.5%) of authorizations, are purely additive, and shouldn’t be considered a substitute for your own risk management program. Ultimately, you need to identify the ideal balance between user experience and risk management that works best for your program’s specific characteristics. The Stripe Defense Layer doesn’t affect liability.

For any authorization that occurs on a Stripe Issuing card, we compare the CVV2 (or security code) and card expiration date entered at checkout with the values on file for the card. If either of them don’t match, Stripe rejects the authorization on your behalf and exposes any potential mismatch details through the API. Read more about the verifications we perform.

[the verifications we perform](/api/issuing/authorizations/object#issuing_authorization_object-verification_data)

Depending on your use case and desired workflow, you can request adjustments to the default Stripe controls to reduce friction but also increase your risk (for example, relaxing 3DS requirements, increasing maximum dollar amount caps, or disabling auto-blocking on high risk transactions). While Stripe might accommodate these requests on a case-by-case basis, you’re ultimately responsible for any increased risk or loss liability such requests generate.

## Post-fraud transaction tools

Manage digital wallet tokens through the API to quickly shut down digital wallet cards that have been associated with fraudulent activity. Read more about enabling token management and the API.

[enabling token management and the API](/issuing/controls/token-management)

If you or your cardholder suspect unauthorized activity, you can temporarily deactivate a card with the Dashboard or API to block further unauthorized use while you investigate. If the activity was authorized, you can preserve the card’s credentials and reactivate it. Whenever you confirm unauthorized use, immediately cancel the card. Read additional details on card management and how to use the API.

[card management and how to use the API](/api/issuing/cards/object#issuing_card_object-status)

When fraudulent transactions occur, you can file disputes with Visa or Mastercard through the Dashboard or API for those transactions with the reason ‘Fraudulent’. In some cases, depending on what verification is conducted at the point of sale, the merchant might be liable for the fraudulent transaction. Read more about handling disputes.

[handling disputes](/issuing/purchases/disputes)

Educate your cardholders about how to keep their card information safe. Teach them to pay close attention to the activity on their accounts to increase the likelihood of them—and you—catching compromised activity early. Make your cardholders aware of the following preventative measures:

- Check for card skimmers in physical stores: Verify no cameras or skimming equipment are present on the payment terminal. Check for anything inserted in, or attached to, the card reader, ports, display, or keypad.

- Transact at trustworthy businesses: Only provide your card information to merchants that you’re familiar with and trust.

- Cancel a card as soon as it’s lost or stolen: Take immediate action to prevent unauthorized use before a fraudulent actor can obtain your card credentials. To continue spending, create a new card after canceling the lost or stolen one.

# Monitor metrics

The following are metrics we recommend monitoring to help identify and measure fraud on your Issuing-enabled accounts.

## Leading metrics

Leading metrics are metrics that can help you identify potential fraud in its early stages.

- Authorization declines due to incorrect verification data (CVC2, expiry date), over time.

- Authorization rate, over time.

- Authorizations outside of geographic footprint, over time.

- Authorizations by acquiring merchant country, over time.

- Authorizations by merchant category code, over time.

- Force captures, over time.

[Force captures](/issuing/purchases/transactions?issuing-capture-type=force_capture)

## Lagging metrics

Lagging metrics are metrics that can help you assess how much fraudulent activity has impacted your Issuing program:

- Percentage of total spend that has been disputed for fraud, over time.

- Dispute win-loss rate, over time.

- Absolute dispute losses, over time.

- Acquiring merchants with the highest percentage of transactions disputed.

# Managing fraud

The potential for fraud in Issuing necessitates thorough monitoring and proactive fraud management. By understanding your roles and responsibilities and effectively leveraging Stripe’s resources, you can reduce these risks to levels that you deem appropriate for your business.

Keep the following in mind as you decide on your approach to fraud management:

How much fraud you should expect to see: The average volume of monthly fraud varies significantly based on industry, geography, business model, and so on. Most users file fraud disputes on 0.1% or less of their transaction volume, but it can vary greatly, depending on your issuing activity. It’s unusual to have no fraud whatsoever, except in rare business models or if you have low volumes.

Definition of a dispute: A dispute occurs when an account holder challenges a charge on their card statement with their card issuer. The reason for the dispute varies—the account holder might not recognize the charge, perceive it as fraudulent, or feel dissatisfied with the goods or services they purchased. Disputes can help issuers recover funds in the event of fraudulent activity.

Additional Stripe fraud signals and controls: Stripe Issuing currently offers an Enhanced Risk Suite beta for API-centric users that are interested in using advanced signals to help identify and prevent transaction fraud. If you’d like to learn more, please contact support.

[contact support](mailto:issuing-beta-feedback@stripe.com)

# Working with Stripe Issuing cards

Stripe Issuing lets you create physical and virtual cards using a financial account as the source of funds.

[Stripe Issuing](/issuing)

[Enable Issuing on connected accounts](#enable)

## Enable Issuing on connected accounts

Request the card_issuing account capability for the connected accounts on your platform and provide the required information for onboarding.

[account capability](/connect/account-capabilities)

[required information](/issuing/connect#required-verification-information)

If successful, the response returns the connected account Account object with the capabilities hash listing the requested capabilities as active.

[Account object](/api/accounts/object)

If you haven’t already, request access to the card_issuing feature on the financial account, as well.

If successful, the response returns the financial account object with the features listed in the active_features or pending_features array.

[Create a card](#create-card)

## Create a card

After the card_issuing capability is active, the sellers and service providers that own your platform’s connected accounts can create cardholders and cards. You can issue cards only through the API.

A Cardholder object represents an individual or business entity that you can issue cards to. You can begin by creating a Cardholder with name, billing information, and whether they’re an individual or company.

[Cardholder object](/api/#issuing_cardholder_object)

If successful, the response returns the newly created Cardholder object.

Create a Card and assign it to both the Cardholder you just created and a financial account. To assign the cardholder and financial account, specify the cardholder ID in the cardholder parameter and the financial account ID in the financial_account parameter of the /v1/issuing/cards request.

[Card](/api/#issuing_card_object)

If successful, the response returns the newly created Card object.

[Handle authorizations](#handle-auth)

## Handle authorizations

Review the Issuing authorizations guide to properly handle authorizations.

[Issuing authorizations](/issuing/purchases/authorizations)

You can test the cards you just issued by following the steps in Testing Issuing to simulate purchases.

[Testing Issuing](/issuing/testing)

If the financial account associated with the issued card has the outbound_flows restricted, authorizations on the card aren’t allowed.

[outbound_flows](/api/treasury/financial_accounts/create#create_financial_account-platform_restrictions-outbound_flows)

See the Issuing transactions guide for information on different transaction types you might test against.

[Issuing transactions](/issuing/purchases/transactions#handling-other-transactions)

[Handle captures and refunds](#capture)

## Handle captures and refunds

See the Issuing transactions guide to learn how to handle refunds and captures.

[Issuing transactions](/issuing/purchases/transactions)

[Handle disputes](#disputes)

## Handle disputes

See the Issuing disputes guide to learn how to properly handle disputes.

[Issuing disputes](/issuing/purchases/disputes)

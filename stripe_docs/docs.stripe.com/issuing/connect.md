# Set up an Issuing and Connect integration

Stripe Connect provides Stripe Issuing platforms with foundational infrastructure to manage funds flows and compliance requirements. In a Connect integration, the platform account makes API calls on behalf of the connected accounts.

[Stripe Connect](/connect)

[When to use Connect](#when-to-use-connect)

## When to use Connect

If you need to issue cards for users that aren’t directly employed by your business, set up Stripe Connect for your Issuing integration. For example, a business building a new expense management product for small businesses can integrate with Connect. Each small business that uses the expense management product is set up as a connected account.

After you set up and onboard connected accounts, your customers can support their card spend by funding their Issuing balance from their external bank account (or, in certain cases, your customers’ spend can be supported by your platform Issuing balance).  Your customers can also create cardholders and cards and set up spending controls.

[Create connected accounts with Issuing capabilities](#create-connected-accounts-with-issuing-capabilities)

## Create connected accounts with Issuing capabilities

Each business entity that issues cards must be represented by a Custom connected account with the card_issuing and transfers account capabilities.

[Custom connected account](/connect/accounts#choosing-approach)

[account capabilities](/connect/account-capabilities)

Create a new Custom connected account through the Dashboard or using the API with create Account.

[through the Dashboard](/connect/dashboard/managing-individual-accounts#creating-accounts)

[create Account](/api/accounts/create)

Test mode connected accounts can’t receive or spend real money and can’t be used in live mode, but they’re identical in configuration and functionality.

If your platform already has a Connect integration with Custom connected accounts, you can request Issuing on those accounts through the Dashboard or by specifying the connected account id in the Accounts update request.

[through the Dashboard](/connect/dashboard/managing-individual-accounts#updating-capabilities)

[Accounts update](/api/accounts/update)

If your platform already has Standard or Express connected accounts, you’ll need to create new Custom accounts to use Issuing or Treasury. You can see your existing account’s type on the Connect accounts page in your Dashboard.

[Standard or Express](/connect/accounts)

[Connect accounts](https://dashboard.stripe.com/connect/accounts/overview)

You can also use the API to retrieve the account information and verify that the capabilities property has the issuing capability active:

[Start the identity verification process](#onboard-connected-accounts)

## Start the identity verification process

After you create a connected account, you need to provide more information about the account holder. The capability object has a requirements hash that contains currently_due identity verification requirements. The user must provide the details itemized in the requirements hash to enable Issuing capabilities.

[capability object](/api/capabilities/object)

[identity verification requirements](/connect/handling-api-verification)

If you create an Account object in test mode and want to bypass onboarding requirements to test functionality, use the Accounts update API to provide test values that fulfill all the requirements.

[Accounts update API](/api/accounts/update)

[test values](/connect/testing-verification)

Depending on the business type, the user provides details about the individual, company, non-profit organization, or government entity (Stripe Treasury doesn’t support government entities).

[business type](/connect/identity-verification#business-type)

Choose one of the following onboarding options:

Stripe-hosted onboarding is a web form hosted by Stripe with your brand’s name, color, and icon. Stripe-hosted onboarding uses the Accounts API to read the requirements and generate an onboarding form with robust data validation and is localized for all Stripe-supported countries.

[Stripe-hosted onboarding](/connect/custom/hosted-onboarding)

[Accounts API](/api/accounts)

Before using Connect Onboarding, you must provide the name, color, and icon of your brand in the Branding section of your Connect settings page.

[Connect settings page](https://dashboard.stripe.com/test/settings/connect)

You can use hosted onboarding to allow users to link an external_account (which is required for payouts) by enabling it through your Connect Onboarding settings.

[Connect Onboarding settings](https://dashboard.stripe.com/settings/connect)

To create a link for the user to onboard to a connected account, use the Account Links API.

[Account Links API](/api/account_links/create)

For security reasons, don’t email, text, or send account link URLs directly to your user. We recommend that you distribute the account link URL from within your platform’s application, where their account is authenticated.

The response you receive includes the url parameter containing the link for your user to onboard to your platform.

[https://connect.stripe.com/setup/s/…](https://connect.stripe.com/setup/s/…)

## Collect and verify required information

When you create a connected account and request capabilities, the response returns a list of all required information. To see the requirements specific to a capability, retrieve the account capability and look at requirements.past_due.

[retrieve the account capability](/api/capabilities/retrieve)

If you don’t intend to allow your connected accounts to pay out an Issuing balance to an external account, then you can ignore requirements past_due for external_account.

[pay out an Issuing balance to an external account](/issuing/connect/funding#pay-out-an-issuing-balance)

Here are the requirements to activate the card_issuing capability:

Terms of service

settings.card_issuing.tos_acceptance.ip settings.card_issuing.tos_acceptance.date

Record the connected accounts accepting the Issuing terms of service.

[accepting the Issuing terms of service](/issuing/connect/tos_acceptance)

Companies and non-profit organizations require additional onboarding information for representatives (that is, directors [relationship.director] and executives [relationship.executive]), and any beneficial owner that owns more than 25% of the company (relationship.owner). Each connected account must have at least one representative, who’s usually an executive or director, depending on where the account is located. They must be able to certify that the information provided is correct. Beneficial owners aren’t required.

Learn more about beneficial owners, representatives, and directors.

[beneficial owners, representatives, and directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[acceptable verification documents by country](/connect/handling-api-verification#acceptable-verification-documents)

[Handle new requirements coming due and changes to the capability status](#handle-new-requirements-changes)

## Handle new requirements coming due and changes to the capability status

Sometimes after providing all required information, an account might need to provide additional details or documents. These new requirements appear in the requirements.eventually_due array or in requirements.currently_due. Set up your integration to listen for changes to account requirements by using webhooks.

[requirements.eventually_due](/api/accounts/object#account_object-requirements-eventually_due)

[requirements.currently_due](/api/accounts/object#account_object-requirements-currently_due)

[using webhooks](/connect/handling-api-verification#verification-process)

If the capability is already active and the account doesn’t satisfy new requirements due on that capability before the current deadline, the capability becomes inactive until the requirements are satisfied.

[current deadline](/api/accounts/object#account_object-requirements-current_deadline)

If an account’s information can’t be verified, Stripe might require a document to verify the identity of a person (for example, a Passport) or to verify information about the legal entity (for example, a letter from the tax authority). To satisfy document requirements, platforms can send the user to Connect Onboarding (where they’ll be prompted to upload the document), or collect the document from the account in another interface and upload it through the API.

[prompted to upload the document](/connect/custom/hosted-onboarding#new-reqs-due)

[upload it through the API](/connect/handling-api-verification#upload-a-file)

After an account submits all the required information for Issuing and accepts the Issuing terms of service, Stripe considers the application complete. If we can’t verify an account’s information, the capability remains inactive until the account provides additional information or uploads a document.

[required information](/issuing/connect#required-verification-information)

If the account remains inactive 29 days after completing the application, you must send an email notice to the account informing them that we couldn’t verify their identity (see the template).

[see the template](/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#spend-card-application-rejected-for-failure-to-verify-identity)

Stripe monitors for completed applications with unverified identities, and takes the following action after 29 days in live mode and after 1 hour in test mode:

[test mode](/connect/testing)

- Generates an account notice

[Generates an account notice](/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#events-that-require-a-customer-notice)

- Clears the Issuing terms of service acceptance hash so terms acceptance becomes a currently_due requirement

[Issuing terms of service acceptance hash](/api/accounts/object#account_object-settings-card_issuing-tos_acceptance)

You can submit a new application at any time by updating the business information and recording a new acceptance of Issuing’s terms.

Stripe recommends that you present the terms of service as the last step of onboarding, which allows you to track the timing of application completion by referring to the term’s acceptance date.

[acceptance date](/api/accounts/object#account_object-settings-card_issuing-tos_acceptance-date)

If Stripe identifies a connect account that has violated Stripe’s terms of service, Stripe sets the Issuing capability on the account to inactive, deactivates any cards, and notifies the account (see the email template). This might happen when an account’s cards are used in relation to prohibited or restricted businesses, such as illegal activities, gambling, firearms, adult content, or cryptocurrencies, or in relation to prohibited activities for Issuing , such as consumer spending, primarily international use, lending, or other abusive or noncompliant use.

[the email template](/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#account-closed-by-stripe-for-terms-of-service-violation)

[prohibited or restricted businesses](https://stripe.com/legal/restricted-businesses)

[prohibited activities for Issuing](https://stripe.com/legal/restricted-businesses#additional-product-specific-prohibitions)

Stripe disables issuing on accounts that haven’t completed any card transactions in the past 13 months (395 days). For accounts with additional capabilities, Stripe only disables Issuing if there have also been no payments or Treasury transactions in the prior 395 days, and the Treasury balance is 9.99 USD or less. When Issuing is disabled for inactivity, the Connect account’s card_issuing capability status changes to inactive and the capability requirements show a disabled_reason of rejected.inactivity. Learn more about managing inactive accounts with Issuing.

[disabled_reason](/api/capabilities/object#capability_object-requirements-disabled_reason)

[managing inactive accounts](https://support.stripe.com/questions/issuing-managing-inactive-connect-accounts)

[Create cardholders and cards](#create-cardholders-and-cards)

## Create cardholders and cards

A Cardholder object represents an individual or business entity that you can issue cards to. Each cardholder needs to be associated with a connected account to be issued a virtual or physical card. One connected account can have many cardholders.

Learn more about Cardholders and cards.

[Cardholders and cards](/issuing/connect/cardholders-and-cards)

[Add funds](#Add-funds)

## Add funds

The Issuing balance is separate from the connected account’s main balance. When issued cards are used for transactions, they draw from the Issuing balance.

Before an issued card can be used for transactions, you must first allocate funds to the connected account’s Issuing balance associated with the card. An Issuing Balance holds funds reserved for the card and is safely separated from earnings, payouts, and funds from other Stripe products. Learn how to fund connected accounts for Issuing.

[Issuing balance](/issuing/funding/balance)

[payouts](/payouts)

[fund connected accounts](/issuing/connect/funding)

[Use the Dashboard for Issuing with Connect](#using-dashboard-issuing)

## Use the Dashboard for Issuing with Connect

View the connected accounts on your platform and create new accounts from the Connect page in the Dashboard. An account might appear as restricted in the Dashboard if requirements are past_due for any of the requested capabilities (including transfers). You can ignore this if card_issuing is active.

[Connect page](https://dashboard.stripe.com/connect/accounts/overview)

You can also do the following from the dashboard:

- View account activity for a selected account.

- Edit business and personal details for a selected account.

- Create cardholders, cards, or test authorizations on the account. To do so, click the overflow menu (), select View Dashboard as (account name), and then navigate to Card issuing.

- View program details for a selected account. Follow the above steps to View Dashboard as (account name), then navigate to Settings, the Issuing section, and click Card programs.

[Card programs](https://dashboard.stripe.com/settings/issuing/card-programs)

You can also access the Issuing page for a connected account directly by navigating to this URL and replacing {{CONNECT_ACCOUNT_ID}} with the appropriate value: https://dashboard.stripe.com/{{CONNECT_ACCOUNT_ID}}/issuing/overview

As the platform, only you can view the Dashboard on behalf of your connected accounts. Your connected accounts won’t have a Stripe username or password, or access to the Dashboard.

[OptionalSet up spending controls](#set-up-spending-controls)

## OptionalSet up spending controls

htmlTesting account verification during API onboarding | Stripe Documentation[Skip to content](#main-content)Test account verification[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftesting-verification)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftesting-verification)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Required verification information](/docs/connect/required-verification-information)# Testing account verification during API onboarding

A walk-through of testing different verification states for connected accounts during API onboarding using your test API key.### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Custom accounts.This document assumes you’re familiar with Custom accounts, how to update accounts, and identity verification.

Test your verification flows to make sure they can handle changes in account state (for example, when you enable or disable charges). Account states generally change after fulfilling requirements or when reaching processing or time thresholds. The sections below describe these changes and how to test your verification flows.

## Testing initial requirements

Start by creating a new Custom account in test mode, adding a bank account, and showing that the account holder accepted the Stripe Services Agreement. Explicit Services Agreement acceptance is required for making payouts. For this example, the business_type is set to company to illustrate a more complex scenario, and the external_account uses a tokenized Stripe test account as a reminder to avoid exposing sensitive information in API calls.

NoteYou must provide a test API key from a Stripe account which has begun Connect platform onboarding. The auto-filled Stripe test API key causes these sample requests to fail.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d country=US \
  -d type=custom \
  -d business_type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d external_account=btok_us \
  -d "tos_acceptance[date]"=1547923073 \
  -d "tos_acceptance[ip]"="172.18.80.19"`At this point, the account is created but charges and payouts are still disabled. In the response, check the requirements.currently_due array to determine what information you need to collect:

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
    "currently_due": [
      "business_profile.mcc",
      "business_profile.url",
      "company.address.city",
      "company.address.line1",
      "company.address.postal_code",
      "company.address.state",
      "company.name",
      "company.phone",
      "company.tax_id",
      "relationship.representative",
      "relationship.owner"
    ],
    ...
  },
  ...
}`Then, use the external account id returned in the response to update the account with the additional required information about the account:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "business_profile[mcc]"=5045 \
  --data-urlencode "business_profile[url]"="https://bestcookieco.com" \
  -d "company[address][city]"=Schenectady \
  -d "company[address][line1]"="123 State St" \
  -d "company[address][postal_code]"=12345 \
  -d "company[address][state]"=NY \
  -d "company[tax_id]"=000000000 \
  -d "company[name]"="The Best Cookie Co" \
  -d "company[phone]"=8888675309`After successfully updating the company details, checking requirements.currently_due shows the relationship requirements are still required:

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
    "currently_due": [
      "relationship.representative",
      "relationship.owner",
    ],
    ...
  },
  ...
}`Use the Persons API to create a profile for the person representing the relationship to the account. For this example, we create a profile for Jenny Rosen, and identify her as the representative. For this example, we also populate the optional title attribute.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d first_name=Jenny \
  -d last_name=Rosen \
  -d "relationship[representative]"=true \
  -d "relationship[title]"=CEO`NoteFor accounts with business_type set to individual, provide at least one individual property (for example, individual.first_name) and a Person object is created automatically. If you don’t, or for accounts with the business_type set to company, you need to create each Person for the account.

When you create a Person, the response includes a requirements hash listing the required verification information for that person.

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
    "currently_due": [
      "address.city",
      "address.line1",
      "address.postal_code",
      "address.state",
      "dob.day",
      "dob.month",
      "dob.year",
      "phone",
      "email",
      "relationship.executive",
      "ssn_last_4"
    ],
    ...
  },
  ...
}`After you create a Person for your external account, checking the Account object shows that the required verification information for the newly created Person has been added to the requirements.currently_due list:

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
    "currently_due": [
      "person.person_xxx.address.city",
      "person.person_xxx.address.line1",
      "person.person_xxx.address.postal_code",
      "person.person_xxx.address.state",
      "person.person_xxx.dob.day",
      "person.person_xxx.dob.month",
      "person.person_xxx.dob.year",
      "person.person_xxx.phone",
      "person.person_xxx.email",
      "person.person_xxx.relationship.executive",
      "person.person_xxx.ssn_last_4",
      "relationship.owner"
    ],
    ...
  },
  ...
}`Use the Update a Person API to provide the requested verification information for Jenny Rosen:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons/{{PERSON_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "address[city]"=Schenectady \
  -d "address[line1]"="123 State St" \
  -d "address[postal_code]"=12345 \
  -d "address[state]"=NY \
  -d "dob[day]"=10 \
  -d "dob[month]"=11 \
  -d "dob[year]"=1980 \
  -d ssn_last_4=0000 \
  -d phone=8888675309 \
  --data-urlencode email="jenny@bestcookieco.com" \
  -d "relationship[executive]"=true`Setting relationship[executive]=true confirms to Stripe that the representative is someone with significant control in the organization. US required verification information has more information about company representative verification details for US businesses.

After providing the representative information, we still need to identify the owner for the account. In this example, Kathleen Banks owns 80% of The Best Cookie Co.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d first_name=Kathleen \
  -d last_name=Banks \
  --data-urlencode email="kathleen@bestcookieco.com" \
  -d "relationship[owner]"=true \
  -d "relationship[percent_ownership]"=80`In our example, Kathleen Banks owns less than 100% of The Best Cookie Co. Since you haven’t defined another owner to make the ownership total 100%, Stripe requires you to confirm that you’ve provided information on all required owners.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[owners_provided]"=true`Successful completion of your connected account at this stage means:

- You’ve completed all required information (`requirements.currently_due=null`).
- Charges are enabled for the account (`charges_enabled=true`).
- You received an`account.updated`[webhook](/webhooks)from Stripe.

## Testing thresholds

Whether you use upfront onboarding or incremental onboarding, Stripe might request more information about connected accounts as different thresholds are reached. Sometimes these thresholds are triggered by verification failures or OFAC checks. Other times, they’re triggered by a processing or time component. For example, more information might be required after 1,500 USD in charges or 30 days after an account is created (whichever comes first). To find out what information is required and by when, you can check the requirements.eventually_due array and the requirements.current_deadline timestamp.

In some cases, if the you don’t collect new information by a certain date, charges and payouts might be disabled until you collect it. You can trigger these scenarios so that you can test these thresholds, and then collect the required information.

### Triggering thresholds

You can create a charge with the verification token (tok_visa_triggerVerification) to trigger a generic verification threshold. This doesn’t block charges or payouts, but it does trigger the request for additional information. If you’re listening to the account.updated webhook, you can check:

- `requirements.currently_due`to find out what information is needed.
- `requirements.current_deadline`to find out when the information is needed.

If the information isn’t collected by the current_deadline, charges and payouts might be disabled. To test scenarios like this, see the blocking charges and payouts sections below.

You can also trigger more specific verification thresholds, like when there’s an identity mismatch or when an OFAC threshold is reached. Testing these thresholds is beneficial because they often happen when verification fails.

### Testing blocked charges

You can block charges by creating a test charge with the charge block token (tok_visa_triggerChargeBlock). After doing this, you should receive an account.updated webhook that shows:

- `charges_enabled=false`.
- The required information in the`requirements.currently_due`array.
- An empty`requirements.eventually_due`array.

You can then update the account with the new information. That triggers another webhook, which indicates that charges are enabled and that the requirements.currently_due and requirements.eventually_due arrays are both empty.

### Testing blocked payouts

You can block payouts by creating a test charge with the block transfer token (tok_visa_triggerTransferBlock). After doing this, you should receive an account.updated webhook that shows:

- `payouts_enabled=false`.
- The required information in the`requirements.currently_due`array.
- An empty`requirements.eventually_due`array.

You can then update the account with the new information. That triggers another webhook, which indicates that payouts are enabled and that the requirements.currently_due and requirements.eventually_due arrays are both empty.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Testing initial requirements](#initial-requirements)[Testing thresholds](#testing-thresholds)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
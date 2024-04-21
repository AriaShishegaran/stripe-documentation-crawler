htmlUsing tokens to securely transmit account data | Stripe Documentation[Skip to content](#main-content)Handle verification with tokens[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-tokens)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-tokens)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Required verification information](/docs/connect/required-verification-information)# Using tokens to securely transmit account data

Connect platforms can use Stripe.js, the API, or mobile client libraries to securely collect account details from their users.Before we can enable charges and payouts for connected accounts, you must fulfill Know Your Customer (KYC) requirements. To do so, provide identity verification information about your accounts to Stripe, which we then verify. Account Tokens and Person Tokens provide a secure and reliable way to perform this task. Tokens ensure that personally identifiable information (PII) doesn’t touch your servers, so your integration can operate in a PCI-compliant way. These tokens also allow Stripe to more accurately detect potential fraud.

### Account types

Connect platforms can work with three different account types.

The content on this page applies only to Custom accounts.

Tokens can be used only for:

- Legal entity details (information about the business or individual)
- Person details
- Indicating acceptance of the Stripe Connected Account Agreement

Tokens cannot be used for any other account information, including:

- Configuration settings on the account (for example, payout schedules)
- Non-sensitive info on the account (for example, support url, support phone number)
- The country of the connected account

Tokens are created using Stripe.js, the API, or one of the mobile client libraries. The process is effectively the same as tokenizing payment details or external accounts. Your connected account’s information is sent directly to Stripe and exchanged for a token that can be used in create and update API calls.

NoteFrench platforms must use account tokens, which are an alternative to the agent model for platform PSD2 compliance. The key benefit of tokens for French platforms is that information is transferred from the user directly to Stripe. Not having to store PII data is still a benefit, but not necessarily a requirement. For platforms in other countries, account tokens are optional but recommended.

## Creating and using tokens

Tokens require both client-side and server-side code:

1. Create the HTML form that takes the user’s input.
2. Add JavaScript that sends the form data to Stripe, receives a token in return, and submits that token to your server.
3. Use the token in a server-side Stripe API call.

The following example shows how to use account tokens and person tokens. Both types are required when providing legal entity and person details for companies. If you onboard only individuals, you don’t need person tokens. Instead, create account tokens and pass the individual hash on the Account object to provide the required information.

### Step 1: Create an HTML form

The first step is to create an HTML form that collects the required information for the account and the person. This includes acceptance of the Stripe Connected Account Agreement.

### Collecting account and person details

Create form elements to collect the required information, such as name, address, and anything else that’s required in the user’s country.

form.html`<form class="my-form" action="/create-person" method="post">
  <input type="hidden" name="token-account" id="token-account">
  <input type="hidden" name="token-person" id="token-person">
  <label>
    <span>Business Name</span>
    <input class="inp-company-name">
  </label>
  <fieldset>
    <legend>Business Address</legend>
    <label>
      <span>Street Address Line 1</span>`See all 55 lines### Presenting the Stripe Connected Account Agreement

As the platform, you must make clear to your users that processing of payments is provided subject to the Stripe Connected Account Agreement. Indicating acceptance of the Stripe Connected Account Agreement is required when using an account token to create a new connected account.

NoteOnly platforms that can accept the service agreement through the API may create Account Tokens that specify tos_shown_and_accepted.

We recommend you include language like the following, including links to both our agreement and your terms of service.

[English](#)`<p>By clicking, you agree to <a href="#">our terms</a> and the <a href="https://stripe.com/connect-account/legal">Stripe Connected Account Agreement</a>.</p>`### Step 2: Add JavaScript

Next, the page needs JavaScript that:

1. Interrupts the form submission.
2. Calls the`stripe.createToken()`method to request account and person tokens.
3. Sends the IDs of the received tokens to your server.

For simplicity, data validation and error handling are omitted in the below code, but remember to add both to your actual integration.

Provide to the stripe.createToken() method two arguments:

- The value`account`or`person`, to specify the kind of token to create
- A generic object of information

The JavaScript object provided as the second argument needs to parallel the structure of the Account or Person object you are tokenizing. Account tokens need either a top-level company or individual property, and person tokens need a top-level person property. Follow the object’s structure through all the required attributes. For example, line1 within address in the code block below is provided as person.address.line1.

To represent the user’s acceptance of the Stripe Connected Account Agreement, provide a top-level tos_shown_and_accepted property with a value of true (only account tokens are used for this).

You must still use tokens—to create or update a person—using server-side code. You can send the token ID to your server using whatever approach makes sense for your application (for example, an XHR request). For simplicity, this code example stores the token ID in a hidden form input and then submits the form.

script.js`// Assumes you've already included Stripe.js!
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const myForm = document.querySelector('.my-form');
myForm.addEventListener('submit', handleForm);

async function handleForm(event) {
  event.preventDefault();

  const accountResult = await stripe.createToken('account', {
    business_type: 'company',
    company: {
      name: document.querySelector('.inp-company-name').value,
      address: {
        line1: document.querySelector('.inp-company-street-address1').value,
        city: document.querySelector('.inp-company-city').value,
        state: document.querySelector('.inp-company-state').value,
        postal_code: document.querySelector('.inp-company-zip').value,
      },
    },
    tos_shown_and_accepted: true,
  });

  const personResult = await stripe.createToken('person', {
    person: {
      first_name: document.querySelector('.inp-person-first-name').value,
      last_name: document.querySelector('.inp-person-last-name').value,
      address: {
        line1: document.querySelector('.inp-person-street-address1').value,
        city: document.querySelector('.inp-person-city').value,
        state: document.querySelector('.inp-person-state').value,
        postal_code: document.querySelector('.inp-person-zip').value,
      },
    },
  });

  if (accountResult.token && personResult.token) {
    document.querySelector('#token-account').value = accountResult.token.id;
    document.querySelector('#token-person').value = personResult.token.id;
    myForm.submit();
  }
}`Upon successfully receiving the tokens from Stripe, the JavaScript stores the token IDs in a hidden form input and then submits the form (to your server). The final steps are for your server-side code to use the tokens to create an account and a person.

### Step 3: Create an account

Use the account token ID to create the account. The country and business type are provided outside the token.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d country=US \
  -d type=custom \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d account_token={{ACCOUNT_TOKEN_ID}}`When creating an account token, setting tos_shown_and_accepted to true automatically populates the date, ip, and user_agent attributes of the Account object’s tos_acceptance attribute. If you create an account without using an account token, you must provide values for those attributes.

Make sure to note the account ID that’s returned so that you can use it to create person objects for the account.

### Step 4: Create a person

Create a person by providing the ID of the person token as the value for the person_token parameter (you also need the account ID the person is for). You can use the requirements hash on the Account object to determine what information needs to be collected and from which persons.



Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d first_name=Jane \
  -d last_name=Diaz \
  -d person_token={{PERSON_ID}}`## Creating account tokens with the mobile SDKs

You can also create an account token with our Android or iOS SDKs. Note that currently only account tokens are supported on mobile. This is sufficient for creating an individual account, but you must use Stripe.js to create the person token that you need for a company account. Support for person tokens in the mobile SDKs will be available in a future release.

iOSAndroid[Swift](#)`import UIKit
import StripePayments

let companyParams = STPConnectAccountCompanyParams()
companyParams.name = company.name
companyParams.address = STPConnectAccountAddress()
companyParams.address.line1 = company.address_line_1
companyParams.address.city = company.address_city
companyParams.address.state = company.address_state
companyParams.address.country = company.address_country
companyParams.address.postalCode = company.address_postal_code

guard let accountParams = STPConnectAccountParams(tosShownAndAccepted: true, company: companyParams) else {
  // The TOS was not accepted
  return
}

STPAPIClient.shared.createToken(withConnectAccount: accountParams) { (accountToken, error) in
    if let error = error {
        // display an error to your user
    }
    else {
        // use account token to create a Connect account server-side
    }
}`## Handling a file upload

When a connected account needs to provide Stripe with a scan of an identity document such as a passport, you can use an account token. However, the JavaScript is more complicated because the file must be sent to Stripe as part of an XHR request. In this flow, the JavaScript:

1. Interrupts the form submission.
2. If a file was uploaded, sends that to Stripe, receiving a file token in return.
3. Adds the file token ID to the generic object for the account token request.
4. Calls the`stripe.createToken()`method to request a token.
5. Sends the ID of the received account token to your server for use.

To begin, add a file element to the form. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10MB in size.

`<input type="file" id="id-file" name="id-file" accept=".jpeg,.jpg,.png">`Next, in your JavaScript that handles the form’s submission, send the uploaded file to Stripe. This needs to happen before creating the account token.

`const data = new FormData();
data.append('file', document.querySelector('#id-file').files[0]);
data.append('purpose', 'identity_document');
const fileResult = await fetch('https://uploads.stripe.com/v1/files', {
  method: 'POST',
  headers: {'Authorization': 'Bearer pk_test_VOOyyYjgzqdm8I3SrBqmh9qY'},
  body: data,
});
const fileData = await fileResult.json();`Finally, include the returned file ID as the verification.document.front value in the generic object provided to the createToken() call:

`const result = await stripe.createToken('account', {
  person: {
    first_name: document.querySelector('.inp-first-name').value,
    last_name: document.querySelector('.inp-last-name').value,
    address: {
      line1: document.querySelector('.inp-street-address1').value,
      city: document.querySelector('.inp-city').value,
      state: document.querySelector('.inp-state').value,
      postal_code: document.querySelector('.inp-zip').value,
    },
    verification: {
        document: {
            front: fileData.id,
            },
        },
    },
  tos_shown_and_accepted: true,
});`## Updating legal entity and person details

You can use tokens to securely update an existing account’s legal entity and person information. Create the tokens you need using the same combination of HTML and JavaScript as above, and then perform an update account or update person call providing the new token ID.

You must create and provide a new token when updating legal entity details previously set using an account token.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account_token={{ACCOUNT_TOKEN_ID}}`### Retrieving legal entity and person details

Legal entity and person details that are provided directly to Stripe using tokens can also be retrieved after the fact using a retrieve account or retrieve person call.

When using tokens for updates:

- An existing value is replaced with a new value.
- If no new value is provided, the existing value remains.
- You cannot unset an existing value.
- The`tos_shown_and_accepted`parameter is ignored and can be omitted.
- You can use an account or person token for an update whether or not a token was originally used when creating the account or person.
- If the account or person was originally created using an account token, you can only update values using another token.

For example, if an account is created with a token containing only a name and date of birth, you’d create a subsequent token containing only the address information and then perform an update account call to add the address details to the account.

## Removing legal entity and person details

To clear any legal entity or person details or to explicitly set a value as null, pass an empty string in an update account or update person call. Use an update call, not a token, even if you originally used a token. You can assign empty strings only to optional attributes (for example, the second line of an address). You can’t assign them to any required attributes.

## See also

- [Identity Verification](/connect/identity-verification)
- [Controlling Bank and Debit Card Payouts](/connect/payouts-connected-accounts)
- [Full API reference](/api)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Creating and using tokens](#workflow)[Creating account tokens with the mobile SDKs](#mobile-tokens)[Handling a file upload](#file-upload)[Updating legal entity and person details](#updating)[Removing legal entity and person details](#removing)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
# Using tokens to securely transmit account data

Before we can enable charges and payouts for connected accounts, you must fulfill Know Your Customer (KYC) requirements. To do so, provide identity verification information about your accounts to Stripe, which we then verify. Account Tokens and Person Tokens provide a secure and reliable way to perform this task. Tokens ensure that personally identifiable information (PII) doesn’t touch your servers, so your integration can operate in a PCI-compliant way. These tokens also allow Stripe to more accurately detect potential fraud.

[payouts](/payouts)

[identity verification information](/connect/identity-verification)

[Account Tokens](/api/tokens/create_account)

[Person Tokens](/api/tokens/create_person)

[PCI-compliant](https://stripe.com/guides/pci-compliance)

Connect platforms can work with three different account types.

[Connect](/connect)

[account types](/connect/accounts)

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

[Stripe.js](/payments/elements)

[the API](/api/tokens)

[payment details](/payments/accept-a-payment-charges#web-create-token)

French platforms must use account tokens, which are an alternative to the agent model for platform PSD2 compliance. The key benefit of tokens for French platforms is that information is transferred from the user directly to Stripe. Not having to store PII data is still a benefit, but not necessarily a requirement. For platforms in other countries, account tokens are optional but recommended.

[PSD2](https://stripe.com/connect/eu-guide)

## Creating and using tokens

Tokens require both client-side and server-side code:

- Create the HTML form that takes the user’s input.

- Add JavaScript that sends the form data to Stripe, receives a token in return, and submits that token to your server.

- Use the token in a server-side Stripe API call.

The following example shows how to use account tokens and person tokens. Both types are required when providing legal entity and person details for companies. If you onboard only individuals, you don’t need person tokens. Instead, create account tokens and pass the individual hash on the Account object to provide the required information.

[individual](/api/accounts/object#account_object-individual)

The first step is to create an HTML form that collects the required information for the account and the person. This includes acceptance of the Stripe Connected Account Agreement.

Create form elements to collect the required information, such as name, address, and anything else that’s required in the user’s country.

[required](/connect/required-verification-information)

As the platform, you must make clear to your users that processing of payments is provided subject to the Stripe Connected Account Agreement. Indicating acceptance of the Stripe Connected Account Agreement is required when using an account token to create a new connected account.

[Stripe Connected Account Agreement](https://stripe.com/connect-account/legal)

Only platforms that can accept the service agreement through the API may create Account Tokens that specify tos_shown_and_accepted.

[accept the service agreement through the API](/connect/service-agreement-types#accepting-the-correct-agreement)

[tos_shown_and_accepted](/api/tokens/create_account#create_account_token-account-tos_shown_and_accepted)

We recommend you include language like the following, including links to both our agreement and your terms of service.

[https://stripe.com/connect-account/legal](https://stripe.com/connect-account/legal)

Next, the page needs JavaScript that:

- Interrupts the form submission.

- Calls the stripe.createToken() method to request account and person tokens.

- Sends the IDs of the received tokens to your server.

For simplicity, data validation and error handling are omitted in the below code, but remember to add both to your actual integration.

Provide to the stripe.createToken() method two arguments:

- The value account or person, to specify the kind of token to create

- A generic object of information

The JavaScript object provided as the second argument needs to parallel the structure of the Account or Person object you are tokenizing. Account tokens need either a top-level company or individual property, and person tokens need a top-level person property. Follow the object’s structure through all the required attributes. For example, line1 within address in the code block below is provided as person.address.line1.

[company](/api/accounts/object#account_object-company)

[individual](/api/accounts/object#account_object-individual)

[person](/api/persons/object)

[person.address.line1](/api/persons/object#person_object-address-line1)

To represent the user’s acceptance of the Stripe Connected Account Agreement, provide a top-level tos_shown_and_accepted property with a value of true (only account tokens are used for this).

You must still use tokens—to create or update a person—using server-side code. You can send the token ID to your server using whatever approach makes sense for your application (for example, an XHR request). For simplicity, this code example stores the token ID in a hidden form input and then submits the form.

Upon successfully receiving the tokens from Stripe, the JavaScript stores the token IDs in a hidden form input and then submits the form (to your server). The final steps are for your server-side code to use the tokens to create an account and a person.

Use the account token ID to create the account. The country and business type are provided outside the token.

When creating an account token, setting tos_shown_and_accepted to true automatically populates the date, ip, and user_agent attributes of the Account object’s tos_acceptance attribute. If you create an account without using an account token, you must provide values for those attributes.

[tos_acceptance](/api#account_object-tos_acceptance)

Make sure to note the account ID that’s returned so that you can use it to create person objects for the account.

Create a person by providing the ID of the person token as the value for the person_token parameter (you also need the account ID the person is for). You can use the requirements hash on the Account object to determine what information needs to be collected and from which persons.

[Create a person](/api/persons/create)

[requirements](/api/accounts/object#account_object-requirements)



## Creating account tokens with the mobile SDKs

You can also create an account token with our Android or iOS SDKs. Note that currently only account tokens are supported on mobile. This is sufficient for creating an individual account, but you must use Stripe.js to create the person token that you need for a company account. Support for person tokens in the mobile SDKs will be available in a future release.

## Handling a file upload

When a connected account needs to provide Stripe with a scan of an identity document such as a passport, you can use an account token. However, the JavaScript is more complicated because the file must be sent to Stripe as part of an XHR request. In this flow, the JavaScript:

[scan of an identity document](/connect/handling-api-verification#handle-identity-verification)

- Interrupts the form submission.

- If a file was uploaded, sends that to Stripe, receiving a file token in return.

- Adds the file token ID to the generic object for the account token request.

- Calls the stripe.createToken() method to request a token.

- Sends the ID of the received account token to your server for use.

To begin, add a file element to the form. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10MB in size.

Next, in your JavaScript that handles the form’s submission, send the uploaded file to Stripe. This needs to happen before creating the account token.

[https://uploads.stripe.com/v1/files](https://uploads.stripe.com/v1/files)

Finally, include the returned file ID as the verification.document.front value in the generic object provided to the createToken() call:

## Updating legal entity and person details

You can use tokens to securely update an existing account’s legal entity and person information. Create the tokens you need using the same combination of HTML and JavaScript as above, and then perform an update account or update person call providing the new token ID.

[update account](/api#update_account)

[update person](/api/persons/update)

You must create and provide a new token when updating legal entity details previously set using an account token.

Legal entity and person details that are provided directly to Stripe using tokens can also be retrieved after the fact using a retrieve account or retrieve person call.

[retrieve account](/api#retrieve_account)

[retrieve person](/api/persons/retrieve)

When using tokens for updates:

- An existing value is replaced with a new value.

- If no new value is provided, the existing value remains.

- You cannot unset an existing value.

- The tos_shown_and_accepted parameter is ignored and can be omitted.

- You can use an account or person token for an update whether or not a token was originally used when creating the account or person.

- If the account or person was originally created using an account token, you can only update values using another token.

For example, if an account is created with a token containing only a name and date of birth, you’d create a subsequent token containing only the address information and then perform an update account call to add the address details to the account.

## Removing legal entity and person details

To clear any legal entity or person details or to explicitly set a value as null, pass an empty string in an update account or update person call. Use an update call, not a token, even if you originally used a token. You can assign empty strings only to optional attributes (for example, the second line of an address). You can’t assign them to any required attributes.

[update account](/api#update_account)

[update person](/api/persons/update)

## See also

- Identity Verification

[Identity Verification](/connect/identity-verification)

- Controlling Bank and Debit Card Payouts

[Controlling Bank and Debit Card Payouts](/connect/payouts-connected-accounts)

- Full API reference

[Full API reference](/api)

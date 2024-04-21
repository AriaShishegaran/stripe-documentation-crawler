- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Tokens

[Tokens](/api/tokens)

Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.

[recommended payments integrations](/payments)

If you can’t use client-side tokenization, you can also create tokens using the API with either your publishable or secret API key. If your integration uses this method, you’re responsible for any PCI compliance that it might require, and you must keep your secret API key safe. Unlike with client-side tokenization, your customer’s information isn’t sent directly to Stripe, so we can’t determine how it’s handled or stored.

You can’t store or use tokens more than once. To store card or bank account information for later use, create Customer objects or Custom accounts. Radar, our integrated solution for automatic fraud protection, performs best with integrations that use client-side tokenization.

[Customer](/api#customers)

[Custom accounts](/api#external_accounts)

[Radar](/radar)

[POST/v1/tokens](/api/tokens/create_account)

[POST/v1/tokens](/api/tokens/create_bank_account)

[POST/v1/tokens](/api/tokens/create_card)

[POST/v1/tokens](/api/tokens/create_cvc_update)

[POST/v1/tokens](/api/tokens/create_person)

[POST/v1/tokens](/api/tokens/create_pii)

[GET/v1/tokens/:id](/api/tokens/retrieve)

# The Token object

[The Token object](/api/tokens/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- cardnullable objectHash describing the card used to make the charge.Show child attributes

Hash describing the card used to make the charge.

- objectstring

- bank_accountnullable object

- client_ipnullable string

- createdtimestamp

- descriptionnullable string

- livemodeboolean

- typestring

- usedboolean

# Create an account token

[Create an account token](/api/tokens/create_account)

Creates a single-use token that wraps a user’s legal entity information. Use this when creating or updating a Connect account. Learn more about account tokens.

[account tokens](/connect/account-tokens)

In live mode, you can only create account tokens with your application’s publishable key. In test mode, you can only create account tokens with your secret key or publishable key.

- accountobjectRequiredInformation for the account this token represents.Show child parameters

Information for the account this token represents.

Returns the created account token if it’s successful. Otherwise, this call raises an error.

[an error](#errors)

# Create a bank account token

[Create a bank account token](/api/tokens/create_bank_account)

Creates a single-use token that represents a bank account’s details. You can use this token with any API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a Custom account.

[Custom account](#accounts)

- bank_accountobjectThe bank account this token will represent.Show child parameters

The bank account this token will represent.

- customerstringConnect only

Returns the created bank account token if it’s successful. Otherwise, this call raises an error.

[an error](#errors)

# Create a card token

[Create a card token](/api/tokens/create_card)

Creates a single-use token that represents a credit card’s details. You can use this token in place of a credit card dictionary with any API method. You can only use these tokens once by creating a new Charge object or by attaching them to a Customer object.

[creating a new Charge object](#create_charge)

[Customer object](#create_customer)

In most cases, you can use our recommended payments integrations instead of using the API.

[payments integrations](/payments)

- cardobject | stringThe card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user’s credit card details, with the options described below.Show child parameters

The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user’s credit card details, with the options described below.

Returns the created card token if it’s successful. Otherwise, this call raises an error.

[an error](#errors)

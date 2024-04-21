- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Create a CVC update token

[Create a CVC update token](/api/tokens/create_cvc_update)

Creates a single-use token that represents an updated CVC value that you can use for CVC re-collection. Use this token when you confirm a card payment or use a saved card on a PaymentIntent with confirmation_method: manual.

[CVC re-collection](/payments/accept-a-payment-synchronously#web-recollect-cvc)

[you confirm a card payment](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-cvc_token)

For most cases, use our JavaScript library instead of using the API. For a PaymentIntent with confirmation_method: automatic, use our recommended payments integration without tokenizing the CVC value.

[JavaScript library](/js/tokens/create_token?type=cvc_update)

[payments integration](/payments/save-during-payment#web-recollect-cvc)

- cvc_updateobjectRequiredThe updated CVC value this token represents.Show child parameters

The updated CVC value this token represents.

Returns the created CVC update token if it’s successful. Otherwise, this call raises an error.

[an error](#errors)

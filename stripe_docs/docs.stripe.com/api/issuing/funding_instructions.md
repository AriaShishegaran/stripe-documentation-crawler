- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Funding Instructions

[Funding Instructions](/api/issuing/funding_instructions)

Funding Instructions contain reusable bank account and routing information. Push funds to these addresses via bank transfer to top up Issuing Balances.

[top up Issuing Balances](/issuing/funding/balance)

[POST/v1/issuing/funding_instructions](/api/issuing/funding_instructions/create)

[GET/v1/issuing/funding_instructions](/api/issuing/funding_instructions/list)

[POST/v1/test_helpers/issuing/fund_balance](/api/issuing/funding_instructions/fund)

# The Funding Instruction object

[The Funding Instruction object](/api/issuing/funding_instructions/object)

- bank_transferobjectDetails to display instructions for initiating a bank transferShow child attributes

Details to display instructions for initiating a bank transfer

- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- funding_typeenumThe funding_type of the returned instructionsPossible enum valuesbank_transferUse a bank_transfer hash to define the bank transfer type

The funding_type of the returned instructions

Use a bank_transfer hash to define the bank transfer type

- objectstring

- livemodeboolean

# Create funding instructions

[Create funding instructions](/api/issuing/funding_instructions/create)

Create or retrieve funding instructions for an Issuing balance. If funding instructions don’t yet exist for the account, we’ll create new funding instructions. If we’ve already created funding instructions for the account, the same we’ll retrieve the same funding instructions. In other words, we’ll return the same funding instructions each time.

- bank_transferobjectRequiredAdditional parameters for bank_transfer funding typesShow child parameters

Additional parameters for bank_transfer funding types

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- funding_typeenumRequiredThe funding_type to get the instructions for.Possible enum valuesbank_transferUse a bank_transfer hash to define the bank transfer type

The funding_type to get the instructions for.

Use a bank_transfer hash to define the bank transfer type

Returns funding instructions for an Issuing balance

# List all funding instructions

[List all funding instructions](/api/issuing/funding_instructions/list)

Retrieve all applicable funding instructions for an Issuing balance.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

Returns all funding instructions for an Issuing balance

# Simulate a top upTest helper

[Simulate a top up](/api/issuing/funding_instructions/fund)

Simulates an external bank transfer and adds funds to an Issuing balance. This method can only be called in test mode.

- amountintegerRequiredThe amount to top up

The amount to top up

- currencyenumRequiredThe currency to top up

The currency to top up

Returns testmode funding instructions for an Issuing balance

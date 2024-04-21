# Required Verification Information for Taxes

Stripe recommends that you consult a tax advisor to determine your tax filing and reporting requirements.

## Required information (1099-K, 1099-MISC, 1099-NEC)

The following table lists the requirements for connected accounts with any of the 1099 capabilities. Stripe requires the business tax details except when the account is set up as a Single Person Entity (SPE) with a US-based representative, in which case we’ll use the representative’s personal tax details.

[1099 capabilities](/connect/account-capabilities#tax-reporting)

Stripe defines a Single Person Entity as follows:

- Individual: business type is individual

[business type](/api/accounts/object#account_object-business_type)

- Sole Proprietorship: business type is sole_prop, or business type is company and business structure is sole_proprietorship

[business type](/api/accounts/object#account_object-business_type)

[business type](/api/accounts/object#account_object-business_type)

[business structure](/api/accounts/create#create_account-company-structure)

- Single Member LLC: business type is company and business structure is single_member_llc

[business type](/api/accounts/object#account_object-business_type)

[business structure](/api/accounts/create#create_account-company-structure)

Even if you don’t add the 1099 capabilities and want to update the information directly in Stripe to file your 1099 forms, these are the fields to populate.

- individual.first_name

- individual.last_name

Address

individual.address

Required address fields are:

- individual.address.line1

[individual.address.line1](/api/accounts/update#update_account-individual-address-line1)

- individual.address.postal_code

[individual.address.postal_code](/api/accounts/update#update_account-individual-address-postal_code)

- individual.address.city

[individual.address.city](/api/accounts/update#update_account-individual-address-city)

- individual.address.state

[individual.address.state](/api/accounts/update#update_account-individual-address-state)

company.address

Required address fields are:

- company.address.line1

[company.address.line1](/api/accounts/update#update_account-company-address-line1)

- company.address.postal_code

[company.address.postal_code](/api/accounts/update#update_account-company-address-postal_code)

- company.address.city

[company.address.city](/api/accounts/update#update_account-company-address-city)

- company.address.state

[company.address.state](/api/accounts/update#update_account-company-address-state)

company.address

Required address fields are:

- company.address.line1

[company.address.line1](/api/accounts/update#update_account-company-address-line1)

- company.address.postal_code

[company.address.postal_code](/api/accounts/update#update_account-company-address-postal_code)

- company.address.city

[company.address.city](/api/accounts/update#update_account-company-address-city)

- company.address.state

[company.address.state](/api/accounts/update#update_account-company-address-state)

If you have any of the 1099 capabilities turned on, Payouts become disabled if the required information isn’t collected and verified by 600 USD in charges.

[Payouts](/payouts)

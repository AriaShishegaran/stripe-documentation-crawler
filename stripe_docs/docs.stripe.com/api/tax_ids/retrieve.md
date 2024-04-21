- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a tax ID

[Retrieve a tax ID](/api/tax_ids/retrieve)

Retrieves an account or customer tax_id object.

No parameters.

Returns a tax_id object if a valid identifier was provided.

# List all Customer tax IDs

[List all Customer tax IDs](/api/tax_ids/customer_list)

Returns a list of tax IDs for a customer.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty. Raises an error if the customer ID is invalid.

[an error](#errors)

# List all tax IDs

[List all tax IDs](/api/tax_ids/list)

Returns a list of tax IDs.

- ownerobjectThe account or customer the tax ID belongs to. Defaults to owner[type]=self.Show child parameters

The account or customer the tax ID belongs to. Defaults to owner[type]=self.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty.

# Delete a Customer tax ID

[Delete a Customer tax ID](/api/tax_ids/customer_delete)

Deletes an existing tax_id object.

No parameters.

Returns an object with a deleted parameter on success. If the tax_id object does not exist, this call raises an error.

[an error](#errors)

# Delete a tax ID

[Delete a tax ID](/api/tax_ids/delete)

Deletes an existing account or customer tax_id object.

No parameters.

Returns an object with a deleted parameter on success. If the tax_id object does not exist, this call raises an error.

[an error](#errors)

- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a Configuration

[Create a Configuration](/api/terminal/configuration/create)

Creates a new Configuration object.

- bbpos_wisepos_eobjectAn object containing device type specific settings for BBPOS WisePOS E readersShow child parameters

An object containing device type specific settings for BBPOS WisePOS E readers

- tippingobjectTipping configurations for readers supporting on-reader tipsShow child parameters

Tipping configurations for readers supporting on-reader tips

- verifone_p400objectAn object containing device type specific settings for Verifone P400 readersShow child parameters

An object containing device type specific settings for Verifone P400 readers

- namestring

- offlineobject

- stripe_s700objectPreview feature

Returns a Configuration object if creation succeeds.

# Update a Configuration

[Update a Configuration](/api/terminal/configuration/update)

Updates a new Configuration object.

- bbpos_wisepos_eobjectAn object containing device type specific settings for BBPOS WisePOS E readersShow child parameters

An object containing device type specific settings for BBPOS WisePOS E readers

- tippingobjectTipping configurations for readers supporting on-reader tipsShow child parameters

Tipping configurations for readers supporting on-reader tips

- verifone_p400objectAn object containing device type specific settings for Verifone P400 readersShow child parameters

An object containing device type specific settings for Verifone P400 readers

- namestring

- offlineobject

- stripe_s700objectPreview feature

Returns a Configuration object if the update succeeds.

# Retrieve a Configuration

[Retrieve a Configuration](/api/terminal/configuration/retrieve)

Retrieves a Configuration object.

No parameters.

Returns a Configuration object if a valid identifier was provided.

# List all Configurations

[List all Configurations](/api/terminal/configuration/list)

Returns a list of Configuration objects.

- is_account_defaultbooleanif present, only return the account default or non-default configurations.

if present, only return the account default or non-default configurations.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit configurations, starting after configurations configurations. Each entry in the array is a separate Terminal configurations object. If no more configurations are available, the resulting array will be empty.

# Delete a Configuration

[Delete a Configuration](/api/terminal/configuration/delete)

Deletes a Configuration object.

No parameters.

Returns the Configuration object that was deleted.

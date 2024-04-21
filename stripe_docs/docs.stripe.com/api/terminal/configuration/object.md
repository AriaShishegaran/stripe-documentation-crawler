- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Configuration object

[The Configuration object](/api/terminal/configuration/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- bbpos_wisepos_enullable objectAn object containing device type specific settings for BBPOS WisePOS EShow child attributes

An object containing device type specific settings for BBPOS WisePOS E

- is_account_defaultnullable booleanWhether this Configuration is the default for your account

Whether this Configuration is the default for your account

- tippingnullable objectOn-reader tipping settingsShow child attributes

On-reader tipping settings

- verifone_p400nullable objectAn object containing device type specific settings for Verifone P400Show child attributes

An object containing device type specific settings for Verifone P400

- objectstring

- livemodeboolean

- namenullable string

- offlinenullable object

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

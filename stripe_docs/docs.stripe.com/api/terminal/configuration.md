- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Configuration

[Configuration](/api/terminal/configuration)

A Configurations object represents how features should be configured for terminal readers.

[POST/v1/terminal/configurations](/api/terminal/configuration/create)

[POST/v1/terminal/configurations/:id](/api/terminal/configuration/update)

[GET/v1/terminal/configurations/:id](/api/terminal/configuration/retrieve)

[GET/v1/terminal/configurations](/api/terminal/configuration/list)

[DELETE/v1/terminal/configurations/:id](/api/terminal/configuration/delete)

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

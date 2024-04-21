- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Location

[Location](/api/terminal/locations)

A Location represents a grouping of readers.

Related guide: Fleet management

[Fleet management](/terminal/fleet/locations)

[POST/v1/terminal/locations](/api/terminal/locations/create)

[POST/v1/terminal/locations/:id](/api/terminal/locations/update)

[GET/v1/terminal/locations/:id](/api/terminal/locations/retrieve)

[GET/v1/terminal/locations](/api/terminal/locations/list)

[DELETE/v1/terminal/locations/:id](/api/terminal/locations/delete)

# The Location object

[The Location object](/api/terminal/locations/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- addressobjectThe full address of the location.Show child attributes

The full address of the location.

- display_namestringThe display name of the location.

The display name of the location.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- objectstring

- configuration_overridesnullable string

- livemodeboolean

# Create a Location

[Create a Location](/api/terminal/locations/create)

Creates a new Location object. For further details, including which address fields are required in each country, see the Manage locations guide.

[Manage locations](/terminal/fleet/locations)

- addressobjectRequiredThe full address of the location.Show child parameters

The full address of the location.

- display_namestringRequiredA name for the location.

A name for the location.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- configuration_overridesstring

Returns a Location object if creation succeeds.

# Update a Location

[Update a Location](/api/terminal/locations/update)

Updates a Location object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- addressobjectThe full address of the location.Show child parameters

The full address of the location.

- display_namestringA name for the location.

A name for the location.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- configuration_overridesstring

Returns an updated Location object if a valid identifier was provided.

# Retrieve a Location

[Retrieve a Location](/api/terminal/locations/retrieve)

Retrieves a Location object.

No parameters.

Returns a Location object if a valid identifier was provided.

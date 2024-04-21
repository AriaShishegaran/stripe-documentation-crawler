- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a Reader

[Retrieve a Reader](/api/terminal/readers/retrieve)

Retrieves a Reader object.

No parameters.

Returns a Reader object if a valid identifier was provided.

# List all Readers

[List all Readers](/api/terminal/readers/list)

Returns a list of Reader objects.

- device_typeenumFilters readers by device type

Filters readers by device type

- locationstringA location ID to filter the response list to only readers at the specific location

A location ID to filter the response list to only readers at the specific location

- serial_numberstringFilters readers by serial number

Filters readers by serial number

- statusenumA status filter to filter readers to only offline or online readers

A status filter to filter readers to only offline or online readers

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit readers, starting after reader starting_after. Each entry in the array is a separate Terminal Reader object. If no more readers are available, the resulting array will be empty.

# Delete a Reader

[Delete a Reader](/api/terminal/readers/delete)

Deletes a Reader object.

No parameters.

Returns the Reader object that was deleted.

# Cancel the current reader action

[Cancel the current reader action](/api/terminal/readers/cancel_action)

Cancels the current reader action.

No parameters.

Returns an updated Reader resource.

# Collect inputs using a ReaderPreview feature

[Collect inputs using a Reader](/api/terminal/readers/collect_inputs)

Initiates an input collection flow on a Reader.

- inputsarray of objectsRequiredList of inputs to be collected using the ReaderShow child parameters

List of inputs to be collected using the Reader

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an updated Reader resource.

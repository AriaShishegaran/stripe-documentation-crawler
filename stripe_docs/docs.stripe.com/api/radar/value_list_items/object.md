- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Value List Item object

[The Value List Item object](/api/radar/value_list_items/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- valuestringThe value of the item.

The value of the item.

- value_liststringThe identifier of the value list this item belongs to.

The identifier of the value list this item belongs to.

- objectstring

- createdtimestamp

- created_bystring

- livemodeboolean

# Create a value list item

[Create a value list item](/api/radar/value_list_items/create)

Creates a new ValueListItem object, which is added to the specified parent value list.

- valuestringRequiredThe value of the item (whose type must match the type of the parent value list).

The value of the item (whose type must match the type of the parent value list).

- value_liststringRequiredThe identifier of the value list which the created item will be added to.

The identifier of the value list which the created item will be added to.

Returns a ValueListItem object if creation succeeds.

# Retrieve a value list item

[Retrieve a value list item](/api/radar/value_list_items/retrieve)

Retrieves a ValueListItem object.

No parameters.

Returns a ValueListItem object if a valid identifier was provided.

# List all value list items

[List all value list items](/api/radar/value_list_items/list)

Returns a list of ValueListItem objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- value_liststringRequiredIdentifier for the parent value list this item belongs to.

Identifier for the parent value list this item belongs to.

- valuestringReturn items belonging to the parent list whose value matches the specified value (using an “is like” match).

Return items belonging to the parent list whose value matches the specified value (using an “is like” match).

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit items, starting after item starting_after. Each entry in the array is a separate ValueListItem object. If no more items are available, the resulting array will be empty.

# Delete a value list item

[Delete a value list item](/api/radar/value_list_items/delete)

Deletes a ValueListItem object, removing it from its parent value list.

No parameters.

Returns an object with the deleted ValueListItem object’s ID and a deleted parameter on success. Otherwise, this call raises an error.

[an error](#errors)

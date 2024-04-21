- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Secret object

[The Secret object](/api/apps/secret_store/secret_resource)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- deletednullable booleanIf true, indicates that this secret has been deleted

If true, indicates that this secret has been deleted

- expires_atnullable timestampThe Unix timestamp for the expiry time of the secret, after which the secret deletes.

The Unix timestamp for the expiry time of the secret, after which the secret deletes.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- namestringA name for the secret that’s unique within the scope.

A name for the secret that’s unique within the scope.

- payloadnullable stringExpandableThe plaintext secret value to be stored.

The plaintext secret value to be stored.

- scopeobjectSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child attributes

Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

# List secrets

[List secrets](/api/apps/secret_store/list)

List all secrets stored on the given scope.

- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit Secrets, starting after Secret starting_after. Each entry in the array is a separate Secret object. If no more Secrets are available, the resulting array will be empty.

# Delete a Secret

[Delete a Secret](/api/apps/secret_store/delete)

Deletes a secret from the secret store by name and scope.

- namestringRequiredA name for the secret that’s unique within the scope.

A name for the secret that’s unique within the scope.

- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Returns the deleted secret object.

# Find a Secret

[Find a Secret](/api/apps/secret_store/find)

Finds a secret in the secret store by name and scope.

- namestringRequiredA name for the secret that’s unique within the scope.

A name for the secret that’s unique within the scope.

- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Returns a secret object.

# Set a Secret

[Set a Secret](/api/apps/secret_store/set)

Create or replace a secret in the secret store.

- namestringRequiredA name for the secret that’s unique within the scope.

A name for the secret that’s unique within the scope.

- payloadstringRequiredThe plaintext secret value to be stored.

The plaintext secret value to be stored.

- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

- expires_attimestampThe Unix timestamp for the expiry time of the secret, after which the secret deletes.

The Unix timestamp for the expiry time of the secret, after which the secret deletes.

Returns a secret object.

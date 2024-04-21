- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Tax Registrations

[Tax Registrations](/api/tax/registrations)

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

[automatically collect tax](/tax)

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

[our guide](/tax/registering)

Related guide: Using the Registrations API

[Using the Registrations API](/tax/registrations-api)

[POST/v1/tax/registrations](/api/tax/registrations/create)

[POST/v1/tax/registrations/:id](/api/tax/registrations/update)

[GET/v1/tax/registrations/:id](/api/tax/registrations/retrieve)

[GET/v1/tax/registrations](/api/tax/registrations/all)

# The Tax Registration object

[The Tax Registration object](/api/tax/registrations/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- active_fromtimestampTime at which the registration becomes active. Measured in seconds since the Unix epoch.

Time at which the registration becomes active. Measured in seconds since the Unix epoch.

- countrystringTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- country_optionsobjectSpecific options for a registration in the specified country.Show child attributes

Specific options for a registration in the specified country.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- expires_atnullable timestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.

If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- statusenumThe status of the registration. This field is present for convenience and can be deduced from active_from and expires_at.Possible enum valuesactiveThe Tax Registration is currently active.expiredThe Tax Registration is no longer active.scheduledThe Tax Registration will become active in the future.

The status of the registration. This field is present for convenience and can be deduced from active_from and expires_at.

The Tax Registration is currently active.

The Tax Registration is no longer active.

The Tax Registration will become active in the future.

# Create a registration

[Create a registration](/api/tax/registrations/create)

Creates a new Tax Registration object.

- active_fromstring | timestampRequiredTime at which the Tax Registration becomes active. It can be either now to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.

Time at which the Tax Registration becomes active. It can be either now to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.

- countrystringRequiredTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- country_optionsobjectRequiredSpecific options for a registration in the specified country.Show child parameters

Specific options for a registration in the specified country.

- expires_attimestampIf set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.

If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.

A Tax Registration object.

# Update a registration

[Update a registration](/api/tax/registrations/update)

Updates an existing Tax Registration object.

A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.

- active_fromstring | timestampTime at which the registration becomes active. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

Time at which the registration becomes active. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

- expires_atstring | timestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

A Tax Registration object.

# Retrieve a registration

[Retrieve a registration](/api/tax/registrations/retrieve)

Returns a Tax Registration object.

No parameters.

A Tax Registration object.

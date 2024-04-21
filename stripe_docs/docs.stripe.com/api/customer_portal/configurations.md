- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Customer Portal Configuration

[Customer Portal Configuration](/api/customer_portal/configurations)

A portal configuration describes the functionality and behavior of a portal session.

[POST/v1/billing_portal/configurations](/api/customer_portal/configurations/create)

[POST/v1/billing_portal/configurations/:id](/api/customer_portal/configurations/update)

[GET/v1/billing_portal/configurations/:id](/api/customer_portal/configurations/retrieve)

[GET/v1/billing_portal/configurations](/api/customer_portal/configurations/list)

# The Customer portal configuration object

[The Customer portal configuration object](/api/customer_portal/configurations/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- activebooleanWhether the configuration is active and can be used to create portal sessions.

Whether the configuration is active and can be used to create portal sessions.

- applicationnullable stringExpandableConnect onlyID of the Connect Application that created the configuration.

ID of the Connect Application that created the configuration.

- business_profileobjectThe business information shown to customers in the portal.Show child attributes

The business information shown to customers in the portal.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- default_return_urlnullable stringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

[overriden](/api/customer_portal/sessions/create#create_portal_session-return_url)

- featuresobjectInformation about the features available in the portal.Show child attributes

Information about the features available in the portal.

- is_defaultbooleanWhether the configuration is the default. If true, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.

Whether the configuration is the default. If true, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.Show child attributes

The hosted login page for this configuration. Learn more about the portal login page in our integration docs.

[integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share)

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- updatedtimestampTime at which the object was last updated. Measured in seconds since the Unix epoch.

Time at which the object was last updated. Measured in seconds since the Unix epoch.

# Create a portal configuration

[Create a portal configuration](/api/customer_portal/configurations/create)

Creates a configuration that describes the functionality and behavior of a PortalSession

- business_profileobjectRequiredThe business information shown to customers in the portal.Show child parameters

The business information shown to customers in the portal.

- featuresobjectRequiredInformation about the features available in the portal.Show child parameters

Information about the features available in the portal.

- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

[overriden](/api/customer_portal/sessions/create#create_portal_session-return_url)

- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.Show child parameters

The hosted login page for this configuration. Learn more about the portal login page in our integration docs.

[integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a portal configuration object.

# Update a portal configuration

[Update a portal configuration](/api/customer_portal/configurations/update)

Updates a configuration that describes the functionality of the customer portal.

- activebooleanWhether the configuration is active and can be used to create portal sessions.

Whether the configuration is active and can be used to create portal sessions.

- business_profileobjectThe business information shown to customers in the portal.Show child parameters

The business information shown to customers in the portal.

- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

The default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.

[overriden](/api/customer_portal/sessions/create#create_portal_session-return_url)

- featuresobjectInformation about the features available in the portal.Show child parameters

Information about the features available in the portal.

- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.Show child parameters

The hosted login page for this configuration. Learn more about the portal login page in our integration docs.

[integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a portal configuration object.

# Retrieve a portal configuration

[Retrieve a portal configuration](/api/customer_portal/configurations/retrieve)

Retrieves a configuration that describes the functionality of the customer portal.

No parameters.

Returns a portal configuration object.

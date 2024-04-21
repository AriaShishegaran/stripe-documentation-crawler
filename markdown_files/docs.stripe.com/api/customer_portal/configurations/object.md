htmlThe Customer portal configuration object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Customer portal configuration object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- activebooleanWhether the configuration is active and can be used to create portal sessions.


- applicationnullablestringExpandableConnect onlyID of the Connect Application that created the configuration.


- business_profileobjectThe business information shown to customers in the portal.

Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- default_return_urlnullablestringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.


- featuresobjectInformation about the features available in the portal.

Show child attributes
- is_defaultbooleanWhether the configuration is the default. If true, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- updatedtimestampTime at which the object was last updated. Measured in seconds since the Unix epoch.



The Customer portal configuration object`{  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",  "object": "billing_portal.configuration",  "active": true,  "application": null,  "business_profile": {    "headline": null,    "privacy_policy_url": "https://example.com/privacy",    "terms_of_service_url": "https://example.com/terms"  },  "created": 1680290736,  "default_return_url": null,  "features": {    "customer_update": {      "allowed_updates": [        "email",        "tax_id"      ],      "enabled": true    },    "invoice_history": {      "enabled": true    },    "payment_method_update": {      "enabled": false    },    "subscription_cancel": {      "cancellation_reason": {        "enabled": false,        "options": [          "too_expensive",          "missing_features",          "switched_service",          "unused",          "other"        ]      },      "enabled": false,      "mode": "at_period_end",      "proration_behavior": "none"    },    "subscription_pause": {      "enabled": false    },    "subscription_update": {      "default_allowed_updates": [],      "enabled": false,      "proration_behavior": "none"    }  },  "is_default": false,  "livemode": false,  "login_page": {    "enabled": false,    "url": null  },  "metadata": {},  "updated": 1680290736}`# Create a portal configuration

Creates a configuration that describes the functionality and behavior of a PortalSession

### Parameters

- business_profileobjectRequiredThe business information shown to customers in the portal.

Show child parameters
- featuresobjectRequiredInformation about the features available in the portal.

Show child parameters
- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.


- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a portal configuration object.

POST/v1/billing_portal/configurationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/billing_portal/configurations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode "business_profile[privacy_policy_url]"="https://example.com/privacy" \  --data-urlencode "business_profile[terms_of_service_url]"="https://example.com/terms" \  -d "features[customer_update][allowed_updates][]"=email \  -d "features[customer_update][allowed_updates][]"=tax_id \  -d "features[customer_update][enabled]"=true \  -d "features[invoice_history][enabled]"=true`Response`{  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",  "object": "billing_portal.configuration",  "active": true,  "application": null,  "business_profile": {    "headline": null,    "privacy_policy_url": "https://example.com/privacy",    "terms_of_service_url": "https://example.com/terms"  },  "created": 1680290736,  "default_return_url": null,  "features": {    "customer_update": {      "allowed_updates": [        "email",        "tax_id"      ],      "enabled": true    },    "invoice_history": {      "enabled": true    },    "payment_method_update": {      "enabled": false    },    "subscription_cancel": {      "cancellation_reason": {        "enabled": false,        "options": [          "too_expensive",          "missing_features",          "switched_service",          "unused",          "other"        ]      },      "enabled": false,      "mode": "at_period_end",      "proration_behavior": "none"    },    "subscription_pause": {      "enabled": false    },    "subscription_update": {      "default_allowed_updates": [],      "enabled": false,      "proration_behavior": "none"    }  },  "is_default": false,  "livemode": false,  "login_page": {    "enabled": false,    "url": null  },  "metadata": {},  "updated": 1680290736}`# Update a portal configuration

Updates a configuration that describes the functionality of the customer portal.

### Parameters

- activebooleanWhether the configuration is active and can be used to create portal sessions.


- business_profileobjectThe business information shown to customers in the portal.

Show child parameters
- default_return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website. This can be overriden when creating the session.


- featuresobjectInformation about the features available in the portal.

Show child parameters
- login_pageobjectThe hosted login page for this configuration. Learn more about the portal login page in our integration docs.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a portal configuration object.

POST/v1/billing_portal/configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode "business_profile[privacy_policy_url]"="https://example.com/new_privacy_url" \  --data-urlencode "business_profile[terms_of_service_url]"="https://example.com/new_terms_of_service_url"`Response`{  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",  "object": "billing_portal.configuration",  "active": true,  "application": null,  "business_profile": {    "headline": null,    "privacy_policy_url": "https://example.com/new_privacy_url",    "terms_of_service_url": "https://example.com/new_terms_of_service_url"  },  "created": 1680290736,  "default_return_url": null,  "features": {    "customer_update": {      "allowed_updates": [        "email",        "tax_id"      ],      "enabled": true    },    "invoice_history": {      "enabled": true    },    "payment_method_update": {      "enabled": false    },    "subscription_cancel": {      "cancellation_reason": {        "enabled": false,        "options": [          "too_expensive",          "missing_features",          "switched_service",          "unused",          "other"        ]      },      "enabled": false,      "mode": "at_period_end",      "proration_behavior": "none"    },    "subscription_pause": {      "enabled": false    },    "subscription_update": {      "default_allowed_updates": [],      "enabled": false,      "proration_behavior": "none"    }  },  "is_default": false,  "livemode": false,  "login_page": {    "enabled": false,    "url": null  },  "metadata": {},  "updated": 1688593779}`# Retrieve a portal configuration

Retrieves a configuration that describes the functionality of the customer portal.

### Parameters

No parameters.

### Returns

Returns a portal configuration object.

GET/v1/billing_portal/configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",  "object": "billing_portal.configuration",  "active": true,  "application": null,  "business_profile": {    "headline": null,    "privacy_policy_url": "https://example.com/privacy",    "terms_of_service_url": "https://example.com/terms"  },  "created": 1680290736,  "default_return_url": null,  "features": {    "customer_update": {      "allowed_updates": [        "email",        "tax_id"      ],      "enabled": true    },    "invoice_history": {      "enabled": true    },    "payment_method_update": {      "enabled": false    },    "subscription_cancel": {      "cancellation_reason": {        "enabled": false,        "options": [          "too_expensive",          "missing_features",          "switched_service",          "unused",          "other"        ]      },      "enabled": false,      "mode": "at_period_end",      "proration_behavior": "none"    },    "subscription_pause": {      "enabled": false    },    "subscription_update": {      "default_allowed_updates": [],      "enabled": false,      "proration_behavior": "none"    }  },  "is_default": false,  "livemode": false,  "login_page": {    "enabled": false,    "url": null  },  "metadata": {},  "updated": 1680290736}`# List portal configurations

Returns a list of configurations that describe the functionality of the customer portal.

### Parameters

- activebooleanOnly return configurations that are active or inactive (e.g., pass true to only list active configurations).


- is_defaultbooleanOnly return the default or non-default configurations (e.g., pass true to only list the default configuration).



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

Returns a list of portal configuration objects.

GET/v1/billing_portal/configurationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/billing_portal/configurations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/billing_portal/configurations",  "has_more": false,  "data": [    {      "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",      "object": "billing_portal.configuration",      "active": true,      "application": null,      "business_profile": {        "headline": null,        "privacy_policy_url": "https://example.com/privacy",        "terms_of_service_url": "https://example.com/terms"      },      "created": 1680290736,      "default_return_url": null,      "features": {        "customer_update": {          "allowed_updates": [            "email",            "tax_id"          ],          "enabled": true        },        "invoice_history": {          "enabled": true        },        "payment_method_update": {          "enabled": false        },        "subscription_cancel": {          "cancellation_reason": {            "enabled": false,            "options": [              "too_expensive",              "missing_features",              "switched_service",              "unused",              "other"            ]          },          "enabled": false,          "mode": "at_period_end",          "proration_behavior": "none"        },        "subscription_pause": {          "enabled": false        },        "subscription_update": {          "default_allowed_updates": [],          "enabled": false,          "proration_behavior": "none"        }      },      "is_default": false,      "livemode": false,      "login_page": {        "enabled": false,        "url": null      },      "metadata": {},      "updated": 1680290736    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
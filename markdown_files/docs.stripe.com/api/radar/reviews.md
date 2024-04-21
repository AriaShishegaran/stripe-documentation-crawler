htmlReviews | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Reviews

Reviews can be used to supplement automated fraud detection with human expertise.

Learn more about Radar and reviewing payments here.

Endpoints
# The Review object

### Attributes

- idstringUnique identifier for the object.


- chargenullablestringExpandableThe charge associated with this review.


- openbooleanIf true, the review needs action.


- payment_intentnullablestringExpandableThe PaymentIntent ID associated with this review, if one exists.


- reasonstringThe reason the review is currently open or closed. One of rule, manual, approved, refunded, refunded_as_fraud, disputed, or redacted.



### More attributesExpand all

- objectstring
- billing_zipnullablestring
- closed_reasonnullableenum
- createdtimestamp
- ip_addressnullablestring
- ip_address_locationnullableobject
- livemodeboolean
- opened_reasonenum
- sessionnullableobject

The Review object`{  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",  "object": "review",  "billing_zip": null,  "charge": null,  "closed_reason": null,  "created": 1689864901,  "ip_address": null,  "ip_address_location": null,  "livemode": false,  "open": true,  "opened_reason": "rule",  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",  "reason": "rule",  "session": null}`# Retrieve a review

Retrieves a Review object.

### Parameters

No parameters.

### Returns

Returns a Review object if a valid identifier was provided.

GET/v1/reviews/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/reviews/prv_1NVyFt2eZvKYlo2CjubqF1xm \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",  "object": "review",  "billing_zip": null,  "charge": null,  "closed_reason": null,  "created": 1689864901,  "ip_address": null,  "ip_address_location": null,  "livemode": false,  "open": true,  "opened_reason": "rule",  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",  "reason": "rule",  "session": null}`# List all open reviews

Returns a list of Review objects that have open set to true. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit reviews, starting after review starting_after. Each entry in the array is a separate Review object. If no more reviews are available, the resulting array will be empty.

GET/v1/reviewsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/reviews \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/reviews",  "has_more": false,  "data": [    {      "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",      "object": "review",      "billing_zip": null,      "charge": null,      "closed_reason": null,      "created": 1689864901,      "ip_address": null,      "ip_address_location": null,      "livemode": false,      "open": true,      "opened_reason": "rule",      "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",      "reason": "rule",      "session": null    }    {...}    {...}  ],}`# Approve a review

Approves a Review object, closing it and removing it from the list of reviews.

### Parameters

No parameters.

### Returns

Returns the approved Review object.

POST/v1/reviews/:id/approveServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/reviews/prv_1NVyFt2eZvKYlo2CjubqF1xm/approve \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",  "object": "review",  "billing_zip": null,  "charge": null,  "closed_reason": null,  "created": 1689864901,  "ip_address": null,  "ip_address_location": null,  "livemode": false,  "open": true,  "opened_reason": "rule",  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",  "reason": "rule",  "session": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
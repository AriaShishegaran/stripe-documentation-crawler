- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Decline an authorization

[Decline an authorization](/api/issuing/authorizations/decline)

[Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the real time authorization flow. This method is deprecated. Instead, respond directly to the webhook request to decline an authorization.

[real time authorization](/issuing/controls/real-time-authorizations)

[respond directly to the webhook request to decline an authorization](/issuing/controls/real-time-authorizations#authorization-handling)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a declined Issuing Authorization object.

# Create a test-mode authorizationTest helper

[Create a test-mode authorization](/api/issuing/authorizations/test_mode_create)

Create a test-mode authorization.

- amountintegerRequiredThe total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card’s currency, and in the smallest currency unit.

The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card’s currency, and in the smallest currency unit.

[smallest currency unit](/currencies#zero-decimal)

- cardstringRequiredCard associated with this authorization.

Card associated with this authorization.

- currencyenumThe currency of the authorization. If not provided, defaults to the currency of the card. Three-letter ISO currency code, in lowercase. Must be a supported currency.

The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- amount_detailsobject

- authorization_methodenum

- is_amount_controllableboolean

- merchant_dataobject

- network_dataobject

- verification_dataobject

- walletenum

An Authorization object

# Capture a test-mode authorizationTest helper

[Capture a test-mode authorization](/api/issuing/authorizations/test_mode_capture)

Capture a test-mode authorization.

- capture_amountintegerThe amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the smallest currency unit.

The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the smallest currency unit.

[smallest currency unit](/currencies#zero-decimal)

- close_authorizationbooleanWhether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.

Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.

- purchase_detailsobjectAdditional purchase information that is optionally provided by the merchant.Show child parameters

Additional purchase information that is optionally provided by the merchant.

An Authorization object.

# Expire a test-mode authorizationTest helper

[Expire a test-mode authorization](/api/issuing/authorizations/test_mode_expire)

Expire a test-mode Authorization.

No parameters.

An Authorization object

# Increment a test-mode authorizationTest helper

[Increment a test-mode authorization](/api/issuing/authorizations/test_mode_increment)

Increment a test-mode Authorization.

- increment_amountintegerRequiredThe amount to increment the authorization by. This amount is in the authorization currency and in the smallest currency unit.

The amount to increment the authorization by. This amount is in the authorization currency and in the smallest currency unit.

[smallest currency unit](/currencies#zero-decimal)

- is_amount_controllablebooleanIf set true, you may provide amount to control how much to hold for the authorization.

If set true, you may provide amount to control how much to hold for the authorization.

[amount](/api/issuing/authorizations/approve#approve_issuing_authorization-amount)

An Authorization object

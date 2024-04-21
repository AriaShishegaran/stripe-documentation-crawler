htmlConnect OAuth reference | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foauth-reference)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foauth-reference)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Connect OAuth reference

This reference lists available public methods for our OAuth endpoints for Connect.### Account types

Connect platforms can work with three different account types.

The content on this page applies only to Standard accounts.

The OAuth Connect flow allows you to customize the user’s experience by passing additional parameters to Stripe. Some common examples are explained below, and the rest of the reference lists every possible option.

NoteAs a platform, remember that data you create for a Standard account (that is, charges, customers, invoices, and so on) will be visible on their Stripe account. This also means if they connect other platforms, those platforms will have access to that data too.

Starting in June 2021, Platforms using OAuth with read_write scope won’t be able to connect to accounts that are controlled by another platform.

Extensions won’t experience any changes to how OAuth behaves. Learn more about OAuth changes for Standard Platforms.

## Common examples

### Prefill fields

Provide the best possible user experience for users who need to create a new Stripe account by prefilling the account form fields with information you already have, like the user’s email and name. Prefilling has no effect if your user already has a Stripe account. You can’t prefill certain fields, including terms of service acceptance and RISA acceptance in Japan.

### Dynamically set the redirect URI

For security purposes, Stripe redirects a user only to a predefined URI. However, Connect allows you to define more than one redirect URI, which you can use to further customize the user’s experience. For example, you could redirect some of your users back to https://sub1.example.com and others to https://sub2.example.com.

To dynamically set the redirect URI:

1. In your[platform settings](https://dashboard.stripe.com/account/applications/settings), add each redirect URI.
2. Add a`redirect_uri`parameter to your authorization request and set the value to one of your redirect URIs.

`https://connect.stripe.com/oauth/authorize?response_type=code&client_id={{CLIENT_ID}}&scope=read_write&redirect_uri=https://sub2.example.com`If no redirect_uri is specified in the URL, then Stripe uses the first URI configured in your platform settings.

## Authorize the account

For Standard accounts: GET https://connect.stripe.com/oauth/authorize

Sends the user to Stripe to connect to your platform.

### Request

ParameterDescription`client_id`The unique identifier provided to your application, found in your[application settings](https://dashboard.stripe.com/account/applications/settings).`response_type`The only option at the moment iscode.`redirect_uri`OptionalThe URL for the authorize[response](#get-authorize-response)redirect. If provided, this must exactly match one of the comma-separated`redirect_uri`values in your[application settings](https://dashboard.stripe.com/account/applications/settings). To protect yourself from certain forms of man-in-the-middle attacks, the live mode`redirect_uri`must use a secure HTTPS connection. Defaults to the`redirect_uri`in your application settings if not provided.`scope`OptionalStandard Onlyread_writeorread_only, depending on the level of access you need. Defaults toread_onlyfor Standard accounts.`state`OptionalAn arbitrary string value we’ll pass back to you, useful for CSRF protection.The following query string parameters are all optional—we use them to prefill details in the account form for new users. Some prefilled fields (for example, URL or product category) might be automatically hidden. Any parameters with invalid values are silently ignored.

Note that some of these parameters apply only to Standard accounts (indicated).

ParameterDescription`stripe_user[email]`RecommendedThe user’s email address. Must be a valid email format.`stripe_user[url]`RecommendedThe URL for the user’s business. This may be the user’s website, a profile page within your application, or another publicly available profile for the business, such as a LinkedIn or Facebook profile. It must be URL-encoded and include a scheme (httporhttps). If you prefill this field, include a description of the user’s products or services and their contact information in the linked page. If we don’t have enough information, we’ll have to reach out to the user directly before initiating payouts.`stripe_user[country]`Two-letter country code (for example,USorCA). Must be a country that Stripe currently supports.`stripe_user[phone_number]`The business phone number. Must be 10 digits only. Must also prefill`stripe_user[country]`with the corresponding country.`stripe_user[business_name]`The legal name of the business.`stripe_user[business_type]`The type of the business.For Standard accounts, the value must besole_prop,corporation,non_profit,partnership, orllc.`stripe_user[first_name]`First name of the person filling out a Stripe application.`stripe_user[last_name]`Last name of the person filling out a Stripe application.`stripe_user[dob_day]``stripe_user[dob_month]``stripe_user[dob_year]`Day (0-31), month (1-12), and year (YYYY, greater than 1900) for the birth date of the person filling out a Stripe application. If you choose to pass these parameters, you must pass all three.`stripe_user[street_address]`Standard onlyStreet address of the business.`stripe_user[city]`Standard onlyAddress city of the business. To prevent ambiguity, also prefill`stripe_user[country]`with the corresponding country.`stripe_user[state]`Standard onlyAddress state of the business. Must be the two-letter state or province code (for example,NYfor a US business orABfor a Canadian one). Must also prefill`stripe_user[country]`with the corresponding country.`stripe_user[zip]`Standard onlyAddress postal code of the business. Must be a string. To prevent ambiguity, also prefill`stripe_user[country]`with the corresponding country.`stripe_user[physical_product]`Standard onlyA string:trueif the user sells a physical product,falseotherwise.`stripe_user[product_description]`A description of what the business is accepting payments for.`stripe_user[currency]`Standard onlyThree-letter[ISO code](http://en.wikipedia.org/wiki/ISO_4217)representing currency, in lowercase (for example,usdorcad). Must be a valid country and currency combination that Stripe supports. Must prefill`stripe_user[country]`with the corresponding country.`stripe_user[first_name_kana]`The Kana variation of the first name of the person filling out a Stripe application. Must prefill`stripe_user[country]`withJP, as this parameter is only relevant for Japan.`stripe_user[first_name_kanji]`The Kanji variation of the first name of the person filling out a Stripe application. Must prefill`stripe_user[country]`withJP, as this parameter is only relevant for Japan.`stripe_user[last_name_kana]`The Kana variation of the last name of the person filling out a Stripe application. Must prefill`stripe_user[country]`withJP, as this parameter is only relevant for Japan.`stripe_user[last_name_kanji]`The Kanji variation of the last name of the person filling out a Stripe application. Must prefill`stripe_user[country]`withJP, as this parameter is only relevant for Japan.`stripe_user[gender]`The gender of the person filling out a Stripe application. (International regulations require eithermaleorfemale.) Must prefill`stripe_user[country]`withJP, as this parameter is only relevant for Japan.`stripe_user[block_kana]`Standard onlyThe Kana variation of the address block. This parameter is only relevant for Japan. You must prefill`stripe_user[country]`withJPand`stripe_user[zip]`with a valid Japanese postal code to use this parameter.`stripe_user[block_kanji]`Standard onlyThe Kanji variation of the address block. This parameter is only relevant for Japan. You must prefill`stripe_user[country]`withJPand`stripe_user[zip]`with a valid Japanese postal code to use this parameter.`stripe_user[building_kana]`Standard onlyThe Kana variation of the address building. This parameter is only relevant for Japan. You must prefill`stripe_user[country]`withJPand`stripe_user[zip]`with a valid Japanese postal code to use this parameter.`stripe_user[building_kanji]`Standard onlyThe Kanji variation of the address building. This parameter is only relevant for Japan. You must prefill`stripe_user[country]`withJPand`stripe_user[zip]`with a valid Japanese postal code to use this parameter.### Response

The user’s browser is redirected back to your configured redirect URI or the value you passed in the redirect_uri parameter. When successful, you receive the following query parameters:

ParameterDescription`code`An authorization code you can use in the next call to get an access token for your user. This can only be used once and expires in 5 minutes.`scope`read_writeorread_only, depending what you passed on the initial GET request.`state`The value of the`state`parameter you provided on the initial GET request.### Error Response

In case of an error, the user’s browser won’t be redirected except in the case of access_denied. Instead, errors will be returned in a JSON dictionary with the following fields:

ParameterDescription`error`A unique[error code](#get-authorize-error-codes)per error type.`error_description`A human readable description of the error.`state`The value of the`state`parameter you provided on the initial GET request.### Error Codes

ParameterDescription`access_denied`User denied authorization.`invalid_scope`Invalid`scope`parameter provided.`invalid_redirect_uri`Provided`redirect_uri`parameter is an invalid URL or isn’t allowed by your[application settings](https://dashboard.stripe.com/account/applications/settings).`invalid_request`Missing`response_type`parameter.`unsupported_response_type`Unsupported`response_type`parameter. Currently the only supported`response_type`iscode.## Complete the connection and get the account ID

POST https://connect.stripe.com/oauth/token

Used both for turning an authorization_code into an account connection, and for getting a new access token using a refresh_token.

### Request

Make this call using your secret API key as a client_secret POST parameter:

Command Line[curl](#)`curl https://connect.stripe.com/oauth/token \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "code"="ac_123456789" \
  -d "grant_type"="authorization_code"`When converting an authorization code to an access token, you must use an API key that matches the mode—live or test—of the authorization code (which depends on whether the client_id used was production or development).

When using a refresh token to request an access token, you may use either a test or live API key to obtain a test or live access token respectively. Any existing access token with the same scope and mode—live or test—is revoked.

NotePer OAuth v2, this endpoint isn’t idempotent. Consuming an authorization code more than once revokes the account connection.

ParameterDescription`grant_type`authorization_codewhen turning an authorization code into an access token, orrefresh_tokenwhen using a refresh token to get a new access token.`code`or`refresh_token`The value of the`code`or`refresh_token`, depending on the`grant_type`.`scope`OptionalWhen requesting a new access token from a refresh token, any scope that has an equal or lesser scope as the refresh token. Has no effect when requesting an access token from an authorization code. Defaults to the scope of the refresh token.### Response

ParameterDescription`scope`The scope granted to the access token, depending on the scope of the authorization code and`scope`parameter.`stripe_user_id`The unique ID of the account you have been granted access to, as a string.`livemode`Indicates whether the platform’s access to perform updates on behalf of the connected account includes livemode access, or is limited to testmode actions. This matches the livemode of the application used[to authorize the OAuth request](#get-authorize).`token_type`Always has a value ofbearer.`access_token`DeprecatedUse the`Stripe-Account`[header](/connect/authentication#stripe-account-header)with your platform’s secret key (that can make requests on behalf of this Stripe account).`stripe_publishable_key`DeprecatedUse the`Stripe-Account`[header](/connect/authentication#stripe-account-header)with your platform’s publishable key (that can make requests on behalf of this Stripe account).`refresh_token`DeprecatedCan be used to get a new access token of an equal or lesser scope, or of a different live mode (where[applicable](/connect/testing#creating-accounts)).### Error Response

ParameterDescription`error`A unique[error code](#post-token-error-codes)per error type.`error_description`A human readable description of the error.### Error Codes

ParameterDescription`invalid_request`No`code`,`refresh_token`, or`grant_type`parameter provided (where required).`invalid_grant`A variety of things can prompt this error:- `code`doesn’t exist, is expired, has been used, or doesn’t belong to you
- `refresh_token`doesn’t exist or doesn’t belong to you
- API key mode (live or test mode) doesn’t match the`code`or`refresh_token`mode

`unsupported_grant_type`Unsupported`grant_type`parameter specified. The only currently supported types areauthorization_codeandrefresh_token.`invalid_scope`Invalid`scope`parameter provided.`unsupported_response_type`Unsupported`response_type`parameter. Currently the only supported`response_type`iscode.APIDashboard## Revoke the account’s access

POST https://connect.stripe.com/oauth/deauthorize

Used for revoking access to an account.

NoteYou can only revoke a Standard account’s access to your platform.

### Request

Make this call using your secret API key as an Authorization header.

Command Line[curl](#)`curl https://connect.stripe.com/oauth/deauthorize \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d client_id="ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb" \
  -d stripe_user_id=acct_ON3nXtRQkhmUIQ`When revoking access to an account, you must use an API key that matches the mode — live or test — used to connect to the account. Use a live mode API key if a production client_id created the connection, or a test mode API key for a development client_id.

ParameterDescription`client_id`The`client_id`of the application that you’d like to disconnect the account from. The account must be connected to this application.`stripe_user_id`The account you’d like to disconnect from.### Response

ParameterDescription`stripe_user_id`The unique ID of the account you have revoked access to, as a string. This is the same as the`stripe_user_id`you passed in. If this is returned, the revocation is successful.### Error Response

ParameterDescription`error`A unique[error code](#post-deauthorize-error-codes)per error type.`error_description`A human readable description of the error.### Error Codes

ParameterDescription`invalid_request`No`client_id`or`stripe_user_id`parameter provided (where required).`invalid_client`A variety of things can prompt this error:- `client_id`doesn’t belong to you
- `stripe_user_id`doesn’t exist or isn’t connected to your application
- API key mode (live or test mode) doesn’t match the`client_id`mode
- `no_deauth_on_controlled_account`the account can’t be disconnected and instead use the[rejection API](/api/account/reject).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Common examples](#common-examples)[Authorize the account](#get-authorize)[Complete the connection and get the account ID](#post-token)[Revoke the account’s access](#post-deauthorize)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
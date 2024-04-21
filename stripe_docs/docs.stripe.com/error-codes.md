# Error codes

Stripe logs every successful or failed API request your integration makes. Use the Developers section of the Dashboard to review errors and monitor your integration.

[Developers](https://dashboard.stripe.com/developers)

Some Errors include an error code—a short string with a brief explanation. These codes play a role in our recommended error handling techniques. See the documentation on payment errors for an example.

[Errors](/api/errors)

[error code](/api/errors#errors-code)

[our recommended error handling techniques](/error-handling)

[payment errors](/error-handling#payment-errors)

Below is a list of possible error codes, along with additional information about how to resolve them. For convenience, every Error object links to this list in its doc_url attribute.

[doc_url](/api/errors#errors-doc_url)

You can also trigger some specific error codes for test purposes.

[trigger some specific error codes](/testing#declined-payments)

The customer’s bank account has been closed.

The country of the business address provided does not match the country of the account. Businesses must be located in the same country as the account.

Your account has already onboarded as a Connect platform. Changing your country requires additional steps. Please reach out to Stripe support for more information.

Some account information mismatches with one another. For example, some banks might require that the business_profile.name must match the account holder name.

The account ID provided as a value for the Stripe-Account header is invalid. Check that your requests are specifying a valid account ID.

The bank account number provided is invalid (e.g., missing digits). Bank account information varies from country to country. We recommend creating validations in your entry forms based on the bank account formats we provide.

[bank account formats](/connect/payouts-bank-accounts)

The ACSS debit session is not ready to transition to complete status yet. Please try again the request later.

This method for creating Alipay payments is not supported anymore. Please upgrade your integration to use Sources instead.

[Sources](https://stripe.com/docs/sources/alipay)

The specified amount is greater than the maximum amount allowed. Use a lower amount and try again.

The specified amount is less than the minimum amount allowed. Use a higher amount and try again.

The API key provided has expired. Obtain your current API keys from the Dashboard and update your integration to use them.

[Dashboard](https://dashboard.stripe.com/account/apikeys)

The proposed money movement could not be completed due to regulatory reasons.

The payment requires authentication to proceed. If your customer is off session, notify your customer to return to your application and complete the payment. If you provided the error_on_requires_action parameter, then your customer should try another card that does not require authentication.

[off session](/api/payment_intents/confirm#confirm_payment_intent-off_session)

[error_on_requires_action](/payments/without-card-authentication)

The transfer or payout could not be completed because the associated account does not have a sufficient balance available. Create a new transfer or payout using an amount less than or equal to the account’s available balance.

Invalid parameter was provided in the balance method object. Check our API documentation or the returned error message for more context.

The bank account is known to not support the currency in question.

The bank account provided can not be used to charge, either because it is not verified yet or it is not supported.

The bank account provided already exists on the specified Customer object. If the bank account should also be attached to a different customer, include the correct customer ID when making the request again.

[Customer](/api#update_customer-source)

The customer’s account cannot be used with the payment method.

The bank account provided cannot be used. A different bank account must be used.

Your Connect platform is attempting to share an unverified bank account with a connected account.

The bank account cannot be verified, either because the microdeposit amounts provided do not match the actual amounts, or because verification has failed too many times.

The Subscription or Invoice attempted payment on a PaymentMethod without an active mandate. In order to create Subscription or Invoice payments with this PaymentMethod, it must be confirmed on-session with a PaymentIntent or SetupIntent first.

A billing policy remote function endpoint response returned invalid data.

A billing policy remote function timed out.

A billing policy remote function returned an invalid status code.

There was an error while executing a billing policy remote function.

This method for creating Bitcoin payments is not supported anymore. Please upgrade your integration to use Sources instead.

[Sources](https://stripe.com/docs/sources)

The charge cannot be captured as the authorization has expired. Refer to the payment method’s documentation to learn more.

[captured](/charges/placing-a-hold)

The charge you’re attempting to capture has not been authorized for capturing payment.

[capture](/charges/placing-a-hold)

This card has been declined too many times. You can try to charge this card again after 24 hours. We suggest reaching out to your customer to make sure they have entered all of their information correctly and that there are no issues with their card.

The card has been declined. When a card is declined, the error returned also includes the decline_code attribute with the reason why the card was declined. Refer to our decline codes documentation to learn more.

[decline codes](/declines/codes)

You must have a phone_number on file for Issuing Cardholders who will be creating EU cards. You cannot create EU cards without a phone_number on file for the cardholder. See the 3D Secure Documenation for more details.

[3D Secure Documenation](/issuing/3d-secure)

The charge you’re attempting to capture has already been captured. Update the request with an uncaptured charge ID.

[capture](/charges/placing-a-hold)

The charge you’re attempting to refund has already been refunded. Update the request to use the ID of a charge that has not been refunded.

[refund](/refunds)

The charge you’re attempting to refund has been charged back. Check the disputes documentation to learn how to respond to the dispute.

[refund](/refunds)

[disputes documentation](/disputes)

This charge would cause you to exceed your rolling-window processing limit for this source type. Please retry the charge later, or contact us to request a higher processing limit.

[contact us](https://support.stripe.com/email)

The charge cannot be captured as the authorization has expired. Auth and capture charges must be captured within a set number of days (7 by default).

[captured within a set number of days](/charges/placing-a-hold)

One or more provided parameters was not allowed for the given operation on the Charge. Check our API reference or the returned error message to see which values were not correct for that Charge.

[API reference](/api/charges)

Attempt to refund a charge was unsuccessful because the charge is no longer refundable.

The clearing code provided is not supported.

The country code provided was invalid.

Your platform attempted to create a custom account in a country that is not yet supported. Make sure that users can only sign up in countries supported by custom accounts.

[countries supported by custom accounts](/connect/custom-accounts#country)

The coupon provided for a subscription or order has expired. Either create a new coupon, or use an existing one that is valid.

[coupon](/api#coupons)

[subscription](/api#subscriptions)

[order](/api#orders)

The maximum number of PaymentMethods for this Customer has been reached. Either detach some PaymentMethods from this Customer or proceed with a different Customer.

[PaymentMethods](/api/payment_methods)

[Customer](/api/customers)

[detach](/api/payment_methods/detach)

The maximum number of subscriptions for a customer has been reached. Contact us if you are receiving this error.

[Contact us](https://support.stripe.com/email)

The customer location information cannot be used to accurately determine tax rates. Verify that address fields such as country, state, and postal code have been added correctly. See the supported address formats.

[supported address formats](/tax/customer-locations#supported-formats)

The customer has notified their bank that this payment was unauthorized.

The email address is invalid (e.g., not properly formatted). Check that the email address is properly formatted and only includes allowed characters.

[allowed characters](https://en.wikipedia.org/wiki/Email_address#Local-part)

The card has expired. Check the expiration date or use a different card.

Data cannot be refreshed on inactive Financial Connections accounts.

Transaction data can only be retrieved for accounts that have at least one successful transaction refresh.

The vault and forward API is currently not accessible with this account and/or config. Please contact us if you are receiving this error.

[contact us](https://support.stripe.com/contact)

Invalid parameter was provided in the vault and forward API. Check our API documentation or the returned error message for more context.

Stripe did not receive a response from the destination endpoint.

The request to the destination endpoint timed out.

The idempotency key provided is currently being used in another request. This occurs if your integration is making duplicate requests simultaneously.

The card’s address is incorrect. Check the card’s address or use a different card.

The card’s security code is incorrect. Check the card’s security code or use a different card.

The card number is incorrect. Check the card’s number or use a different card.

The card’s postal code is incorrect. Check the card’s postal code or use a different card.

This connected account is not eligible for Instant Payouts. Ask the platform to enable Instant Payouts.

This connected account is not eligible for Instant Payouts in this currency. Ask the platform to enable Instant Payouts in this currency.

You have reached your daily processing limits for Instant Payouts.

This card is not eligible for Instant Payouts. Try a debit card from a supported bank.

[supported bank](https://stripe.com/docs/payouts/instant-payouts-banks)

The customer’s account has insufficient funds to cover this payment.

Intent is not in the state that is required to perform the operation.

Intent does not have verification method specified in its PaymentMethodOptions object.

The card provided as an external account is not supported for payouts. Provide a non-prepaid debit card instead.

[external account](https://stripe.com/docs/api#external_accounts)

This value provided to the field contains characters that are unsupported by the field.

The specified amount is invalid. The charge amount must be a positive integer in the smallest currency unit, and not exceed the minimum or maximum amount.

[charge amount](/api#create_charge-amount)

[minimum or maximum amount](/currencies#minimum-and-maximum-charge-amounts)

The card’s security code is invalid. Check the card’s security code or use a different card.

The card’s expiration month is incorrect. Check the expiration date or use a different card.

The card’s expiration year is incorrect. Check the expiration date or use a different card.

The card number is invalid. Check the card details or use a different card.

The source cannot be used because it is not in the correct state (e.g., a charge request is trying to use a source with a pending, failed, or consumed source). Check the status of the source you are attempting to use.

[status](/api#source_object-status)

The specified location is invalid. Check the Supported address formats for the address formats supported when calculating tax.

[Supported address formats](/tax/customer-locations#supported-formats)

An invoice cannot be generated for the specified customer as there are no pending invoice items. Check that the correct customer is being specified or create any necessary invoice items first.

An invoice cannot be finalized because there are no payment method types available to process the payment. Your invoice template settings or the invoice’s payment_settings might be restricting which payment methods are available, or you might need to activate more payment methods in the Dashboard.

[invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)

[payment_settings](/api/invoices/object#invoice_object-payment_settings)

[payment methods](https://dashboard.stripe.com/settings/payments)

An invoice cannot be generated for the specified subscription as there are no pending invoice items. Check that the correct subscription is being specified or create any necessary invoice items first.

The specified invoice can no longer be edited. Instead, consider creating additional invoice items that will be applied to the next invoice. You can either manually generate the next invoice or wait for it to be automatically generated at the end of the billing cycle.

[invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

[manually generate](/billing/invoices/subscription#generating-invoices)

You cannot update the on_behalf_of property of an invoice after the invoice has been assigned a number.

This payment requires additional user action before it can be completed successfully. Payment can be completed using the PaymentIntent associated with the invoice. See this page for more details.

[this page](https://stripe.com/docs/billing/subscriptions/payment#handling-action-required)

There is no upcoming invoice on the specified customer to preview. Only customers with active subscriptions or pending invoice items have invoices that can be previewed.

Test and live mode API keys, requests, and objects are only available within the mode they are in.

This object cannot be accessed right now because another API request or Stripe process is currently accessing it. If you see this error intermittently, retry the request. If you see this error frequently and are making multiple concurrent requests to a single object, make your requests serially or at a lower rate. See the rate limit documentation for more details.

[rate limit documentation](/rate-limits#object-lock-timeouts)

Both a customer and source ID have been provided, but the source has not been saved to the customer. To create a charge for a customer with a specified source, you must first save the card details.

[save the card details](/saving-cards)

The bank account could not be located.

Transfers and payouts on behalf of a Standard connected account are not allowed.

One or more line item(s) are out of stock. If more stock is available, update the inventory’s orderable quantity and try again.

Company ownership declaration is allowed only during account updates and accounts created via account tokens.

One or more required values were not provided. Make sure requests include all required parameters.

One or more of the parameters requires an integer, but the values provided were a different type. Make sure that only supported values are provided for each attribute. Refer to our API documentation to look up the type of data each attribute supports.

[API documentation](https://stripe.com/docs/api)

One or more values provided only included whitespace. Check the values in your request and update any that contain only whitespace.

One or more required string values is empty. Make sure that string values contain at least one character.

One or more required values are missing. Check our API documentation to see which values are required to create or modify the specified resource.

[API documentation](/api)

The request contains one or more unexpected parameters. Remove these and try again.

Two or more mutually exclusive parameters were provided. Check our API documentation or the returned error message to see which values are permitted when creating or modifying the specified resource.

[API documentation](/api)

The provided payment method requires customer actions to complete, but error_on_requires_action was set. If you’d like to add this payment method to your integration, we recommend that you first upgrade your integration to handle actions.

[upgrade your integration to handle actions](/payments/payment-intents/upgrade-to-handle-actions)

The provided payment method has failed authentication. Provide a new payment method to attempt to fulfill this PaymentIntent again.

The PaymentIntent expected a payment method with different properties than what was provided.

One or more provided parameters was not allowed for the given operation on the PaymentIntent. Check our API reference or the returned error message to see which values were not correct for that PaymentIntent.

[API reference](/api/payment_intents)

The confirmation_number provided in payment_method_options[konbini] was rejected by the processing partner at time of PaymentIntent confirmation.

The provided mandate is invalid and can not be used for the payment intent.

The latest payment attempt for the PaymentIntent has expired. Check the last_payment_error property on the PaymentIntent for more details, and provide a new payment method to attempt to fulfill this PaymentIntent again.

[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)

The latest payment attempt for the PaymentIntent has failed. Check the last_payment_error property on the PaymentIntent for more details, and provide a new payment method to attempt to fulfill this PaymentIntent again.

[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)

The PaymentIntent’s state was incompatible with the operation you were trying to perform.

This bank account has already been verified.

This bank account has failed verification in the past and can not be used. Contact us if you wish to attempt to use these bank account credentials.

[Contact us](https://support.stripe.com/email)

The PaymentMethod’s billing details is missing address details. Please update the missing fields and try again.

Attempt to create or modify Payment Method Configuration was unsuccessful.

The currency specified does not match the currency for the attached payment method. A payment can only be created for the same currency as the corresponding payment method.

The customer did not approve the payment. Please provide a new payment method to attempt to fulfill this intent again.

Invalid parameter was provided in the payment method object. Check our API documentation or the returned error message for more context.

[API documentation](/api)

The parameter provided for payment method is not allowed to be used in testmode. Check our API documentation or the returned error message for more context.

[API documentation](/api)

Microdeposits were failed to be deposited into the customer’s bank account. Please check the account, institution and transit numbers as well as the currency type.

You must provide exactly two microdeposit amounts.

The amounts provided do not match the amounts that were sent to the bank account.

You have exceeded the number of allowed verification attempts.

The verification code provided does not match the one sent to the bank account.

Payment method should be verified with microdeposits within the required period.

The payment processor for the provided payment method is temporarily unavailable. Please try a different payment method or retry later with the same payment method.

The payment or setup attempt was declined by the issuer or customer. Check the last_payment_error or last_setup_error property on the PaymentIntent or SetupIntent respectively for more details, and provide a new payment method to attempt to fulfill this intent again.

[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)

[last_setup_error](/api/setup_intents/object#setup_intent_object-last_setup_error)

The payment method failed due to a timeout. Check the last_payment_error or last_setup_error property on the PaymentIntent or SetupIntent respectively for more details, and provide a new payment method to attempt to fulfill this intent again.

[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)

[last_setup_error](/api/setup_intents/object#setup_intent_object-last_setup_error)

The operation cannot be performed as the payment method used has not been activated. Activate the payment method in the Dashboard, then try again.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

The provided payment method’s state was incompatible with the operation you were trying to perform. Confirm that the payment method is in an allowed state for the given operation before attempting to perform it.

The API only supports payment methods of certain types.

Reconciliation for this payout is still in progress.

You have reached your daily processing limits for this payout type.

Payouts have been disabled on the connected account. Check the connected account’s status to see if any additional information needs to be provided, or if payouts have been disabled for another reason.

[additional information](/connect/identity-verification)

[another reason](/connect/handling-api-verification#determining-if-identity-verification-is-needed)

Only Stripe Connect platforms can work with other accounts. If you need to setup a Stripe Connect platform, you can do so in the dashboard.

[in the dashboard](https://dashboard.stripe.com/account/applications/settings)

The API key provided by your Connect platform has expired. This occurs if your platform has either generated a new key or the connected account has been disconnected from the platform. Obtain your current API keys from the Dashboard and update your integration, or reach out to the user and reconnect the account.

[Dashboard](https://dashboard.stripe.com/account/apikeys)

The postal code provided was incorrect.

An error occurred while processing the card. Try again later or with a different payment method.

The product this SKU belongs to is no longer available for purchase.

Progressive onboarding limit has been reached for the platform.

Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.

The customer has stopped the payment with their bank. Contact them for details and to arrange payment.

You cannot refund a disputed payment.

A resource with a user-specified ID (e.g., plan or coupon) already exists. Use a different, unique value for id and try again.

The ID provided is not valid. Either the resource does not exist, or an ID for a different resource has been provided.

You cannot confirm this refund as it is already processed.

The bank routing number provided is invalid.

The API key provided is a publishable key, but a secret key is required. Obtain your current API keys from the Dashboard and update your integration to use them.

[Dashboard](https://dashboard.stripe.com/account/apikeys)

Your account does not support SEPA payments.

[SEPA](/sources/sepa-debit)

The latest setup attempt for the SetupIntent has failed. Check the last_setup_error property on the SetupIntent for more details, and provide a new payment method to attempt to set it up again.

The provided payment method has failed authentication. Provide a new payment method to attempt to fulfill this SetupIntent again.

One or more provided parameters was not allowed for the given operation on the SetupIntent. Check our API reference or the returned error message to see which values were not correct for that SetupIntent.

[API reference](/api/setup_intents)

The provided mandate is invalid and can not be used for the setup intent.

The latest setup attempt for the SetupIntent has expired. Check the last_setup_error property on the SetupIntent for more details, and provide a new payment method to attempt to complete this SetupIntent again.

[last_setup_error](/api/setup_intents/object#setup_intent_object-last_setup_error)

The SetupIntent’s state was incompatible with the operation you were trying to perform.

Shipping calculation failed as the information provided was either incorrect or could not be verified.

The SKU is inactive and no longer available for purchase. Use a different SKU, or make the current SKU active again.

Occurs when providing the legal_entity information for a U.S. custom account, if the provided state is not supported. (This is mostly associated states and territories.)

The requested status transition is not valid.

Stripe Tax has not been activated on your account. Check the setup documentation to get started.

[setup documentation](/tax/set-up)

The tax ID number provided is invalid (e.g., missing digits). Tax ID information varies from country to country, but must be at least nine digits.

Tax calculation for the order failed.

Terminal is currently only available in some countries. Locations in your country cannot be created in livemode.

Reader is currently busy processing another request. Please reference the integration guide for details on how to handle this error.

[integration guide](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

Reader can no longer accept payments as an unrecoverable hardware fault has been detected. Please reach out to Stripe support at https://support.stripe.com/contact/email and provide your reader’s serial number for replacement.

Reader is currently offline, please ensure the reader is powered on and connected to the internet before retrying your request. Reference the integration guide for details on how to handle this error.

[integration guide](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

There was a timeout when sending this command to the reader. Please reference the integration guide for details on how to handle this error.

[integration guide](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

Your account has not been activated and can only make test charges. Activate your account in the Dashboard to begin processing live charges.

[Activate your account](https://dashboard.stripe.com/account/onboarding)

Your integration is using an older version of TLS that is unsupported. You must be using TLS 1.2 or above.

[TLS](/security#tls)

The token provided has already been used. You must create a new token before you can retry this request.

Invalid card network parameter was provided in the card token object. Check our API documentation or the returned error message for more context.

[API documentation](/api)

The token provided is currently being used in another request. This occurs if your integration is making duplicate requests simultaneously.

When creating a Transfer, the payments parameter in source_balance should not be passed in when balance type is set to issuing.

The requested transfer cannot be created. Contact us if you are receiving this error.

[Contact us](https://support.stripe.com/email)

The URL provided is invalid.

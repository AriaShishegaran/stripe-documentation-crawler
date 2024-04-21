# API upgrades

Your API version controls the API and webhook behavior you see (for example, what properties you see in responses, what parameters you’re permitted to send in requests, and so on). Your version gets set the first time you make an API request. When a breaking change is introduced to the Stripe API, a new dated version is released. To avoid breaking your code, we don’t change your version until you’re ready to upgrade.

If you make requests on behalf of other users using Connect, we’ll use your application’s API version to help you to write code that works for all your users no matter what API versions they’re individually running.

[Connect](https://stripe.com/connect)

## Backwards-compatible changes

Stripe considers the following changes to be backwards-compatible:

- Adding new API resources.

- Adding new optional request parameters to existing API methods.

- Adding new properties to existing API responses.

- Changing the order of properties in existing API responses.

- Changing the length or format of opaque strings, such as object IDs, error messages, and other human-readable strings.This includes adding or removing fixed prefixes (such as ch_ on charge IDs).Make sure that your integration can handle Stripe-generated object IDs, which can contain up to 255 characters. For example, if you’re using MySQL, store the IDs in a VARCHAR(255) COLLATE utf8_bin column (the COLLATE configuration provides case-sensitivity during lookups).

- This includes adding or removing fixed prefixes (such as ch_ on charge IDs).

- Make sure that your integration can handle Stripe-generated object IDs, which can contain up to 255 characters. For example, if you’re using MySQL, store the IDs in a VARCHAR(255) COLLATE utf8_bin column (the COLLATE configuration provides case-sensitivity during lookups).

- Adding new event types.Make sure that your webhook listener gracefully handles unfamiliar event types.

- Make sure that your webhook listener gracefully handles unfamiliar event types.

## Upgrade your API version

If you’re running an older version of the API, upgrade to the latest version to take advantage of new functionality or to streamline responses so the API is faster for you.

Upgrading your API version affects:

- The API calls you make without a Stripe-Version header: the parameters you can send and the structure of objects returned.

- The structure of objects received with Stripe.js methods such as confirmCardPayment.

[Stripe.js](/payments/elements)

[confirmCardPayment](/js#stripe-confirm-card-payment)

- The structure of objects sent to your webhook endpoints (both Account and Connect ones.) If an endpoint has an explicit version set, it will remain unaffected.

[Connect](/connect/webhooks)

- Automated Billing operations performed by Stripe (for example, generating an invoice for a new subscription period) use your account’s default API version. See the API changelog for details about how your default API version will impact these operations.

[invoice](/api/invoices)

To see what version you’re running and the latest upgrade, visit your Developer Dashboard.

[Developer Dashboard](https://dashboard.stripe.com/developers)

When performing an API upgrade, make sure that you specify the API version that you’re integrating against in your code instead of relying on your account’s default API version. To test a newer version for API calls, set the Stripe-Version header (in live or test mode). Learn how to manage versioning in our server-side libraries.

[server-side libraries](/libraries#server-side-libraries)

For webhooks, you can override the version of a single test webhook endpoint in your Dashboard. To safely upgrade your webhooks, Stripe recommends that you:

[version](/webhooks#api-versions)

[Dashboard](https://dashboard.stripe.com/account/webhooks)

- Check for breaking changes to see which objects will be structured differently.

[breaking changes](#api-versions)

- Update your webhook code to handle both the old and new version of each object.

- Change the version of a test webhook endpoint to the version you want to test.

- Trigger the event in test mode and validate that your code works for the new structure.

When you’re confident that your code can handle the latest API version, click the Upgrade version button in your Dashboard. This switches the version used by API calls that don’t have the Stripe-Version header and also switches the version used to render objects sent to your webhooks.

The shape of resources inside events retrieved from the API is defined by the default API version of your account at the time the event occurred. If your code retrieves events created when your default API version was different your code will need to account for these changes when processing events.

[events retrieved from the API](/api/events)

For 72 hours after you’ve upgraded your API version, you can safely roll back to the version you were upgrading from in your Dashboard.

After you’ve rolled back, webhooks that were sent with the new object structure and failed will be retried with the old structure.

## Stay informed

We send information on new additions and changes to Stripe’s API and language libraries in the Stripe Developer Digest. Be sure to subscribe to stay informed.

[privacy policy](https://stripe.com/privacy)

## API versions

Listed below are all the breaking changes to the Stripe API. Each date corresponds with a new version of the Stripe API. If you’re looking for all API additions and updates, see the API changelog. If you are looking for new product releases, see the product changelog.

[breaking changes](#breaking-change)

[API changelog](/changelog)

[product changelog](https://stripe.com/blog/changelog)

- PaymentIntents now has automatic_async as the default capture method when capture method is not specified during PaymentIntents creation. For more information about async capture, view the asynchronous capture guide.

PaymentIntents now has automatic_async as the default capture method when capture method is not specified during PaymentIntents creation. For more information about async capture, view the asynchronous capture guide.

[PaymentIntents](/api/payment_intents)

[asynchronous capture guide](/payments/payment-intents/asynchronous-capture)

- Fields under rendering_options for invoices are now migrated under rendering.

Fields under rendering_options for invoices are now migrated under rendering.

- Product ‘features’ has been renamed to marketing_features.

Product ‘features’ has been renamed to marketing_features.

- In the Accounts API, the following error codes have been added as new error codes in the requirements.errors array. See Account requirements errors for more information.invalid_address_highway_contract_boxinvalid_address_private_mailboxinvalid_business_profile_nameinvalid_business_profile_name_denylistedinvalid_company_name_denylistedinvalid_dob_age_over_maximuminvalid_dob_age_under_minimuminvalid_product_description_lengthinvalid_product_description_url_matchinvalid_statement_descriptor_business_mismatchinvalid_statement_descriptor_denylistedinvalid_statement_descriptor_lengthinvalid_statement_descriptor_prefix_denylistedinvalid_statement_descriptor_prefix_mismatchinvalid_tax_id_formatinvalid_url_denylistedinvalid_url_formatinvalid_url_web_presence_detectedinvalid_url_website_business_information_mismatchinvalid_url_website_emptyinvalid_url_website_inaccessibleinvalid_url_website_inaccessible_geoblockedinvalid_url_website_inaccessible_password_protectedinvalid_url_website_incompleteinvalid_url_website_incomplete_cancellation_policyinvalid_url_website_incomplete_customer_service_detailsinvalid_url_website_incomplete_legal_restrictionsinvalid_url_website_incomplete_refund_policyinvalid_url_website_incomplete_return_policyinvalid_url_website_incomplete_terms_and_conditionsinvalid_url_website_incomplete_under_constructioninvalid_url_website_other

In the Accounts API, the following error codes have been added as new error codes in the requirements.errors array. See Account requirements errors for more information.

[Account requirements errors](/api/accounts/object#account_object-requirements-errors)

- invalid_address_highway_contract_box

- invalid_address_private_mailbox

- invalid_business_profile_name

- invalid_business_profile_name_denylisted

- invalid_company_name_denylisted

- invalid_dob_age_over_maximum

- invalid_dob_age_under_minimum

- invalid_product_description_length

- invalid_product_description_url_match

- invalid_statement_descriptor_business_mismatch

- invalid_statement_descriptor_denylisted

- invalid_statement_descriptor_length

- invalid_statement_descriptor_prefix_denylisted

- invalid_statement_descriptor_prefix_mismatch

- invalid_tax_id_format

- invalid_url_denylisted

- invalid_url_format

- invalid_url_web_presence_detected

- invalid_url_website_business_information_mismatch

- invalid_url_website_empty

- invalid_url_website_inaccessible

- invalid_url_website_inaccessible_geoblocked

- invalid_url_website_inaccessible_password_protected

- invalid_url_website_incomplete

- invalid_url_website_incomplete_cancellation_policy

- invalid_url_website_incomplete_customer_service_details

- invalid_url_website_incomplete_legal_restrictions

- invalid_url_website_incomplete_refund_policy

- invalid_url_website_incomplete_return_policy

- invalid_url_website_incomplete_terms_and_conditions

- invalid_url_website_incomplete_under_construction

- invalid_url_website_other

- In the Accounts API, if no settings.payments.statement_descriptor is supplied, the statement descriptor is automatically set to the first supplied parameter of (in priority order):business_profile.namebusiness_profile.urlcompany.name or individual.first_name + individual.last_name (dependent on the business_type)The statement descriptor is only set automatically when one of the above fields is provided as a parameter, so existing accounts will not be impacted unless a dependent field is updated. Similarly, settings.card_payments.statement_descriptor_prefix will be defaulted to a shortened version of the settings.payments.statement_descriptor. This will take place whenever the statement descriptor is updated (either explicitly, or when defaulted).

In the Accounts API, if no settings.payments.statement_descriptor is supplied, the statement descriptor is automatically set to the first supplied parameter of (in priority order):

- business_profile.name

- business_profile.url

- company.name or individual.first_name + individual.last_name (dependent on the business_type)

The statement descriptor is only set automatically when one of the above fields is provided as a parameter, so existing accounts will not be impacted unless a dependent field is updated. Similarly, settings.card_payments.statement_descriptor_prefix will be defaulted to a shortened version of the settings.payments.statement_descriptor. This will take place whenever the statement descriptor is updated (either explicitly, or when defaulted).

- MajorPaymentIntents and SetupIntents now have automatic_payment_methods enabled by default, which allows you to configure payment method settings from the Dashboard—no code required. The previous default was to accept only card payments when both payment_method_types and automatic_payment_methods were not specified. For more information, view the upgrade guide.When confirming a PaymentIntent, you will be required to provide a return_url unless off_session=true.When confirming a PaymentIntent, you cannot use error_on_requires_action. Use payment_method_types with error_on_requires_action if you wish to fail payment attempts when PaymentIntents transition into requires_action.When confirming a SetupIntent, you will be required to provide a return_url.You can bypass the return_url requirement using automatic_payment_methods[allow_redirects]=never, this will automatically filter payment methods that require redirect even if they are enabled in the Dashboard.

PaymentIntents and SetupIntents now have automatic_payment_methods enabled by default, which allows you to configure payment method settings from the Dashboard—no code required. The previous default was to accept only card payments when both payment_method_types and automatic_payment_methods were not specified. For more information, view the upgrade guide.

[PaymentIntents](/api/payment_intents)

[SetupIntents](/api/setup_intents)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[upgrade guide](/upgrades/manage-payment-methods)

- When confirming a PaymentIntent, you will be required to provide a return_url unless off_session=true.

- When confirming a PaymentIntent, you cannot use error_on_requires_action. Use payment_method_types with error_on_requires_action if you wish to fail payment attempts when PaymentIntents transition into requires_action.

- When confirming a SetupIntent, you will be required to provide a return_url.

- You can bypass the return_url requirement using automatic_payment_methods[allow_redirects]=never, this will automatically filter payment methods that require redirect even if they are enabled in the Dashboard.

[require redirect](/payments/payment-methods/integration-options#additional-api-supportability)

- No-cost orders are now enabled for one-time payments in Checkout Sessions. The value of payment_method_collection has changed from always to if_required accordingly.

No-cost orders are now enabled for one-time payments in Checkout Sessions. The value of payment_method_collection has changed from always to if_required accordingly.

[No-cost orders](/payments/checkout/no-cost-orders)

- When being viewed by a platform, PaymentMethod fingerprints of types us_bank_account, acss_debit, sepa_debit, bacs_debit, and au_becs_debit are rendered in platform scope, not the owning merchant (connected account) scope. This works similarly to the 2018-01-23 change for cards and bank accounts.

When being viewed by a platform, PaymentMethod fingerprints of types us_bank_account, acss_debit, sepa_debit, bacs_debit, and au_becs_debit are rendered in platform scope, not the owning merchant (connected account) scope. This works similarly to the 2018-01-23 change for cards and bank accounts.

[2018-01-23](#2018-01-23)

- Added more specific error codes to the PaymentIntent API for when a Klarna payment fails:payment_method_customer_declinepayment_method_not_availablepayment_method_provider_declinepayment_intent_payment_attempt_expired

Added more specific error codes to the PaymentIntent API for when a Klarna payment fails:

[PaymentIntent](/api/payment_intents)

[Klarna](/payments/klarna)

- payment_method_customer_decline

- payment_method_not_available

- payment_method_provider_decline

- payment_intent_payment_attempt_expired

- In the Accounts API, verification_missing_directors, verification_directors_mismatch, verification_document_directors_mismatch and verification_extraneous_directors has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

In the Accounts API, verification_missing_directors, verification_directors_mismatch, verification_document_directors_mismatch and verification_extraneous_directors has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

[Account requirements errors](/api/accounts/object#account_object-requirements-errors)

- Charge no longer auto-expands refunds by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

Charge no longer auto-expands refunds by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

[Charge](/api/charges/object)

[expand the list](/api#expanding_objects)

- The charges property on PaymentIntent has been removed. You can use the latest_charge property instead.

The charges property on PaymentIntent has been removed. You can use the latest_charge property instead.

[PaymentIntent](/api/payment_intents/object)

- Added more specific error codes for the following bank redirect payment methods: Bancontact, EPS, Giropay, iDEAL, Przelewy24, and Sofort.Added the following error codes to the PaymentIntent and PaymentMethod APIs:payment_intent_payment_attempt_expiredpayment_method_customer_declinepayment_method_provider_timeoutpayment_method_not_availablepayment_method_provider_declineAdded the following error codes to the SetupIntent APIs:setup_intent_setup_attempt_expiredpayment_method_customer_declinepayment_method_provider_timeoutpayment_method_not_availablepayment_method_provider_decline

Added more specific error codes for the following bank redirect payment methods: Bancontact, EPS, Giropay, iDEAL, Przelewy24, and Sofort.

- Added the following error codes to the PaymentIntent and PaymentMethod APIs:payment_intent_payment_attempt_expiredpayment_method_customer_declinepayment_method_provider_timeoutpayment_method_not_availablepayment_method_provider_decline

Added the following error codes to the PaymentIntent and PaymentMethod APIs:

[PaymentIntent](/api/payment_intents)

[PaymentMethod](/api/payment_methods)

- payment_intent_payment_attempt_expired

- payment_method_customer_decline

- payment_method_provider_timeout

- payment_method_not_available

- payment_method_provider_decline

- Added the following error codes to the SetupIntent APIs:setup_intent_setup_attempt_expiredpayment_method_customer_declinepayment_method_provider_timeoutpayment_method_not_availablepayment_method_provider_decline

Added the following error codes to the SetupIntent APIs:

[SetupIntent](/api/setup_intents)

- setup_intent_setup_attempt_expired

- payment_method_customer_decline

- payment_method_provider_timeout

- payment_method_not_available

- payment_method_provider_decline

- In the Accounts API, verification_legal_entity_structure_mismatch has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

In the Accounts API, verification_legal_entity_structure_mismatch has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

[Account requirements errors](/api/accounts/object#account_object-requirements-errors)

- The pending_invoice_items_behavior parameter on create Invoice no longer supports the include_and_require value. When the parameter is omitted the default value of pending_invoice_items_behavior is now exclude.

The pending_invoice_items_behavior parameter on create Invoice no longer supports the include_and_require value. When the parameter is omitted the default value of pending_invoice_items_behavior is now exclude.

[create Invoice](/api/invoices/create)

- When creating a Checkout Session in payment mode, the default value of customer_creation has changed from always to if_required.

When creating a Checkout Session in payment mode, the default value of customer_creation has changed from always to if_required.

- A PaymentIntent is no longer created during Checkout Session creation in payment mode. Instead, a PaymentIntent will be created when the Session is confirmed.

A PaymentIntent is no longer created during Checkout Session creation in payment mode. Instead, a PaymentIntent will be created when the Session is confirmed.

- Checkout Sessions no longer return the setup_intent property in subscription mode.

Checkout Sessions no longer return the setup_intent property in subscription mode.

- The following parameters have been removed from create Checkout Session:line_items[amount]line_items[currency]line_items[name]line_items[description]line_items[images]You can use the price and price_data parameters instead.

The following parameters have been removed from create Checkout Session:

[create Checkout Session](/api/checkout/sessions/create)

- line_items[amount]

- line_items[currency]

- line_items[name]

- line_items[description]

- line_items[images]

You can use the price and price_data parameters instead.

- The subscription_data[coupon] parameter has been removed from create Checkout Session. You can use the discounts parameter instead.

The subscription_data[coupon] parameter has been removed from create Checkout Session. You can use the discounts parameter instead.

[create Checkout Session](/api/checkout/sessions/create)

- The shipping_rates parameter has been removed from create Checkout Session. You can use the shipping_options parameter instead.

The shipping_rates parameter has been removed from create Checkout Session. You can use the shipping_options parameter instead.

[create Checkout Session](/api/checkout/sessions/create)

- On the Checkout Session resource, several shipping properties have changed.shipping_rate has been moved into the new shipping_cost hash.shipping has been renamed to shipping_details.

On the Checkout Session resource, several shipping properties have changed.

- shipping_rate has been moved into the new shipping_cost hash.

- shipping has been renamed to shipping_details.

- exempted now appears in the three_d_secure hash for card Charges. It indicates that a 3D Secure exemption was granted.

exempted now appears in the three_d_secure hash for card Charges. It indicates that a 3D Secure exemption was granted.

- In the Accounts API, invalid_tos_acceptance has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

In the Accounts API, invalid_tos_acceptance has been added as a new error code in the requirements.errors array. See Account requirements errors for more information.

[Account requirements errors](/api/accounts/object#account_object-requirements-errors)

- When creating a physical Issuing card in testmode, its shipping status no longer automatically changes from pending to delivered. This functionality is now accessible via the following new endpoints:/v1/test_helpers/issuing/cards/:card/shipping/ship/v1/test_helpers/issuing/cards/:card/shipping/deliver/v1/test_helpers/issuing/cards/:card/shipping/return/v1/test_helpers/issuing/cards/:card/shipping/fail

When creating a physical Issuing card in testmode, its shipping status no longer automatically changes from pending to delivered. This functionality is now accessible via the following new endpoints:

[status](/api/issuing/cards/object#issuing_card_object-shipping-status)

- /v1/test_helpers/issuing/cards/:card/shipping/ship

- /v1/test_helpers/issuing/cards/:card/shipping/deliver

- /v1/test_helpers/issuing/cards/:card/shipping/return

- /v1/test_helpers/issuing/cards/:card/shipping/fail

- design_rejected is now a possible value for the cancellation_reason field on the issued card object, indicating that the card’s design was rejected by Stripe.

design_rejected is now a possible value for the cancellation_reason field on the issued card object, indicating that the card’s design was rejected by Stripe.

- The default_currency field on the Customer API resource has been removed.

The default_currency field on the Customer API resource has been removed.

- We have removed tax_percent from objects and requests in favor of tax rates.

We have removed tax_percent from objects and requests in favor of tax rates.

[tax rates](/api/tax_rates)

- 

- 

- On subscription schedules, phases.plans has been renamed to phases.items. This applies for the subscription schedule object as well as create and update requests.

On subscription schedules, phases.plans has been renamed to phases.items. This applies for the subscription schedule object as well as create and update requests.

[subscription schedule](/api/subscription_schedules/object#subscription_schedule_object-phases)

[create](/api/subscription_schedules/create#create_subscription_schedule-phases)

[update](/api/subscription_schedules/update#update_subscription_schedule-phases)

- Deprecate the payment_method.card_automatically_updated webhook in favor of payment_method.automatically_updated.

Deprecate the payment_method.card_automatically_updated webhook in favor of payment_method.automatically_updated.

- Checkout Sessions no longer include the display_items property. Use the includable line_items property instead.

Checkout Sessions no longer include the display_items property. Use the includable line_items property instead.

- The requirements hash on the Account and Capability objects, and the verification_fields hash on the Country Spec object have newly formatted strings for requirements that are related to key persons associated with an account:Fields that are required for persons with representative, owner, director, and executive roles will be prefixed with representative, owners, directors, and executives, respectively. Person requirements will be previewed as follows:When the representative’s phone number is required, it will appear as representative.phone instead of relationship.representative.When an owner’s full name is required, it will appear as owners.first_name and owners.last_name instead of relationship.owner.When an executive’s ID number is required, it will appear as executives.id_number instead of relationship.executive.When a director’s date of birth is required, it will appear as directors.dob.day, directors.dob.month, and directors.dob.year instead of relationship.director.The boolean values that indicate the associated owners, executives, or directors have been provided now appear as company.owners_provided, company.executives_provided, or company.directors_provided instead of relationship.owner, relationship.executive, or relationship.director, respectively.

The requirements hash on the Account and Capability objects, and the verification_fields hash on the Country Spec object have newly formatted strings for requirements that are related to key persons associated with an account:

- Fields that are required for persons with representative, owner, director, and executive roles will be prefixed with representative, owners, directors, and executives, respectively. Person requirements will be previewed as follows:When the representative’s phone number is required, it will appear as representative.phone instead of relationship.representative.When an owner’s full name is required, it will appear as owners.first_name and owners.last_name instead of relationship.owner.When an executive’s ID number is required, it will appear as executives.id_number instead of relationship.executive.When a director’s date of birth is required, it will appear as directors.dob.day, directors.dob.month, and directors.dob.year instead of relationship.director.

- When the representative’s phone number is required, it will appear as representative.phone instead of relationship.representative.

- When an owner’s full name is required, it will appear as owners.first_name and owners.last_name instead of relationship.owner.

- When an executive’s ID number is required, it will appear as executives.id_number instead of relationship.executive.

- When a director’s date of birth is required, it will appear as directors.dob.day, directors.dob.month, and directors.dob.year instead of relationship.director.

- The boolean values that indicate the associated owners, executives, or directors have been provided now appear as company.owners_provided, company.executives_provided, or company.directors_provided instead of relationship.owner, relationship.executive, or relationship.director, respectively.

- In the Accounts/Persons/Capabilities API, several new error codes have been introduced in the requirements.errors array. See Account requirements errors for more information. These error codes are:verification_document_issue_or_expiry_date_missingverification_document_not_signedverification_failed_tax_id_not_issuedverification_failed_tax_id_matchinvalid_address_po_boxes_disallowed

In the Accounts/Persons/Capabilities API, several new error codes have been introduced in the requirements.errors array. See Account requirements errors for more information. These error codes are:

[Account requirements errors](/api/accounts/object#account_object-requirements-errors)

- verification_document_issue_or_expiry_date_missing

- verification_document_not_signed

- verification_failed_tax_id_not_issued

- verification_failed_tax_id_match

- invalid_address_po_boxes_disallowed

- The payment_method_details.card.three_d_secure fields on the Charge object have been updated. The succeeded and authenticated booleans have been removed; please use the result enum instead.

The payment_method_details.card.three_d_secure fields on the Charge object have been updated. The succeeded and authenticated booleans have been removed; please use the result enum instead.

- The subscriptions property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

The subscriptions property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

[expand the list](https://stripe.com/docs/api#expanding_objects)

- The tiers property on Plan is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

The tiers property on Plan is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

[expand the list](https://stripe.com/docs/api#expanding_objects)

- The sources property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

The sources property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

[expand the list](https://stripe.com/docs/api#expanding_objects)

- The tax_ids property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

The tax_ids property on Customers is no longer included by default. You can expand the list but for performance reasons we recommended against doing so unless needed.

[expand the list](https://stripe.com/docs/api#expanding_objects)

- The prorate and subscription_prorate parameters are deprecated in favor of proration_behavior.

The prorate and subscription_prorate parameters are deprecated in favor of proration_behavior.

- MajorYou can now optionally number invoices sequentially across your account instead of sequentially for each customer. To use this feature, enable account level numbering in the Stripe Dashboard.To ensure invoices are numbered sequentially and without gaps, invoices that can be deleted (drafts) are only assigned numbers when finalized.

You can now optionally number invoices sequentially across your account instead of sequentially for each customer. To use this feature, enable account level numbering in the Stripe Dashboard.

[sequentially across your account](https://stripe.com/docs/billing/invoices/customizing#invoice-prefix-number)

[account level numbering](https://dashboard.stripe.com/settings/billing/invoice)

- To ensure invoices are numbered sequentially and without gaps, invoices that can be deleted (drafts) are only assigned numbers when finalized.

- MajorThe id field of all invoice line items have changed and are now prefixed with il_. The new id has consistent prefixes across all line items, is globally unique, and can be used for pagination. Old prefixes included sub_, su_, item_, sli_, and ii_ and weren’t globally unique.You can no longer use the prefix of the id to determine the source of the line item. Instead use the type field for this purpose.For lines with type=invoiceitem, use the invoice_item field to reference or update the originating Invoice Item object.The Invoice Line Item object on earlier API versions also have a unique_id field to be used for migrating internal references before upgrading to this version.When setting a tax rate to individual line items, use the new id. Users on earlier API versions can pass in either a line item id or unique_id.

The id field of all invoice line items have changed and are now prefixed with il_. The new id has consistent prefixes across all line items, is globally unique, and can be used for pagination. Old prefixes included sub_, su_, item_, sli_, and ii_ and weren’t globally unique.

[id](/api/invoices/line_item#invoice_line_item_object-id)

- You can no longer use the prefix of the id to determine the source of the line item. Instead use the type field for this purpose.

- For lines with type=invoiceitem, use the invoice_item field to reference or update the originating Invoice Item object.

- The Invoice Line Item object on earlier API versions also have a unique_id field to be used for migrating internal references before upgrading to this version.

- When setting a tax rate to individual line items, use the new id. Users on earlier API versions can pass in either a line item id or unique_id.

[setting a tax rate to individual line items](/billing/invoices/tax-rates#setting-tax-rates-on-individual-items)

- When creating a post-payment credit note on an invoice:out_of_band_amount is required if the sum of credit_amount and (refund or refund_amount) is less than the credit note total.In previous API versions out_of_band_amount is optional and, in the case that the credit_amount and refund amounts are less than the credit note total, the difference will automatically be allocated to the out_of_band_amount.

When creating a post-payment credit note on an invoice:

[creating](/api/credit_notes/create)

- out_of_band_amount is required if the sum of credit_amount and (refund or refund_amount) is less than the credit note total.

[out_of_band_amount](/api/credit_notes/create#create_credit_note-out_of_band_amount)

- In previous API versions out_of_band_amount is optional and, in the case that the credit_amount and refund amounts are less than the credit note total, the difference will automatically be allocated to the out_of_band_amount.

- Customer balances applied to all invoices are now debited or credited back to the customer when voided. Earlier, applied customer balances were not returned back to the customer and were consumed.To achieve this behavior in earlier API versions:Set consume_applied_balance to false when voiding invoices in /v1/invoices/:id/void.Set invoice_customer_balance_settings[consume_applied_balance_on_void] to false in /v1/subscriptions create or update to force this behavior for Invoices voided by a Subscription.Set subscription_data[invoice_customer_balance_settings][consume_applied_balance_on_void] to false in /v1/checkout/sessions create to force this behavior for Invoices voided by Subscriptions created with Checkout.

Customer balances applied to all invoices are now debited or credited back to the customer when voided. Earlier, applied customer balances were not returned back to the customer and were consumed.

- To achieve this behavior in earlier API versions:Set consume_applied_balance to false when voiding invoices in /v1/invoices/:id/void.Set invoice_customer_balance_settings[consume_applied_balance_on_void] to false in /v1/subscriptions create or update to force this behavior for Invoices voided by a Subscription.Set subscription_data[invoice_customer_balance_settings][consume_applied_balance_on_void] to false in /v1/checkout/sessions create to force this behavior for Invoices voided by Subscriptions created with Checkout.

- Set consume_applied_balance to false when voiding invoices in /v1/invoices/:id/void.

[/v1/invoices/:id/void](/api/invoices/void)

- Set invoice_customer_balance_settings[consume_applied_balance_on_void] to false in /v1/subscriptions create or update to force this behavior for Invoices voided by a Subscription.

[create](/api/subscriptions/create)

[update](/api/subscriptions/update)

- Set subscription_data[invoice_customer_balance_settings][consume_applied_balance_on_void] to false in /v1/checkout/sessions create to force this behavior for Invoices voided by Subscriptions created with Checkout.

[create](/api/checkout/sessions/create)

- Deprecated tax information for Customers have been removed.The deprecated tax_info and tax_info_verification fields on the Customer object are now removed in favor of tax_ids.The deprecated tax_info parameter on the Customer create and update methods are removed in favor of tax_id_data.For more information, view the migration guide.

Deprecated tax information for Customers have been removed.

- The deprecated tax_info and tax_info_verification fields on the Customer object are now removed in favor of tax_ids.

- The deprecated tax_info parameter on the Customer create and update methods are removed in favor of tax_id_data.

- For more information, view the migration guide.

[migration guide](/billing/taxes/tax-rates#migration)

- In the Accounts API, the requested_capabilities property is now required at creation time for Custom accounts in all countries. See Account capabilities for more information.

In the Accounts API, the requested_capabilities property is now required at creation time for Custom accounts in all countries. See Account capabilities for more information.

[Account capabilities](/connect/account-capabilities)

- On subscription schedules, invoice_settings, default_payment_method, billing_thresholds and collection_method are now nested under default_settings.

On subscription schedules, invoice_settings, default_payment_method, billing_thresholds and collection_method are now nested under default_settings.

- There are changes to subscription schedules.Rename renewal_behavior to end_behavior with values cancel and release.Remove renewal_interval.A side effect of this change is that if you wrote a renewal_behavior of none on an old API version, end_behavior will be converted to cancel when reading the value back.In the event that you are upgrading your API and set renewal_behavior as renew, with this API version enabled you will see end_behavior as renew however you will not be able to update renewal_interval. Additionally you can not set end_behavior to renew, so it is in a read-only state.

There are changes to subscription schedules.

- Rename renewal_behavior to end_behavior with values cancel and release.

- Remove renewal_interval.

- A side effect of this change is that if you wrote a renewal_behavior of none on an old API version, end_behavior will be converted to cancel when reading the value back.

- In the event that you are upgrading your API and set renewal_behavior as renew, with this API version enabled you will see end_behavior as renew however you will not be able to update renewal_interval. Additionally you can not set end_behavior to renew, so it is in a read-only state.

- The start field on a subscription resource has been removed and is replaced by a start_date field which represents when the entire subscription started as opposed to when the current plan configuration started.

The start field on a subscription resource has been removed and is replaced by a start_date field which represents when the entire subscription started as opposed to when the current plan configuration started.

- The due_date property is always null on invoices with billing=charge_automatically.

The due_date property is always null on invoices with billing=charge_automatically.

- The billing attribute on invoices, subscriptions, and subscription schedules is renamed to collection_method.

The billing attribute on invoices, subscriptions, and subscription schedules is renamed to collection_method.

- The customer object’s account_balance value has been renamed to balance. A new customer balance transactions API is available:Update the customer’s balance by incrementing or decrementing its current value by a specified amount and attaching metadata to the change.Retrieve history of changes to the customer’s balance.

The customer object’s account_balance value has been renamed to balance. A new customer balance transactions API is available:

[customer object](https://stripe.com/docs/api/customers)

[customer balance transactions API](https://stripe.com/docs/api/customer_balance_transactions)

- Update the customer’s balance by incrementing or decrementing its current value by a specified amount and attaching metadata to the change.

- Retrieve history of changes to the customer’s balance.

- The relationship[account_opener] field on a Person object has been renamed to relationship[representative].

The relationship[account_opener] field on a Person object has been renamed to relationship[representative].

- In the Accounts API, the requested_capabilities property is now required at creation time for accounts in Australia, Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, New Zealand, Norway, Portugal, Spain, Sweden, Switzerland, and the United Kingdom. See Account capabilities for more information.

In the Accounts API, the requested_capabilities property is now required at creation time for accounts in Australia, Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, New Zealand, Norway, Portugal, Spain, Sweden, Switzerland, and the United Kingdom. See Account capabilities for more information.

[Account capabilities](/connect/account-capabilities)

- Adds additional details_code values to the verification[document] hash on a Person object.

Adds additional details_code values to the verification[document] hash on a Person object.

- MajorThe platform_payments capability has been renamed to transfers, to better indicate the Stripe primitives that this capability supports.The card_payments capability has been updated to no longer imply transfers. You’ll now need to additionally request the transfers capability when creating an account.

The platform_payments capability has been renamed to transfers, to better indicate the Stripe primitives that this capability supports.

- The card_payments capability has been updated to no longer imply transfers. You’ll now need to additionally request the transfers capability when creating an account.

- The relationship[executive] field on a Person object will no longer be automatically set to true when a Person object with relationship[account_opener] is created. The requirements hash on an Account object may require that you explicitly indicate that the account_opener is also an executive. If this is the case, you will need to indicate it by setting relationship[executive]=true.

The relationship[executive] field on a Person object will no longer be automatically set to true when a Person object with relationship[account_opener] is created. The requirements hash on an Account object may require that you explicitly indicate that the account_opener is also an executive. If this is the case, you will need to indicate it by setting relationship[executive]=true.

- Bank pull payments no longer expose internal system refunds on failure.System refunds can still be accessed via the list refunds endpoint.

Bank pull payments no longer expose internal system refunds on failure.

System refunds can still be accessed via the list refunds endpoint.

[list refunds](https://stripe.com/docs/api/refunds/list#list_refunds-charge)

- The application_fee parameter on invoice API methods and the application_fee field on the invoice object have both been renamed to application_fee_amount.

The application_fee parameter on invoice API methods and the application_fee field on the invoice object have both been renamed to application_fee_amount.

- MajorCreating a subscription succeeds even when the first payment fails. The subscription will be created in an incomplete status, where it will remain for up to 23 hours. During that time period, it can be moved into an active state by paying the first invoice. If no successful payment is made, the subscription will move into a final incomplete_expired state. Updates to a non-incomplete subscription that require a payment will also succeed regardless of the payment status. Prior to this version, all creations or updates would fail if the corresponding payment failed. For more details see our guide.

Creating a subscription succeeds even when the first payment fails. The subscription will be created in an incomplete status, where it will remain for up to 23 hours. During that time period, it can be moved into an active state by paying the first invoice. If no successful payment is made, the subscription will move into a final incomplete_expired state. Updates to a non-incomplete subscription that require a payment will also succeed regardless of the payment status. Prior to this version, all creations or updates would fail if the corresponding payment failed. For more details see our guide.

[our guide](https://stripe.com/docs/billing/subscriptions/overview#subscription-lifecycle)

- There are a few changes to the invoice object:A status_transitions hash now contains the timestamps when an invoice was finalized, paid, marked uncollectible, or voided.The date property has been renamed to created.The finalized_at property has been moved into the status_transitions hash.

There are a few changes to the invoice object:

[invoice object](https://stripe.com/docs/api/invoices)

- A status_transitions hash now contains the timestamps when an invoice was finalized, paid, marked uncollectible, or voided.

- The date property has been renamed to created.

- The finalized_at property has been moved into the status_transitions hash.

- MajorStatement descriptor behaviors for card payments created via /v1/charges have changed. See our statement descriptor guide for details.Instead of using the platform’s statement descriptor, charges created with on_behalf_of or destination will now use the descriptor of the connected account.The full statement descriptor for a card payment may no longer be provided at charge creation. Dynamic descriptors provided at charge time will now be prefixed by the descriptor prefix set in the dashboard or via the new settings[card_payments][statement_descriptor_prefix] parameter in the Accounts API.If an account has no statement_descriptor set, the account’s business or legal name will be used as statement descriptor.Statement descriptors may no longer contain *, ', and ".

Statement descriptor behaviors for card payments created via /v1/charges have changed. See our statement descriptor guide for details.

[created via /v1/charges](/api/charges/create)

[our statement descriptor guide](/payments/charges-api#dynamic-statement-descriptor)

- Instead of using the platform’s statement descriptor, charges created with on_behalf_of or destination will now use the descriptor of the connected account.

- The full statement descriptor for a card payment may no longer be provided at charge creation. Dynamic descriptors provided at charge time will now be prefixed by the descriptor prefix set in the dashboard or via the new settings[card_payments][statement_descriptor_prefix] parameter in the Accounts API.

- If an account has no statement_descriptor set, the account’s business or legal name will be used as statement descriptor.

- Statement descriptors may no longer contain *, ', and ".

- 

- 

- 

- 

- 

- 

- 

- legal_entity[business_id_number] has been renamed legal_entity[business_registration_number].

legal_entity[business_id_number] has been renamed legal_entity[business_registration_number].

- 

- 

- 

- 

- 

- 

- MajorMany properties on the Account API object have been reworked. To see a mapping of the old argument names to the new ones, see Accounts API Argument Changes.The legal_entity property on the Account API resource has been replaced with individual, company, and business_type.The verification hash has been replaced with a requirements hash.The verification[fields_needed] array has been replaced with three arrays to better represent when info is required: requirements[eventually_due], requirements[currently_due], and requirements[past_due].verification[due_by] has been renamed to requirements[current_deadline].The disabled_reason enum value of fields_needed has been renamed to requirements.past_due.Properties on the Account API object that configure behavior within Stripe have been moved into the new settings hash.The payout_schedule, payout_statement_descriptor and debit_negative_balances fields have been moved to settings[payouts] and renamed to schedule, statement_descriptor and debit_negative_balances.The statement_descriptor field has been moved to settings[payments][statement_descriptor].The decline_charge_on fields have been moved to settings[card_payments] and renamed to decline_on.The business_logo, business_logo_large and business_primary_color fields have been moved to settings[branding] and renamed to icon, logo and primary_color. The icon field additionally requires the uploaded image file to be square.The display_name and timezone fields have been moved to settings[dashboard].business_name, business_url, product_description, support_address, support_email, support_phone and support_url have been moved to the business_profile subhash.The legal_entity[verification][document] property (now located at individual[verification] and at verification in the Person API object) has been changed to a hash.The front and back fields support uploading both sides of documents.The details_code field has new error types: document_corrupt, document_failed_copy, document_failed_greyscale, document_failed_other, document_failed_test_mode, document_fraudulent, document_id_country_not_supported, document_id_type_not_supported, document_invalid, document_manipulated, document_missing_back, document_missing_front, document_not_readable, document_not_uploaded, document_photo_mismatch, and document_too_large.The keys property on Account creation has been removed. Platforms should now authenticate as their connected accounts with their own key via the Stripe-Account header.Starting with the 2019-02-19 API, the requested_capabilities property is now required at creation time for accounts in the U.S. See Account capabilities for more information.

Many properties on the Account API object have been reworked. To see a mapping of the old argument names to the new ones, see Accounts API Argument Changes.

[Accounts API Argument Changes](/connect/updated-requirements/accounts-arguments)

- The legal_entity property on the Account API resource has been replaced with individual, company, and business_type.

- The verification hash has been replaced with a requirements hash.The verification[fields_needed] array has been replaced with three arrays to better represent when info is required: requirements[eventually_due], requirements[currently_due], and requirements[past_due].verification[due_by] has been renamed to requirements[current_deadline].The disabled_reason enum value of fields_needed has been renamed to requirements.past_due.

- The verification[fields_needed] array has been replaced with three arrays to better represent when info is required: requirements[eventually_due], requirements[currently_due], and requirements[past_due].

- verification[due_by] has been renamed to requirements[current_deadline].

- The disabled_reason enum value of fields_needed has been renamed to requirements.past_due.

- Properties on the Account API object that configure behavior within Stripe have been moved into the new settings hash.The payout_schedule, payout_statement_descriptor and debit_negative_balances fields have been moved to settings[payouts] and renamed to schedule, statement_descriptor and debit_negative_balances.The statement_descriptor field has been moved to settings[payments][statement_descriptor].The decline_charge_on fields have been moved to settings[card_payments] and renamed to decline_on.The business_logo, business_logo_large and business_primary_color fields have been moved to settings[branding] and renamed to icon, logo and primary_color. The icon field additionally requires the uploaded image file to be square.The display_name and timezone fields have been moved to settings[dashboard].

- The payout_schedule, payout_statement_descriptor and debit_negative_balances fields have been moved to settings[payouts] and renamed to schedule, statement_descriptor and debit_negative_balances.

- The statement_descriptor field has been moved to settings[payments][statement_descriptor].

- The decline_charge_on fields have been moved to settings[card_payments] and renamed to decline_on.

- The business_logo, business_logo_large and business_primary_color fields have been moved to settings[branding] and renamed to icon, logo and primary_color. The icon field additionally requires the uploaded image file to be square.

- The display_name and timezone fields have been moved to settings[dashboard].

- business_name, business_url, product_description, support_address, support_email, support_phone and support_url have been moved to the business_profile subhash.

- The legal_entity[verification][document] property (now located at individual[verification] and at verification in the Person API object) has been changed to a hash.The front and back fields support uploading both sides of documents.The details_code field has new error types: document_corrupt, document_failed_copy, document_failed_greyscale, document_failed_other, document_failed_test_mode, document_fraudulent, document_id_country_not_supported, document_id_type_not_supported, document_invalid, document_manipulated, document_missing_back, document_missing_front, document_not_readable, document_not_uploaded, document_photo_mismatch, and document_too_large.

- The front and back fields support uploading both sides of documents.

- The details_code field has new error types: document_corrupt, document_failed_copy, document_failed_greyscale, document_failed_other, document_failed_test_mode, document_fraudulent, document_id_country_not_supported, document_id_type_not_supported, document_invalid, document_manipulated, document_missing_back, document_missing_front, document_not_readable, document_not_uploaded, document_photo_mismatch, and document_too_large.

- The keys property on Account creation has been removed. Platforms should now authenticate as their connected accounts with their own key via the Stripe-Account header.

[the Stripe-Account header](https://stripe.com/docs/connect/authentication#stripe-account-header)

- Starting with the 2019-02-19 API, the requested_capabilities property is now required at creation time for accounts in the U.S. See Account capabilities for more information.

[Account capabilities](/connect/account-capabilities)

- Some PaymentIntent statuses have been renamedrequires_source is now requires_payment_methodrequires_source_action is now requires_actionAll other statuses are unchanged

Some PaymentIntent statuses have been renamed

- requires_source is now requires_payment_method

- requires_source_action is now requires_action

- All other statuses are unchanged

- save_source_to_customer has been renamed to save_payment_method.

save_source_to_customer has been renamed to save_payment_method.

- allowed_source_types has been renamed to payment_method_types.

allowed_source_types has been renamed to payment_method_types.

- The next_source_action property on PaymentIntent has been renamed to next_action, and the authorize_with_url within has been renamed to redirect_to_url.

The next_source_action property on PaymentIntent has been renamed to next_action, and the authorize_with_url within has been renamed to redirect_to_url.

- The closed property on the invoice object controls automatic collection. closed has been deprecated in favor of the more specific auto_advance field. Where you might have set closed=true on invoices in the past, set auto_advance=false.

The closed property on the invoice object controls automatic collection. closed has been deprecated in favor of the more specific auto_advance field. Where you might have set closed=true on invoices in the past, set auto_advance=false.

[invoice object](https://stripe.com/docs/api/invoices)

[automatic collection](/billing/invoices/workflow#auto_advance)

- auto_advance now also defaults to false for one-off invoices, allowing you to control how long their status stays a draft. A longer explanation of these series of changes is in the documentation.

auto_advance now also defaults to false for one-off invoices, allowing you to control how long their status stays a draft. A longer explanation of these series of changes is in the documentation.

[status](https://stripe.com/docs/billing/migration/invoice-states#status)

[in the documentation](https://stripe.com/docs/billing/migration/invoice-states#autoadvance)

- Instead of checking the forgiven field on an invoice, check for the uncollectible status.Instead of setting the forgiven field on an invoice, mark it as uncollectible.

Instead of checking the forgiven field on an invoice, check for the uncollectible status.

- Instead of setting the forgiven field on an invoice, mark it as uncollectible.

[mark it as uncollectible.](/api/invoices/mark_uncollectible)

- The immutable_frozen_invoice error code was renamed to invoice_already_finalized

The immutable_frozen_invoice error code was renamed to invoice_already_finalized

- The following changes only affect users of PaymentIntents as part of the private beta before November 15, 2018. If you did not use PaymentIntents before then, these don’t affect you.The next_source_action dictionary on PaymentIntents previously contained a key called value. This has been replaced with the authorize_with_url and use_stripe_sdk keys.When creating PaymentIntents, the attempt_confirmation parameter has been renamed to confirm.The PaymentIntent confirm endpoint no longer supports the payment_intent parameter. To update a PaymentIntent’s source, pass source or source_data as a top-level parameter.The return_url parameter is only allowed when confirming a PaymentIntent. Passing return_url when updating a PaymentIntent is no longer allowed.When creating a PaymentIntent with transfer_data[destination], the on_behalf_of parameter must be provided and must match the account provided to transfer_data[destination]. This is because when you provide a destination, Stripe will settle charges in the country of the destination account.The next_source_action dictionary on PaymentIntents no longer contains the source_type property. To view the source type when retrieving PaymentIntents, expand the source parameter.

The following changes only affect users of PaymentIntents as part of the private beta before November 15, 2018. If you did not use PaymentIntents before then, these don’t affect you.

- The next_source_action dictionary on PaymentIntents previously contained a key called value. This has been replaced with the authorize_with_url and use_stripe_sdk keys.

- When creating PaymentIntents, the attempt_confirmation parameter has been renamed to confirm.

- The PaymentIntent confirm endpoint no longer supports the payment_intent parameter. To update a PaymentIntent’s source, pass source or source_data as a top-level parameter.

- The return_url parameter is only allowed when confirming a PaymentIntent. Passing return_url when updating a PaymentIntent is no longer allowed.

- When creating a PaymentIntent with transfer_data[destination], the on_behalf_of parameter must be provided and must match the account provided to transfer_data[destination]. This is because when you provide a destination, Stripe will settle charges in the country of the destination account.

[settle charges in the country of the destination account](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant)

- The next_source_action dictionary on PaymentIntents no longer contains the source_type property. To view the source type when retrieving PaymentIntents, expand the source parameter.

[expand](https://stripe.com/docs/api/expanding_objects)

- The description field on customer endpoints has a maximum character length limit of 350 now. The name field on product endpoints has a maximum character length limit of 250 now. The description field on invoice line items has a maximum character length limit of 500 now.

The description field on customer endpoints has a maximum character length limit of 350 now. The name field on product endpoints has a maximum character length limit of 250 now. The description field on invoice line items has a maximum character length limit of 500 now.

- The billing_reason attribute of the invoice object now can take the value of subscription_create, indicating that it is the first invoice of a subscription. For older API versions, billing_reason=subscription_create is represented as subscription_update.

The billing_reason attribute of the invoice object now can take the value of subscription_create, indicating that it is the first invoice of a subscription. For older API versions, billing_reason=subscription_create is represented as subscription_update.

- FileUpload objects have been renamed to File objects. Additionally, the url attribute now contains an authenticated URL (i.e. you will need to use your secret API key to download the file’s contents.) You can create a file link to obtain a publicly-accessible URL for the file.

FileUpload objects have been renamed to File objects. Additionally, the url attribute now contains an authenticated URL (i.e. you will need to use your secret API key to download the file’s contents.) You can create a file link to obtain a publicly-accessible URL for the file.

[create a file link](/api#create_file_link)

- When creating or updating a SKU, its attribute values no longer need to be unique. It is now possible to create multiple SKUs without attributes or with identical attribute values.

When creating or updating a SKU, its attribute values no longer need to be unique. It is now possible to create multiple SKUs without attributes or with identical attribute values.

- You can no longer set at_period_end in the subscription DELETE endpoints. The DELETE endpoint is reserved for immediate canceling going forward. Use cancel_at_period_end on the subscription update endpoints instead.

You can no longer set at_period_end in the subscription DELETE endpoints. The DELETE endpoint is reserved for immediate canceling going forward. Use cancel_at_period_end on the subscription update endpoints instead.

- The customer object’s business_vat_id was changed from String to Hash called tax_info, consisting of tax_id and type, in both requests and responses.

The customer object’s business_vat_id was changed from String to Hash called tax_info, consisting of tax_id and type, in both requests and responses.

[customer object](https://stripe.com/docs/api/customers)

- The amount field field in the tiers configuration for plans was renamed to unit_amount.

The amount field field in the tiers configuration for plans was renamed to unit_amount.

- The subscription endpoints no longer support the source parameter. If you want to change the default source for a customer, instead use the source creation API to add the new source and then the customer update API to set it as the default.

The subscription endpoints no longer support the source parameter. If you want to change the default source for a customer, instead use the source creation API to add the new source and then the customer update API to set it as the default.

[source creation API](https://stripe.com/docs/api#create_source)

[customer update API](https://stripe.com/docs/api#update_customer)

- When ending a trial on a subscription using trial_end=now the updated subscription will now receive a trial_end timestamp from the time of the request rather than being unset.

When ending a trial on a subscription using trial_end=now the updated subscription will now receive a trial_end timestamp from the time of the request rather than being unset.

- The percent_off field of coupons was changed from Integer to Float, with a precision of two decimal places.

The percent_off field of coupons was changed from Integer to Float, with a precision of two decimal places.

- When creating or updating a customer the email parameter must contain an email address of valid shape.

When creating or updating a customer the email parameter must contain an email address of valid shape.

- Products no longer have SKU lists embedded.

Products no longer have SKU lists embedded.

- MajorThe id field of invoice line items of type=subscription no longer can be interpreted as a subscription ID, but instead is a unique invoice line item ID. It can be used for pagination.

The id field of invoice line items of type=subscription no longer can be interpreted as a subscription ID, but instead is a unique invoice line item ID. It can be used for pagination.

- Coupon, SKU, customer, product and plan ids may only contain alphanumeric and _- characters on creation.

Coupon, SKU, customer, product and plan ids may only contain alphanumeric and _- characters on creation.

- MajorWhen creating or updating subscriptions, the default value of trial_from_plan is now false, meaning that a subscription will not automatically inherit a plan’s trial_period_days. If a subscription is already trialing, switching to a new plan without specifying trial_from_plan will maintain the trial. We recommend setting an explicit trial per subscription instead of setting trials on plans.

When creating or updating subscriptions, the default value of trial_from_plan is now false, meaning that a subscription will not automatically inherit a plan’s trial_period_days. If a subscription is already trialing, switching to a new plan without specifying trial_from_plan will maintain the trial. We recommend setting an explicit trial per subscription instead of setting trials on plans.

- When changing the plan on a subscription to a new plan with a trial (together with trial_from_plan=true), the new plan’s full trial period will be added to the subscription, without subtracting already-used time from previous trials.

When changing the plan on a subscription to a new plan with a trial (together with trial_from_plan=true), the new plan’s full trial period will be added to the subscription, without subtracting already-used time from previous trials.

- Updating a subscription set to cancel on a future date no longer clears the cancellation status. In order to clear the cancellation status, specify cancel_at_period_end=false when updating a subscription.

Updating a subscription set to cancel on a future date no longer clears the cancellation status. In order to clear the cancellation status, specify cancel_at_period_end=false when updating a subscription.

[cancel_at_period_end=false](/api#update_subscription-cancel_at_period_end)

- For a Source’s card[three_d_secure] property, adds recommended as a possible value. Previously, the only valid values were not supported, optional, and required.

For a Source’s card[three_d_secure] property, adds recommended as a possible value. Previously, the only valid values were not supported, optional, and required.

- MajorEach plan object is now linked to a product object with type=service. The plan object statement_descriptor and name attributes have been moved to product objects, and plan objects now have a nickname attribute. Creating a plan now requires passing a product attribute to POST /v1/plans. This may be either an existing product ID or a dictionary of product fields, so that you may continue to create plans without separately creating products.

Each plan object is now linked to a product object with type=service. The plan object statement_descriptor and name attributes have been moved to product objects, and plan objects now have a nickname attribute. Creating a plan now requires passing a product attribute to POST /v1/plans. This may be either an existing product ID or a dictionary of product fields, so that you may continue to create plans without separately creating products.

[moved to product](/api#product_object-statement_descriptor)

[product attribute](/api#create_plan-product)

- Products now have a required type: good for products used with Orders SKUs, or service for products used with Subscriptions and Plans.On API versions older than 2018-02-05, type is set to good by default, and GET /v1/products omits products with type=service from the list. (If you want to see products with type=service on API versions older than 2018-02-05, you can specify type=service when listing products.)

Products now have a required type: good for products used with Orders SKUs, or service for products used with Subscriptions and Plans.

- On API versions older than 2018-02-05, type is set to good by default, and GET /v1/products omits products with type=service from the list. (If you want to see products with type=service on API versions older than 2018-02-05, you can specify type=service when listing products.)

[type=service](/api/products/list#list_products-type)

- MajorAllows a new subscription’s first full invoice to be on a future date, by specifying billing_cycle_anchor, with an optional proration up to that date.billing_cycle_anchor on its own is available retroactively to past versions, and starting in this version, billing_cycle_anchor can be combined with a trial, enabling a free trial to be followed by a prorated period, followed by a fixed billing cycle.

Allows a new subscription’s first full invoice to be on a future date, by specifying billing_cycle_anchor, with an optional proration up to that date.billing_cycle_anchor on its own is available retroactively to past versions, and starting in this version, billing_cycle_anchor can be combined with a trial, enabling a free trial to be followed by a prorated period, followed by a fixed billing cycle.

- Prorations on free plans now create $0 invoices. In past versions, these did not create invoices.

Prorations on free plans now create $0 invoices. In past versions, these did not create invoices.

- When being viewed by a platform, cards and bank accounts created on behalf of connected accounts will have a fingerprint that is universal across all connected accounts. For accounts that are not connect platforms, there will be no change.

When being viewed by a platform, cards and bank accounts created on behalf of connected accounts will have a fingerprint that is universal across all connected accounts. For accounts that are not connect platforms, there will be no change.

- Updates invoice payment attempts to return a card_error when the charge is declined. This aligns /v1/invoices/{INVOICE_ID}/pay with /v1/charges.

Updates invoice payment attempts to return a card_error when the charge is declined. This aligns /v1/invoices/{INVOICE_ID}/pay with /v1/charges.

- Updates invoice line items to always have a description set, including invoice line items generated from subscription items.

Updates invoice line items to always have a description set, including invoice line items generated from subscription items.

- Adds not_required as a possible redirect[status] value on the Source object. Previously, optional redirects were marked as succeeded.

Adds not_required as a possible redirect[status] value on the Source object. Previously, optional redirects were marked as succeeded.

- Adds under_review as a possible verification[disabled_reason] value on the Account object. Previously, an under review status used the value other.

Adds under_review as a possible verification[disabled_reason] value on the Account object. Previously, an under review status used the value other.

- Replaces the managed Boolean property on Account objects with type, whose possible values are: standard, express, and custom. A type value is required when creating accounts. The standard type replaces managed: false, and the custom type replaces managed: true.

Replaces the managed Boolean property on Account objects with type, whose possible values are: standard, express, and custom. A type value is required when creating accounts. The standard type replaces managed: false, and the custom type replaces managed: true.

- Updates the previous_attributes property on Event objects to show entire sub-arrays when those arrays have changes. Previously, those sub-arrays only showed the specific fields that changed.

Updates the previous_attributes property on Event objects to show entire sub-arrays when those arrays have changes. Previously, those sub-arrays only showed the specific fields that changed.

- Updates the request property on the Event object to be a hash containing the request ID and the idempotency key. Previously, request was just the ID.

Updates the request property on the Event object to be a hash containing the request ID and the idempotency key. Previously, request was just the ID.

- Renames the user_id property on Connect-related event objects to account.

Renames the user_id property on Connect-related event objects to account.

- MajorSplits the Transfer object into Payout and Transfer. The Payout object represents money moving from a Stripe account to an external account (bank or debit card). The Transfer object now only represents money moving between Stripe accounts on a Connect platform. For more details, see https://stripe.com/docs/transfer-payout-split.

Splits the Transfer object into Payout and Transfer. The Payout object represents money moving from a Stripe account to an external account (bank or debit card). The Transfer object now only represents money moving between Stripe accounts on a Connect platform. For more details, see https://stripe.com/docs/transfer-payout-split.

[https://stripe.com/docs/transfer-payout-split](https://stripe.com/docs/transfer-payout-split)

- Updates the dispute property on the Charge object to contain the ID of an associated dispute. Previously, dispute contained the entire Dispute object. You can expand this property when retrieving charges to render the full Dispute object as before.

Updates the dispute property on the Charge object to contain the ID of an associated dispute. Previously, dispute contained the entire Dispute object. You can expand this property when retrieving charges to render the full Dispute object as before.

[expand this property](https://stripe.com/docs/api#expanding_objects)

- Updates the outcome[rule] property on the Charge object to contain the ID of the rule that blocked the charge. Previously, outcome[rule] contained the entire Rule object. You can expand this property when retrieving charges to render the full Rule object as before.

Updates the outcome[rule] property on the Charge object to contain the ID of the rule that blocked the charge. Previously, outcome[rule] contained the entire Rule object. You can expand this property when retrieving charges to render the full Rule object as before.

[expand this property](https://stripe.com/docs/api#expanding_objects)

- Removes the sourced_transfers property from the Balance Transaction object.

Removes the sourced_transfers property from the Balance Transaction object.

- Returns the status code 403 when an API request is made with insufficient permission. Previously, the API returned a 401 status code.

Returns the status code 403 when an API request is made with insufficient permission. Previously, the API returned a 401 status code.

- Updates the list all subscriptions call to also return canceled subscriptions. The endpoint now supports fetching only canceled subscriptions by specifying status=canceled. You can now retrieve a single canceled subscription by providing its ID.

Updates the list all subscriptions call to also return canceled subscriptions. The endpoint now supports fetching only canceled subscriptions by specifying status=canceled. You can now retrieve a single canceled subscription by providing its ID.

- Updates the active property on the Product object so that setting active to false no longer marks the product’s SKUs as inactive.

Updates the active property on the Product object so that setting active to false no longer marks the product’s SKUs as inactive.

- Removes the currencies_supported property from the Account object. You can find a list of supported currencies by retrieving a Country Spec object for the country of the account.

Removes the currencies_supported property from the Account object. You can find a list of supported currencies by retrieving a Country Spec object for the country of the account.

- Adds postal code validation for legal entity addresses when creating and updating accounts.

Adds postal code validation for legal entity addresses when creating and updating accounts.

- Updates the behavior of orders so that changing an order from paid or fulfilled to canceled or returned automatically refunds the associated charge. Previously, attempting to change an order from paid or fulfilled to canceled or returned raised an error if the associated charge had not already been refunded.

Updates the behavior of orders so that changing an order from paid or fulfilled to canceled or returned automatically refunds the associated charge. Previously, attempting to change an order from paid or fulfilled to canceled or returned raised an error if the associated charge had not already been refunded.

- Returns an error on attempts to add more than 250 invoice items to an invoice.

Returns an error on attempts to add more than 250 invoice items to an invoice.

- Renames the name property on the Bank Account object to account_holder_name.

Renames the name property on the Bank Account object to account_holder_name.

- Updates the returned Account object to only show sub-properties of legal_entity that are applicable to the account’s country, or that were previously provided.

Updates the returned Account object to only show sub-properties of legal_entity that are applicable to the account’s country, or that were previously provided.

- Returns an error if a tax_percent is provided without a plan during a customer update or creation.

Returns an error if a tax_percent is provided without a plan during a customer update or creation.

- MajorReturns an error when invalid parameters are passed in the card or bank account hash during token, source, or external account creation. Changes the error code returned for missing required parameters in the card or bank account hash to 400. Previously, a 402 code was returned.

Returns an error when invalid parameters are passed in the card or bank account hash during token, source, or external account creation. Changes the error code returned for missing required parameters in the card or bank account hash to 400. Previously, a 402 code was returned.

- Replaces the bank_accounts property on the Account object with external_accounts. Replaces the bank_account value in the fields_needed property with external_account.

Replaces the bank_accounts property on the Account object with external_accounts. Replaces the bank_account value in the fields_needed property with external_account.

- Updates the charge property on the Invoice object to always show the invoice’s latest charge, regardless of the charge’s source (e.g, a card or a bank account). Removes the payment property, which previously reflected a non-card charge.

Updates the charge property on the Invoice object to always show the invoice’s latest charge, regardless of the charge’s source (e.g, a card or a bank account). Removes the payment property, which previously reflected a non-card charge.

- MajorUpdates the list all charges call to return all charges, including those made to bank accounts and other non-card sources. Previously, it only returned charges made to cards. Updates the deprecated offset parameter to only be supported when filtering by source type.

Updates the list all charges call to return all charges, including those made to bank accounts and other non-card sources. Previously, it only returned charges made to cards. Updates the deprecated offset parameter to only be supported when filtering by source type.

- Updates API rate limit errors to return a 429 HTTP status code instead of 400. They also no longer return a rate_limit error code.

Updates API rate limit errors to return a 429 HTTP status code instead of 400. They also no longer return a rate_limit error code.

- Returns an error if a request reuses an idempotency token with different parameters than the original request. Previously, errors were only returned for reusing the same idempotency token across different API endpoints.

Returns an error if a request reuses an idempotency token with different parameters than the original request. Previously, errors were only returned for reusing the same idempotency token across different API endpoints.

- Updates the Balance Transaction object to provide the refund ID or dispute ID as the source value when the balance transaction is associated with a refund or dispute. Previously, the original charge ID was shown.

Updates the Balance Transaction object to provide the refund ID or dispute ID as the source value when the balance transaction is associated with a refund or dispute. Previously, the original charge ID was shown.

- Adds date validation to the tos_acceptance[date] property on the Account object. Accepted values are timestamps after 2009 and before the current moment.

Adds date validation to the tos_acceptance[date] property on the Account object. Accepted values are timestamps after 2009 and before the current moment.

- The balance.available event is now triggered when immediate transfers are processed.

The balance.available event is now triggered when immediate transfers are processed.

- Replaces the verification[contacted] Boolean property on the Account object with a verification[disabled_reason] string that describes why the account is unable to make transfers or charges.

Replaces the verification[contacted] Boolean property on the Account object with a verification[disabled_reason] string that describes why the account is unable to make transfers or charges.

- Updates the status property on the Transfer object so that transfers not yet submitted to the bank are still pending and transfers submitted to the bank that have not yet arrived are in_transit. Previously, both states were described as pending.

Updates the status property on the Transfer object so that transfers not yet submitted to the bank are still pending and transfers submitted to the bank that have not yet arrived are in_transit. Previously, both states were described as pending.

- Updates the payout_schedule[delay_days] property on the Account object to return an error if provided when the interval is set to manual. Manual payouts always use the minimum delay_days value.

Updates the payout_schedule[delay_days] property on the Account object to return an error if provided when the interval is set to manual. Manual payouts always use the minimum delay_days value.

- Updates the period[end] property on proration invoice line items to reflect the subscription’s current_period_end property when the update and proration was made. A proration invoice line item’s period[start] and period[end] properties now represent the prorated adjustment interval. Previously, period[end] marked the time at which the proration was made, and was the same as period[start].

Updates the period[end] property on proration invoice line items to reflect the subscription’s current_period_end property when the update and proration was made. A proration invoice line item’s period[start] and period[end] properties now represent the prorated adjustment interval. Previously, period[end] marked the time at which the proration was made, and was the same as period[start].

- Updates the Invoice object to change the order of the lines list: first invoice items in reverse chronological order, followed by the subscription, if applicable.

Updates the Invoice object to change the order of the lines list: first invoice items in reverse chronological order, followed by the subscription, if applicable.

- Updates coupons so they no longer apply to negative invoice items by default. Previously, coupons applied to all non-proration invoice items. To allow a coupon to apply to a negative invoice item, pass discountable=true when creating or updating the invoice item.

Updates coupons so they no longer apply to negative invoice items by default. Previously, coupons applied to all non-proration invoice items. To allow a coupon to apply to a negative invoice item, pass discountable=true when creating or updating the invoice item.

- Updates the status property on the Charge object to have a value of succeeded for successful charges. Previously, the status property would be paid for successful charges.

Updates the status property on the Charge object to have a value of succeeded for successful charges. Previously, the status property would be paid for successful charges.

- MajorReplaces the card property on the Charge object with source. Provide this parameter with a Card token, as before, or with a Source token that has an object value of card. Older API versions return both the card and source properties on Charge.

Replaces the card property on the Charge object with source. Provide this parameter with a Card token, as before, or with a Source token that has an object value of card. Older API versions return both the card and source properties on Charge.

- MajorReplaces the cards and default_card properties on the Customer object with sources and default_source. Both properties can represent Card objects, as before, and Source objects with an object value of card. Older API versions return both the new and old properties on Customer. Replaces the customer.card.* and customer.bank_account.* events with customer.source.*.

Replaces the cards and default_card properties on the Customer object with sources and default_source. Both properties can represent Card objects, as before, and Source objects with an object value of card. Older API versions return both the new and old properties on Customer. Replaces the customer.card.* and customer.bank_account.* events with customer.source.*.

- Renames the transfer.canceled event to transfer.reversed.

Renames the transfer.canceled event to transfer.reversed.

- Adds the value warning_closed to the status property on the Dispute object.

Adds the value warning_closed to the status property on the Dispute object.

- Updates test mode transfers to require sufficient funds in your available test mode balance (for consistency with live mode transfers). Add funds directly to your available test mode balance—bypassing the pending balance—by creating a charge using the special test card number 4000 0000 0000 0077.

Updates test mode transfers to require sufficient funds in your available test mode balance (for consistency with live mode transfers). Add funds directly to your available test mode balance—bypassing the pending balance—by creating a charge using the special test card number 4000 0000 0000 0077.

- Updates the presentation of nested hashes in the previous_attributes property of events to only show the difference. For example, a change from {address: {line1: "Foo", line2: "Bar"}} to {address: {line1: "Foo", line2: "Baz"}} is represented as {previous_attributes: {address: {line2: "Baz"}}}. Previously, it was represented as {previous_attributes: {address: {line1: "Foo", line2: "Baz"}}}.

Updates the presentation of nested hashes in the previous_attributes property of events to only show the difference. For example, a change from {address: {line1: "Foo", line2: "Bar"}} to {address: {line1: "Foo", line2: "Baz"}} is represented as {previous_attributes: {address: {line2: "Baz"}}}. Previously, it was represented as {previous_attributes: {address: {line1: "Foo", line2: "Baz"}}}.

- Updates the canceled_at property on the Subscription object to always be the timestamp from the API call or invoice payment failure that canceled the subscription. Previously, canceled_at reflected “at period end” subscription cancellations, too. The ended_at property still reflects the time that the subscription actually stopped.

Updates the canceled_at property on the Subscription object to always be the timestamp from the API call or invoice payment failure that canceled the subscription. Previously, canceled_at reflected “at period end” subscription cancellations, too. The ended_at property still reflects the time that the subscription actually stopped.

- Removes the mimetype property from the File Upload object. Returns simplified file types in the type property and uses simpler naming conventions than mimetypes (e.g., type contains pdf instead of application/pdf).

Removes the mimetype property from the File Upload object. Returns simplified file types in the type property and uses simpler naming conventions than mimetypes (e.g., type contains pdf instead of application/pdf).

- Updates the Card object so a value of unchecked for the address_line1_check, address_zip_check, or cvc_check properties means the property has not been checked. Previously, it meant the issuing bank does not support the particular check. That state now shows as unavailable. Unchecked properties are checked when a card is charged or added to a Customer object.

Updates the Card object so a value of unchecked for the address_line1_check, address_zip_check, or cvc_check properties means the property has not been checked. Previously, it meant the issuing bank does not support the particular check. That state now shows as unavailable. Unchecked properties are checked when a card is charged or added to a Customer object.

- Removes the customer property from the Card object that appears on the Token object.

Removes the customer property from the Card object that appears on the Token object.

- Replaces the statement_description property on the Charge, Invoice, Plan, and Transfer objects with statement_descriptor. To determine what appears on a customer’s transaction, statement_description is appended to your Stripe account’s statement descriptor while statement_descriptor sets the full statement value. If not on this API version or newer, providing a statement_descriptor still triggers the statement_description behavior. Regardless of API version, the statement_description behavior does not apply with PaymentIntents.

Replaces the statement_description property on the Charge, Invoice, Plan, and Transfer objects with statement_descriptor. To determine what appears on a customer’s transaction, statement_description is appended to your Stripe account’s statement descriptor while statement_descriptor sets the full statement value. If not on this API version or newer, providing a statement_descriptor still triggers the statement_description behavior. Regardless of API version, the statement_description behavior does not apply with PaymentIntents.

- Updates the Accounts API to require API version 2014-12-17 or newer.

Updates the Accounts API to require API version 2014-12-17 or newer.

- Updates the Dispute object so evidence can be provided as a hash of typed fields rather than a single block of text. Replaces the evidence_due_by property with the evidence_details hash, which includes due_by and submission_count (for the number of times a dispute has been submitted).

Updates the Dispute object so evidence can be provided as a hash of typed fields rather than a single block of text. Replaces the evidence_due_by property with the evidence_details hash, which includes due_by and submission_count (for the number of times a dispute has been submitted).

- Updates disputes that are won to return the status won even if the charge was refunded. Previously, a dispute won that had a refunded charge would transition to charge_refunded.

Updates disputes that are won to return the status won even if the charge was refunded. Previously, a dispute won that had a refunded charge would transition to charge_refunded.

- Updates the metadata property of the Invoice Item object with a type of subscription to show the subscription’s metadata. Previously, it showed the plan’s metadata.

Updates the metadata property of the Invoice Item object with a type of subscription to show the subscription’s metadata. Previously, it showed the plan’s metadata.

- Renames the charge_enabled and transfer_enabled properties on the Account object to charges_enabled and transfers_enabled.

Renames the charge_enabled and transfer_enabled properties on the Account object to charges_enabled and transfers_enabled.

- Prevents publishable keys from retrieving Token objects. When a card or bank account token is created with a publishable key, the fingerprint property is not included in the response.

Prevents publishable keys from retrieving Token objects. When a card or bank account token is created with a publishable key, the fingerprint property is not included in the response.

- Replaces the disabled, validated, and verified properties on the Bank Account object with a status enum property.

Replaces the disabled, validated, and verified properties on the Bank Account object with a status enum property.

- Adds three values to the status property on the Dispute object: warning_needs_response, warning_under_review, and charge_refunded. Replaces the balance_transaction property of the Dispute object with balance_transactions (this provides greater detail around funds withdrawn and reinstated as a result of disputes).

Adds three values to the status property on the Dispute object: warning_needs_response, warning_under_review, and charge_refunded. Replaces the balance_transaction property of the Dispute object with balance_transactions (this provides greater detail around funds withdrawn and reinstated as a result of disputes).

- Removes the other_transfers, summary, and transactions properties from automatic transfer responses in favor of the balance history endpoint (/v1/balance/history).

Removes the other_transfers, summary, and transactions properties from automatic transfer responses in favor of the balance history endpoint (/v1/balance/history).

- Changes the refunds property on the Application Fee object from an array to a sublist object, which contains the data, has_more, and url properties. This makes application fee refunds consistent with charge refunds.

Changes the refunds property on the Application Fee object from an array to a sublist object, which contains the data, has_more, and url properties. This makes application fee refunds consistent with charge refunds.

- Updates proration line items on invoices to include the associated subscription’s plan and quantity.

Updates proration line items on invoices to include the associated subscription’s plan and quantity.

- Changes the refunds property on the Charge object from an array to a sublist object, which contains the data, has_more, and url properties.

Changes the refunds property on the Charge object from an array to a sublist object, which contains the data, has_more, and url properties.

- Renames the type property on the Card object to brand.

Renames the type property on the Card object to brand.

- Replaces the account property on the Transfer object with bank_account. The bank_account property is only included when the transfer is made to a bank account.

Replaces the account property on the Transfer object with bank_account. The bank_account property is only included when the transfer is made to a bank account.

- MajorRemoves the count property from list responses.

Removes the count property from list responses.

- Renames the statement_descriptor property on the Transfer object to statement_description.

Renames the statement_descriptor property on the Transfer object to statement_description.

- MajorReplaces the subscription property on the Customer object with the subscriptions property, as customers can have multiple subscriptions.

Replaces the subscription property on the Customer object with the subscriptions property, as customers can have multiple subscriptions.

- Ignores trial dates on canceled subscriptions when automatically computing trial end dates for new subscriptions.

Ignores trial dates on canceled subscriptions when automatically computing trial end dates for new subscriptions.

- Replaces the user and user_email properties on the Application Fee object with an expandable account property.

Replaces the user and user_email properties on the Application Fee object with an expandable account property.

- Updates the refunding of application fees to be proportional to the amount of the charge refunded (when setting refund_application_fee=true). Previously, the entire application fee was refunded even when only part of the charge was.

Updates the refunding of application fees to be proportional to the amount of the charge refunded (when setting refund_application_fee=true). Previously, the entire application fee was refunded even when only part of the charge was.

- MajorChanges coupon behavior so that applying an amount-off coupon to an invoice does not increase the Customer account balance if the discount is greater than the invoice amount. Coupons are ignored—and not counted as redeemed—when applied to zero-cost invoices. This change does not apply to coupons created on earlier API version.

Changes coupon behavior so that applying an amount-off coupon to an invoice does not increase the Customer account balance if the discount is greater than the invoice amount. Coupons are ignored—and not counted as redeemed—when applied to zero-cost invoices. This change does not apply to coupons created on earlier API version.

- Removes the fee and fee_details properties from the Charge and Transfer objects. Fee information is in the corresponding balance transaction.

Removes the fee and fee_details properties from the Charge and Transfer objects. Fee information is in the corresponding balance transaction.

- Allows the description property on Customer, Charge, InvoiceItem, and Recipient objects, and the email property on Customer and Recipient objects, to be set to null by providing empty string values in POST requests.

Allows the description property on Customer, Charge, InvoiceItem, and Recipient objects, and the email property on Customer and Recipient objects, to be set to null by providing empty string values in POST requests.

- MajorReplaces the active_card property on the Customer object with a cards sublist and a default_card ID property.

Replaces the active_card property on the Customer object with a cards sublist and a default_card ID property.

- Updates the Charge object so disputed charges include another stripe_fee object in the fee_details array, representing the dispute fees. Includes the dispute fees in the fee total on the Charge object.

Updates the Charge object so disputed charges include another stripe_fee object in the fee_details array, representing the dispute fees. Includes the dispute fees in the fee total on the Charge object.

- MajorUpdates the pay invoice call to return an error when the charge is not successful. Previously, the API would return a 200 status and set the invoice’s paid property to false.

Updates the pay invoice call to return an error when the charge is not successful. Previously, the API would return a 200 status and set the invoice’s paid property to false.

- Replaces the disputed property on the Charge object with dispute.

Replaces the disputed property on the Charge object with dispute.

- Updates the Invoice object format. The lines property is now a sublist, a paginated list of all items that contribute to the invoice.

Updates the Invoice object format. The lines property is now a sublist, a paginated list of all items that contribute to the invoice.

- Removes the extraneous id property from the Discount object.

Removes the extraneous id property from the Discount object.

- Removes the uncaptured property from the Customer object.

Removes the uncaptured property from the Customer object.

- (Changes introduced in this version have since been removed.)

- Removes the amount and currency properties from the Token object.

Removes the amount and currency properties from the Token object.

- Removes the next_recurring_charge property from the Customer object. Use the upcoming invoice call instead.

Removes the next_recurring_charge property from the Customer object. Use the upcoming invoice call instead.

- Shows all response fields, even those with null values. Previously, the API hid fields with null values.

Shows all response fields, even those with null values. Previously, the API hid fields with null values.

- (Changes introduced in this version have since been removed.)

- Updates the card validation behavior when creating tokens.

Updates the card validation behavior when creating tokens.

- Updates the list format. New list objects have a data property that represents an array of objects (by default, 10) and a count property that represents the total count.

Updates the list format. New list objects have a data property that represents an array of objects (by default, 10) and a count property that represents the total count.

- Removes the identifier property (duplicate of id) from the Plan object.

Removes the identifier property (duplicate of id) from the Plan object.

- Raises exceptions on unrecognized parameters passed to the API instead of silently allowing and ignoring them.

Raises exceptions on unrecognized parameters passed to the API instead of silently allowing and ignoring them.

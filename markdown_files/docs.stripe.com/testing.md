htmlTest payment methods | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Testing

Simulate payments to test your integration.### Not a developer?

Check out our no-code docs, use a prebuilt solution from our partner directory, or hire a Stripe-certified expert.

To confirm that your integration works correctly, simulate transactions without moving any money using special values in test mode.

Test cards let you simulate several scenarios:

- Successful payments by[card brand](#cards)or[country](#international-cards)
- Card errors due to[declines](#declined-payments),[fraud](#fraud-prevention), or[invalid data](#invalid-data)
- [Disputes](#disputes)and[refunds](/testing#refunds)
- Authentication with[3D Secure](#regulatory-cards)and[PINs](#terminal)

Testing non-card payments works similarly. Each payment method has its own special values. Because of rate limits, we don’t recommend using test mode to load-test your integration. Instead, see our documentation on load testing.

## How to use test cards

Any time you work with a test card, use test API keys in all API calls. This is true whether you’re serving a payment form to test interactively or writing test code.

Common mistakeDon’t use real card details. The Stripe Services Agreement prohibits testing in live mode using real payment method details. Use your test API keys and the card numbers below.

### Testing interactively

When testing interactively, use a card number, such as 4242 4242 4242 4242.  Enter the card number in the Dashboard or in any payment form.

- Use a valid future date, such as12/34.
- Use any three-digit CVC (four digits for American Express cards).
- Use any value you like for other form fields.

![An example payment form showing how to enter a test card number. The card number is "4242 4242 4242 4242", the expiration date is "12/34", and the CVC is "567". Other fields have arbitrary values. For instance, the email address is "test@example.com"](https://b.stripecdn.com/docs-statics-srv/assets/test-card.c3f9b3d1a3e8caca3c9f4c9c481fd49c.jpg)

Testing a form interactively with the test card number 4242 4242 4242 4242

### Test code

When writing test code, use a PaymentMethod such as pm_card_visa instead of a card number. We don’t recommend using card numbers directly in API calls or server-side code, even in test mode. If you do use them, your code might not be PCI-compliant when you go live. By default, a PaymentMethod isn’t attached to a Customer.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=500 \
  -d currency=gbp \
  -d payment_method=pm_card_visa`Most integrations don’t use Tokens anymore, but we make test Tokens such as tok_visa available if you need them.

When you’re ready to take your integration live, replace your test publishable and secret API keys with live ones. You can’t process live payments if your integration is still using your test API keys.

## Cards by brand

To simulate a successful payment, use test cards from the following list. The billing country for each test card is set to the United States. If you need to create test card payments using cards for other billing countries, use international test cards.

CautionCross border fees are assessed based on the country of the card issuer. While each of the cards in this section use US as the billing country, cards where the issuer country isn’t the US (such as JCB and UnionPay) might be subject to a cross border fee, even in test mode.

Card numbersPaymentMethodsTokensBrandNumberCVCDateVisa4242424242424242Any 3 digitsAny future dateVisa (debit)4000056655665556Any 3 digitsAny future dateMastercard5555555555554444Any 3 digitsAny future dateMastercard (2-series)2223003122003222Any 3 digitsAny future dateMastercard (debit)5200828282828210Any 3 digitsAny future dateMastercard (prepaid)5105105105105100Any 3 digitsAny future dateAmerican Express378282246310005Any 4 digitsAny future dateAmerican Express371449635398431Any 4 digitsAny future dateDiscover6011111111111117Any 3 digitsAny future dateDiscover6011000990139424Any 3 digitsAny future dateDiscover (debit)6011981111111113Any 3 digitsAny future dateDiners Club3056930009020004Any 3 digitsAny future dateDiners Club (14-digit card)36227206271667Any 3 digitsAny future dateBCcard and DinaCard6555900000604105Any 3 digitsAny future dateJCB3566002020360505Any 3 digitsAny future dateUnionPay6200000000000005Any 3 digitsAny future dateUnionPay (debit)6200000000000047Any 3 digitsAny future dateUnionPay (19-digit card)6205500000000000004Any 3 digitsAny future dateMost Cartes Bancaires and eftpos cards are co-branded with either Visa or Mastercard. The test cards in the following table simulate successful payments with co-branded cards.

Card numbersPaymentMethodsTokensBrand/Co-brandNumberCVCDateCartes Bancaires/Visa4000002500001001Any 3 digitsAny future dateCartes Bancaires/Mastercard5555552500001001Any 3 digitsAny future dateeftpos Australia/Visa4000050360000001Any 3 digitsAny future dateeftpos Australia/Mastercard5555050360000080Any 3 digitsAny future date## Cards by country

To simulate successful payments from specific countries, use test cards from the following sections.

Card numbersPaymentMethodsTokensCountryNumberBrandAMERICASUnited States (US)4242424242424242VisaArgentina (AR)4000000320000021VisaBrazil (BR)4000000760000002VisaCanada (CA)4000001240000000VisaChile (CL)4000001520000001VisaColombia (CO)4000001700000003VisaCosta Rica (CR)4000001880000005VisaEcuador (EC)4000002180000000VisaMexico (MX)4000004840008001VisaPanama (PA)4000005910000000VisaParaguay (PY)4000006000000066VisaPeru (PE)4000006040000068VisaUruguay (UY)4000008580000003VisaEUROPE and MIDDLE EASTSecurity tipStrong Customer Authentication regulations require 3D Secure authentication for online payments within the European Economic Area. The test cards in this section simulate a payment that succeeds without authentication. We recommend also testing scenarios that involve authentication, using 3D Secure test cards.

United Arab Emirates (AE)4000007840000001VisaUnited Arab Emirates (AE)5200007840000022MastercardAustria (AT)4000000400000008VisaBelgium (BE)4000000560000004VisaBulgaria (BG)4000001000000000VisaBelarus (BY)4000001120000005VisaCroatia (HR)4000001910000009VisaCyprus (CY)4000001960000008VisaCzech Republic (CZ)4000002030000002VisaDenmark (DK)4000002080000001VisaEstonia (EE)4000002330000009VisaFinland (FI)4000002460000001VisaFrance (FR)4000002500000003VisaGermany (DE)4000002760000016VisaGibraltar (GI)4000002920000005VisaGreece (GR)4000003000000030VisaHungary (HU)4000003480000005VisaIreland (IE)4000003720000005VisaItaly (IT)4000003800000008VisaLatvia (LV)4000004280000005VisaLiechtenstein (LI)4000004380000004VisaLithuania (LT)4000004400000000VisaLuxembourg (LU)4000004420000006VisaMalta (MT)4000004700000007VisaNetherlands (NL)4000005280000002VisaNorway (NO)4000005780000007VisaPoland (PL)4000006160000005VisaPortugal (PT)4000006200000007VisaRomania (RO)4000006420000001VisaSaudi Arabia (SA)4000006820000007VisaSlovenia (SI)4000007050000006VisaSlovakia (SK)4000007030000001VisaSpain (ES)4000007240000007VisaSweden (SE)4000007520000008VisaSwitzerland (CH)4000007560000009VisaUnited Kingdom (GB)4000008260000000VisaUnited Kingdom (GB)4000058260000005Visa (debit)United Kingdom (GB)5555558265554449MastercardASIA PACIFICRegional considerationsIndiaTo test subscriptions that require mandates and pre-debit notifications, see India recurring payments.

Australia (AU)4000000360000006VisaChina (CN)4000001560000002VisaHong Kong (HK)4000003440000004VisaIndia (IN)4000003560000008VisaJapan (JP)4000003920000003VisaJapan (JP)3530111333300000JCBMalaysia (my)4000004580000002VisaNew Zealand (NZ)4000005540000008VisaSingapore (SG)4000007020000003VisaTaiwan (TW)4000001580000008VisaThailand (TH)4000007640000003Visa (credit)Thailand (TH)4000057640000008Visa (debit)## Declined payments

To test your integration’s error-handling logic by simulating payments that the issuer declines for various reasons, use test cards from this section. Using one of these cards results in a card error with the given error code and decline code.

Common mistakeTo simulate an incorrect CVC, you must provide one using any three-digit number. If you don’t provide a CVC, Stripe doesn’t perform the CVC check, so the check can’t fail.

Card numbersPayment MethodTokensDescriptionNumberError codeDecline codeGeneric decline4000000000000002[card_declined](/error-codes#card-declined)[generic_decline](/declines/codes#generic_decline)Insufficient funds decline4000000000009995[card_declined](/error-codes#card-declined)[insufficient_funds](/declines/codes#insufficient_funds)Lost card decline4000000000009987[card_declined](/error-codes#card-declined)[lost_card](/declines/codes#lost_card)Stolen card decline4000000000009979[card_declined](/error-codes#card-declined)[stolen_card](/declines/codes#stolen_card)Expired card decline4000000000000069[expired_card](/error-codes#expired-card)n/aIncorrect CVC decline4000000000000127[incorrect_cvc](/error-codes#incorrect-cvc)n/aProcessing error decline4000000000000119[processing_error](/error-codes#processing-error)n/aIncorrect number decline4242424242424241[incorrect_number](/error-codes#incorrect-number)n/aExceeding velocity limit decline4000000000006975[card_declined](/error-codes#card-declined)[card_velocity_exceeded](/declines/codes#card_velocity_exceeded)The cards in the previous table can’t be attached to a Customer object. To simulate a declined payment with a successfully attached card, use the next one.

DescriptionNumberDetailsDecline after attaching4000000000000341Attaching this card to a[Customer](/api/customers)object succeeds, but attempts to charge the customer fail.## Fraud prevention

Stripe’s fraud prevention system, Radar, can block payments when they have a high risk level or fail verification checks. You can use the cards in this section to test your Radar settings. You can also use them to test how your integration responds to blocked payments.

Each card simulates specific risk factors. Your Radar settings determine which risk factors cause it to block a payment. Blocked payments result in card errors with an error code of fraud.

Common mistakeTo simulate a failed CVC check, you must provide a CVC using any three-digit number. To simulate a failed postal code check, you must provide any valid postal code. If you don’t provide those values, Radar doesn’t perform the corresponding checks, so the checks can’t fail.

Card numbersPaymentMethodsTokensDescriptionNumberDetailsAlways blocked

4100000000000019The charge has a risk level of “highest”

Radar always blocks it.

Highest risk

4000000000004954The charge has a risk level of “highest”

Radar might block it depending on your settings.

Elevated risk

4000000000009235The charge has a risk level of “elevated”

If you use Radar for Fraud Teams, Radar might queue it for review.

CVC check fails

4000000000000101If you provide a CVC number, the CVC check fails.

Radar might block it depending on your settings.

Postal code check fails

4000000000000036If you provide a postal code, the postal code check fails.

Radar might block it depending on your settings.

Line1 check fails

4000000000000028The address line 1 check fails.

The payment succeeds unless you block it with a custom Radar rule.

Address checks fail

4000000000000010The address postal code check and address line 1 check both fail.

Radar might block it depending on your settings.

Address unavailable

4000000000000044The address postal code check and address line 1 check are both unavailable.

The payment succeeds unless you block it with a custom Radar rule.

## Invalid data

To test errors resulting from invalid data, provide invalid details. You don’t need a special test card for this. Any invalid value works. For instance:

- [invalid_expiry_month](/error-codes#invalid-expiry-month): Use an invalid month, such as13.
- [invalid_expiry_year](/error-codes#invalid-expiry-year): Use a year up to 50 years in the past, such as95.
- [invalid_cvc](/error-codes#invalid-cvc): Use a two-digit number, such as99.
- [incorrect_number](/error-codes#incorrect-number): Use a card number that fails the[Luhn check](https://en.wikipedia.org/wiki/Luhn_algorithm), such as4242424242424241.

## Disputes

To simulate a disputed transaction, use the test cards in this section. Then, to simulate winning or losing the dispute, provide winning or losing evidence.

Card numbersPaymentMethodsTokensDescriptionNumberDetailsFraudulent4000000000000259With default account settings, charge succeeds, only to be disputed as[fraudulent](/disputes/categories). This type of dispute is[protected](/payments/3d-secure/authentication-flow#disputed-payments)after 3D Secure authentication.Not received4000000000002685With default account settings, charge succeeds, only to be disputed as[product not received](/disputes/categories). This type of dispute[isn’t protected](/payments/3d-secure/authentication-flow#disputed-payments)after 3D Secure authentication.Inquiry4000000000001976With default account settings, charge succeeds, only to be disputed as[an inquiry](/disputes/how-disputes-work#inquiries).Warning4000000000005423With default account settings, charge succeeds, only to receive[an early fraud warning](/disputes/how-disputes-work#early-fraud-warnings).Multiple disputes4000000404000079With default account settings, charge succeeds, only to be disputed[multiple times](/disputes/how-disputes-work#multiple-disputes).### Evidence

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.

- If you[respond using the API](/disputes/api), pass the value from the table as[uncategorized_text](/api/disputes/update#update_dispute-evidence-uncategorized_text).
- If you[respond in the Dashboard](/disputes/responding), enter the value from the table in theAdditional informationfield. Then, clickSubmit evidence.

EvidenceDescription`winning_evidence`The dispute is closed and marked as won. Your account is credited the amount of the charge and related fees.`losing_evidence`The dispute is closed and marked as lost. Your account isn’t credited.## Refunds

In live mode, refunds are asynchronous: a refund can appear to succeed and later fail, or can appear as pending at first and later succeed. To simulate refunds with those behaviors, use the test cards in this section. (With all other test cards, refunds succeed immediately and don’t change status after that.)

Card numbersPaymentMethodsTokensDescriptionNumberDetailsAsynchronous success4000000000007726The charge succeeds. If you initiate a refund, its status begins as`pending`. Some timelater, its status transitions to`succeeded`and sends a`charge.refund.updated`[webhook](/api/events/types#event_types-charge.refund.updated)event.Asynchronous failure4000000000005126The charge succeeds. If you initiate a refund, its status begins as`succeeded`. Some timelater, its status transitions to`failed`and sends a`charge.refund.updated`[webhook](/api/events/types#event_types-charge.refund.updated)event.## Available balance

To send the funds from a test transaction directly to your available balance, use the test cards in this section. Other test cards send funds from a successful payment to your pending balance.

Card numbersPaymentMethodsTokensDescriptionNumberDetailsBypass pending balance4000000000000077The US charge succeeds. Funds are added directly to your available balance, bypassing your pending balance.Bypass pending balance4000003720000278The international charge succeeds. Funds are added directly to your available balance, bypassing your pending balance.## 3D Secure authentication

3D Secure requires an additional layer of authentication for credit card transactions. The test cards in this section allow you to simulate triggering authentication in different payment flows.

Only cards in this section effectively test your 3D Secure integration by simulating defined 3DS behavior, such as a challenge flow or an unsupported card. Other Stripe testing cards might still trigger 3DS, but we return attempt_acknowledged to bypass the additional steps since 3DS testing isn’t the objective for those cards.

Dashboard not supported3D Secure redirects won’t occur for payments created directly in the Stripe Dashboard. Instead, use your integration’s own frontend or an API call.

### Authentication and setup

To simulate payment flows that include authentication, use the test cards in this section. Some of these cards can also be set up for future payments, or have already been.

Card numbersPaymentMethodsDescriptionNumberDetailsAuthenticate unless set up4000002500003155This card requires authentication for off-session payments unless you[set it up](/payments/save-and-reuse)for future payments. After you set it up, off-session payments no longer require authentication.Always authenticate4000002760003184This card requires authentication on all transactions, regardless of how the card is set up.Already set up4000003800000446This card is already set up for off-session use. It requires authentication for[one-time](/payments/accept-a-payment?platform=web)and other[on-session](/payments/save-during-payment#web-submit-payment)payments. However, alloff-session paymentssucceed as if the card has been previously[set up](/payments/save-and-reuse).Insufficient funds4000008260003178This card requires authentication for[one-time payments](/payments/accept-a-payment?platform=web). All payments are declined with an`insufficient_funds`failure code even after being successfully authenticated or previously[set up](/payments/save-and-reuse).### Support and availability

Stripe requests authentication when required by regulation or when triggered by your Radar rules or custom code. Even if authentication is requested, it can’t always be performed—for instance, the customer’s card might not be enrolled, or an error might occur. Use the test cards in this section to simulate various combinations of these factors.

NoteAll 3DS references indicate 3D Secure 2.

Card numbersPaymentMethodsTokens3D Secure usageOutcomeNumberDetails3DS RequiredOK40000000000032203D Secure authentication must be completed for the payment to be successful.By default, your Radar rules request 3D Secure authentication for this card.3DS RequiredDeclined40000084000016293D Secure authentication is required, but payments are declinedwith a`card_declined`failure code after authentication.By default, your Radar rules request 3D Secure authentication for this card.3DS RequiredError40000084000012803D Secure authentication is required, but the 3D Secure lookup request fails with a processing error.Payments are declined with a`card_declined`failure code.By default, your Radar rules request 3D Secure authentication for this card.3DS SupportedOK40000000000030553D Secure authentication might still be performed, but isn’t required.By default, your Radar rules don’t request 3D Secure authentication for this card.3DS SupportedError40000000000030973D Secure authentication might still be performed, but isn’t required.However, attempts to perform 3D Secure result in a processing error.By default, your Radar rules don’t request 3D Secure authentication for this card.3DS SupportedUnenrolled42424242424242423D Secure is supported for this card, but this card isn’t enrolled in 3D Secure.Even if your Radar rules request 3D Secure, the customer won’t be prompted to authenticate.By default, your Radar rules don’t request 3D Secure authentication for this card.3DS Not supported3782822463100053D Secure isn’t supported on this card and can’t be invoked.The PaymentIntent or SetupIntent proceeds without performing authentication.### 3D Secure mobile challenge flows

In a mobile payment, several challenge flows for authentication—where the customer has to interact with prompts in the UI—are available. Use the test cards in this section to trigger a specific challenge flow for test purposes. These cards aren’t useful in browser-based payment forms or in API calls. In those environments, they work but don’t trigger any special behavior. Because they’re not useful in API calls, we don’t provide any PaymentMethod or Token values to test with.

Challenge flowNumberDetailsOut of band40000000000032203D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with Out of Band UI.One time passcode40000000000032383D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with One Time Passcode UI.Single select40000000000032463D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with single-select UI.Multi select40000000000032533D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with multi-select UI.## Payments with PINs

Use the test cards in this section to simulate successful in-person payments where a PIN is involved. There are many other options for testing in-person payments, including a simulated reader and physical test cards. See Test Stripe Terminal for more information.

Card numbersPaymentMethodsDescriptionNumberDetailsOffline PIN4001007020000002This card simulates a payment where the cardholder is prompted for and enters anoffline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`offline_pin`.Offline PIN retry4000008260000075Simulates an SCA-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to insert their card and enter theiroffline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`offline_pin`.Online PIN4001000360000005This card simulates a payment where the cardholder is prompted for and enters anonline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`online_pin`.Online PIN retry4000002760000008Simulates an SCA-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to insert their card and enter theironline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`online_pin`.## Webhooks

To test webhooks, you have two options:

1. Perform actions in test mode that send legitimate events to your endpoint. For instance, to trigger the[charge.succeeded](/api#event_types-charge.succeeded)event, you can use a[test card that produces a successful charge](#cards).
2. [Trigger events using the Stripe CLI](/webhooks#test-webhook)or[using Stripe for Visual Studio Code](/stripe-vscode#webhooks).

## Rate limits

If your requests in test mode begin to receive 429 HTTP errors, make them less frequently. These errors come from our rate limiter, which is stricter in test mode than in live mode.

We don’t recommend load testing your integration using the Stripe API in test mode. Because the load limiter is stricter in test mode, you might see errors that you wouldn’t see in production. See load testing for an alternative approach.

## Non-card payments

Any time you use a test non-card payment method, use test API keys in all API calls. This is true whether you’re serving a payment form you can test interactively or writing test code.

Different payment methods have different test procedures:

ACH Direct DebitSEPA debitBACS debitBECSLinkOthersLearn how to test scenarios with instant verifications using Financial Connections.

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

Common mistakeYou need to activate your Stripe account before you can trigger these emails in Test mode.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

Account numberTokenRouting numberBehavior`000123456789``pm_usBankAccount_success``110000000`The payment succeeds.`000111111113``pm_usBankAccount_accountClosed``110000000`The payment fails because the account is closed.`000111111116``pm_usBankAccount_noAccount``110000000`The payment fails because no account is found.`000222222227``pm_usBankAccount_insufficientFunds``110000000`The payment fails due to insufficient funds.`000333333335``pm_usBankAccount_debitNotAuthorized``110000000`The payment fails because debits aren’t authorized.`000444444440``pm_usBankAccount_invalidCurrency``110000000`The payment fails due to invalid currency.`000666666661``pm_usBankAccount_failMicrodeposits``110000000`The payment fails to send microdeposits.`000555555559``pm_usBankAccount_dispute``110000000`The payment triggers a dispute.`000000000009``pm_usBankAccount_processing``110000000`The payment stays in processing indefinitely. Useful for testing[PaymentIntent cancellation](/api/payment_intents/cancel).Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

Microdeposit values0.01 descriptor code valuesScenario`32`and`45`SM11AASimulates verifying the account.`10`and`11`SM33CCSimulates exceeding the number of allowed verification attempts.`40`and`41`SM44DDSimulates a microdeposit timeout.## Redirects

To test your integration’s redirect-handling logic by simulating a payment that uses a redirect flow (for example, iDEAL), use a supported payment method that requires redirects.

To create a test PaymentIntent that either succeeds or fails:

1. Navigate to the[payment methods settings in the Dashboard](https://dashboard.stripe.com/settings/payment_methods)and enable a supported payment method by clickingTurn onin test mode.
2. Collect payment details.
3. Submit the payment to Stripe.
4. Authorize or fail the test payment.

Make sure that the page (corresponding to return_url) on your website provides the status of the payment.

## See also

- [Testing your Connect integration](/connect/testing)
- [Testing your Billing integration](/billing/testing)
- [Testing your Terminal integration](/terminal/references/testing)
- [Load testing](/rate-limits#load-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How to use test cards](#use-test-cards)[Cards by brand](#cards)[Cards by country](#international-cards)[Declined payments](#declined-payments)[Fraud prevention](#fraud-prevention)[Invalid data](#invalid-data)[Disputes](#disputes)[Refunds](#refunds)[Available balance](#available-balance)[3D Secure authentication](#regulatory-cards)[Payments with PINs](#terminal)[Webhooks](#webhooks)[Rate limits](#rate-limits)[Non-card payments](#non-card-payments)[Redirects](#redirects)[See also](#see-also)Related Guides[Test mode](/docs/test-mode)[API keys](/docs/keys)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
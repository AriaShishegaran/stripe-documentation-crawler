# Using the APIBeta

Refer to the following developer flows when building your onramp integration.

## How to integrate the onramp into your application

Integrating an application to use the onramp requires the following:

- Onboard onto Stripe and get API keys

Go to the Dashboard and get:

[Dashboard](https://dashboard.stripe.com/apikeys)

- The secret key that you need to make API calls to Stripe from a server you control

[secret key](/keys#obtain-api-keys)

- The publishable key that you use to make requests from your frontend client

[publishable key](/keys#obtain-api-keys)

- Generate a CryptoOnrampSession server-side

Your onramp application must be approved first for live mode access. Learn more about submitting an application or check the status of your application by visiting the onboarding page.

[submitting an application](/crypto/overview#to-submit-your-application:)

[onboarding page](https://dashboard.stripe.com/crypto-onramp/onboarding)

On a server you control, expose a new API endpoint (for example, myserver.com/mint-onramp-session) which makes a call to the Stripe POST /v1/crypto/onramp_sessions endpoint. This “mints” an onramp session with Stripe that you can use with new or returning users. You need to mint one session per user.

The request:

The response:

This endpoint returns error codes if Stripe can’t create onramp sessions. See the supportability section below to learn why this might happen.

For an optimal user experience, render the onramp component conditional when a user gets an HTTP status 200 during session creation and provide a fallback UI that can deal with session creation errors.

- Use the session client_secret in the frontend

To initialize the onramp component you’ll need:

- Your publishable API key from step 1

- The client_secret from your request to  POST /v1/crypto/onramp_sessions in step 2 above

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)

The above code mounts an iframe on the #onramp-element node, which hosts all of the onramp. You can use an event listener to enhance the user experience—for example, resuming operation in a Dapp after crypto purchases (see the frontend events section for all events which can be subscribed to).

[frontend events section](/crypto/using-the-api#frontend-events)

- CryptoOnramp element renders and takes over

After the above CryptoOnramp html element renders, the frontend client drives the interface. As the state of the session changes and we collect more details around transaction_details, the CryptoOnrampSession object updates accordingly. Webhooks and frontend events are generated for every status transition that occurs. By using frontend event listeners, you can redirect users back to your application user flow after the onramp session completes.

- (Optional) Change the appearance of the onramp

To enable darkmode, include an appearance struct in the session creation call from above.

If you don’t specify the appearance, the onramp defaults to a light theme. You can also change the theme after the onramp renders by calling:

You can use branding settings to upload your logo and brand colors which automatically apply to onramp sessions created with your platform API key.

[branding settings](/payments/checkout/customization#branding)

## How to pre-populate transaction parameters

To deliver a seamless onramp user flow, you can pre-populate some of the parameters of the onramp session. For example, a Dapp or wallet would already have a user’s wallet_addresses. You can achieve this during session creation as follows:

The response:

We allow the following parameters to be pre-populated:

- wallet_addresses: The suggested wallet address to deliver crypto to (the default selection on the wallet attach screen)

- lock_wallet_address: Whether or not to lock the suggested wallet address

- source_currency: The fiat currency for the transaction (usd only for now)

- source_amount: The amount of fiat currency to use for the purchase of crypto (mutually exclusive with destination amount)

- destination_network: The default crypto network for this onramp (for example, ethereum)

- destination_currency: The default cryptocurrency for this onramp session (for example, eth)

- destination_amount: The amount of cryptocurrency to purchase (mutually exclusive with the source amount)

- destination_currencies: An array of cryptocurrencies you want to restrict to (for example, [eth, usdc])

- destination_networks: An array of crypto networks you want to restrict to (for example, [ethereum, polygon])

Refer to the API reference for more details on the specific requirements and how they impact users in the onramp UI.

## How to pre-populate customer information

To reduce user friction during the onramp flow and increase conversion, you might want to pre-populate some of the required KYC information for the user if you’ve already collected it within your application.

Throughout the flow, users will be required to provide at least:

- Email

- First name

- Last name

- Date of birth

- SSN

- Home address (country, address line 1, address line 2, city, state, postal code)

The onramp API provides the ability to pre-populate all of those fields except for SSN. To pre-populate this information, you can provide it using the customer_information parameter in the OnrampSession creation API.

Example request:

Response:

We allow the following parameters to be pre-populated:

- customer_information.email—Freeform string for the user’s email

- customer_information.first_name—Freeform string for the user’s first name

- customer_information.last_name—Freeform string for the user’s last name

- customer_information.dob.year—Integer for the user’s birth year

- customer_information.dob.month—Integer for the user’s birth month

- customer_information.dob.day—Integer for the user’s birth day

- customer_information.address.country—String of the two letter country code for the user’s country of residence

- customer_information.address.line1—Freeform string for the user’s address line one

- customer_information.address.line2—Freeform string for the user’s address line two

- customer_information.address.city—Freeform string for the user’s city

- customer_information.address.state—String of the two letter state code for US states (the full state name also works), for example, “CA” or “California”

- customer_information.address.postal_code—Freeform string for the user’s postal code

All of the fields are optional and you can provide any subset of them for pre-population. However, if you provide date of birth, you must also provide all of year, month, and day (that is, not just one or two of the birth fields).

## Dealing with user supportability and fraud

Stripe enforces limitations on the onramp product for both user supportability and in the event of fraud attacks.

As noted in the Feature Set section, the onramp is only available in the United States at this time.

[Feature Set](/crypto/overview#feature-set)

Pass customer_ip_address during session creation so we can preemptively check the aforementioned limitation. The endpoint returns HTTP 400 with code=crypto_onramp_unsupportable_customer if the customer is in a geography we can’t support (based on customer_ip_address)

You might want to hide the onramp option from users in this case. Otherwise, our onramp UI renders in a disabled state.

Here’s a sample request and response (400) illustrating this behavior:

Stripe serves as the business of record and takes on the liability for disputes and fraud. Stripe has deep expertise in risk management, but we might decide to temporarily restrict creation of onramp sessions if we detect a high risk situation (for example, if we see active attacks and exploits).

If we need to shut off the API because of an unbounded fraud attack, we’ll return the following when anyone attempts to create a new session: Request:

Response (400):

## API reference

The CryptoOnrampSession resource looks as follows:

[https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95](https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95)

The status field represents a state machine for the session with the following states:

- initialized—The application has newly minted the onramp session on the server-side, but the customer hasn’t used it yet. Sessions are in this state until the user onboards and is ready to pay.

- rejected—We rejected the customer for some reason (KYC failure, sanctions screening issues, fraud checks).

- requires_payment—The user has completed onboarding or sign-in and gets to the payment page. If they attempt payment and fail, they stay in this status.

- fulfillment_processing—The customer successfully completed payment. We haven’t delivered the crypto they purchased yet.

- fulfillment_complete—The customer was successfully able to pay for crypto and we have confirmed delivery.

All endpoints require authentication with your API key. The authentication header is omitted in the example requests.

[API key](/keys)

Applications can perform the following operations on a CryptoOnrampSession:

- Create a session

- Get an existing session

Endpoint: POST /v1/crypto/onramp_sessions

- When left null, the user enters their wallet in the onramp UI.

- When set, the platform must set either destination_networks or destination_network and we perform address validation. Users can still select a different wallet in the onramp UI.

For assets that use destination tags or memos, you can nest a destination_tags map in wallet_addresses that maps assets to the specified destination tag for a user.

- When left null, a default currency is selected based on user locale.

- When set, it must be one of the fiat currencies supported by onramp. Users can still select a different currency in the onramp UI.

- When left null, a default value is computed if destination_amount is set.

- When set, setting source_amount is mutually exclusive with setting destination_amount (only one or the other is supported). We don’t support fractional pennies. If fractional minor units of a currency are passed in, it generates an error. Users can update the value in the onramp UI.

- When left null, all supported crypto networks are shown in the onramp UI.

- When set, it must be a non-empty array where values in the array are each a valid crypto network. Allowed values are {solana, ethereum, bitcoin, polygon}. It can be used to lock users to a specific network by passing a single value array. Users cannot override this parameter.

- When left null, all supported cryptocurrencies are shown in the onramp UI subject to destination_networks if set.

- When set, it must be a non-empty array where all values in the array are valid cryptocurrencies. These are {eth, matic, sol, usdc, btc}. You can use it to lock users to a specific cryptocurrency by passing a single value array. Users cannot override this parameter.

- When left null, the first value of destination_networks is selected.

- When set, if destination_networks is also set, the value of destination_network must be present in that array. To lock a destination_network, specify that value as the single value for destination_networks. Supported destination networks are {solana, bitcoin, ethereum, polygon}. Users can select a different network in the onramp UI subject to destination_networks if set.

- When left null, the first value of destination_currencies is selected.

- When set, if destination_currencies is also set, the value of destination_currency must be present in that array. To lock a destination_currency, specify that value as the single value for destination_currencies. Supported destination currencies are {eth, matic, sol, usdc, btc}. Users can select a different cryptocurrency in the onramp UI subject to destination_currencies if set.

- When left null, a default value is computed if source_amount, destination_currency, and destination_network are set.

- When set, both destination_currency and destination_network must also be set. All cryptocurrencies are supported to their full precisions (for example, 18 decimal places for eth). We validate and generate an error if the amount exceeds the supported precision based on the exchange currency. Setting source_amount is mutually exclusive with setting destination_amount (only one or the other is supported). Users can update the amount in the onramp UI.

Sample request and response:

Endpoint: GET /v1/crypto/onramp_sessions/:id

Sample request and response:

[Dashboard](https://dashboard.stripe.com/settings/public/)

Endpoint: GET /v1/crypto/onramp_sessions

Fetch multiple onramp sessions at the same time using the list endpoint.

[list endpoint](/api/crypto/onramp_sessions/list)

We send a crypto.onramp_session_updated webhook every time the status of an onramp session changes post creation. We won’t send one when a new session is created. You can configure webhooks in the Dashboard.

[configure webhooks](/webhooks)

The resource used by the webhook will be the CryptoOnrampSession resource above:

Here is the list of frontend events that you can subscribe to:

As shown above, events can be subscribed to and unsubscribed to using the standard addEventListener/removeEventListener functions over OnrampSession.  You can use '*' to match all events.

You can use session persistence to help you provide notifications and keep users engaged with the onramp after fulfilling their purchase.

You might want to persist an onramp session across user visits in some instances. For example, when a user’s onramp session is disrupted or dropped, you could prompt them and provide ways to resume the onramp session later. Or if a user refreshes the page after completing the payment, you can retain the ability to notify them when a previous onramp purchase was fulfilled. For this reason, the OnrampSession object is stateful and stored as a server side resource. By initializing the onramp UI using a previously used OnrampSession client secret, users return to where they left off.

A client secret is a unique identifier for the onramp session that stores the lifecycle of a session without leaking sensitive payment information. However, it exposes private information such as wallet addresses. Don’t log it, embed it in URLs, or expose it to anyone other than the customer. Make sure that you have TLS on any page that includes the client secret. If you have a Web2-like account structure, you could link OnrampSession to your user object and fetch it upon authentication. For an account-less Web3 application, it would add user friction to require the use of message signing for authentication. Privacy-preserving local storage yields an acceptable user experience.

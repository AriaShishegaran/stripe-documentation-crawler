htmlForward card details to third-party API endpoints | Stripe Documentation[Skip to content](#main-content)Forward card details to third-party API endpoints[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fvault-and-forward)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fvault-and-forward)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)# Forward card details to third-party API endpointsBeta

Learn how to use card details stored with Stripe across your multiprocessor setup.Available in:The Vault and Forward API allows you to tokenize and store card details in Stripe’s PCI-compliant vault and route that data to supported processors or endpoints. Leverage the API to:

- Use the[Payment Element](/payments/payment-element)[across multiple processors](/payments/forwarding-third-party-processors).
- Use Stripe as your primary vault for card details across processors.
- Route card details to your own[PCI compliant token vault](/payments/forwarding-token-vault).

When you use the Vault and Forward API, you send Stripe the API request that you intend to make to your destination endpoint, the destination endpoint itself, and placeholders for sensitive card information. Stripe routes the request to the destination endpoint and populates unredacted card details from our secure card vault. Subsequently, Stripe relays the response from your destination endpoint back to you, with no sensitive card information included.

Request accessTo gain access to use Stripe’s forwarding service, contact your Stripe representative or Stripe support.

[Collect card details and create a PaymentMethod](#collect-card-details)To collect card details and send them to Stripe for use with the Vault and Forward API, use the Payment Element to create a PaymentMethod. After you create a PaymentMethod, we automatically store card details in Stripe’s PCI compliant vault. If you have your own frontend, you can still use the Vault and Forward API by creating a PaymentMethod directly.

NoteTypically, you can only reuse PaymentMethods by attaching them to a Customer. However, the Vault and Forward API accepts all PaymentMethod objects, including those not attached to a customer.

CVCs expire automatically after a certain time period and also expire when used with the Vault and Forward API. If you require a CVC after either of these conditions are met, you must recollect the card details.

[Create a ForwardingRequest](#create-fwd-request)To send card details from Stripe’s vault, you must Create a ForwardingRequest and include the following parameters:

- `payment_method`: Object that enables Stripe to identify your customer’s card details within Stripe’s vault and insert that data into the request body.
- `url`: The exact destination endpoint of your request.
- `request.body`: The API request body that you want to send to the destination endpoint (for example, the payments request you send to another processor). Leave any field where you normally input your customer’s card details blank.
- `replacements`: Fields that you want Stripe to substitute in the`request.body`. The[available fields](/api/forwarding/forwarding_requests/create#forwarding_request_create-replacements)that we recommend always setting are`card_number`,`card_expiry`,`card_cvc`, and`cardholder_name`. For example, including`card_number`in the`replacements`array replaces the appropriate card number field for your destination endpoint in the`request.body`.

You must format your request based on the data that the destination endpoint expects. In the example below, the destination endpoint expects an Idempotency-Key header and accepts a JSON body with the payment details.

Command Line[curl](#)`curl https://api.stripe.com/v1/forwarding/requests \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode url="https://endpoint-url/v1/payments" \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}} \
  --data-urlencode "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \
  -d "replacements[0]"=card_number \
  -d "replacements[1]"=card_expiry \
  -d "replacements[2]"=card_cvc \
  -d "replacements[3]"=cardholder_name`Security tipWe require you to pass API keys for the destination endpoint on each API request. Stripe forwards the request using the API keys you provide, and only retains hashed and encrypted versions of destination endpoint API keys.

CautionYou can provide a Idempotency-Key to make sure that requests with the same key result in only one outbound request. Use a different and unique key for Stripe and any idempotency keys you provide on the underlying third-party request.

Use a new Idempotency-Key every time you make updates to request.body or request.header fields. Passing in the older idempotency key results in the API replaying older responses, including any previous validation errors.

[Forward the request with card details](#forward-request)Stripe makes a request to the destination endpoint on your behalf by inserting the card details from the PaymentMethod into the request.body. Where enabled and available, Card Account Updater (CAU) automatically attempts to update and provide the latest available card details for requests.

Stripe then forwards the request to the destination endpoint. For example:

1. Stripe makes a POST request to the endpoint:

`POST /v1/payments HTTP/1.1
User-Agent: Stripe
Accept: */*
Host: endpoint-url
Content-Type: application/json
Content-Length: 321`
2. Stripe includes the following headers:

`Destination-API-Key: {{DESTINATION_API_KEY}}
Destination-Idempotency-Key: {{DESTINATION_IDEMPOTENCY_KEY}}`
3. Stripe includes the following JSON body in the request:

`{
  amount: {
    value: 1000,
    currency: 'usd'
  },
  paymentMethod: {
    number: '4242424242424242',
    expiryMonth: '03',
    expiryYear: '2030',
    cvc: '123',
    holderName: 'First Last',
  },
  reference: '{{REFERENCE_ID}}'
}`

NoteIf you’re using the Vault and the Forward API to make an authorization request, you must handle any post-transaction actions, such as refunds or disputes, directly with the third-party processor. Contact your Stripe representative if you require 3DS authentication across your multiprocessor setup.

[Handle the response from the destination endpoint](#return-response)When you use the Vault and Forward API to forward card details to a third-party processor, Stripe synchronously waits for a response from the destination endpoint. The timeout period for this response is less than a minute. Stripe redacts identified PCI-sensitive data, stores the redacted response from the destination endpoint, and returns a ForwardingRequest object, which contains data about the request and response.

CautionWhen you use the Vault and Forward API to forward card details to a third-party processor, Stripe can’t guarantee that the processor will provide any particular response to your forwarded API requests. If the third-party processor is unresponsive, you must reach out directly to that processor to resolve the issue.

`{
  id: "fwdreq_123",
  object: "forwarding.request",
  payment_method: "{{PAYMENT_METHOD}}",
  request_details: {
    body: '{
      "amount": {
        "value": 1000,
        "currency": "usd"
      },
      "paymentMethod": {
        "number": "424242******4242",
        "expiryMonth": "03",
        "expiryYear": "2030",
        "cvc": "***",
        "holderName": "First Last",
      },
      "reference": "{{REFERENCE_ID}}"
    }',
    headers: [
      {
        name: "Content-Type",
        value: "application/json",
      },
      {
        name: "Destination-API-Key",
        value: "{{DESTINATION_API_KEY}}",
      },
      {
        name: "Destination-Idempotency-Key",
        value: "{{DESTINATION_IDEMPOTENCY_KEY}}",
      },
      ...
    ]
  },
  response_context: {
      "destination_duration": 234,
      "destination_ip_address": "35.190.113.80"
  },
  response_details: {
    body: '{
      // Response from the third-party endpoint goes here
      ...
    }',
    headers: [
      ...
    ],
    status: 200,
  },
  replacements: [
    "card_number",
    "card_expiry",
    "card_cvc",
    "cardholder_name"
  ]
  ...
}`[Configure your Vault and Forward API endpoint](#configuring)To set up your Vault and Forward API endpoint, you must:

- [Confirm that we support the destination endpoint](#confirm-endpoint).
- Provide a test and production account to your Stripe representative.
- [Share the production details](#share-production-details)for the destination endpoint to your Stripe representative.

### Confirm that we support the destination endpoint

Stripe supports forwarding API requests to the following endpoints:

- Adyen:  - `[prefix]-checkout-live.adyenpayments.com/v68/payments`
  - `[prefix]-checkout-live.adyenpayments.com/v69/payments`
  - `[prefix]-checkout-live.adyenpayments.com/v70/payments`


- Braintree:`payments.braintree-api.com/graphql`
- Checkout:  - `api.checkout.com/tokens`
  - `api.checkout.com/payments`


- GMO Payments Gateway:`p01.mul-pay.jp/payment/ExecTran.json`
- PaymentsOS:`api.paymentsos.com/tokens`
- Worldpay:`access.worldpay.com/tokens`
- [Your own PCI-compliant token vault](/payments/forwarding-token-vault)

The Vault and Forward API can only forward requests to the following countries:

### Supported countries

We can support HTTPS-based APIs that accept JSON requests and return JSON responses. If we don’t already have support for destination endpoint or you require a different API format, provide the details of the endpoint to your Stripe representative or contact Stripe support so we can support your destination endpoint.

### Provide test accounts to your Stripe representative

To access the Vault and Forward API, share the account IDs (acct_xxxx) for your test accounts with your Stripe representative.

### Share production details

Share the production details for destination endpoint with your Stripe representative. These include the following for destination endpoint: URL, HTTP method, documentation, fields, request headers, and encryption keys. Stripe then sets up destination endpoint for use with the Vault and Forward API in live mode.

To share third-party API keys, you must encrypt them by using the Stripe public key that’s specific to the Vault and Forward API. Start by importing a public key using the GNU Privacy Guard (PGP). After you familiarize yourself with the basics of PGP, use the following PGP key to encrypt your third-party API keys:

### Vault and Forward API PGP key

To encrypt your third-party API keys with the Vault and Forward API PGP key:

1. Calculate the SHA256 hash of your private key and hex encode the hash. Treat this hash as a secret.

Command Line`echo -n "{{THIRD_PARTY_SECRET_KEY}}" | sha256sum`
2. Encrypt the SHA256 hash with Stripe’s public key, Base64 encode the result, and set the Stripe key as trusted.

Command Line`echo -n "{{SHA256_HASH}}" |  gpg -e -r AE863ADA1603150856C0A853A7B203177D034588 --always-trust | base64 > encrypted_base64.txt`
3. Verify encrypted_base64.txt by running the following command:

Command Line`cat encrypted_base64.txt | base64 -d | gpg --list-only --list-packets`

Make sure that encrypted_base64.txt contains the following characteristics:

- Key ID:`27E4B9436302901A`
- Key type: RSA
- Key size: 4096 bits
- User ID:`Forward API Secret Encryption Key (Forward API Secret Encryption Key) <multiprocessor-ext@stripe.com>`

[Test your integration](#testing-your-integration)To confirm that your integration works correctly with destination endpoint, initiate a ForwardingRequest using the PaymentMethod you created. This example uses pm_card_visa as a payment method.

Command Line[curl](#)`curl https://api.stripe.com/v1/forwarding/requests \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
  -d payment_method=pm_card_visa \
  -d url="{{DESTINATION ENDPOINT}}" \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}} \
  --data-urlencode "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \
  -d "replacements[0]"=card_number \
  -d "replacements[1]"=card_expiry \
  -d "replacements[2]"=card_cvc \
  -d "replacements[3]"=cardholder_name`Common mistakeThe Vault and Forward API treats any response from the destination endpoint as a success and returns a 200, along with the destination endpoint’s response code in the response.body. For example, when the destination endpoint returns a status code of 400 to Stripe, the Vault and Forward API responds with a status code of 200. The response.body includes the destination endpoint’s 400 response and error message. Separately test the API request that you send to your destination endpoint to make sure that you don’t have any errors.

### View your request logs in the Dashboard

You can view request logs and errors related to the Vault and Forward API in the Developers Dashboard. Additionally, you can use the List API to fetch the logs from Stripe.

Security tipThe request.headers and request.body in the incoming request are encrypted and appear as encrypted_request in the Dashboard.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Collect card details and create a PaymentMethod](#collect-card-details)[Create a ForwardingRequest](#create-fwd-request)[Forward the request with card details](#forward-request)[Handle the response from the destination endpoint](#return-response)[Configure your Vault and Forward API endpoint](#configuring)[Test your integration](#testing-your-integration)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
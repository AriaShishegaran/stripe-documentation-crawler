# Forward card details to your own token vaultBeta

Create a PaymentMethod and forward the payment method to your token vault.

[PaymentMethod](/api/payment_methods)

[forward](/api/forwarding/request)

To gain access to use Stripe’s forwarding service, contact your Stripe representative or Stripe support.

[Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)

[Create a PaymentMethod](#create-payment-method)

## Create a PaymentMethod

To collect card details and send them to Stripe for use with the Vault and Forward API, use the Payment Element to create a PaymentMethod. After you create a PaymentMethod, we automatically store card details in Stripe’s PCI compliant vault. If you have your own frontend, you can still use the Vault and Forward API by creating a PaymentMethod directly.

[a PaymentMethod](/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)

[creating a PaymentMethod directly](/api/payment_methods/create)

[Create a ForwardingRequest](#create-payment-method)

## Create a ForwardingRequest

Pass the PaymentMethod ID to the Request endpoint on your server. Stripe provides a test endpoint (https://forwarding-api-demo.stripedemos.com/tokens) and a test payment method (pm_card_visa) to verify that you can successfully retrieve card credentials from Stripe’s vault. Send the card details to this test endpoint before you connect your integration with your in-house vault.

[https://forwarding-api-demo.stripedemos.com/tokens](https://forwarding-api-demo.stripedemos.com/tokens)

[Configure your in-house token vault endpoint](#configuring-in-house-vault)

## Configure your in-house token vault endpoint

To receive Primary Account Numbers (PANs) from the Vault and Forward API, your token vault must comply with the following specifications.

Make sure that your vault is PCI compliant and provide a valid PCI Attestation of Compliance to your Stripe representative. You must refresh this Attestation annually.

Your vault must contain HTTPS-based APIs that accept JSON and return JSON responses; other formats, such as XML or ISO 8583, aren’t supported.

Make sure that the API contains a single, static URL. Configure this in the Vault and Forward API for security measures. Don’t change it between requests.

Use the Vault and Forward API to authenticate with your vault using HTTP header based authentication schemes, including bearer tokens.

Make sure that every forwarded API call includes the authentication header to authenticate with your vault.

We don’t support client certificate authentication.

You can include additional headers in the forwarded request to your vault. However, you must verify that the configuration for your vault explicitly supports these headers. Reach out to your Stripe representative before you begin your integration to verify that the required additional headers are properly configured. Additionally, make sure that the headers don’t include any sensitive information, except for the bearer token.

Make sure that your vault receives a JSON object with the following shape.

You can include additional fields as needed under the metadata key in this request. We pass them through without any additional processing.

The Vault and Forward API places the decrypted data into the following fields:

You don’t need to support all of these fields in your vault. The Vault and Forward API places values into the request only if they’re present in the request body that you send to the Vault and Forward API. Additionally, you can include additional fields in the request body, which the Vault and Forward API passes to the receiving endpoint.

The Vault and Forward API doesn’t require any response body from your vault. If you provide a body, we return it to the caller of the Vault and Forward API. Don’t include any sensitive fields in your response.

The Vault and Forward API treats any response as a “success” and returns the same response code sent by the token vault endpoint back to the caller through Stripe. For example, when the upstream returns a status code of 400 to Stripe, the Vault and Forward API responds with a status code of 200. The response body includes the upstream’s 400 response and error message.

[Verify your integration with your token vault](#verifying-your-integration)

## Verify your integration with your token vault

To confirm the correct functionality of your integration with the vault endpoint, replace Stripe’s endpoint with your vault configuration. Then, initiate a ForwardingRequest using the PaymentMethod you created.

[Update your token vault with the latest credentials](#update-your-vault)

## Update your token vault with the latest credentials

Listen to Stripe webhooks to learn if a card has been updated. Call the Vault and Forward API to forward the updated PaymentMethod to your token vault.

[learn if a card has been updated](/payments/cards/overview#automatic-card-updates)

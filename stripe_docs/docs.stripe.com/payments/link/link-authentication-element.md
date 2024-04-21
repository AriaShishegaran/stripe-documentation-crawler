# Explore the Link Authentication Element

If you already have customer email addresses, pass them directly to the Payment Element instead.

[pass them directly to the Payment Element](/payments/link/payment-element-link?elements=pass-email)

Create a single email input for both email collection and Link authentication by adding the Link Authentication Element to your Elements integration. If your customer doesn’t have a Link account, and they select one of its supported payment methods (credit card, debit card, or US bank), they’re given the option of signing up.

[Link Authentication Element](/payments/elements/link-authentication-element)

Alternatively, if your customer already has a Link account, it authenticates them with a one-time-password, then automatically fills their payment details in the Payment Element.

Use the Link Authentication Element as part of your checkout page

## Add the Link Authentication Element

Put the Link Authentication Element at the beginning of the checkout page, followed by the Address Element (optional), then the Payment Element. The following code creates an instance of the Link Authentication Element and mounts it to the DOM:

[Address Element](/elements/address-element)

[creates](/js/elements_object/create_link_authentication_element)

[mounts](/js/element/mount)

linkAuthenticationElement renders an email address input. When Link matches a customer email with an existing Link account, it sends the customer a secure, one-time code to their phone to authenticate. If the customer successfully authenticates, Stripe displays their Link-saved addresses and payment methods automatically so they can use them. You also need to register your domain.

[register your domain](/payments/payment-methods/pmd-registration)

## See also

- Stripe Web Elements

[Stripe Web Elements](/payments/elements)

- Payment Element

[Payment Element](/payments/payment-element)

- Address Element

[Address Element](/elements/address-element)

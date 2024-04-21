# Strong Customer Authentication readiness

- Watch the SCA video

[Watch the SCA video](https://stripe.com/payments/strong-customer-authentication)

- See SCA payment scenarios

[See SCA payment scenarios](https://stripe.com/guides/sca-payment-flows)

- View the webinar

[View the webinar](https://go.stripe.global/sca-webinar.html)

Strong Customer Authentication (SCA), a rule in effect as of September 14, 2019, as part of PSD2 regulation in Europe, requires changes to how your European customers authenticate online payments. Card payments require a different user experience, namely 3D Secure, in order to meet SCA requirements. Transactions that don’t follow the new authentication guidelines may be declined by your customers’ banks.

[Strong Customer Authentication (SCA)](https://stripe.com/guides/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

To support SCA, you should:

- Determine if your business is impacted

- Decide which one of the SCA-ready products is right for your business

- Make changes now to avoid declined payments

If you use a third-party plugin, platform, or extension partner from the Partners gallery, contact your Stripe partner to see what (if any) work you need to do to support SCA. Please reach out if you have any questions. You can also see the frequently asked questions for information on SCA enforcement.

[Partners gallery](https://stripe.partners)

[reach out](https://support.stripe.com/contact)

[frequently asked questions](/strong-customer-authentication/sca-enforcement)

## Impacted businesses and payments

Update your Stripe integration for SCA if all of the following apply:

- Your business is based in the European Economic Area or you create payments on behalf of connected accounts based in the EEA

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[create payments on behalf of connected accounts based in the EEA](/strong-customer-authentication/connect-platforms)

- You serve customers in the EEA

- You accept cards (credit or debit)

While some low-risk transactions (based on the volume of fraud rates associated with the payment provider or bank) do not require authentication, banks can choose to not honor these exemptions and request that the customer complete authentication. Even if you’re primarily processing low-risk transactions, update your integration so your customers can complete authentication when requested by the bank. Stripe’s new products and APIs help you claim these exemptions and maximize conversion by only requesting authentication when absolutely necessary. Learn more about SCA exemptions.

[new products and APIs](#preparing)

[SCA exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

## SCA-ready products and APIs

Stripe provides prebuilt and customizable solutions to help you meet SCA requirements. Integrations that aren’t SCA-ready, like those using the legacy Charges API, will see high rates of declines as banks begin enforcing SCA.

[Charges API](/payments/charges-api)

Whether you collect one-time payments or save cards for later reuse, Stripe has SCA-ready products that let us update your integration for future regulations, with minimal changes required by you.

Accept card payments with the Payment Intents API and Stripe’s new version of Checkout—a prebuilt, Stripe-hosted checkout flow that automatically handles SCA requirements for you. Checkout is customizable and lets you accept payments for one-time purchases and subscriptions on your website.

[Payment Intents API](/payments/payment-intents)

[subscriptions](/billing/subscriptions/creating)

- Use a prebuilt checkout page

[Use a prebuilt checkout page](/payments/accept-a-payment?integration=checkout)

- Build a custom payment flow

[Build a custom payment flow](/payments/accept-a-payment?integration=elements)

Save a card for later reuse with Stripe’s new Payment Intents and Setup Intents APIs. You can also use Checkout—a prebuilt, Stripe-hosted checkout flow—to automatically handle SCA requirements, or use Stripe Billing to handle SCA for subscription models.

[Setup Intents APIs](/api/setup_intents)

- Use a prebuilt checkout page

[Use a prebuilt checkout page](/payments/save-and-reuse?platform=checkout)

- Build a custom flow to save card details

[Build a custom flow to save card details](/payments/save-and-reuse)

- Use Billing for subscription models

[Use Billing for subscription models](/billing/migration/strong-customer-authentication)

## SCA Migration

Read the SCA migration guide to learn more about which products are best suited for you. For specific product recommendations based on common business scenarios, check out the SCA payment flows guide.

[SCA migration](/strong-customer-authentication/migration)

[SCA payment flows](https://stripe.com/guides/sca-payment-flows)

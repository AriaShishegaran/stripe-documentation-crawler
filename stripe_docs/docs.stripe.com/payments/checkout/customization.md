# Customize Checkout

Customize branding, configure legal and return policies, enable customer payment autofill, and so on for Checkout.

[AppearanceCustomize the look and feel of Checkout, including branding.](/payments/checkout/customization#branding)

Customize the look and feel of Checkout, including branding.

[Text and policiesCustomize the support contact information, policies, and other text that your customers see.](/payments/checkout/customization#policies)

Customize the support contact information, policies, and other text that your customers see.

[Checkout experienceCustomize the behavior of Checkout to optimize conversion and boost revenue.](/payments/checkout/customization#policies)

Customize the behavior of Checkout to optimize conversion and boost revenue.

[Customize the appearance](#customize-appearance)

## Customize the appearance

You can customize the look and feel of Checkout from the Dashboard.

You can apply custom branding to Checkout. Go to Branding Settings to:

[Branding Settings](https://dashboard.stripe.com/settings/branding/checkout)

- Upload a logo or icon (only applies to Checkout’s Stripe-hosted page)

[Stripe-hosted page](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

- Customize the Checkout page’s background color, button color, font, and shapes

Read about font compatibility to learn which fonts Checkout supports in different locales.

[font compatibility](/payments/checkout/customization/font-compatibility)

For platforms performing direct charges, and destination charges with on_behalf_of, Checkout uses the brand settings of the connected account. Platforms can configure the brand settings of connected Express and Custom accounts using the Accounts API.

[Accounts](/api/accounts/object#account_object-settings-branding)

You can change a Checkout page’s name by modifying the Public business name field in public settings.

[public settings](https://dashboard.stripe.com/settings/public)

You can also customize the domain name of a Stripe-hosted Checkout page.

[customize the domain name](/payments/checkout/custom-domains)

- Font compatibility by locale

[Font compatibility by locale](/payments/checkout/customization/font-compatibility)

- Customize the domain name

[Customize the domain name](/payments/checkout/custom-domains)

[Customize text and policies](#customize-text-policies)

## Customize text and policies

You can customize the text that your customers see, as well as the policies Checkout displays.

You can present additional text to customers when they pay with Stripe Checkout, such as shipping and processing times.

You are prohibited from using this feature to create custom text that will violate or create ambiguity with the Stripe generated text on Checkout, obligations under your Stripe agreement, Stripe’s policies, and applicable laws.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

Custom text near the shipping address collection fields

Custom text above the Pay button

Custom text after the Pay button

Your custom text can be up to 1200 characters in length. However, Stripe Checkout is optimized for conversion, and adding extra information might affect your conversion rate. You can bold text or insert a link using Markdown syntax.

[Markdown syntax](https://www.markdownguide.org/cheat-sheet/)

You can display your return, refund, legal policies, and support contact information to your customers on Checkout. Go to Checkout Settings to configure the information you want to display, including:

[Checkout Settings](https://dashboard.stripe.com/settings/checkout)

- Details about your return and refund policies

- Your support phone number, email, and website

- Links to your terms of service and privacy policy

Presenting this information can increase buyer confidence and minimize cart abandonment.

From Checkout Settings, add support contact information to your sessions by enabling Contact information. Similarly, add links to your Terms of service and Privacy policy to your sessions by enabling Legal policies. If you require customers to implicitly consent to your legal policies when they complete their checkout, select the Display agreement to legal terms checkbox.

[Checkout Settings](https://dashboard.stripe.com/settings/checkout)

You must add your support contact information and legal policy links in your Public Detail Settings.

[Public Detail Settings](https://dashboard.stripe.com/settings/public)

The following previews show how Checkout displays a dialog with the support contact information, links to the store legal policies, and information about the payment terms.

Preview of contact information on Checkout.

Preview of legal policies on Checkout.

Display your return, refund, or exchange policies, by enabling Return and Refund policies. Although businesses that sell physical goods use return policies, businesses that sell digital goods or customized physical goods typically use refund policies. Because they’re not mutually exclusive, you can select both options if your business sells both categories of goods. You can edit your return and refund details, including:

- Whether you accept returns, refunds, or exchanges

- Whether returns, refunds, or exchanges are free or if they’re subject to a fee

- How many days after a purchase you’ll accept returns, refunds, or exchanges

- How customers can return items shipped to them

- Whether you accept in-store returns

- A link to the full return and refund policy

- A custom message

If you accept free returns, refunds, or exchanges, Checkout highlights the policy for customers.

The following previews show how Checkout displays a return policy. In this example, it’s for purchases that can be returned by shipping them or in-store for a full refund (or exchange) for up to 60 days. You can display similar information for refunds.

Preview of return policies on Checkout.

Preview of a policy highlight on Checkout.

Businesses often require their customers to agree to their terms of service before they can pay. This might depend on the type of product or subscription. Checkout helps you collect the necessary agreement by requiring a customer to accept your terms before paying.

Collect terms of service agreement

You can collect a terms of service agreement with Stripe Checkout when you create a Session:

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[https://example.com/terms)](https://example.com/terms))

When consent_collection.terms_of_service='required', Checkout dynamically displays a checkbox for collecting the customer’s terms of service agreement. If consent_collection.terms_of_service='none', Checkout won’t display the checkbox and won’t require customers to accept the terms of service. Before requiring agreement to your terms, set your terms of service URL in your business’ Public details. Setting a privacy policy URL is optional—Checkout also links to your privacy policy when a URL to your Privacy policy is set in your Public details.

[Public details](https://dashboard.stripe.com/settings/public)

[Public details](https://dashboard.stripe.com/settings/public)

After a customer completes checkout, you can verify that the customer accepted your terms of service by looking at the Session object in the checkout.session.completed webhook, or by retrieving the Session using the API. When the terms are accepted, the Session’s consent.terms_of_service field is set to "accepted".

[consent.terms_of_service](/api/checkout/sessions/object#checkout_session_object-consent)

You can customize the text that appears next to the checkbox by using custom_text.terms_of_service_acceptance. You need to set consent_collection.terms_of_service='required'. To use your own terms, insert a Markdown link. For example: I agree to the [Terms of Service](https://example.com/terms)

Consult your legal and compliance advisors before making any changes to this text. You may not use this feature to display custom text that violates or creates ambiguity with the Stripe-generated text on Checkout, obligations under your Stripe agreement, Stripe policies, and applicable laws.

- Collect consent for promotional emails

[Collect consent for promotional emails](/payments/checkout/promotional-emails-consent)

- Customize payment method reuse agreement

[Customize payment method reuse agreement](/payments/checkout/customize-payment-method-reuse-agreement)

[Customize checkout experience](#customize-checkout-experience)

## Customize checkout experience

You can customize how Checkout behaves during the payment process. These changes can help increase conversion and boost revenue.

To better align Checkout with your business model, configure the copy displayed on the Checkout submit button for one-time purchases.

Define a submit_type on your session. In this example (for a 5 USD donation), your customized Checkout submit button would read Donate $5.00. See the API reference for a complete list of submit_type options.

[API reference](/api/checkout/sessions/create#create_checkout_session-submit_type)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

By default, Checkout detects the locale of the customer’s browser and displays a translated version of the page in their language, if it is supported. You can override the browser locale for Checkout by passing the locale parameter when you create a Checkout Session.

[supported](https://support.stripe.com/questions/supported-languages-for-stripe-checkout)

[parameter](/api/checkout/sessions/create#create_checkout_session-locale)

Checkout also uses the locale to format numbers and currencies. For example, when selling a product whose price is set in EUR with the locale set to auto, a browser configured to use English (en) would display €25.00 while one configured for German (de) would display 25,00 €.

You can automatically use Link (Stripe’s one-click checkout) in your prebuilt Checkout page. To learn more, see Link with Checkout.

[Link with Checkout](/payments/link/checkout-link)

- Customize redirect behavior (Embedded form)

[Customize redirect behavior (Embedded form)](/payments/checkout/custom-redirect-behavior)

- Collect taxes

[Collect taxes](/payments/checkout/taxes)

- Collect phone numbers

[Collect phone numbers](/payments/checkout/phone-numbers)

- Add custom fields

[Add custom fields](/payments/checkout/custom-fields)

- Make line item quantities adjustable

[Make line item quantities adjustable](/payments/checkout/adjustable-quantity)

- Customize payment method reuse agreement

[Customize payment method reuse agreement](/payments/checkout/customize-payment-method-reuse-agreement)

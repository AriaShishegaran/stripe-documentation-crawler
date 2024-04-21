# Before going live

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you have completed so far.

- Make sure your use case and business are supportedReview the supported use cases and terms of service to make sure that your business can use Stripe Identity.

Review the supported use cases and terms of service to make sure that your business can use Stripe Identity.

[supported use cases](/identity/use-cases)

[terms of service](https://stripe.com/identity/legal)

- Setup brandingThe verification experience shows your company name, logo, and color. Make sure to configure the branding settings for your account before going live.

The verification experience shows your company name, logo, and color. Make sure to configure the branding settings for your account before going live.

[branding settings](https://dashboard.stripe.com/settings/branding)

- Limit the number of submission attemptsTo prevent fraudsters from abusing your verification flow and incurring charges on your account, we recommend that you limit the number of times a user can verify themselves.

To prevent fraudsters from abusing your verification flow and incurring charges on your account, we recommend that you limit the number of times a user can verify themselves.

- Limit how much sensitive information you storeAs much as possible, store only references to the verification and use the API to retrieve the VerificationSession when you need access to sensitive information. This simplifies your integration and limits your exposure from a security perspective, and helps you comply with privacy laws (such as GDPR) that require you to minimize data retention.

As much as possible, store only references to the verification and use the API to retrieve the VerificationSession when you need access to sensitive information. This simplifies your integration and limits your exposure from a security perspective, and helps you comply with privacy laws (such as GDPR) that require you to minimize data retention.

[retrieve the VerificationSession](/api/identity/verification_sessions/retrieve)

- Always authenticate your userWe recommend that you authenticate your user before showing or sending them to Stripe Identity. This allows you to keep relevant internal references and adds a layer of security to prevent fraudsters from abusing your verification flow.

We recommend that you authenticate your user before showing or sending them to Stripe Identity. This allows you to keep relevant internal references and adds a layer of security to prevent fraudsters from abusing your verification flow.

- Provide an alternative verification methodStripe Identity may not be able to verify all of your users. For example, your user might decline to be verified using biometric technology, they might attempt to verify with an unsupported document type, or they might not be covered by Identity’s verification checks. We recommend that you provide alternative ways to verify your user, such as reaching out to your support team. In some jurisdictions, privacy laws (such as GDPR) might require you to offer a non-biometric verification option for users who decline to consent to using their biometric information.

Stripe Identity may not be able to verify all of your users. For example, your user might decline to be verified using biometric technology, they might attempt to verify with an unsupported document type, or they might not be covered by Identity’s verification checks. We recommend that you provide alternative ways to verify your user, such as reaching out to your support team. In some jurisdictions, privacy laws (such as GDPR) might require you to offer a non-biometric verification option for users who decline to consent to using their biometric information.

[verification checks](/identity/verification-checks)

- Follow webhook best practicesIf your integration depends on webhooks, make you sure you’ve tested that your integration handles Identity events correctly and that you’re following the Best practices for using webhooks.

If your integration depends on webhooks, make you sure you’ve tested that your integration handles Identity events correctly and that you’re following the Best practices for using webhooks.

[webhooks](/webhooks#webhooks-def)

[tested](/identity/handle-verification-outcomes#test)

[Best practices for using webhooks](/webhooks#best-practices)

- Follow the Stripe development checklistFollow the Development checklist to ensure a smooth transition when taking your integration live.

Follow the Development checklist to ensure a smooth transition when taking your integration live.

[Development checklist](/get-started/checklist/go-live)

- Update your privacy policy if necessaryStripe Identity collects sensitive information, such as facial and identity document images. Make sure that your own privacy policy tells your customers about all the ways you may use or reuse the collected identity data and that this data is shared with Stripe. You could add the following paragraph to your policy if it doesn’t already include information about how their data is disclosed to Stripe:We use Stripe for identity document verification. Stripe collects identity document images, facial images, ID numbers and addresses as well as advanced fraud signals and information about the devices that connect to its services. Stripe shares this information with us and also uses this information to operate and improve the services it provides, including for fraud detection. You may also choose to allow Stripe to use your data to improve Stripe’s biometric verification technology. You can learn more about Stripe and read its privacy policy at https://stripe.com/privacy.

Stripe Identity collects sensitive information, such as facial and identity document images. Make sure that your own privacy policy tells your customers about all the ways you may use or reuse the collected identity data and that this data is shared with Stripe. You could add the following paragraph to your policy if it doesn’t already include information about how their data is disclosed to Stripe:

We use Stripe for identity document verification. Stripe collects identity document images, facial images, ID numbers and addresses as well as advanced fraud signals and information about the devices that connect to its services. Stripe shares this information with us and also uses this information to operate and improve the services it provides, including for fraud detection. You may also choose to allow Stripe to use your data to improve Stripe’s biometric verification technology. You can learn more about Stripe and read its privacy policy at https://stripe.com/privacy.

- Provide a URL to your privacy policyMake sure your account settings include a link to your privacy policy. This URL will be linked from Stripe Identity.

Make sure your account settings include a link to your privacy policy. This URL will be linked from Stripe Identity.

[account settings](https://dashboard.stripe.com/settings/account?support_details=true)

- Explain ID verification and Stripe Identity to your customersAdd information to your site answering common questions about identity verification and your use of Stripe Identity. See the FAQ template.

Add information to your site answering common questions about identity verification and your use of Stripe Identity. See the FAQ template.

[FAQ template](/identity/explaining-identity)

- Explain to your users how to delete their data from Stripe’s serversWhen your users request their data to be deleted, redact the VerificationSession and let your users know that they’ll need to contact Stripe support to remove their data from Stripe’s servers. You could add the following paragraph to your application:We use Stripe for identity document verification. Stripe retains a copy of all the data provided as part of a verification. You may also have consented to allow Stripe to use your data to improve their technology. You can delete your information from Stripe’s servers or revoke your consent by visiting https://support.stripe.com.

When your users request their data to be deleted, redact the VerificationSession and let your users know that they’ll need to contact Stripe support to remove their data from Stripe’s servers. You could add the following paragraph to your application:

[redact the VerificationSession](/identity/verification-sessions#redact)

We use Stripe for identity document verification. Stripe retains a copy of all the data provided as part of a verification. You may also have consented to allow Stripe to use your data to improve their technology. You can delete your information from Stripe’s servers or revoke your consent by visiting https://support.stripe.com.

## See also

- Is my use case supported?

[Is my use case supported?](/identity/use-cases)

- Development checklist

[Development checklist](/get-started/checklist/go-live)

- Take webhooks live

[Take webhooks live](/webhooks#register-webhook)

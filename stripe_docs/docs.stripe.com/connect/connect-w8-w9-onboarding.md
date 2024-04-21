# Connect W-8 and W-9

## What’s the Stripe W-8 and W-9 Connect product?

Stripe’s W-8 and W-9 Connect product provides a seamless way to collect certified tax information from connected accounts through the Express Dashboard or Stripe-hosted onboarding. This includes the name, address, and TIN (Tax ID) of a taxpayer. A W-9 tax form is for US residents or citizens and is used to confirm their TIN (SSN/ITIN/EIN). A W-8 tax form is for non-US tax residents and is used to certify their name, address, and foreign TIN (if applicable), to confirm that they’re not a US taxpayer. A non-US resident can also specify the appropriate treaty and/or withholding rates applicable to their business.

[W-9 tax form](https://www.irs.gov/pub/irs-pdf/fw9.pdf)

[US residents or citizens](https://www.irs.gov/individuals/international-taxpayers/classification-of-taxpayers-for-us-tax-purposes)

[W-8 tax form](https://www.irs.gov/pub/irs-pdf/fw8ben.pdf)

Platforms might be subject to IRS fines up to 290 USD per incorrect submission if they file 1099s with incorrect information. W-8 and W-9s provide a way for Platforms to collect certified tax information throughout the year directly from your Connected Accounts before issuing 1099s to make sure the correct information is used on the appropriate 1099 forms.

With the W-8 and W-9 Connect product, your connected accounts can complete the appropriate W8 or W9 form with a few simple clicks. Any information connected accounts have already provided is pre-populated onto the forms for the ease of your users. They only need to confirm the information is accurate and make updates where needed. No more PDFs, emails, or wet-ink signatures needed.

Platforms will have a fully customizable Dashboard which tracks the status of all W-8 or W-9 requests. You’ll be able to easily see which users have completed the appropriate documentation and which users are still pending, and you can download PDFs of any submitted forms.

Connected Accounts will also have a unified tax experience where they can manage completing their tax forms and storage of their tax documents all within the Tax Center.

Stripe W-8 and W-9 forms dashboard

## How does it work?

Platforms determine appropriate collection timing for when to request a W-8 or W-9. If choosing to collect at onboarding, all new users are asked to verify and attest to their tax information. If choosing to collect at a later date, Platforms request W-8 or W-9 collection with the Accounts API and then route their user to verify and attest to their tax information. Platforms can also request W-8 or W-9 collection from all accounts—existing accounts will be notified at that time.

[Accounts API](/api/connected_accounts)

Customize the W-8 and W-9 collection configuration

Platforms have full customization in setting enforcement thresholds to determine when Connected Accounts will be required to submit a W-8/W-9 tax form:

- Volume: Block payouts if a W-8 or W-9 isn’t submitted after processing x USD.

- Time: Block payouts if a W-8 or W-9 isn’t submitted after x days.

- Combo: Block payouts if a W-8 or W-9 isn’t submitted after x days or after processing x USD.

## How do I get started?

Currently, access to Stripe’s W-8/W-9 Connect product is limited to US beta users. To request access to the beta and to learn more about pricing, reach out to your account team or contact Stripe for more information.

[contact Stripe](https://stripe.com/contact/sales)

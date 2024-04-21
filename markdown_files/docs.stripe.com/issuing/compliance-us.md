htmlTreasury and Issuing product marketing, design, and compliance guidelines | Stripe Documentation[Skip to content](#main-content)Product and marketing compliance guidance (US)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcompliance-us)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcompliance-us)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Treasury and Issuing product marketing, design, and compliance guidelines

Learn how to keep your Treasury or Issuing program and marketing campaigns compliant.CautionDon’t consider any of the information in this guide as legal advice. If you use Stripe Treasury and Stripe Issuing, consult your own legal counsel for advice about product branding and using Stripe products to offer financial services.

To offer and promote Stripe Treasury and Issuing products to your users, your marketing and user interfaces must adhere to the guidelines that we outline here. These guidelines help you navigate the financial regulations that apply to Stripe products—we’ve organized them by the following components:

- [Account management](#account-management)
- [Going live](#going-live)
- [Recordkeeping](#recordkeeping)

The following table outlines the steps you must complete before onboarding your first connected account users. If you need help, contact the Stripe Compliance team at platform-compliance@stripe.com.

If you make changes to any items in the table at a later date you must submit a request to the Stripe Compliance team using the Change Request Form.

TopicChecklistProduct applicabilityApplication flowYour application flow:- Includes bank disclosures
- Includes required agreements
- Required KYC fields
- Approved by Stripe Compliance

Treasury and IssuingFees and creditsYou’ve submitted your planned fees and credits to Stripe through[the submission form](/treasury/compliance#fees,-credits,-and-rewards-programs)Treasury and IssuingMarketing and user interfacesYour marketing materials, including your website landing pages, dashboards, and support pages:- Are approved by Stripe Compliance (or align with messaging guidelines)
- Include bank disclosures

Treasury and IssuingCustomer service channelsYour customers can access your customer service channels and they can:- Submit complaints
- Submit disputes

Treasury and IssuingAccount statements (optional)If you choose to send account statements, they must:- Be approved by Stripe Compliance
- Include Bank disclosures and relevant contact information

TreasuryReceiptsYou have a mechanism to send your customers Stripe-generated money transmission receiptsTreasury and IssuingRegulated customer noticesYou send regulated customer notices to applicants and accountholders, and they’re either:- Sent by Stripe on your behalf
- Sent by your platform with templates approved by Stripe Compliance

Issuing Spend Card and Charge CardRecordkeepingYou have a mechanism to retain copies of:- Customer consent to open accounts
- Marketing materials and user interfaces
- Customer communications, such as support emails
- Account statements, if applicable

Treasury and Issuing## Account management

You need the proper internal compliance controls before launching Stripe Treasury or Stripe Issuing. You also need to build the processes described in this section into your various workflows, customer service, and product channels.

### Complaints program guidance

Complaints are any expression of dissatisfaction with a product, service, policy, or employee related to Stripe Treasury or Stripe Issuing, except those expressions made by employees of your company. Properly handling complaints is mandatory when offering financial services products. See the Handling complaints guide for detailed complaint management requirements.

### Disputes and charge errors

As part of providing customer support, you might be notified of suspected disputed charges, charge errors, or both. The two most common types of disputes or errors are:

- You or your customer believe a charge is unauthorized
- You or your customer see an error on an account statement

If these errors occur, submit the dispute through the Stripe Dashboard. Select the relevant transactions and choose Dispute. Be prepared to provide Stripe with specific information to investigate the dispute, such as:

- Details about the authorized user
- Details about the disputed charge amount
- The transaction date
- An explanation of why the disputed charge is an error or unauthorized

You must report any disputed charge or error immediately upon notification of it. Failure to do so might impact your financial liability. To avoid a sustained reduction to your available balance, you can pay the disputed charge while we determine the validity of the dispute. If Stripe deems the dispute valid, we credit the disputed charge amount back to the appropriate account.

### Application flow

Your platform must provide for three main compliance requirement workflows:

- Collection of required KYC information
- Presentation of the required bank disclosure
- Ensuring that your applicant reads and accepts the required legal agreements

## Required agreements and disclosures

If you’re a platform and you’re not using Stripe Hosted Onboarding, you must present the following agreements and disclosures, specific to your program, for your users to accept during their account opening process. You must also provide ongoing access to these agreements after your users open an account.

### Issuing

Spend card users![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Connected Account Agreements and Disclosures.

You must surface the following agreements to your Connected Accounts before they can start using the Stripe Issuing Spend Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder Terms](https://stripe.com/legal/issuing-accountholder)
- Issuing Bank Terms  - Celtic Bank Users only:[Issuing Bank Terms - Spend Card (Celtic Bank)](https://stripe.com/legal/celtic-spend-card)
  - Cross River Bank Users only:[Issuing Bank Terms - Spend Card (Cross River Bank)](https://stripe.com/legal/issuing/crb-spend-card)


- Apple Pay Terms(if enabled for your program)  - [Apple Pay Accountholder Terms](https://stripe.com/issuing/celtic/apple-payment-platform-program-manager-customer-terms-and-conditions/legal#exhibit-c-pass-through-provisions)



In addition to the above agreements, you must surface the following disclosures to your Connected Accounts before they can start using the Stripe Issuing Spend Card Program:

- Electronic Signature Consent: You must include text near the “Issuing Bank Terms” link that states: “By clicking “submit application,” you agree to the Issuing Bank Terms, Stripe Connected Account Agreement, and Stripe Issuing Accountholder Terms, and you consent to electronic signatures as set forth in the Issuing Bank Terms.”
- Commercial Financing Disclosure: For Connected Accounts with a business address in CA, NY, or UT, you must present one of the following disclosures:  - For platforms that don’t charge fees:    - Celtic Bank Users only:[Commercial Financing Disclosure (Celtic Bank) (no fee)](https://stripe.com/legal/issuing-offer-document)
    - Cross River Bank Users only:[Commercial Financing Disclosure (Cross River Bank) (no fee)](https://stripe.com/legal/crb-issuing-offer-document)


  - For platforms that charge a $0.10 fee when creating cards for users:    - Celtic Bank Users only:[Commercial Financing Disclosure (Celtic Bank) (fee included)](https://stripe.com/legal/issuing-offer-document-fees)
    - Cross River Bank Users only:[Commercial Financing Disclosure (Cross River Bank) (fee included)](https://stripe.com/legal/crb-issuing-offer-document-fees)


  - For platforms that charge fees other than a $0.10 fee when creating cards for users:    - You may be required to create your own commercial financing disclosure to present to your connected accounts if you charge fees beyond Stripe’s fee of $0.10 for creating virtual cards. You must report custom fees through Stripe’s[Fee Intake Form](https://docs.google.com/forms/d/e/1FAIpQLSdp2Hl1N_K1lpkOe30qV0NUiUAhGsfVRWojiqle7fizyTaqdQ/viewform?usp=sf_link), and you must submit custom commercial financing disclosures to[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com). Both the custom fee and custom disclosure are subject to Stripe’s review and approval. Please contact[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com)to assess the applicability of commercial financing disclosures to your program.





Authorized User Agreements and Disclosures.

If you or your connected accounts create an individual type Cardholder, otherwise known as an “authorized user”, you must present to cardholders—typically during the card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- Authorized User Terms  - Celtic Bank Users only:[Authorized User Terms (Celtic Bank)](https://stripe.com/legal/issuing/celtic-authorized-user-terms)
  - Cross River Bank Users only:[Authorized User Terms (Cross River Bank)](https://stripe.com/legal/issuing/crb-authorized-user-terms)



Charge card users![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Connected Account Agreements and Disclosures.

You must surface the following agreements to your Connected Accounts before they can start using the Stripe Issuing Charge Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder Terms](https://stripe.com/legal/issuing-accountholder)or Custom Platform Accountholder Terms
- Issuing Bank Terms  - Celtic Bank Users only:[Issuing Bank Terms - Charge Card (Celtic Bank)](https://stripe.com/legal/celtic-charge-card)
  - Cross River Bank Users only:[Issuing Bank Terms - Charge Card (Cross River Bank)](https://stripe.com/legal/issuing/crb-charge-card)


- Apple Pay Terms(if enabled for your program)  - [Apple Pay Accountholder Terms](https://stripe.com/issuing/celtic/apple-payment-platform-program-manager-customer-terms-and-conditions/legal#exhibit-c-pass-through-provisions)


- Card Program Terms: These are your bespoke program terms that supplement the Issuing Bank Terms. At a minimum, you should consider including in your terms the following items. Please consult your legal counsel on all items that should be defined within your own Card Program Terms.  - Repayment methods, including automatic withdrawal consents
  - Billing cycles, including due dates
  - Fees
  - Rewards
  - Credit limits
  - Account closure requirements



In addition to the above agreements, you must surface the following disclosures to your Connected Accounts before they can start using the Stripe Issuing Spend Card Program:

- Electronic Signature Consent: You must include text near the “Issuing Bank Terms” link that states that by signing the Issuing Bank Terms, the user consents to electronic signatures and communications. For example, your message to users might read: “By clicking the submit application button, you agree to the Issuing Bank Terms, Stripe Connected Account Agreement, and Stripe Issuing Accountholder Terms, and you consent to electronic signatures as set forth in the Issuing Bank Terms.
- Commercial Financing Disclosure: You must present your own custom commercial financing disclosure for Connected Accounts with a business address in CA, NY, or UT. You must report custom fees through Stripe’s[Fee Intake Form](https://docs.google.com/forms/d/e/1FAIpQLSdp2Hl1N_K1lpkOe30qV0NUiUAhGsfVRWojiqle7fizyTaqdQ/viewform?usp=sf_link), and you must submit custom commercial financing disclosures to[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com). Both the custom fee and custom disclosure are subject to Stripe’s review and approval. Please contact[platform-compliance@stripe.com](mailto:platform-compliance@stripe.com)to assess the commercial financing disclosure requirements of your program.

Authorized User Agreements and Disclosures.

If you or your connected accounts create an individual type Cardholder, otherwise known as an “authorized user”, you must present to cardholders—typically during the card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- Authorized User Terms  - Celtic Bank Users only:[Authorized User Terms (Celtic Bank)](https://stripe.com/legal/issuing/celtic-authorized-user-terms)
  - Cross River Bank Users only:[Authorized User Terms (Cross River Bank)](https://stripe.com/legal/issuing/crb-authorized-user-terms)



Commercial prepaid debit users![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must surface the following agreements to your connected accounts before they can start using the Stripe Issuing Commercial Prepaid Debit Card Program:

- [Stripe Connected Account Agreement](https://stripe.com/legal/connect-account)
- [Stripe Issuing Accountholder Terms](https://stripe.com/legal/issuing-accountholder)
- [Issuing Bank Terms (Sutton Bank)](https://stripe.com/legal/issuing/commercial-prepaid-sutton-terms)

Authorized User Agreements and Disclosures.

If you or your connected accounts create an individual type Cardholder, otherwise known as an “authorized user”, you must present to cardholders—typically during the card activation process—the following agreements:

- [Stripe E-Sign Disclosure](https://stripe.com/issuing/e-sign-disclosure/legal)
- [Sutton Bank Authorized User Terms](https://stripe.com/legal/issuing/sutton-authorized-user-terms)

Treasury![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must surface the following terms of service to your connected accounts and record their agreement before they can start using the Stripe Treasury Program:

- [Stripe Services Agreement](https://stripe.com/legal/ssa)
- [Stripe Treasury Terms - Connected Accounts](https://stripe.com/legal/ssa#services-terms)

## Fees, credits, and rewards programs

In addition to the previous agreements, your terms of service and fee schedule must clearly outline the fees and terms that you implement as part of your Treasury or Issuing program. You’re required to report to Stripe the amount of any fees and credits that you plan to offer your users. This helps ensure your user interfaces and marketing materials are compliant with financial regulations regarding fees or offer credits, especially in the form of rewards programs. Use the Fee Intake Form to report all fees, credits, and rewards programs.

## Customer communications

To comply with applicable laws and regulations, you must send certain communications to both your applicants and accountholders upon certain trigger events. To learn more, see our Issuing and Treasury customer communications page.

## Statements

Providing statements, while optional, is a best practice that allows your Treasury or Issuing customers to periodically check their transaction history. If you send statements, make sure they contain the following information:

- [Company] name and address.
- Your company’s customer support contact number and website
- Customer account number
- Customer name and address
- Required disclosures
- Transaction history (including opening and closing balances for the statement period)
- Fees and credits.
- Information about how you resolve errors and complaints

## Receipts

One of the most important ongoing obligations you have in overseeing your Treasury or Issuing program is providing your customers with money transmissions receipts. Every regulated transaction your customers initiate generates a compliant money transmission receipt URL that you must share with your customer. You can provide these URL receipts in a few different ways, such as emailing them or making them available in your customer’s Dashboard. See the Regulatory receipts guide for more information on how to access hosted receipts. If you plan to charge your connected account owners any fees, whether they’re transactional or monthly recurring, include a description of the fee on the receipt so that they can reconcile it to corresponding transactions or monthly statements.

## Going live

The following information pertains to releasing your Stripe Treasury or Issuing programs to the public.

### Marketing your account offerings-general requirements

Any message or communication you provide to the public for financial products or services they don’t currently use must be truthful and fair, and in the interest of your potential customers.

### UDAP and correct messaging

Federal regulation prohibits unfair and deceptive acts or practices (UDAP). To avoid UDAP violations, you must think of the end user first when developing and deploying any marketing materials.

Make sure that marketing materials use clear messaging that fully explains product features, costs, benefits, and limitations. Don’t leave out key terms or fees, and don’t advertise product uses or features that aren’t true.

DoDon’tOnly use statements about products that are true, accurate, and aligned with how users engage with the products.Don’t leave out key information from marketing content. If the information is likely to affect whether someone uses the product, then it’s “key."If you make claims that require additional data to support them, or if an end user needs to know more details to know how a certain claim is true, you must:- Provide documented evidence
- Disclose that information

Make exaggerated claims that are hard to prove. Don’t make absolute statements that are disproved by a single exception. For example, “number 1," “every," “only," “all," “never," “always."Clearly explain all qualifying limitations and requirements needed by end users to get the product or features that you’ve advertised.Don’t advertise features or programs that only a few applicants actually qualify for.All disclosures must meet a “clear and conspicuous” standard:- Font size must be large enough to read.
- Font color must visibly contrast with the background.
- Dynamic or video ads must have the disclosure on screen long enough to be read.

Don’t make disclosures hard to read.Disclosures used to explain or modify a claim must be ‘tied’ to the claim they’re explaining.- Use a hyperlink directly linking to the disclosure (or include the disclosure next to the claim in the copy itself)
- Use reference text or symbols (an asterisk, for example) directly after the claim and before the disclosure language.

Don’t bury disclosures in other non-key disclosures or footnotes.Disclose all account fees, costs, benefits, and terms as part of onboarding before your end users take out a product.Don’t advertise products as “free” if you’re charging fees.Make sure all images used are properly licensed and that you can document this fact.Don’t use images, formatting, or copy that implies products are endorsed by, or affiliated with, government entities or celebrities.### Messaging guidelines

Use the following suggested messaging guidelines to convey key aspects of Stripe Issuing, Stripe Treasury, or both programs. Stripe or our banking partners have validated (proven as true) this content, so you can confidently use this messaging in user-facing materials.

- [Issuing](#issuing-messaging-guidelines)
- [Treasury](#treasury-messaging-guidelines)

The following tables include validated content you can provide in your marketing campaigns. You can make non-substantive changes (for example, changing the design or infusing your brand’s voice) to the suggested messaging as long as the key information remains the same. Any substantive deviations from these guidelines require you to submit marketing materials and get approval from Stripe and our bank partners. Approvals might take up to 10 business days to process.

You’re responsible for training employees on these requirements if they engage in marketing or sales activities for your Treasury or Issuing program.

### Issuing messaging guidelines

The following table provides guidelines for you to follow when developing messaging around your Issuing program.

Topic categoryDoDon’tLogo and name usage

Your card program name and your brand name must have equal status, as with plain text: Widget balance® + Stripe. When referencing registered brand products, you must adhere to their separate brand guidelines. You only need to use the ®, ™, SM, mark once per asset.

Don’t maintain unequal status between the card program name and your brand name:

Widget balance® + Stripe

Comparison value propositionsUse language promoting the benefits of the card:- Better than cash
- Safer than carrying cash
- Manage your money hassle free
- Spend only what you load
- Spend only what you have on your card

Don’t make disparaging remarks about other financial products or institutions: this includes debit, credit, bank accounts, banks, or other financial products used or issued by financial institutions. Don’t allude to prepaid card programs as superior to other card products with terms like:- Better than credit
- Better than a bank account
- No interest
- No security deposit
- No debt

Currency and using the fundsUse phrases like:- Access your contractor earnings
- All [card program] cards are USD denominated
- [Card program] cards can be used anywhere that accepts Visa cards

Don’t use phrases like:- Access your wages
- Get funds in any format you want
- Can spend money across the world

What you can use the card for and limitationsUse phrases like:- Use [card program] for business needs
- Get [card program] for your commercial needs
- [Card program] can only be used for commercial purposes, and can’t be used for personal, family, or household purposes
- Spend [only] what you load
- Spend [only] what you have on your card

Don’t use phrases like:- Use [card program] for anything you want
- Spend funds to buy the things you love
- Personal cards
- Use these cards like a payday loan, title loan, or pawn shop loan

Where to spend fundsUse phrases like:- [Card program] can only be used for commercial purposes, and can’t be used for personal, family, or household purposes
- Spend funds easily on your business

Don’t use phrases like:- Can be used just like a personal account
- Get consumer cards
- Spend funds to buy the things you love

### Issuing messaging specifics per product

The following table provides guidelines for you to follow when developing messaging for specific cards in your Issuing program.

CardDoDon’tSpend card onlyUse phrases like:- …is a commercial credit program
- A business credit card

Don’t use phrases like:- Debit card
- Prepaid card
- Better than a debit card

Payout account only (Treasury account connected)Money management accountDon’t use phrases like:- Bank account
- Deposit account
- Checking account
- Savings account
- Similar terms to the previous ones that connote a traditional bank account product

### Treasury messaging guidelines

Don’t use words like “bank account,” “deposit account," “checking account,” “savings account,” or similar terms that imply a traditional bank account product because Stripe isn’t a bank. Pre-approved terms include the following:

- Business account
- Cash management account
- Financial account
- Money transfer account

See Marketing Treasury-based services for a full list of terms you can and can’t use to describe your accounts. Inaccurately referring to Treasury accounts as “bank accounts” could result in regulatory action, including fines.

CategoryDoDon’tLogo and name usage

When referencing registered/® brand products, you must adhere to their separate brand guidelines. You only need to reference the ®, ™, SM mark once per asset.

Don’t apply unequal status between the card program name and your brand name:

Widget balance® + Stripe

Description of account value propositionsUse the following terms:- Business account
- Cash management account
- Financial account
- Money transfer account

Don’t use the following terms:- “Bank account”
- “Deposit account”
- “Checking account”
- “Savings account”
- Similar terms to the previous ones that imply a traditional bank account product, because Stripe isn’t a bank

FDIC insuranceUse the following terms that incorporate the term “eligible”:- “Eligible for FDIC insurance”
- “FDIC insurance-eligible accounts”
- “Eligible for FDIC pass-through insurance”
- “Eligible for FDIC insurance up to the standard maximum deposit insurance per depositor in the same capacity"
- “Eligible for FDIC insurance up to $250K”

Don’t use the following terms:- “FDIC insured”
- “FDIC insured accounts”
- “FDIC pass-through insurance guaranteed”

### CAN-SPAM

The CAN-SPAM Act regulates marketing activity conducted by email. An email is deemed a commercial message, subject to the CAN-SPAM act, if the primary purpose of the email is to convey a commercial advertisement, or to promote a product or service. A transactional email is an email sent to a customer that has a primary purpose relating to a particular transaction or relationship between you and the customer, such as a payment reminder. The CAN-SPAM Act imposes more rigorous requirements on commercial email messages, as compared with transactional messages. Transactional messages aren’t subject to most of the requirements of the CAN-SPAM Act. If a message contains both transactional content and commercial content, the CAN-SPAM Act commercial email requirements might apply, if the primary purpose of the message can be considered commercial.

To facilitate compliance with the CAN-SPAM Act, any employee or staff using or having access to your email systems and resources for marketing must adhere to the following guidelines:

- Misleading header information. Any email message, whether commercial or transactional, must not contain:  - False or misleading header information.
  - A “from” line that doesn’t accurately identify any person (individual or business) who initiated the message.
  - Inaccurate or misleading identification of a protected computer used to initiate the message for purposes of disguising its origin.


- Deceptive subject headings. Any commercial email message must not contain deceptive subject headings. For example, a deceptive subject heading is one that likely misleads the recipient about a material fact regarding the message’s contents or subject matter.
- Opt-out mechanism. You must provide your customers with the ability to opt-out of receiving future commercial messages, and you must honor customer requests to opt-out within 10 days. You can’t require a user to pay a fee or provide information other than an email address to opt-out.
- Advertisement identification. Any commercial email message must contain clear and conspicuous identification that the message is an advertisement or solicitation.
- Physical address disclosure. Any commercial email message must disclose a valid physical address of the sender.

Failure to comply with CAN-SPAM could result in large fines for each violation.

### Testimonials

If you’re using testimonials or endorsements in advertising Stripe products to your users, consider the following:

- The person giving a testimonial must be a real person and a true, bona fide user of the service or product they’re talking about.
- You must obtain and keep their permission in writing to use their quote. You must update that permission every 24 months.
- Product benefits, costs, or features in any quotes must be verifiable and true to what most users can expect to get.
- If you paid someone for their quote, or gave them anything of value, you must put a disclaimer near the quote stating this fact. This includes paid actors, if their scripting makes it sound like they’re giving a testimonial.

### Prohibited advertising

You can’t advertise Stripe Issuing or Treasury, in any print, radio, TV, on the internet, or any other digital format that promotes any unlawful activity or causes reputation concerns for Stripe or our bank partners.

### Prohibition on international marketing

Treasury isn’t available to users or merchants located outside the US, so limit all marketing for Treasury to US domestic audiences.

For Issuing, although you may ship cards to international addresses for US-domiciled cardholders, you must not engage in marketing the Issuing program internationally or to persons located outside of the United States. This includes advertising or promoting Issuing through marketing channels such as social media, email, and paid search results. As with all other aspects of the Issuing program, you must comply with card network rules in connection with marketing activities.

### Required disclosures

Your users must understand the role that Stripe’s bank partners play in offering and operating certain financial products—and in many cases, that they’re entering into a contractual relationship with these banks. Your users must also understand the material costs and fees associated with their use of each financial product. We require you to build the following disclosures into your marketing materials:

Issuing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Issuing users must include the following information in an easily discoverable and accessible area on all marketing materials, account opening flows, and all product pages or interfaces:

- The name for your card program (for example, Rocket Rides Corporate Card).
- The relevant statement from the following table identifying the issuing bank. It can be in the footers section of your materials; however, it must be a legible font size and a contrasting color to the background.

Statement for Celtic Bank usersStatement for Sutton Bank usersStatement for Cross River Bank users[Card Program Name] Visa® Commercial Credit cards are issued by Celtic Bank.[Card Program Name] Visa® Prepaid Cards are issued by Sutton Bank®, Member FDIC, pursuant to a license from Visa USA Inc.[Card Program Name] Charge Cards are issued by Cross River Bank, Member FDIC.Treasury![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Treasury users must include the following information in an easily discoverable and accessible area on marketing materials, account opening flows, and all product pages or interfaces:

- A statement that you’re neither a bank nor a money transmitter.
- Statement of partnership with Stripe.
- “Stripe Payments Company” must be hyperlinked and point to`https://stripe.com`.

Statement for Evolve bank usersStatement for Goldman bank users[Company Name] partners with[Stripe Payments Company](https://stripe.com/)for money transmission services and account services with funds held at Evolve Bank & Trust, Member FDIC.[Company Name] partners with[Stripe Payments Company](https://stripe.com/)for money transmission services and account services with funds held at Goldman Sachs Bank USA, Member FDIC.Treasury and Issuing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If you’re using both Treasury and Issuing connected products, you must include the following information in an easily discoverable and accessible area on all marketing materials, account opening flows, and product surfaces:

- A name for your card program (for example, Rocket Rides Corporate Card).
- A combined statement identifying the issuing bank and saying that you’re neither a bank nor a money transmitter.

Example combined statement (Payout Card)[Company Name] partners with[Stripe Payments Company](https://stripe.com/)for money transmission services and account services with funds held at Evolve Bank & Trust, Member FDIC. [Card Program Name] Visa® Prepaid Cards are issued by Sutton Bank®, Member FDIC, pursuant to a license from Visa USA Inc.### Materials submission

Submit copies of your marketing materials and user interface mockups through our Review Intake Form for review before you launch. If you make any changes to marketing materials, application flows, or user communications, Stripe’s compliance team must perform a review before going live. Our team of compliance specialists reviews them with our bank partners and responds within 10 business days.

When submitting your materials:

- Provide full screenshots or product pages that include headings and footers.
- The preferable format for materials is PDF, however any format where all text is legible is acceptable.
- You will be asked what type of marketing material you’re submitting (for example, web banners, emails, search engine marketing, if marketing text only or images and text).
- You can send up to 5 attachments per submission.

Additional questions can be sent to our team at platform-compliance@stripe.com.

We might request that you change your marketing materials to comply with regulatory requirements. If we request a change, it’s your responsibility to update the materials and provide evidence of the change to Stripe. Failure to update materials at our request might result in Stripe disabling your Treasury or Issuing capabilities.

## Recordkeeping

To demonstrate your adherence to the requirements listed in this guide, we ask that you keep thorough records of all marketing materials, customer data, account information, and other disclosures you make to customers for at least 5 years. The following is a list of all records to keep, and examples of what could constitute a record.

Record typeExample form of recordsProduct user experienceScreenshots of all deployed versions of the product user experience and when each version was deployed, include application flow, customer dashboard, support pages, and so on.MarketingInventory of all marketing copy deployed, email distribution lists used, and email solicitation opt out lists (including timestamps of user opt outs).Customer communications and complaintsEmail interactions and documentation developed in the course of resolving complaints.ReceiptsReceipts provided by Stripe and evidence they’re uploaded to the customer’s Dashboard.Customer statementsHistorical statements generated and made available to customers for download.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Account management](#account-management)[Required agreements and disclosures](#required-agreements-and-disclosures)[Fees, credits, and rewards programs](#fees,-credits,-and-rewards-programs)[Customer communications](#customer-communications)[Statements](#statements)[Receipts](#receipts)[Going live](#going-live)[Recordkeeping](#recordkeeping)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
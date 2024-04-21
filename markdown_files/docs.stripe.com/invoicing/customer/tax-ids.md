htmlCustomer tax IDs | Stripe Documentation[Skip to content](#main-content)Customer tax IDs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fcustomer%2Ftax-ids)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fcustomer%2Ftax-ids)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Customers](/docs/invoicing/customer)# Customer tax IDs

Store, validate, and render customer tax ID numbers with Stripe Invoicing.### Missing Tax ID support?

Need another tax ID type? Request additional Tax ID types by emailing stripe-tax@stripe.com.

Displaying a customer’s tax ID on invoice documents is a common requirement that you can satisfy by adding tax IDs to customers. A customer’s tax IDs display in the header of invoice and credit note PDFs.

## Supported Tax ID types

Currently, Stripe supports the following Tax ID types in the following regions:

CountryEnumDescriptionExampleAndorra`ad_nrt`Andorran NRT numberA-123456-ZArgentina`ar_cuit`Argentinian tax ID number12-3456789-01Australia`au_abn`Australian Business Number (AU ABN)12345678912Australia`au_arn`Australian Taxation Office Reference Number123456789123Austria`eu_vat`European VAT numberATU12345678Bahrain`bh_vat`Bahraini VAT Number123456789012345Belgium`eu_vat`European VAT numberBE0123456789Bolivia`bo_tin`Bolivian tax ID123456789Brazil`br_cnpj`Brazilian CNPJ number01.234.456/5432-10Brazil`br_cpf`Brazilian CPF number123.456.789-87Bulgaria`bg_uic`Bulgaria Unified Identification Code123456789Bulgaria`eu_vat`European VAT numberBG0123456789Canada`ca_bn`Canadian BN123456789Canada`ca_gst_hst`Canadian GST/HST number123456789RT0002Canada`ca_pst_bc`Canadian PST number (British Columbia)PST-1234-5678Canada`ca_pst_mb`Canadian PST number (Manitoba)123456-7Canada`ca_pst_sk`Canadian PST number (Saskatchewan)1234567Canada`ca_qst`Canadian QST number (Québec)1234567890TQ1234Chile`cl_tin`Chilean TIN12.345.678-KChina`cn_tin`Chinese tax ID123456789012345678Colombia`co_nit`Colombian NIT number123.456.789-0Costa Rica`cr_tin`Costa Rican tax ID1-234-567890Croatia`eu_vat`European VAT numberHR12345678912Cyprus`eu_vat`European VAT numberCY12345678ZCzech Republic`eu_vat`European VAT numberCZ1234567890Denmark`eu_vat`European VAT numberDK12345678Dominican Republic`do_rcn`Dominican RCN number123-4567890-1Ecuador`ec_ruc`Ecuadorian RUC number1234567890001Egypt`eg_tin`Egyptian Tax Identification Number123456789El Salvador`sv_nit`El Salvadorian NIT number1234-567890-123-4Estonia`eu_vat`European VAT numberEE123456789EU`eu_oss_vat`European One Stop Shop VAT number for non-Union schemeEU123456789Finland`eu_vat`European VAT numberFI12345678France`eu_vat`European VAT numberFRAB123456789Georgia`ge_vat`Georgian VAT123456789Germany`eu_vat`European VAT numberDE123456789Greece`eu_vat`European VAT numberEL123456789Hong Kong`hk_br`Hong Kong BR number12345678Hungary`eu_vat`European VAT numberHU12345678Hungary`hu_tin`Hungary tax number (adószám)12345678-1-23Iceland`is_vat`Icelandic VAT123456India`in_gst`Indian GST number12ABCDE3456FGZHIndonesia`id_npwp`Indonesian NPWP number12.345.678.9-012.345Ireland`eu_vat`European VAT numberIE1234567ABIsrael`il_vat`Israel VAT000012345Italy`eu_vat`European VAT numberIT12345678912Japan`jp_cn`Japanese Corporate Number (*Hōjin Bangō*)1234567891234Japan`jp_rn`Japanese Registered Foreign Businesses' Registration Number (*Tōroku Kokugai Jigyōsha no Tōroku Bangō*)12345Japan`jp_trn`Japanese Tax Registration Number (*Tōroku Bangō*)T1234567891234Kazakhstan`kz_bin`Kazakhstani Business Identification Number123456789012Kenya`ke_pin`Kenya Revenue Authority Personal Identification NumberP000111111ALatvia`eu_vat`European VAT numberLV12345678912Liechtenstein`li_uid`Liechtensteinian UID numberCHE123456789Lithuania`eu_vat`European VAT numberLT123456789123Luxembourg`eu_vat`European VAT numberLU12345678Malaysia`my_frp`Malaysian FRP number12345678Malaysia`my_itn`Malaysian ITNC 1234567890Malaysia`my_sst`Malaysian SST numberA12-3456-78912345Malta`eu_vat`European VAT numberMT12345678Mexico`mx_rfc`Mexican RFC numberABC010203AB9Netherlands`eu_vat`European VAT numberNL123456789B12New Zealand`nz_gst`New Zealand GST number123456789Nigeria`ng_tin`Nigerian Tax Identification Number12345678-0001Norway`no_vat`Norwegian VAT number123456789MVANorway`no_voec`Norwegian VAT on e-commerce number1234567Oman`om_vat`Omani VAT NumberOM1234567890Peru`pe_ruc`Peruvian RUC number12345678901Philippines`ph_tin`Philippines Tax Identification Number123456789012Poland`eu_vat`European VAT numberPL1234567890Portugal`eu_vat`European VAT numberPT123456789Romania`eu_vat`European VAT numberRO1234567891Romania`ro_tin`Romanian tax ID number1234567890123Russia`ru_inn`Russian INN1234567891Russia`ru_kpp`Russian KPP123456789Saudi Arabia`sa_vat`Saudi Arabia VAT123456789012345Serbia`rs_pib`Serbian PIB number123456789Singapore`sg_gst`Singaporean GSTM12345678XSingapore`sg_uen`Singaporean UEN123456789FSlovakia`eu_vat`European VAT numberSK1234567891Slovenia`eu_vat`European VAT numberSI12345678Slovenia`si_tin`Slovenia tax number (davčna številka)12345678South Africa`za_vat`South African VAT number4123456789South Korea`kr_brn`Korean BRN123-45-67890Spain`es_cif`Spanish NIF number (previously Spanish CIF number)A12345678Spain`eu_vat`European VAT numberESA1234567ZSweden`eu_vat`European VAT numberSE123456789123Switzerland`ch_vat`Switzerland VAT numberCHE-123.456.789 MWSTTaiwan`tw_vat`Taiwanese VAT12345678Thailand`th_vat`Thai VAT1234567891234Turkey`tr_tin`Turkish Tax Identification Number0123456789Ukraine`ua_vat`Ukrainian VAT123456789United Arab Emirates`ae_trn`United Arab Emirates TRN123456789012345United Kingdom`eu_vat`Northern Ireland VAT numberXI123456789United Kingdom`gb_vat`United Kingdom VAT numberGB123456789United States`us_ein`United States EIN12-3456789Uruguay`uy_ruc`Uruguayan RUC number123456789012Venezuela`ve_rif`Venezuelan RIF numberA-12345678-9Vietnam`vn_tin`Vietnamese tax ID number1234567890## Validation

You’re responsible for the accuracy of customer information including their tax ID number. The invoice includes the customer tax ID whether or not it’s valid.

Stripe provides automatic validation to help determine ​​if the formatting is correct when you add the ID to our system. You can see the results of the validation in the Dashboard along with other customer information, including details returned from the government databases, and the registered name and address. However, we don’t continue to validate them over time. ​​If automatic validation isn’t available, you must manually verify these IDs.

### Australian Business Numbers (ABN)

Stripe automatically validates all Australian Business Numbers (ABNs) with the Australian Business Register (ABR).

### European Value-Added-Tax (EU VAT) Numbers

Stripe also automatically validates all European Value-Added-Tax (EU VAT) numbers with the European Commission’s VAT Information Exchange System (VIES). This process only validates whether or not the tax ID is valid—you still need to verify the customer’s name and address to make sure it matches the registration information.

VIES validation usually takes only a few seconds, but depending on the availability of various government databases, might take longer. Stripe automatically handles VIES downtime and attempts retries.

### United Kingdom Value-Added-Tax (GB VAT) Numbers

Stripe automatically validates all UK Value-Added-Tax (GB VAT) numbers with the United Kingdom’s Revenue & Customs (HMRC). This process only validates whether or not the tax ID is valid—you still need to verify the customer’s name and address to make sure it matches the registration information.

HMRC validation usually takes only a few seconds, but depending on the availability, might take longer. Stripe automatically handles HMRC downtime and attempts retries.

### Testing customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode. The tax ID type must be either the EU VAT Number or Australian Business Number (ABN).

NumberType`000000000`Successful verification`111111111`Unsuccessful verification`222222222`Verification remains pending indefinitely### Validation webhooks and Dashboard display

Because this validation process happens asynchronously, the customer.tax_id.updated webhook notifies you of validation updates.

![Tax validation tooltip in the Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/validation-tooltip.de17a6f286a786e5643e39f43c02a42e.png)

Hover over a customer’s EU VAT number to display their VIES information.

The Dashboard displays the results of the validation within the customer details, including information returned from the government databases, and the registered name and address.

When automatic validation isn’t available, you must manually verify these IDs.

## Managing

You can manage tax IDs in the Dashboard, with the customer portal, or the Tax ID API.

DashboardAPITo add a tax ID:

1. Navigate to the[Customers](https://dashboard.stripe.com/customers)page.
2. ClickActions>Edit information.
3. Scroll down to see theTax StatusandTax IDfields.
4. ClickAdd another IDto add a row to the tax ID list, where you can select the ID type and value.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported Tax ID types](#supported-tax-id)[Validation](#validation)[Managing](#managing)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
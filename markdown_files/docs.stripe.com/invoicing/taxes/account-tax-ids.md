htmlAccount tax IDs | Stripe Documentation[Skip to content](#main-content)Account tax IDs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Faccount-tax-ids)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Faccount-tax-ids)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Taxes](/docs/invoicing/taxes)# Account tax IDs

Store and render your tax IDs with Stripe Invoicing.### Missing Tax ID support?

Need another tax ID type? Request additional tax ID types by emailing Stripe support.

Displaying your tax IDs on invoice documents is a common regulatory requirement. With Stripe, you can add up to 25 tax IDs to your account. Both the account and customer tax IDs display in the header of invoice and credit note PDFs.

In the Invoice template, you can:

- Select default tax IDs to appear on every invoice and credit note PDF.
- Define a list of tax IDs to appear on a specific invoice.

WarningYou can’t add, change, or remove account tax IDs after an invoice is finalized.

## Managing account tax IDs

You can add and delete tax IDs using the invoice settings page in the Dashboard. After you add a tax ID in the Dashboard, you can set it as the default tax ID for every invoice and credit note PDF. Tax IDs are immutable—you can’t change the country and ID after you save the tax ID to your account.

Additionally, you can add and delete tax IDs with the create and delete endpoints.

### Adding and removing IDs

DashboardAPIVisit the invoice settings page. Click the Tax tab and add a new tax ID or remove an existing tax ID:

![Manage tax IDs in the Stripe Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-add.f10a7efcaf2ce75e42bc986ff3954c0b.png)

Manage account tax IDs in the Dashboard

### Setting default tax IDs

On the invoice settings page, click the Tax tab and locate the tax ID you want to set as the default. Click the overflow menu (), select Set as default, and click Save.

![Set default tax ID in the Stripe Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-default.c36bf6e90db0825b107b5b6d375396cf.png)

Set default account tax ID in the Dashboard

​​After you set a tax ID as the default, you can see a label in the tax information box:

![A default tax ID in the Stripe Dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/manage-default-set.a1c4d9a7605eabbe0491fb64cf031397.png)

A default account tax ID in the Dashboard

## Displaying tax IDs on invoices

Stripe automatically pulls your default tax IDs during invoice finalization.

To override the default and display multiple tax IDs on invoices, you can set tax IDs in the Dashboard or by using the API. To learn more about taxes and invoices, see Taxes.

DashboardAPIYou can set a list of tax IDs in the Dashboard using the Invoice Editor. ​​You can’t modify account tax IDs after an Invoice has been finalized.

In the Invoice Editor, scroll down to the Advanced Options section. Click the checkboxes to toggle which tax IDs ​​to display on that invoice. To remove tax IDs from the invoice, uncheck the boxes.

![Tax ID invoice settings in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/invoice-editor.1e64187379099e87ac0eb00a4a1c0e15.png)

Advanced Options section in the Invoice Editor

## Supported tax ID types

Currently, Stripe Invoicing supports the following tax ID types in the following regions:

CountryEnumDescriptionExampleAndorra`ad_nrt`Andorran NRT numberA-123456-ZArgentina`ar_cuit`Argentinian tax ID number12-3456789-01Australia`au_abn`Australian Business Number (AU ABN)12345678912Australia`au_arn`Australian Taxation Office Reference Number123456789123Austria`eu_vat`European VAT numberATU12345678Bahrain`bh_vat`Bahraini VAT Number123456789012345Belgium`eu_vat`European VAT numberBE0123456789Bolivia`bo_tin`Bolivian tax ID123456789Brazil`br_cnpj`Brazilian CNPJ number01.234.456/5432-10Brazil`br_cpf`Brazilian CPF number123.456.789-87Bulgaria`bg_uic`Bulgaria Unified Identification Code123456789Bulgaria`eu_vat`European VAT numberBG0123456789Canada`ca_bn`Canadian BN123456789Canada`ca_gst_hst`Canadian GST/HST number123456789RT0002Canada`ca_pst_bc`Canadian PST number (British Columbia)PST-1234-5678Canada`ca_pst_mb`Canadian PST number (Manitoba)123456-7Canada`ca_pst_sk`Canadian PST number (Saskatchewan)1234567Canada`ca_qst`Canadian QST number (Québec)1234567890TQ1234Chile`cl_tin`Chilean TIN12.345.678-KChina`cn_tin`Chinese tax ID123456789012345678Colombia`co_nit`Colombian NIT number123.456.789-0Costa Rica`cr_tin`Costa Rican tax ID1-234-567890Croatia`eu_vat`European VAT numberHR12345678912Cyprus`eu_vat`European VAT numberCY12345678ZCzech Republic`eu_vat`European VAT numberCZ1234567890Denmark`eu_vat`European VAT numberDK12345678Dominican Republic`do_rcn`Dominican RCN number123-4567890-1Ecuador`ec_ruc`Ecuadorian RUC number1234567890001Egypt`eg_tin`Egyptian Tax Identification Number123456789El Salvador`sv_nit`El Salvadorian NIT number1234-567890-123-4Estonia`eu_vat`European VAT numberEE123456789EU`eu_oss_vat`European One Stop Shop VAT number for non-Union schemeEU123456789Finland`eu_vat`European VAT numberFI12345678France`eu_vat`European VAT numberFRAB123456789Georgia`ge_vat`Georgian VAT123456789Germany`eu_vat`European VAT numberDE123456789Greece`eu_vat`European VAT numberEL123456789Hong Kong`hk_br`Hong Kong BR number12345678Hungary`eu_vat`European VAT numberHU12345678Hungary`hu_tin`Hungary tax number (adószám)12345678-1-23Iceland`is_vat`Icelandic VAT123456India`in_gst`Indian GST number12ABCDE3456FGZHIndonesia`id_npwp`Indonesian NPWP number12.345.678.9-012.345Ireland`eu_vat`European VAT numberIE1234567ABIsrael`il_vat`Israel VAT000012345Italy`eu_vat`European VAT numberIT12345678912Japan`jp_cn`Japanese Corporate Number (*Hōjin Bangō*)1234567891234Japan`jp_rn`Japanese Registered Foreign Businesses' Registration Number (*Tōroku Kokugai Jigyōsha no Tōroku Bangō*)12345Japan`jp_trn`Japanese Tax Registration Number (*Tōroku Bangō*)T1234567891234Kazakhstan`kz_bin`Kazakhstani Business Identification Number123456789012Kenya`ke_pin`Kenya Revenue Authority Personal Identification NumberP000111111ALatvia`eu_vat`European VAT numberLV12345678912Liechtenstein`li_uid`Liechtensteinian UID numberCHE123456789Lithuania`eu_vat`European VAT numberLT123456789123Luxembourg`eu_vat`European VAT numberLU12345678Malaysia`my_frp`Malaysian FRP number12345678Malaysia`my_itn`Malaysian ITNC 1234567890Malaysia`my_sst`Malaysian SST numberA12-3456-78912345Malta`eu_vat`European VAT numberMT12345678Mexico`mx_rfc`Mexican RFC numberABC010203AB9Netherlands`eu_vat`European VAT numberNL123456789B12New Zealand`nz_gst`New Zealand GST number123456789Nigeria`ng_tin`Nigerian Tax Identification Number12345678-0001Norway`no_vat`Norwegian VAT number123456789MVANorway`no_voec`Norwegian VAT on e-commerce number1234567Oman`om_vat`Omani VAT NumberOM1234567890Peru`pe_ruc`Peruvian RUC number12345678901Philippines`ph_tin`Philippines Tax Identification Number123456789012Poland`eu_vat`European VAT numberPL1234567890Portugal`eu_vat`European VAT numberPT123456789Romania`eu_vat`European VAT numberRO1234567891Romania`ro_tin`Romanian tax ID number1234567890123Russia`ru_inn`Russian INN1234567891Russia`ru_kpp`Russian KPP123456789Saudi Arabia`sa_vat`Saudi Arabia VAT123456789012345Serbia`rs_pib`Serbian PIB number123456789Singapore`sg_gst`Singaporean GSTM12345678XSingapore`sg_uen`Singaporean UEN123456789FSlovakia`eu_vat`European VAT numberSK1234567891Slovenia`eu_vat`European VAT numberSI12345678Slovenia`si_tin`Slovenia tax number (davčna številka)12345678South Africa`za_vat`South African VAT number4123456789South Korea`kr_brn`Korean BRN123-45-67890Spain`es_cif`Spanish NIF number (previously Spanish CIF number)A12345678Spain`eu_vat`European VAT numberESA1234567ZSweden`eu_vat`European VAT numberSE123456789123Switzerland`ch_vat`Switzerland VAT numberCHE-123.456.789 MWSTTaiwan`tw_vat`Taiwanese VAT12345678Thailand`th_vat`Thai VAT1234567891234Turkey`tr_tin`Turkish Tax Identification Number0123456789Ukraine`ua_vat`Ukrainian VAT123456789United Arab Emirates`ae_trn`United Arab Emirates TRN123456789012345United Kingdom`eu_vat`Northern Ireland VAT numberXI123456789United Kingdom`gb_vat`United Kingdom VAT numberGB123456789United States`us_ein`United States EIN12-3456789Uruguay`uy_ruc`Uruguayan RUC number123456789012Venezuela`ve_rif`Venezuelan RIF numberA-12345678-9Vietnam`vn_tin`Vietnamese tax ID number1234567890## See also

- [Connected account tax IDs on invoices](/connect/invoices#account-tax-ids)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Managing account tax IDs](#managing-tax-ids)[Displaying tax IDs on invoices](#tax-ids-invoices)[Supported tax ID types](#supported-tax-id)[See also](#see-also)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
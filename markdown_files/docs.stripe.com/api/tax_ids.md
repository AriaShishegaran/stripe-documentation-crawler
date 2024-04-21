htmlTax IDs | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Tax IDs

You can add one or multiple tax IDs to a customer or account. Customer and account tax IDs get displayed on related invoices and credit notes.

Related guides: Customer tax identification numbers, Account tax IDs

Endpoints
# The Tax ID object

### Attributes

- idstringUnique identifier for the object.


- countrynullablestringTwo-letter ISO code representing the country of the tax ID.


- customernullablestringExpandableID of the customer.


- typeenumType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat. Note that some legacy tax IDs have type unknown

Possible enum values`ad_nrt``ae_trn``ar_cuit``au_abn``au_arn``bg_uic``bh_vat``bo_tin``br_cnpj``br_cpf`[Show 62 more](#)
- valuestringValue of the tax ID.



### More attributesExpand all

- objectstring
- createdtimestamp
- livemodeboolean
- ownernullableobject
- verificationnullableobject

The Tax ID object`{  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",  "object": "tax_id",  "country": "DE",  "created": 123456789,  "customer": null,  "livemode": false,  "type": "eu_vat",  "value": "DE123456789",  "verification": null,  "owner": {    "type": "self",    "customer": null  }}`# Create a Customer tax ID

Creates a new tax_id object for a customer.

### Parameters

- typestringRequiredType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat


- valuestringRequiredValue of the tax ID.



### Returns

The created tax_id object.

POST/v1/customers/:id/tax_idsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=eu_vat \  -d value=DE123456789`Response`{  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",  "object": "tax_id",  "country": "DE",  "created": 1679431857,  "customer": "cus_NZKoSNZZ58qtO0",  "livemode": false,  "type": "eu_vat",  "value": "DE123456789",  "verification": {    "status": "pending",    "verified_address": null,    "verified_name": null  }}`# Create a tax ID

Creates a new account or customer tax_id object.

### Parameters

- typestringRequiredType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat


- valuestringRequiredValue of the tax ID.



### More parametersExpand all

- ownerobject

### Returns

The created tax_id object.

POST/v1/tax_idsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax_ids \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=eu_vat \  -d value=DE123456789`Response`{  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",  "object": "tax_id",  "country": "DE",  "created": 123456789,  "customer": null,  "livemode": false,  "type": "eu_vat",  "value": "DE123456789",  "verification": null,  "owner": {    "type": "self",    "customer": null  }}`# Retrieve a Customer tax ID

Retrieves the tax_id object with the given identifier.

### Parameters

No parameters.

### Returns

Returns a tax_id object if a valid identifier was provided.

GET/v1/customers/:id/tax_ids/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",  "object": "tax_id",  "country": "DE",  "created": 1679431857,  "customer": "cus_NZKoSNZZ58qtO0",  "livemode": false,  "type": "eu_vat",  "value": "DE123456789",  "verification": {    "status": "pending",    "verified_address": null,    "verified_name": null  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
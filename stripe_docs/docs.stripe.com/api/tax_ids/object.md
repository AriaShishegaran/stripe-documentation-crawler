- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Tax ID object

[The Tax ID object](/api/tax_ids/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- countrynullable stringTwo-letter ISO code representing the country of the tax ID.

Two-letter ISO code representing the country of the tax ID.

- customernullable stringExpandableID of the customer.

ID of the customer.

- typeenumType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat. Note that some legacy tax IDs have type unknownPossible enum valuesad_nrtae_trnar_cuitau_abnau_arnbg_uicbh_vatbo_tinbr_cnpjbr_cpfShow 62 more

Type of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat. Note that some legacy tax IDs have type unknown

- valuestringValue of the tax ID.

Value of the tax ID.

- objectstring

- createdtimestamp

- livemodeboolean

- ownernullable object

- verificationnullable object

# Create a Customer tax ID

[Create a Customer tax ID](/api/tax_ids/customer_create)

Creates a new tax_id object for a customer.

- typestringRequiredType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat

Type of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat

- valuestringRequiredValue of the tax ID.

Value of the tax ID.

The created tax_id object.

# Create a tax ID

[Create a tax ID](/api/tax_ids/create)

Creates a new account or customer tax_id object.

- typestringRequiredType of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat

Type of the tax ID, one of ad_nrt, ae_trn, ar_cuit, au_abn, au_arn, bg_uic, bh_vat, bo_tin, br_cnpj, br_cpf, ca_bn, ca_gst_hst, ca_pst_bc, ca_pst_mb, ca_pst_sk, ca_qst, ch_vat, cl_tin, cn_tin, co_nit, cr_tin, do_rcn, ec_ruc, eg_tin, es_cif, eu_oss_vat, eu_vat, gb_vat, ge_vat, hk_br, hu_tin, id_npwp, il_vat, in_gst, is_vat, jp_cn, jp_rn, jp_trn, ke_pin, kr_brn, kz_bin, li_uid, mx_rfc, my_frp, my_itn, my_sst, ng_tin, no_vat, no_voec, nz_gst, om_vat, pe_ruc, ph_tin, ro_tin, rs_pib, ru_inn, ru_kpp, sa_vat, sg_gst, sg_uen, si_tin, sv_nit, th_vat, tr_tin, tw_vat, ua_vat, us_ein, uy_ruc, ve_rif, vn_tin, or za_vat

- valuestringRequiredValue of the tax ID.

Value of the tax ID.

- ownerobject

The created tax_id object.

# Retrieve a Customer tax ID

[Retrieve a Customer tax ID](/api/tax_ids/customer_retrieve)

Retrieves the tax_id object with the given identifier.

No parameters.

Returns a tax_id object if a valid identifier was provided.

# Retrieve a tax ID

[Retrieve a tax ID](/api/tax_ids/retrieve)

Retrieves an account or customer tax_id object.

No parameters.

Returns a tax_id object if a valid identifier was provided.

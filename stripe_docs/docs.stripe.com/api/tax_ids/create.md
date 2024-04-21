- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# List all Customer tax IDs

[List all Customer tax IDs](/api/tax_ids/customer_list)

Returns a list of tax IDs for a customer.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty. Raises an error if the customer ID is invalid.

[an error](#errors)

# List all tax IDs

[List all tax IDs](/api/tax_ids/list)

Returns a list of tax IDs.

- ownerobjectThe account or customer the tax ID belongs to. Defaults to owner[type]=self.Show child parameters

The account or customer the tax ID belongs to. Defaults to owner[type]=self.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty.

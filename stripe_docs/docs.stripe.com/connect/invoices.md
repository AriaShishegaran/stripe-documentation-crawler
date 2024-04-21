# Create invoices with Connect

Don’t know much about Connect? Check out our Overview article.

[Connect](/connect)

[Overview](/connect)

You can create invoices for connected accounts, which support several approaches for collecting payments. You can use direct charges to create them directly on the connected account. Alternatively, you can create invoices on the platform with transfers to the connected account by using destination charges. You can also take an application fee on these invoices.

[invoices](/api/invoices)

[several approaches](/connect/charges)

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

Invoice transactions are based on Invoicing pricing.

[Invoicing pricing](https://stripe.com/invoicing/pricing)

## Create an invoice using direct charges

To create an invoice that directly charges on a connected account, create an invoice while authenticated as the connected account. For this to work, the customer must be defined on the connected account.

[create an invoice](/api#create_invoice)

[authenticated](/connect/authentication#stripe-account-header)

As with creating a direct charge on a connected account, you can create a customer on a connected account by using either the platform’s publishable key or the connected account’s publishable key. You can also create a token by using shared customers. When you use direct charges, the connected account is responsible for the cost of the Stripe fees, refunds, and chargebacks.

[creating a direct charge](/connect/direct-charges#collect-fees)

[shared customers](/connect/cloning-customers-across-accounts)

## Create an invoice using destination charges

To create an invoice that charges on the platform and creates automatic transfers to a connected account, create an invoice while providing the connected account ID as the transfer_data[destination] value.

[create an invoice](/api#create_invoice)

[value](/api/invoices/object#invoice_object-transfer_data)

For this to work, the customer must be defined on the platform account, and you must create the connected account token by using the platform’s publishable key. If charging a customer, the customer must exist within the platform account. When using automatic transfers, the platform is the business of record.

## Display Connected Account Tax IDs and Business Details on your Invoices

Certain regions have regulatory requirements for merchants to show their tax IDs and other business details on customer-facing documents.

In some cases, you can fulfill these requirements by displaying information about a connected account instead of information about your platform. The following steps show how to render a connected account’s tax ID and business details on invoice emails, invoice PDFs, Hosted Invoice Pages, and invoice receipts:

- Create tax IDs for your connected account.

- Set default tax IDs for your connected account.

- Specify the connected account either using the on_behalf_of parameter or as the issuer on existing or new invoices, subscriptions, and subscription schedules.

[on_behalf_of parameter](#on-behalf-of)

The following example creates a single tax ID for the connected account. Stripe stores the tax ID on the connected account. To create additional tax IDs, call the endpoint again.

Stripe automatically pulls default tax IDs from the invoice issuer’s account during finalization unless account_tax_ids is already set on the invoices.

You can set the tax IDs stored on the connected account as the default tax IDs for that account. The following example sets existing tax IDs as default tax IDs:

The following example sets issuer on an existing subscription. During invoice finalization, subscription invoices pull in the issuer’s default tax IDs:

The following example sets issuer during invoice creation:

Alternatively, the on_behalf_of parameter also prints a connected account’s details on the invoice email, invoice PDF, Hosted Invoice Page, and invoice receipt.

You can specify account_tax_ids for invoices, subscriptions, and subscription schedules to override the default tax IDs. The following example sets account_tax_ids on an existing subscription:

The following example sets account_tax_ids during invoice creation:

The tax ID you create is stored on the platform account instead of the connected account. The following example creates a single tax ID for the connected account without using the Stripe-Account header:

## Collect application fees

On the invoice, you can optionally withhold an application fee. The following example shows an application_fee_amount for an invoice with a direct charge on the connected account:

[application_fee_amount](/api/subscriptions/object#subscription_object-application_fee_percent)

This example shows an application_fee_amount for an invoice with a destination charge:

## Make the connected account the settlement merchant

To make the connected account the settlement merchant, charge the customer using the on_behalf_of parameter when you create or update the invoice. You must set on_behalf_of in the API before finalizing an invoice—the Dashboard doesn’t have an interface for invoices you send on behalf of connected accounts.

Setting the on_behalf_of parameter applies the branding, contact information, and account tax ID of the connected account to the invoice email, invoice PDF, Hosted Invoice Page, and invoice receipt. However, when you use on_behalf_of in test mode, emails aren’t sent—just like standard invoices sent via API. In test mode, you can verify that Stripe created an invoice by checking the Invoices page of the Dashboard.

[Invoices page](https://dashboard.stripe.com/test/invoices)

To collect payments on behalf of the connected account, the connected account also needs to have account capabilities enabled for the relevant payment methods. You can automatically transfer payments for invoices created on behalf of the connected account by using destination charges. For more information about the on_behalf_of​ parameter, refer to the relevant Connect documentation:

[account capabilities](/connect/account-capabilities)

- For automatic transfers to the connected account, refer to the on_behalf_of parameter details in the Create a charge guide.

[Create a charge](/connect/charges#on_behalf_of)

- For information on how to transfer payments manually, refer to Transfer availability.

[Transfer availability](/connect/separate-charges-and-transfers#transfer-availability)

- For a list of account capabilities that are required to collect payments on behalf of the connected account, refer to Payment method capabilities.

[Payment method capabilities](/connect/account-capabilities#payment-methods)

The following example shows how to use the on_behalf_of parameter for a new invoice by using separate charges and transfers:

As with standard destination charges, ​​you can set an application_fee_amount on invoices. This example shows how to use on_behalf_of with a destination charge and application fee.

Invoices created on behalf of a connected account ​​don’t support bank transfers payment methods, such as ACH Credit Transfer and paper checks.

## Integrate tax calculation and collection

You need to first determine which entity is liable for tax. The entity that’s liable for tax might be your connected account or the platform, depending on your business model. To learn more, see Stripe Tax with Connect.

[Stripe Tax with Connect](/tax/connect)

## See also

- Create charges

[Create charges](/connect/charges)

- Share customers across accounts

[Share customers across accounts](/connect/cloning-customers-across-accounts)

- Multiple currencies

[Multiple currencies](/connect/currencies)

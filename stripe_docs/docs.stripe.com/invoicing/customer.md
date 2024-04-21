# Customers

Create a customer for every new user or business you want to bill. When you create a new customer, set up a minimal customer profile to help generate more useful invoices, and enable Smart Retries (if you’re an Invoicing Plus user). After you set up your customer, you can issue one-off invoices or create subscriptions.

[minimal customer profile](#customer-profile)

[Invoicing Plus](https://stripe.com/invoicing/pricing)

[subscriptions](/billing/subscriptions/creating)

Before you create a new customer, make sure that the customer doesn’t already exist in the Dashboard. Creating multiple customer entries for the same customer can cause you problems later on, such as when you need to reconcile transaction history or coordinate saved payment methods.

You can create and manage customers on the Customers page when you don’t want to use code to create a customer, or if you want to manually bill a customer with a one-off invoice.

[Customers page](https://dashboard.stripe.com/customers)

You can also create a customer in the Dashboard during invoice creation.

When you create a new customer, you can set their account and billing information, such as Email, Name, and Country. You can also set a customer’s preferred language, currency, and other important details.

You can also perform these actions on the Customers page:

- Filter your customers.

- Delete customers.

- View all of your customers.

- Export a list of customer data.

To create a customer, complete these steps:

- Verify that the customer doesn’t already exist.

Verify that the customer doesn’t already exist.

- Click Add customer, or press N, on the Customers page.

Click Add customer, or press N, on the Customers page.

- At a minimum, enter your customer’s Name and Account email.

At a minimum, enter your customer’s Name and Account email.

- Click Add customer in the dialog.

Click Add customer in the dialog.

To edit a customer’s profile, complete these steps:

- Find the customer you want to modify and click the name on the Customers page.

Find the customer you want to modify and click the name on the Customers page.

- In the account information page, select Actions > Edit information.

In the account information page, select Actions > Edit information.

- Make your changes to the customer profile.

Make your changes to the customer profile.

- Click Update customer.

Click Update customer.

To delete a customer, complete these steps:

- Find the customer you want to delete on the Customers page.

Find the customer you want to delete on the Customers page.

- Click the checkbox next to your customer’s name followed by Delete. You can also click into the customer’s details page and select Actions > Delete customer.

Click the checkbox next to your customer’s name followed by Delete. You can also click into the customer’s details page and select Actions > Delete customer.

## Customer profiles

​​Use a basic customer profile for invoice and receipt generation or as a lightweight customer relationship management system (CRM) for your application. To create a minimal customer profile, set these properties:

- Email address.

- Customer name.

- Metadata with a reference to your application’s internal customer ID.

Stripe uses your customer’s email address to notify them of payment failures. Stripe also uses email addresses to notify customers when they need to perform an action to complete a payment.

[email address](/api/customers/object#customer_object-email)

Store the internal customer ID for your application in the metadata attribute. Like most Stripe resources, the Customer resource includes a Metadata object hash to flexibly store contextual key-value information. To aid in auditing and support, store your internal customer ID as a key-value pair on the Customer resource. This allows you to search for the customer using your internal reference ID. We recommend storing Stripe customer IDs against the internal customer model of your application.

[metadata](/api/customers/object#customer_object-metadata)

[Metadata](/api/metadata)

Use the address attributes to set a billing address for invoicing and credit notes. For physical good delivery, add a shipping address.

[address attributes](/api/customers/object#customer_object-address)

[shipping](/api/customers/object#customer_object-shipping)

Invoices, credit notes, and receipts display the billing address—a common requirement for tax compliance.

When you create a customer, use the Language dropdown to add their preferred language. (You can also add or edit a customer’s preferred language in the Customer details page or when creating an invoice.) Stripe uses the chosen language to localize invoice emails and PDFs, receipt emails and PDFs, and credit note PDFs.

To update the language through the API, use the preferred_locales parameter. This parameter accepts an ordered list of preferred languages sorted by preference. These preferred locale values are based on RFC-4646. Examples include en for English, or fr-CA for Canadian French. To learn more, see Customer preferred languages.

[preferred_locales](/api/customers/object#customer_object-preferred_locales)

[RFC-4646](https://tools.ietf.org/html/rfc4646)

[Customer preferred languages](/invoicing/customize#customer-language)

## Customer properties

The following table contains additional customer properties:

[payment](/payments)

[Payment Methods API](/payments/payment-methods)

[Customer credit balance](/invoicing/customer/balance)

[invoicing-related resources](/api/customers/create#create_customer-invoice_settings)

[tax IDs](/invoicing/customer/tax-ids)

[tax exemption status](/api/customers/create#create_customer-tax_exempt)

[addresses](#addresses)

[Tax Rates](/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)

## Common tasks

Here are some of the common tasks you can perform with the Customer resource:

- Sending an invoice to a customer: After you create the customer, you can send them an invoice.

Sending an invoice to a customer: After you create the customer, you can send them an invoice.

[send them an invoice](/invoicing/dashboard#create-invoice)

- Storing a customer credit balance: The customer credit balance feature allows you to assign credit and debit adjustments to a specific customer and then apply the resulting balance toward future invoices for them.

Storing a customer credit balance: The customer credit balance feature allows you to assign credit and debit adjustments to a specific customer and then apply the resulting balance toward future invoices for them.

- Adding and validating tax ID numbers: Displaying a customer’s tax ID on an invoice is a common requirement, and Stripe allows you to add multiple tax IDs to a customer. Their tax IDs display in the header of invoice and credit note PDFs. See the Customer tax IDs page for more details.

Adding and validating tax ID numbers: Displaying a customer’s tax ID on an invoice is a common requirement, and Stripe allows you to add multiple tax IDs to a customer. Their tax IDs display in the header of invoice and credit note PDFs. See the Customer tax IDs page for more details.

[Customer tax IDs](/invoicing/customer/tax-ids)

- Adding a coupon to a customer: A coupon contains information about a percent-off or amount-off discount, and Stripe Invoicing allows you to associate a coupon with a customer. Coupons apply a discount to the invoice amount due, on a pre-tax basis.

Adding a coupon to a customer: A coupon contains information about a percent-off or amount-off discount, and Stripe Invoicing allows you to associate a coupon with a customer. Coupons apply a discount to the invoice amount due, on a pre-tax basis.

[coupon](/api/coupons)

- Setting the currency for a customer: You can set the default currency to charge a customer for invoices using the Dashboard by navigating to the Customers page, selecting your customer, and clicking Edit next to Details. See the Multi-currency customers page for more details on billing the same customer using a different currency than their default currency.

Setting the currency for a customer: You can set the default currency to charge a customer for invoices using the Dashboard by navigating to the Customers page, selecting your customer, and clicking Edit next to Details. See the Multi-currency customers page for more details on billing the same customer using a different currency than their default currency.

[Multi-currency customers](/invoicing/multi-currency-customers)

- Creating customers in bulk: Bulk upload Customers using the Invoice & Customer Uploader app.

Creating customers in bulk: Bulk upload Customers using the Invoice & Customer Uploader app.

[Invoice & Customer Uploader](https://marketplace.stripe.com/apps/invoice-uploader)

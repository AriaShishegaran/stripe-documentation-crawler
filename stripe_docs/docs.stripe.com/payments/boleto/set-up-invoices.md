# Use Boleto with invoices

Learn how to set up Boleto as a payment method. Boleto is a voucher with a generated number that Customers can obtain from an ATM, a bank, an online bank portal, or an authorized agency.

[Boleto](/payments/boleto)

[payment method](/api/payment_methods)

[Customers](/api/customers)

[Enable Boleto emails](#enable-boleto-emails)

## Enable Boleto emails

Before you start your integration, go to Manage payments that require confirmation in your Subscriptions and emails settings and enable Send a Stripe-hosted link for customers to confirm their payments when required.

[Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic)

[Decide the collection method](#set-collection-method)

## Decide the collection method

You can set the collection method in the Dashboard or API. For invoices, you can choose to either send an invoice or charge your customer automatically. If you’re using the API, the send_invoice and charge_automatically values determine the collection method.

[API](/api/invoices/create#create_invoice-collection_method)

- Your customer hasn’t defined their preferred payment method to pay invoices or subscriptions. In this case, you want to give them the option to use either a credit card or Boleto.

- You’re missing important customer information required to use Boleto (full name, address, and tax ID).

- Your customer already chose to pay for their invoices or subscriptions using boletos.

- You have the customer information needed to create an invoice that uses Boleto (full name, address, and tax ID).

- Your customer needs to reenter their personal information details (full name, address, and tax ID) every time you send a new invoice, or for each new subscription cycle. This collection method doesn’t take into account the default payment method associated with that customer.

- Your customer has Boleto set up as their default payment method. Your customer receives an email with a Boleto voucher every time you send them an invoice, or there’s a subscription cycle.

- The invoice must contain a due date.

- Stripe creates the boleto—regardless of the invoice due date—as soon as your customer enters the needed details. Because boletos have their own expiration date (the default is 3 days), the invoice due date and the boleto expiration date won’t necessarily match. The boleto might expire before or after the invoice is due.

- The invoice doesn’t have a due date.

- Stripe creates the boleto when the merchant creates the invoice with a selected expiration date (the default is 3 days).

[Create a customer](#create-customers)

## Create a customer

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

[Create a product and price](#create-product-price)

## Create a product and price

Define all your business and product offerings in one place. Products define what you sell and Prices track how much and how often to charge. This is a core entity within Stripe that works with subscriptions, invoices, and Checkout.

[Products](/api/products)

[Prices](/api/prices)

[subscriptions](/billing/subscriptions/creating)

[invoices](/api/invoices)

[Checkout](/payments/checkout)

Prices enable these use cases:

- A software provider that charges a one-time setup fee whenever a user creates a new subscription.

- An e-commerce store that sends a recurring box of goods for 10 USD per month and wants to allow customers to purchase one-time add-ons.

- A professional services firm that can now create a standard list of services and choose from that list per invoice instead of typing out each line item by hand.

- A non-profit organization that allows donors to define a custom recurring donation amount per customer.

You can manage your product catalog with products and prices. Products define what you sell and prices track how much and how often to charge. Manage your products and their prices in the Dashboard or through the API.

If you used the Dashboard in test mode to set up your business, you can copy each of your products over to live mode by using Copy to live mode in the Product catalog page. Use our official libraries to access the Stripe API from your application.

[Product catalog page](https://dashboard.stripe.com/products)

- Navigate to the Product catalog page, and click Add product.

Navigate to the Product catalog page, and click Add product.

- Select whether you want to create a One-time product, or a Recurring one-time product.

Select whether you want to create a One-time product, or a Recurring one-time product.

- Give your product a name, and assign it a price.

Give your product a name, and assign it a price.

[Create and send an invoice](#create-invoice)

## Create and send an invoice

To create and send an invoice, complete these steps:

- In the Dashboard, go to the Invoices overview page, then click Create Invoice to open the invoice editor.   Whenever you exit the invoice editor, Stripe saves a draft. To delete a draft invoice, click the overflow menu () next to an invoice on the Invoices page.

[Invoices overview page](https://dashboard.stripe.com/invoices)

[invoice editor](https://dashboard.stripe.com/invoices/create)

[Invoices page](https://dashboard.stripe.com/invoices)

- Choose an existing customer by entering their name.

- Select your product under Items, and enter the Quantity. Stripe automatically populates the product’s price based on what you selected when you first created the product.

- Optional Click Item options if you need to add a tax rate, coupon, or supply date.NoteUse the Dashboard to create a tax rate or coupon.

Use the Dashboard to create a tax rate or coupon.

[tax rate](https://dashboard.stripe.com/tax-rates)

[coupon](https://dashboard.stripe.com/coupons/create)

- Optional Use the Memo box to provide more information to your customer. You can edit the memo on an invoice by clicking Edit memo on its details page.

- Select the following invoice delivery option, depending on whether you want to send the invoice or charge your customer automatically:NoteIf you want to automatically charge your customer using Boleto, navigate to the Customers page, click on the customer, and select Add Boleto under Payment methods.Automatically charge a payment method on file—Immediately charges the invoice amount to the payment method that you have on file for the customer. (Select Boleto as the payment option.)Email invoice with link—Enables Stripe to send an email with a payment page and an invoice PDF. (Select Boleto and card as the payment options.)

If you want to automatically charge your customer using Boleto, navigate to the Customers page, click on the customer, and select Add Boleto under Payment methods.

[Customers page](https://dashboard.stripe.com/customers)

- Automatically charge a payment method on file—Immediately charges the invoice amount to the payment method that you have on file for the customer. (Select Boleto as the payment option.)

Automatically charge a payment method on file—Immediately charges the invoice amount to the payment method that you have on file for the customer. (Select Boleto as the payment option.)

- Email invoice with link—Enables Stripe to send an email with a payment page and an invoice PDF. (Select Boleto and card as the payment options.)

Email invoice with link—Enables Stripe to send an email with a payment page and an invoice PDF. (Select Boleto and card as the payment options.)

- Optional Expand Advanced options, and add custom fields. You can also choose whether you want item prices to Include inclusive tax or Exclude tax. To learn more, see Net prices and taxes. Expand Advanced options, and add custom fields.

[custom fields](/invoicing/customize#custom-fields)

[Net prices and taxes](/invoicing/taxes#net-price-taxes)

[custom fields](/invoicing/customize#custom-fields)

- Click Review invoice and decide whether you want to include additional emails or continue editing. Send the invoice.

If you automatically charge your customer, they still need to pay the Boleto for the payment to succeed (despite the finalization of the invoice.) Stripe sends your customer an email with a link that they can visit to complete their Boleto payment.

Create an invoice with the Dashboard

## See also

- How Invoicing works

[How Invoicing works](/invoicing/overview)

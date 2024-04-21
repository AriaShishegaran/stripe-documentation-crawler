# Request a PAN data import

You can bring your existing customer data from another payment processor and import it into your Stripe account. We work with your current payment processor to securely migrate your data, including payment information. This allows you to continue charging customers without interruption or asking them to provide their payment details again.

## Data migration process

Migrating data to Stripe typically involves these steps:

- Build your Stripe integration.

[Build your Stripe integration](#build-integration)

- Ask your current processor to transfer your data to Stripe.

[Ask your current processor](#ask-current-processor)

- Update your integration to complete the migration.

[Update your integration](#update-integration)

- (Optional) Migrate subscriptions, if you have any.

[Migrate subscriptions](#work-with-subscriptions)

After the migration process is complete, you can process all of your payments on Stripe.

Build and test your Stripe integration before requesting data from your current processor. This gives you plenty of time to verify and test your new integration. If you have any questions about the migration process or integrating with Stripe, let us know.

[let us know](https://support.stripe.com/contact/email?topic=migrations)

[Build your Stripe integration](#build-integration)

## Build your Stripe integration

Stripe simplifies your security requirements so that your customers don’t have to leave your site to complete a payment. This is done through a combination of client-side and server-side steps:

- From your website running in the customer’s browser, Stripe securely collects your customer’s payment details.

- Stripe responds with a representative token.

- The browser submits the token, along with any other form data, to your server.

- Your server-side code uses that token in an API request (for example, when creating a charge).

[creating a charge](/payments/charges-api)

This approach streamlines your website’s checkout flow and ensures that sensitive payment information never touches your server, helping to ensure PCI-compliance.

[PCI-compliance](/security/guide#validating-pci-compliance)

Stripe’s payment process flow

With a Stripe integration:

- Your customer never leaves your website.

- Token creation isn’t tied to a specific product or amount.

- There’s no need to create a client-side key on-demand. You use a set, publishable API key instead.

[API key](/keys)

Before you begin your migration, set up your Stripe integration with Checkout. You can integrate it as a Stripe-hosted page or as an embedded form on your website.

[Checkout](/payments/checkout/how-checkout-works)

[Stripe-hosted page](/checkout/quickstart)

[embedded form](/checkout/embedded/quickstart)

Using this approach, you can accept payments on Stripe without impacting your current customers.

Before you ask your payment processor to transfer data to Stripe, be prepared to:

- Remap customer records.

[Remap customer records.](#remap-customer-records)

- Handle updates to payment information during the migration.

[Handle updates to payment information during the migration.](#handle-payment-information-updates)

You need to remap Customer records on your end after the migration. For example, a customer with an email address of jenny.rosen@example.com has an ID of 42 in your database, which corresponds to a customer ID of 1893 in your previous processor’s system.

[Customer](/api/customers)

After the migration, this same customer has an ID of cus_12345 in your Stripe account. To make it so that you can update your database with new references, a Stripe migrations specialist provides an import mapping file during your email correspondence. In some rarer cases, we upload this file to your Dashboard through a secure file drop.

[Dashboard](https://dashboard.stripe.com/settings/documents)

As an alternative to creating a new customer in your Stripe account for each unique customer ID in the files we receive from your prior processor, we can import the payment method data from prior records into existing Stripe customer objects instead. To choose this option:

- In the intake request form, choose Yes in response to Do you want to import data into Stripe Customer objects that already exist in your Stripe account?.

In the intake request form, choose Yes in response to Do you want to import data into Stripe Customer objects that already exist in your Stripe account?.

- Prepare a CSV mapping file containing two columns:old_customer_id: The unique identifier used by your previous processor.stripe_customer_id: That customer’s corresponding Stripe customer ID in cus_xxxx format.Don’t include sensitive data in the file.

Prepare a CSV mapping file containing two columns:

- old_customer_id: The unique identifier used by your previous processor.

- stripe_customer_id: That customer’s corresponding Stripe customer ID in cus_xxxx format.

Don’t include sensitive data in the file.

- When we receive the intake form, we email you a request for the CSV mapping file. Reply to the email with the prepared file.

When we receive the intake form, we email you a request for the CSV mapping file. Reply to the email with the prepared file.

Customers might need to update their payment information after you ask your previous processor to transfer your data but before it’s received and imported by Stripe. During this window, payment method changes submitted to your previous processor will be lost as they aren’t included in the transferred data. These changes also can’t be made on Stripe because the data hasn’t been imported yet, and the customer’s new Stripe customer ID isn’t yet known.

To handle this, make changes to your site’s process for handling updates to saved payment information. This includes preparations to perform a self-migration for any customer without a stored Stripe customer ID:

- Create a new Customer object in Stripe for your customer.

[Customer object](/api/customers/object)

- Attach the payment method to the Customer object.

- (Optional) Recreate the subscription.

[Recreate the subscription](#update-integration)

Updating your integration to handle these possibilities can prevent your customers from seeing errors or experiencing billing issues.

After the migration takes place, card-triggered updates, such as an expiration date change, are automatically handled by Stripe.

[automatically handled by Stripe](https://stripe.com/blog/smarter-saved-cards)

[Ask your current processor](#ask-current-processor)

## Ask your current processor

When you’ve built your integration and are ready to process payments on Stripe, it’s time to request your payment data from your previous processor. Having the account owner contact the processor aids in this process, as most will only initiate a data transfer upon the account owner’s request.

After requesting the data transfer from your previous processor, let us know. Stripe can import your customer payment details (such as credit cards and bank account information for ACH and SEPA payments) and billing address information. Stripe can’t, however, import any subscriptions—these need to be recreated separately.

[let us know](https://support.stripe.com/contact?email=true&subject=Migration+to+Stripe)

[ACH](/payments/ach-debit)

[SEPA](/payments/sepa-debit)

[recreated](#working-with-subscriptions)

Don’t send sensitive credit card details or customer information directly to Stripe. If you have this data, please contact migration support so that we can help you securely transfer your data.

[contact migration support](https://support.stripe.com/contact?subject=Migration+to+Stripe)

It can take between a few days and several weeks for your previous processor to transfer the final data to Stripe, so make sure to allow for this transition time in your migration plan. If the data we receive can’t be used, we’ll outline any issues and work with your previous processor to correct the data.

After your previous processor transfers your data, Stripe begins importing it into your account. Stripe creates a Customer for each unique customer in the transferred data file, and creates and attaches the customer’s cards as Card or Source objects. If the transferred data indicates the customer’s default card, we set that as the customer’s default payment method for charges and subscription payments.

[Customer](/api#customer_object)

[Card](/api#card_object)

[Source](/api#source_object)

[default payment method](/api#customer_object-default_source)

[subscription](/billing/subscriptions/creating)

This import process usually occurs within 10 business days of receiving complete and correct data from your previous processor.

[Update your integration](#update-integration)

## Update your integration

After the import process is complete, Stripe sends you a JSON file that maps your current processor’s IDs to the imported Stripe object IDs—you need to parse this mapping file and update your database accordingly. If you build your Stripe integration before attempting to import it, your system would have handled any card updates that happened during the transition.

After you update your integration with this mapping file, you can begin charging all your customers on Stripe. In the following example:

- Customer ID 1893 is imported as a new Customer with ID cus_abc123def456.

[Customer](/api#customer_object)

- The customer’s card with ID 2600 is imported as a new Card with ID card_2222222222.

[Card](/api#card_object)

- The customer’s card with ID 3520 is imported as a new Card with ID card_3333333333.

[Card](/api#card_object)

You can request that the data be imported as PaymentMethods when you submit the migration request to us, if you prefer. In this format, the only change to the mapping file is that IDs are in the form pm_2222222222.

[PaymentMethods](/api#payment_method_object)

If a customer’s credit card is declined after you complete the migration, ask them to provide their card’s CVC number or to update their card information. When that’s done, attempt the charge again.

[Work with subscriptions (Optional)](#work-with-subscriptions)

## Work with subscriptions (Optional)

Migrations that involve subscriptions typically involve these stages:

- Set up your billing integration.

[billing integration](/billing/subscriptions/build-subscriptions)

- Migrate your customer and payment processor information (as described on this page).

[described on this page](#data-migration-process)

- Import your subscriptions to Stripe Billing. Learn more about migrating subscriptions from other processors to Stripe.

[migrating subscriptions from other processors to Stripe](/billing/subscriptions/migrate-subscriptions)

You can import existing subscriptions by:

[subscriptions](/billing/subscriptions/creating)

- Using Stripe APIs.

[Using Stripe APIs](/billing/subscriptions/import-subscriptions)

After leaving your payment processor, confirm that any automatic billing of your customers has been canceled.

[Migration PGP key](#migration-pgp-key)

## Migration PGP key

If you’re unfamiliar with PGP, see GPG and start by importing a public key. After you familiarize yourself with the basics of PGP, use the following PGP key to encrypt sensitive data (like credit card information) for PCI-compliant migration. If you have any questions, or encounter any issues, contact us through our intake form.

[GPG](http://gnupg.org)

[importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84)

[intake form](https://support.stripe.com/contact/email?topic=migrations)

After you import our key, you can encrypt files to send by running:

This creates FILENAME.gpg with the following information:

- Key ID: 9C78B7620C1E99AD

- Key type: RSA

- Key size: 4096 bits

- Fingerprint: AEBF 7C48 38C4 4D2F DC99 A3F9 9C78 B762 0C1E 99AD

- User ID: Stripe Import Key (PCI) <support-migrations@stripe.com>

htmlRequired Verification Information for Taxes | Stripe Documentation[Skip to content](#main-content)Identity information on tax forms[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frequired-verification-information-taxes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frequired-verification-information-taxes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Required Verification Information for Taxes

Learn what account information you need to provide for your Connect accounts if you want Stripe to help you with US federal 1099 tax reporting.NoteStripe recommends that you consult a tax advisor to determine your tax filing and reporting requirements.

## Required information (1099-K, 1099-MISC, 1099-NEC)

The following table lists the requirements for connected accounts with any of the 1099 capabilities. Stripe requires the business tax details except when the account is set up as a Single Person Entity (SPE) with a US-based representative, in which case we’ll use the representative’s personal tax details.

Stripe defines a Single Person Entity as follows:

- Individual:[business type](/api/accounts/object#account_object-business_type)is`individual`
- Sole Proprietorship:[business type](/api/accounts/object#account_object-business_type)is`sole_prop`, or[business type](/api/accounts/object#account_object-business_type)is`company`and[business structure](/api/accounts/create#create_account-company-structure)is`sole_proprietorship`
- Single Member LLC:[business type](/api/accounts/object#account_object-business_type)is`company`and[business structure](/api/accounts/create#create_account-company-structure)is`single_member_llc`

Even if you don’t add the 1099 capabilities and want to update the information directly in Stripe to file your 1099 forms, these are the fields to populate.

TypeSPE with US-based representativeSPE with non-US-based representativeCompanyName- `individual.first_name`
- `individual.last_name`

`company.name``company.name`TIN`individual.id_number``company.tax_id``company.tax_id`Address

individual.address

Required address fields are:

- [individual.address.line1](/api/accounts/update#update_account-individual-address-line1)
- [individual.address.postal_code](/api/accounts/update#update_account-individual-address-postal_code)
- [individual.address.city](/api/accounts/update#update_account-individual-address-city)
- [individual.address.state](/api/accounts/update#update_account-individual-address-state)

company.address

Required address fields are:

- [company.address.line1](/api/accounts/update#update_account-company-address-line1)
- [company.address.postal_code](/api/accounts/update#update_account-company-address-postal_code)
- [company.address.city](/api/accounts/update#update_account-company-address-city)
- [company.address.state](/api/accounts/update#update_account-company-address-state)

company.address

Required address fields are:

- [company.address.line1](/api/accounts/update#update_account-company-address-line1)
- [company.address.postal_code](/api/accounts/update#update_account-company-address-postal_code)
- [company.address.city](/api/accounts/update#update_account-company-address-city)
- [company.address.state](/api/accounts/update#update_account-company-address-state)

If you have any of the 1099 capabilities turned on, Payouts become disabled if the required information isn’t collected and verified by 600 USD in charges.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
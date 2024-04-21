# Using Treasury to set up financial accounts and cards

Homebox is a fictitious vertical SaaS that builds software for home-services companies like HVAC technicians, cleaners, and plumbers. Homebox begins its Treasury integration by setting up a Treasury financial account and creating payment cards. To see how Homebox moves money to and from external bank accounts, see the Using Treasury to move money example integration.

[Using Treasury to move money](/treasury/examples/moving-money)

## Platform onboarding

Homebox is already a Stripe platform with Payments and Connect enabled. Homebox uses Custom connected accounts, and those connected accounts already have the card_payments capability enabled.

[Payments](/payments)

[Connect](/connect)

[Custom connected accounts](/connect/accounts)

## Adding capabilities

To use Treasury and Issuing services, Homebox needs to request the additional treasury and card_issuing capabilities for the platform’s users. The connected accounts must then onboard before Stripe can create a Treasury financial account for the user.

To use ACH transfers with Treasury, Homebox also needs to request the us_bank_account_ach_payments capability.

To request the treasury, card_issuing, and us_bank_account_ach_payments capabilities, Homebox makes a request to the Accounts API.

[Accounts API](/api/accounts)

To use Hosted Onboarding, Homebox makes a call to Account Links to retrieve a URL their customer can use to submit onboarding information for the Treasury financial account.

[Account Links](/api/account_links)

[https://example.com/reauth](https://example.com/reauth)

[https://example.com/return](https://example.com/return)

The response includes a URL the customer uses to access the application, which must be done before the link expires.

[https://connect.stripe.com/setup/s/iCtLfmYb2tEU](https://connect.stripe.com/setup/s/iCtLfmYb2tEU)

Homebox listens for the account.updated webhook to confirm the following fields and capabilities on the connected account:

## Creating a FinancialAccount

After Stripe adds the treasury capability to an account, Homebox can create the FinancialAccount object for the account. To do so, Homebox calls FinancialAccounts and requests the Features the company wants to provide.

The response confirms the account is processing. After complete and all relevant features are active, Homebox gets a confirmation from their treasury.financial_account.features_status_updated webhook listener.

## Creating a payment cardholder

Before Homebox can create cards for Treasury financial accounts, it needs to create cardholders. The cardholders in this example are plumbers who utilize Homebox services and own the connected accounts on the platform.

The response confirms the cardholder is created.

## Creating payment cards

Now that the connected account has a FinancialAccount object associated with it and an available cardholder, Homebox can create a payment card using the FinancialAccount balance as the card’s available balance.

The response confirms the card is issued.

## See also

- Using Treasury to move money

[Using Treasury to move money](/treasury/examples/moving-money)

- API reference

[API reference](/api/treasury/financial_accounts)

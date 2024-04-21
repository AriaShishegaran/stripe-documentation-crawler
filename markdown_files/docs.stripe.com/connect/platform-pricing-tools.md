htmlPlatform pricing tools | Stripe Documentation[Skip to content](#main-content)Platform pricing tools[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-pricing-tools)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-pricing-tools)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Platform pricing toolsBeta

Use platform pricing tools to create pricing schemes.Platform pricing tools enable you to store pricing logic within Stripe for monetization, reducing the effort needed to successfully integrate. As a beta feature, your platform needs to have permissions to access the platform pricing tools.

Platform pricing tools allow you to create pricing schemes that apply different application fees based on the properties of a transaction, without having to pass an application fee amount through the API. These pricing schemes apply to activity on your connected accounts where your platform is responsible for the Stripe fees.

## Request an invite

Interested in pricing tools?Access to pricing tools is currently limited to beta users. If you're interested in trying it out, please enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you for your interest. We will be in touch shortly.## Create a pricing scheme

A pricing scheme is a list of conditional fees that Stripe evaluates from top to bottom, with a default fee applied to any transactions that don’t match a defined condition exactly. A conditional fee is made up of a fee and a set of conditions. When a transaction occurs, Stripe applies the first matching conditional fee (from top to bottom). If no conditional fees match the transaction, Stripe uses the default fee.

1. Go to the[Connect settings](https://dashboard.stripe.com/settings/connect)page in your Stripe Dashboard.
2. Click[Platform pricing](https://dashboard.stripe.com/settings/connect/platform_pricing)to go to your Platform pricing page.
3. ClickAdd rulesto open theSet a default payment pricing schemedialog.
4. ClickAdd pricing ruleto create a new conditional fee rule. Use the dropdown menus to define the rule. Stripe calculates the fee in the specified currency, and then converts it to the settlement currency of the payment, if needed. You can add multiple pricing rules for the same pricing scheme, and they will be evaluated in the order that you select.  - Condition: Use the dropdown menus to define a condition that the rule applies to. The options available for the right input depend on the selection you make on the left dropdown, For more information about conditions on specific transactions, see[Products](#products).
  - Fee type: SelectFixed,Variable, orBlended.    - Fixed: Charge a specific amount. For example, charge 1.10 USD for every payment.
    - Variable: Charge a percentage of the total amount of the payment. For example, charge .45% of the total payment amount.      - Minimum (optional): Specify a lower bound for the fee amount. For example, charge at least 0.50 USD for every payment.
      - Maximum (optional): Specify an upper bound for the fee amount. For example, cap every fee at 2.00 USD.


    - Blended: Charge a specific amount on top of a percentage of the total payment. For example, charge 1.10 USD for every transaction in addition to .45% of the total payment amount.      - Maximum (optional): Specify an upper bound for the fee amount. For example, cap every fee at 2.00 USD.






5. UnderSet fallback rule, set a variable amount, fixed amount, or both. Use the Fixed dropdown to select the appropriate currency for the fixed amount. Stripe applies the default fee rule if any of the conditional fees you set aren’t matched by a particular transaction. The default fee must be a non-zero amount. You can’t have a zero percentage variable amount and a zero fixed amount.
6. (Optional) Click theAdd modifierif you want to take the calculated application fee and either mark it up or discount it by a certain percentage.
7. ClickSave. Alternatively, clickXat the top to close the dialog without saving the conditions you created.
8. If you’re passing in an explicit`application_fee`or`transfer_data[amount]`parameter on a payment, they take precedence over the no-code pricing schemes. To apply the configured pricing, stop passing in these parameters.

When you save the pricing scheme, Stripe automatically copies the pricing scheme to all of your connected accounts. The time it takes to update all your accounts depends on the number of connected accounts on your platform. Stripe displays a notice with the progress update in the Connect settings page.

## Override a specific account

After you set up a pricing scheme, you can override the rules for specific connected accounts on your platform. All connected account types support this, except for Standard connected accounts.

1. Select the account from the[Connected accounts page](https://dashboard.stripe.com/connect/accounts/overview)in your Dashboard.
2. On the connected account details page, clickCustomize pricingin theAccount pricingsection forCOLLECT APPLICATION FEES ON PAYMENTSto open theCustomize pricingdialog. If an overridden pricing scheme already exists, clickEditto open the dialog and make changes.![Account pricing section with the Customize pricing button highlighted.](https://b.stripecdn.com/docs-statics-srv/assets/customize-pricing.6839b07bcee32ec7ad40a4dd9b3c6ca0.png)


3. If you’re creating a new override, Stripe provides the option to start a blank pricing scheme(Create a new scheme)or to copy the pricing scheme set at the platform level as a starting point(Copy from your platform’s pricing scheme). If you want to make small adjustments to a complex pricing scheme of your platform, click theCopy from your platform’s pricing schemebutton. Otherwise, clickCreate new pricingto build a new pricing scheme from scratch.![Customize account pricing dialog with Cancel, Create new pricing, and Copy pricing buttons.](https://b.stripecdn.com/docs-statics-srv/assets/custom-dialog.1dbb42ae35cdac263dff5a412e81a43c.png)


4. Set the desired conditional and default fees as described in the preceding[Create a pricing scheme](#create-a-pricing-scheme)section.![Customize account pricing rule editor.](https://b.stripecdn.com/docs-statics-srv/assets/customize-pricing-dialog.abf5ceefac307b3299f2c860782a8309.png)


5. ClickSaveto save the override. Alternatively, clickXat the top to close the dialog without saving. You’ll be prompted toConfirmthe changes.

Subsequent edits to the platform pricing scheme don’t update the pricing scheme of overridden connected accounts.

## Revert overridden pricing schemes

You can revert overridden pricing schemes on the account details page. Click Revert to platform pricing in the Account pricing section of a connected account details page to use the platform’s pricing scheme for the connected account.

![Account pricing section with Revert to platform pricing button highlighted.](https://b.stripecdn.com/docs-statics-srv/assets/revert.151b51aa9959624829112e773e26faa4.png)

Revert to platform pricing

## Products

PaymentsInstant Payouts### Pricing scheme application

Stripe applies pricing schemes to a payment when all of the following are true:

- The pricing scheme is enabled.
- Your platform is responsible for the Stripe fees on the payment.
- The account is in a country that your platform is eligible to take application fees for.
- The`application_fee`or`transfer_data[amount]`parameters aren’t present on the payment. An explicit`application_fee`or`transfer_data[amount]`always takes precedence over managed application fees.
- The payment did not use multi-capture
- The amount used to calculate a fee is the captured amount of the payment. If the payment is a card charge authorized for 10 USD, and only 5 USD is captured, 5 USD is the amount used to compute the fee.

### Conditions

FieldApplies toDescriptionPayment methodAll paymentsThe payment method used, for example`card`,`us_bank_account`, or`boleto`Presentment currencyAll paymentsThe currency that the customer paid inSettlement merchant countryAll paymentsThe country of the payment settlement merchantCard brandCard paymentsThe type of card used, for example Visa or MastercardCard presentCard paymentsWhether or not the payment is in-personCard countryCard paymentsThe country of the card that the customer paid withCard product codeCard paymentsThe[product code](/connect/platform-pricing-tools/card-product-codes)of the card that the customer paid withCard typeCard paymentsFunding source of the card, such as a credit card or debit cardCard product categoryCard paymentsCard[class classification](https://support.stripe.com/questions/what-s-the-difference-between-standard-and-premium-cards), such as a Standard or Premium cardKlarna payment categoryKlarna paymentsThe[Klarna payment category](/api/charges/object#charge_object-payment_method_details-klarna-payment_method_category)used on a Klarna payment### Fee modifier

A fee modifier can either be a discount or markup. A markup applies a percent increase on the fee amount, whereas a discount applies a percent decrease. These will be calculated on the fee amount determined by the conditional and fallback rules.

Modifiers will compound based on the order they were added. For example, a 5% discount followed by a 10% markup will adjust a $1.00 fee to a $1.05 fee ($1.00 * 0.95 * 1.1 = $1.05).

### Interaction with subscriptions and invoices

Stripe applies managed application fees, configured in pricing tools, on invoice and subscription payments.

If you provide an application fee amount when creating an invoice, that fee takes precedence and Stripe doesn’t apply the configured managed application fee.

If you provide an application fee percent on a subscription, that fee takes precedence and Stripe doesn’t apply the configured managed application fee.

## Access platform pricing tools

Different roles have different levels of access to pricing schemes.

Although some roles don’t have access to the platform’s default pricing, they might be able to deduce it based on the version copied to the connected accounts.

Platform accountConnected accountsRolePermissionsAdministratorRead/WriteDeveloperNoneIAM AdminNoneConnect Onboarding AnalystNoneTransfer AnalystNoneAnalystNoneDispute AnalystNoneRefund AnalystNoneSupport SpecialistNoneSupport OnlyNoneTax AnalystNoneView OnlyNoneTopups OnlyNoneWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Request an invite](#request-an-invite)[Create a pricing scheme](#create-a-pricing-scheme)[Override a specific account](#override-a-specific-account)[Revert overridden pricing schemes](#revert-overridden-pricing-schemes)[Products](#products)[Access platform pricing tools](#access-platform-pricing-tools)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
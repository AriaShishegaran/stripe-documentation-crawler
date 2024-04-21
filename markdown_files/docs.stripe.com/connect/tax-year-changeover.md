htmlTax year changeover | Stripe Documentation[Skip to content](#main-content)Tax year changeover[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-year-changeover)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-year-changeover)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Tax year changeover

Learn how to manage tax forms for a new tax year.Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

# Preparing for tax year changeover

When a new tax year starts, you need to collect financial data for the new year in a new tax form for the new tax year. This is often before a user completes and submits tax forms from the previous year and before you provide them to users on your platform. To view the tax forms for the new year, you need to change the year selected either on the Tax forms page or on the Tax form settings page.

## About tax year settings

When a new tax year starts, we apply your settings from the previous year to the new one. If no settings are in place from the previous tax year, the Tax year settings dialog displays so you can configure settings for that tax year.

Tax forms are generated as soon as a new tax year starts and a payment is made. To see the tax forms that belong to the new tax year, users need to go through a changeover process. This means they need to enable the tax year picker either on the tax forms list or on the Tax Forms settings pages, and they need to create new settings.

## Selecting a tax year

The Tax forms page displays tax forms and settings for the current tax year.

You can display a different tax year by doing one of the following:

- Selecting a new tax year from the drop-down on theTax formspage
- Selecting a new tax year from the drop-down on theTax form settingspage

When you select a tax year from the drop-down for a year that has no activity, the Tax form defaults dialog opens. To activate the tax year, configure and save the Tax form default settings. If you don’t configure and save settings, you see the onboarding page when you open the Tax forms page. Select a different tax year from the drop-down to change to that year.

The selection persists between sessions, so it displays the same tax year when you next use the Dashboard. This lets you start working with tax forms for the current year and then switch back to the previous year to file or correct existing forms.

## Frequently asked questions

The following section provides answers to common questions about tax year changeover.

### How does the user change between tax years?

Click the small downward arrow next to the current tax year. All available tax years appear in a dropdown menu. Click one of these years to change the user’s view to that tax year.

### What is the default tax year?

After the new year’s forms become available, your Dashboard automatically changes over to that year.

### Does the default tax year reset when you log in? Will it remember what year I last looked at?

The year you select to view persists between logins. If you select to view your 2023 forms, the UI defaults to your 2023 forms when you log back in.

### What determines how many tax years are available to me?

Every time a tax year launches and those forms become available while you have a Stripe account with Tax Form Defaults configured, that year becomes available to you in your drop-down. If you began processing transactions in 2022, you won’t see 2021 forms in your Dashboard because you didn’t have an account when those were launched.

### Will I see tax years from before I used Stripe?

No. You only see years that launched while you had a Stripe account.

### Will I see tax years for which I filed no forms?

You are able to see any year in which you previously generated 1099 forms in the Connect dashboard, regardless of whether or not they were filed.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[About tax year settings](#about-tax-year-settings)[Selecting a tax year](#selecting-a-tax-year)[Frequently asked questions](#frequently-asked-questions)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
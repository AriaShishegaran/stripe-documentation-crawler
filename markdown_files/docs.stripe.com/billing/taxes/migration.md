htmlMigrate to Stripe Tax | Stripe Documentation[Skip to content](#main-content)Migrate to Stripe Tax[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftaxes%2Fmigration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftaxes%2Fmigration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Tax](/docs/billing/taxes)# Migrate to Stripe Tax

Learn how to migrate existing subscriptions to Stripe Tax.Stripe Tax allows you to calculate the tax to collect on your transactions. It computes the taxes and adds them to the payment automatically, based on the product and the customer location.

When you integrate with Stripe Tax, you need to update existing subscriptions to make sure that tax is automatically calculated going forward. This guide assumes that you have existing, active subscriptions. Otherwise, see how to automatically collect tax on new subscriptions or learn more about subscriptions.

Use the following high-level steps to update your active subscriptions to Stripe Tax:

1. [Activate Stripe Tax](#activate)if you haven’t already.
2. [Check customer locations](#customer-locations). In some cases, you might need to update the locations.
3. [Update products and prices](#products-prices)with tax codes and tax behaviors.
4. [Update subscriptions](#subs)to automatically calculate taxes on future[invoices](/api/invoices).
5. [Confirm](#confirm)that you’ve updated the subscriptions correctly.

Interested in using Stripe Tax and currency conversion?We’re developing a Payment Element integration that manages tax, discounts, shipping, and currency conversion. Read the Build a checkout page guide to learn more.

[Activate Stripe Tax](#activate)First, you need to activate Stripe Tax. Read the set up guide to learn how.

[Check customer locations](#customer-locations)To correctly calculate tax, we need to know the customer’s location. After activating Stripe Tax, you can check their tax location status by using the Dashboard, the API, or Dashboard exports.

DashboardAPIDashboard ExportsTo check a customer’s tax location status through the Dashboard, go to the Customers page, select the customer, and expand the customer’s details. The tax location status (automatic_tax) has four possible statuses:

StatusDescriptionPossible ActionValid (`supported`)Automatic tax fully supported.No further action required.Unrecognized location (`unrecognized_location`)The address isn’t valid for determining a tax location.Ask the customer for an updated address and set[customer.address](/api/customers/update#update_customer-address)to the new value. You can update the value through the API or Dashboard by editing the customer’s details.Not registered (`not_collecting`)The address is recognized and resolved to a location that you haven’t set up a collection location for.The action to take depends on your[tax obligations](/tax/monitoring). If you proceed, Stripe Tax doesn’t assess any taxes. If you want it to assess tax,[add an active registration](/tax/registering)for the jurisdiction the customer is based in.`failed`An[error](/error-codes)occurred with Stripe’s servers. This is rare.Try the request again or contact Stripe support for additional assistance.In case the status=unrecognized_location you need to update the customer location with an address that Stripe Tax can use. In the Dashboard, you can go into the Customers page, select the customer, and change its billing or shipping address under Details.

For more information on which customer address is valid, how they’re used, or how to handle errors, see Collect customer addresses.

[Update products and prices](#products-prices)Your products and prices use the default tax behavior you assigned when activating Stripe Tax. If you’d prefer to update active products and prices to calculate tax independently, set a tax_code and tax_behavior. See the full list of available tax codes and the guide for setting up tax codes and tax behavior for more information. For more information about products and prices, including how to decide whether a price should be inclusive or exclusive, see the Tax Setup FAQ.

### Update products

First, update any existing products with a tax_code. If you don’t explicitly define a tax_code on your product, Stripe Tax uses the preset product tax code from your settings.

Here’s how to update a Product with a tax_code using the API:

Command Line[curl](#)`curl https://api.stripe.com/v1/products/{{PRODUCT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d tax_code=txcd_10000000`To update a Product with a tax_code in the Dashboard, go to the Products page, select a product to edit and, in the product information page, choose the tax code from the drop-down menu.

### Update prices

Next, update the tax behavior for your prices.

Common mistakeYou can’t change tax_behavior after it’s been set to one of exclusive or inclusive. If you want to change the tax behavior of a price, you need to create a new price with the desired behavior, and archive the old price.

Here’s how to update a price with the API:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices/{{PRICE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d tax_behavior=exclusive`To update a price with the Dashboard, go to the products page, select the product with the price you want to update, and select additional options in the price information section. In the Include tax in price drop-down menu, select the behavior you want to associate with the price.

[Update subscriptions](#subs)With your customers, products, and prices updated, you’re ready to update existing subscriptions.

CautionStripe Tax requires a recognized customer location to calculate tax for a subscription. Therefore, an invoice for a subscription with automatic_tax[enabled]=true can’t be finalized when the customer’s location is unrecognized. Payment can’t be collected if the invoice can’t be finalized. Read more about the behavior of subscriptions when the customer’s location is unrecognized.

To get a list of subscriptions that need to be updated, go to the subscriptions page, click Export, select All as the Date range,  and select All columns in the Columns drop-down menu. Then you can filter by Automatic Tax Enabled column in the CSV export.

How you update the subscriptions depends on their state:

- If your subscriptions[don’t have existing tax rates](#no-tax-rates), you only need to enable automatic tax.
- If your subscriptions have[existing tax rates](#existing-tax-rates)(at either the subscription or line-item level), you need to clear out any existing tax rates and enable automatic tax. To avoid creating prorated items, you can schedule this update.
- If your subscriptions have[subscriptions schedules](#existing-subscription-schedules), you need to remove instances of`automatic_tax[enabled]=false`in the subscription schedule plans.

### Update subscriptions with no existing tax rates

To update subscriptions that have no tax rates configured, set automatic_tax.enabled to true.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "automatic_tax[enabled]"=true`Setting automatic_tax.enabled=true activates automatic tax calculations for all subsequent invoices created for that subscription.

To do this through the Dashboard, update the subscription and turn on the Calculate tax automatically option.

### Update subscriptions with existing tax rates

To update subscriptions with tax rates set at the subscription level, you need to remove the tax rates before enabling automatic_tax. When you make the update:

- Pass an empty string in the[default_tax_rates](/api/subscriptions/update#update_subscription-default_tax_rates)and[tax_rates](/api/subscriptions/object#subscription_object-items-data-tax_rates)fields for each subscription[item](/api/subscriptions/object#subscription_object-items). Doing this clears out tax rates set at both the subscription (`default_tax_rates`) and line-item (`tax_rates`) levels.
- Set[automatic_tax.enabled](/api/subscriptions/update#update_subscription-automatic_tax)to`true`.

server.rb[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

subscription = Stripe::Subscription.retrieve('{{SUBSCRIPTION_ID}}')
Stripe::Subscription.update(
  subscription.id,
  {
    automatic_tax: { enabled: true },
    # Removes existing tax_rates for each item in the subscription
    items: subscription.items.data.map {|item| {id: item.id, tax_rates: ''}},
    default_tax_rates: ''
  }
)`To make this update through the Dashboard, edit the subscription, then enable the calculate tax automatically option. The Dashboard automatically calculates tax going forward and removes any existing tax rates. If you haven’t updated your prices to set tax_behavior, the Dashboard prompts you to update any missing details before you can update the subscription.

### Update Subscriptions with subscription schedules

If you need to collect tax and any of your subscriptions include a subscription schedule that sets automatic_tax[enabled]=false, you must remove this parameter. To do this, update all phases of the subscription’s schedule by removing automatic_tax[enabled]=false and setting default_settings[automatic_tax][enabled]=true.

When you update a subscription schedule, you need to pass in all current and future phases. To do this, verify the set parameters, then enable Stripe Tax in the subscription schedule.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`To update the subscription schedule after you obtain it, remove the automatic_tax[enabled]=false parameter, and pass down the other phases and parameters:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][start_date]"=1577865600 \
  -d "phases[0][end_date]"=1578038400 \
  -d "phases[1][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
  -d "phases[1][items][0][quantity]"=2 \
  -d "phases[1][start_date]"=1578038400 \
  -d "phases[1][end_date]"=1580544000 \
  -d "default_settings[automatic_tax][enabled]"=true`Schedule the update![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If you want to avoid creating a prorated item, you can schedule the update to occur at the start of the next cycle.

You can currently only schedule subscription updates with the API:

server.rb[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

subscription = Stripe::Subscription.retrieve(
  '{{SUBSCRIPTION_ID}}',
)
schedule = Stripe::SubscriptionSchedule.create({
  from_subscription: subscription.id
})
Stripe::SubscriptionSchedule.update(
  schedule.id,
  {
    end_behavior: 'release',
    phases: [
      # The first phase contains items for the
      # latest subscription invoice
      {
        items: [
          # Prices and tax_rates for each item
          {
            price: '{{PRICE_ID}}',
            tax_rates: [
              '{{TAX_RATE_ID}}'
            ]
          }
        ],
        default_tax_rates: ['{{TAX_RATE_ID}}'],
        start_date: subscription.current_period_start,
        end_date: subscription.current_period_end
      },
      # The second phase removes manual tax rates and enables
      # automatic tax calculation
      {
        items: [
          # Prices for each item with tax_rates: ''
          {
            price: '{{PRICE_ID}}',
            tax_rates: ''
          }
        ],
        default_tax_rates: '',
        automatic_tax: {enabled: true},
        iterations: 1
      }
    ]
  }
)`[Confirm updates](#confirm)To confirm that you’ve properly updated your subscriptions, retrieve the upcoming invoice of a subscription and inspect the results of its tax calculation.

You can retrieve the tax amounts from the tax and total_tax_amounts fields on the upcoming invoice, and from the per-line-item tax_amounts fields. The invoice has an automatic_tax field showing the status of the calculation, with one of three possible statuses:

StatusDescriptionPossible Action`complete`Stripe Tax has successfully assessed the taxes on the payment.You can retrieve the tax amounts from the tax and`total_tax_amounts`fields on the latest invoice, and from the per-line item`tax_amounts`fields.`requires_location_inputs`Stripe Tax didn’t have enough information to determine the customer’s location and was unable to assess taxes.Collect more information from a customer (such as a full street address) and update the[customer.address](/api/invoices/object#invoice_object-customer_address)field.`failed`Internal Stripe error.Try the request again or contact Stripe support for additional assistance.## See also

- [Collect taxes for recurring payments](/billing/taxes/collect-taxes?tax-calculation=stripe-tax)
- [Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Activate Stripe Tax](#activate)[Check customer locations](#customer-locations)[Update products and prices](#products-prices)[Update subscriptions](#subs)[Confirm updates](#confirm)[See also](#see-also)Products Used[Billing](/billing)[Tax](/tax)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
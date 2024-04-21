htmlLists | Stripe Documentation[Skip to content](#main-content)Lists[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Flists)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Flists)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)# Lists

Create your own lists of information to block, allow, or review matching payments.Users of Stripe Radar for Fraud Teams can create lists of specific types of information and use them in rules. For example, you might want to create rules using a list of:

- Customer IDs for trusted customers. Use this list to automatically allow payments by these customers.
- Email addresses you tied to fraud. Automatically block any payment with an email address on this list.
- Suspicious IP addresses. Place payments into review that have a matching IP address.

Lists make rules more manageable. Instead of creating individual rules for one item at a time, you can add similar types of information to a list (for example, email addresses) for a rule to use automatically.

## Default lists

Stripe Radar includes a set of default lists to help you get started. Each of the following types of information has a separate allow and block list that your default allow and block rules can reference.

- Card BIN

The Bank Identification Number (BIN) of the card being used to make the payment. This is the first six digits of the card number (for example, 424242).


- Card country

The two-letter code corresponding to the country where the card was issued (for example, US).


- Card fingerprint

The fingerprint of the card being used to make the payment. The card fingerprint is a unique Stripe identifier of a particular card number (for example, 6GX8LJs7yxR8xV). It’s a property of the Card object and you can see it in the Dashboard when viewing a payment.


- Charge description

The description supplied with the payment.


- Client IP country

The two-letter code corresponding to the country-level geolocation of the IP address where the payment originates (for example, GB).


- Client IP address

The IP address from which the payment originates (for example, 13.112.224.240).


- Customer ID

The customer ID supplied with the payment (for example, cus_AeFLnRaI51AbRi).


- Email

The first email derived from the charge, card, or customer objects, in that order (for example, jenny.rosen@example.com).


- Email domain

The first email domain derived from the Charge, Card, or Customer objects, in that order (for example, example.com).



NoteYou can add and remove items from these lists but you can’t edit or remove the default lists themselves.

## Custom lists

You can create lists of your own that contain items that are a specific type of information. The types of lists you can create are:

- String
- Case-sensitive string
- Card fingerprint
- Card BIN
- Customer ID
- Email
- IP address
- Country

Use the Dashboard or the API to create lists. To create a new list in the Dashboard:

1. ClickNew.
2. Enter a name for the list (we automatically generate an alias to use as a reference when writing rules, but you can override this).
3. Select the type of list to create.
4. ClickAddto save your new list.

After creating your new list, add a new rule that references it.

You can edit or remove lists you’ve created by clicking the overflow menu (•••), and you can edit the list directly by clicking the name of the list.

## Managing list items

### Adding items with Stripe Radar for Fraud Teams

Users of Stripe Radar for Fraud Teams can also add items directly to lists from the Dashboard.

You can view and remove items when viewing a list in the Dashboard. Each item includes information about when it was added and by whom. You can filter items by value, author, and date added. Each list can contain up to 50,000 items.

You can add items to your default block list by refunding and reporting a payment as fraudulent. Doing so takes the following actions:

- Adds the card fingerprint to your default card fingerprint block list. If the payment is made using a[Customer](/api#customer_object)object, it adds the card fingerprints of any other cards also added to the list.
- Adds any email address associated with the payment to your default email block list. It takes the email address from:  - The`receipt_email`of the payment
  - The`email`of the`Customer`object that the payment was created on
  - Any email addresses found in the customer or payment`description`fields, and in the card’s`name`field



When refunding a payment because of suspected fraud, make sure to specify this reason to help our machine learning systems recognize similar cases in the future.

You can also make a charge update request using the API and set fraud_details.user_report to fraudulent. This also adds any associated cards and email addresses to your card fingerprint and email block lists.

When adding string list items in the Dashboard, you have the option of selecting the length of time before expiration. These items are only active in the list for as long as you specify. After they expire, they’re no longer active in rule evaluation.

## See also

- [Rules](/radar/rules)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Default lists](#default-lists)[Custom lists](#custom-lists)[Managing list items](#managing-list-items)[See also](#see-also)Products Used[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
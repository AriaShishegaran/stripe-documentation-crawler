# Lists

Users of Stripe Radar for Fraud Teams can create lists of specific types of information and use them in rules. For example, you might want to create rules using a list of:

[rules](/radar/rules)

- Customer IDs for trusted customers. Use this list to automatically allow payments by these customers.

- Email addresses you tied to fraud. Automatically block any payment with an email address on this list.

- Suspicious IP addresses. Place payments into review that have a matching IP address.

Lists make rules more manageable. Instead of creating individual rules for one item at a time, you can add similar types of information to a list (for example, email addresses) for a rule to use automatically.

## Default lists

Stripe Radar includes a set of default lists to help you get started. Each of the following types of information has a separate allow and block list that your default allow and block rules can reference.

[default allow and block rules](/radar/rules)

- Card BINThe Bank Identification Number (BIN) of the card being used to make the payment. This is the first six digits of the card number (for example, 424242).

Card BIN

The Bank Identification Number (BIN) of the card being used to make the payment. This is the first six digits of the card number (for example, 424242).

- Card countryThe two-letter code corresponding to the country where the card was issued (for example, US).

Card country

The two-letter code corresponding to the country where the card was issued (for example, US).

- Card fingerprintThe fingerprint of the card being used to make the payment. The card fingerprint is a unique Stripe identifier of a particular card number (for example, WNI3WbPbnfltHZ). It’s a property of the Card object and you can see it in the Dashboard when viewing a payment.

Card fingerprint

The fingerprint of the card being used to make the payment. The card fingerprint is a unique Stripe identifier of a particular card number (for example, WNI3WbPbnfltHZ). It’s a property of the Card object and you can see it in the Dashboard when viewing a payment.

[fingerprint](/api#card_object-fingerprint)

[Card](/api#card_object)

- Charge descriptionThe description supplied with the payment.

Charge description

The description supplied with the payment.

[description](/api#charge_object-description)

- Client IP countryThe two-letter code corresponding to the country-level geolocation of the IP address where the payment originates (for example, GB).

Client IP country

The two-letter code corresponding to the country-level geolocation of the IP address where the payment originates (for example, GB).

- Client IP addressThe IP address from which the payment originates (for example, 13.112.224.240).

Client IP address

The IP address from which the payment originates (for example, 13.112.224.240).

- Customer IDThe customer ID supplied with the payment (for example, cus_AeFLnRaI51AbRi).

Customer ID

The customer ID supplied with the payment (for example, cus_AeFLnRaI51AbRi).

[customer ID](/api#charge_object-customer)

- EmailThe first email derived from the charge, card, or customer objects, in that order (for example, jenny.rosen@example.com).

Email

The first email derived from the charge, card, or customer objects, in that order (for example, jenny.rosen@example.com).

- Email domainThe first email domain derived from the Charge, Card, or Customer objects, in that order (for example, example.com).

Email domain

The first email domain derived from the Charge, Card, or Customer objects, in that order (for example, example.com).

You can add and remove items from these lists but you can’t edit or remove the default lists themselves.

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

[Dashboard](https://dashboard.stripe.com/test/radar/lists)

[API](/api/radar/value_lists/create)

- Click New.

- Enter a name for the list (we automatically generate an alias to use as a reference when writing rules, but you can override this).

- Select the type of list to create.

- Click Add to save your new list.

After creating your new list, add a new rule that references it.

[add a new rule](/radar/rules/reference#lists)

You can edit or remove lists you’ve created by clicking the overflow menu (•••), and you can edit the list directly by clicking the name of the list.

## Managing list items

Users of Stripe Radar for Fraud Teams can also add items directly to lists from the Dashboard.

You can view and remove items when viewing a list in the Dashboard. Each item includes information about when it was added and by whom. You can filter items by value, author, and date added. Each list can contain up to 50,000 items.

[Dashboard](https://dashboard.stripe.com/test/radar/lists)

You can add items to your default block list by refunding and reporting a payment as fraudulent. Doing so takes the following actions:

[refunding and reporting a payment as fraudulent](/radar/risk-evaluation#feedback-on-risk-evaluations)

- Adds the card fingerprint to your default card fingerprint block list. If the payment is made using a Customer object, it adds the card fingerprints of any other cards also added to the list.

[Customer](/api#customer_object)

- Adds any email address associated with the payment to your default email block list. It takes the email address from:The receipt_email of the paymentThe email of the Customer object that the payment was created onAny email addresses found in the customer or payment description fields, and in the card’s name field

- The receipt_email of the payment

- The email of the Customer object that the payment was created on

- Any email addresses found in the customer or payment description fields, and in the card’s name field

When refunding a payment because of suspected fraud, make sure to specify this reason to help our machine learning systems recognize similar cases in the future.

You can also make a charge update request using the API and set fraud_details.user_report to fraudulent. This also adds any associated cards and email addresses to your card fingerprint and email block lists.

[charge update](/api/charges/update#update_charge-fraud_details)

When adding string list items in the Dashboard, you have the option of selecting the length of time before expiration. These items are only active in the list for as long as you specify. After they expire, they’re no longer active in rule evaluation.

## See also

- Rules

[Rules](/radar/rules)
htmlConnected accounts, cardholders, and cards | Stripe Documentation[Skip to content](#main-content)Connected accounts cardholders and cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fconnect%2Fcardholders-and-cards)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fconnect%2Fcardholders-and-cards)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Connected accounts, cardholders, and cards

Learn how to create and manage cardholders and cards with Stripe Connect.Connected accounts represent business entities. Cardholders represent individuals associated with those business entities. One connected account can have multiple cardholders. For example, a connected account for a small business may have multiple cardholders for the owner and its employees. After you create a cardholder, you issue them a virtual or physical card.

[Create cardholders](#create-cardholders)To create a Cardholder, use the Cardholders API and provide the required information. A valid phone number and email address are required to use digital wallets but are optional for physical cards.

NoteAs a Connect platform, you make API calls on behalf of your connected accounts by including a Stripe-Account header and the connected account’s account ID.

FieldParameterDescriptionBilling information`billing`Cardholder’s billing address (typically the primary business address)Type`type`Whether the cardholder is a ‘company’ or ‘individual’. See[Choose a cardholder type](/issuing/other/choose-cardholder)for guidance.Phone number`phone_number`Required if using digital walletsEmail`email`Email address of the cardholder. Required if using digital walletsCommand Line[curl](#)`curl https://api.stripe.com/v1/issuing/cardholders \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d name="Jenny Rosen" \
  --data-urlencode email="jenny.rosen@example.com" \
  --data-urlencode phone_number="+18008675309" \
  -d status=active \
  -d type=individual \
  -d "individual[first_name]"=Jenny \
  -d "individual[last_name]"=Rosen \
  -d "individual[dob][day]"=1 \
  -d "individual[dob][month]"=11 \
  -d "individual[dob][year]"=1981 \
  -d "billing[address][line1]"="510 Townsend Street" \
  -d "billing[address][city]"="San Francsico" \
  -d "billing[address][state]"=CA \
  -d "billing[address][postal_code]"=94111 \
  -d "billing[address][country]"=US`Stripe returns a Cardholder object that contains the information you provided and sends the issuing_cardholder.created webhook event.

Stripe must screen cardholder identity information in accordance with legal and regulatory guidelines. This can block authorizations based on cardholder attributes. Learn more about watchlist reviews.

After you create a Cardholder, call the Cardholder update endpoint with the parameters that need to be changed. If successful, an updated Cardholder object is returned.

Cardholders have a default active status, which means that any cards attached to the cardholder can approve authorizations. You can change the status to inactive by updating the cardholder. An inactive status on a Cardholder means all authorizations will be declined for any attached cards with a reason of cardholder_inactive.

[Create cards](#create-cards)After you create a Cardholder, issue them a card with the Cards API.

A Card object represents a physical card or virtual card. Creating a physical card requires a shipping address, and you can provide additional arguments to specify shipment packaging and delivery service.

Cardholder`cardholder`Cardholder’s IDCurrency`currency`Three-letter ISO currency code, in lowercase. Supported currencies are`usd`in the US,`gbp`in the UK, and`eur`in euro area counties.Type`type`Can be`physical`or`virtual`The following call is an example of issuing a virtual card attached to the specified Cardholder:

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d cardholder=ich_1234 \
  -d currency=usd \
  -d type=virtual`Stripe returns a Card object upon creation and sends the issuing_card.created webhook event.

[Activate cards](#activate-cards)Cards must be activated before authorizations are approved.

If you don’t specify a status when you create the card, the card has the default status of inactive. A card remains inactive until the status is changed with the Card update endpoint.

To activate a card:

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d status=active`[Deactivating cards](#deactivating-cards)You can deactivate cards  by setting the status to inactive with Card update endpoint. This means you can’t approve any new authorizations for the card. You can still approve authorizations that were opened on the card before the status was set to inactive. To approve any new authorizations, you need to change the status of the card to active.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d status=inactive`## See also

Managing authorizations.

[Cancel cards](#cancel-cards)You can cancel a card by changing the status to canceled with the Card update endpoint. The canceled status is terminal and can’t be reverted. You can’t approve new authorizations for a card with a canceled status. You can still approve authorizations that were opened on the card before the status was set to canceled.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d status=canceled`### Listing Cardholders

Find cardholders associated with a connected account by by making a Cardholders API GET request and passing the specific Stripe-Account into the header.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cardholders \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response contains a list of cardholders:

`{
  "object": "list",
  "data": [
    {
      "id": "ich_1234a",
      "object": "issuing.cardholder",
      "billing": {
        "address": {
          "city": "San Francisco",
          "country": "US",
          "line1": "510 Townsend Street",
          "line2": null,
          "postal_code": "94111",
          "state": "CA"
        }
      },
      "company": null,
      "created": 1657144326,
      "email": "jenny.rosen@example.com",
      "individual": null,
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "phone_number": "+18008675309",
      "requirements": {
        "disabled_reason": null,
        "past_due": []
      },
      "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
      },
      "status": "active",
      "type": "individual"
    },
    {
      "id": "ich_1234b",
      "object": "issuing.cardholder",
      "billing": {
        "address": {
          "city": "San Francisco",
          "country": "US",
          "line1": "510 Townsend Street",
          "line2": null,
          "postal_code": "94111",
          "state": "CA"
        }
      },
      "company": null,
      "created": 1656537695,
      "email": "jenny.rosen@example.com",
      "individual": null,
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "phone_number": "+18008675309",
      "requirements": {
        "disabled_reason": null,
        "past_due": []
      },
      "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
      },
      "status": "active",
      "type": "individual"
    }
  ],
  "has_more": false,
  "url": "/v1/issuing/cardholders"
}`[Listing cards](#listing-cards)You can also see a list of cards created on a connected account by making a Cards API GET request and passing the specific Stripe-Account into the header.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, you will receive a list of cards:

`{
  "object": "list",
  "data": [
    {
      "id": "ic_1234a",
      "object": "issuing.card",
      "brand": "Visa",
      "cancellation_reason": null,
      "cardholder": {
        "id": "ich_1234a",
        "object": "issuing.cardholder",
        "billing": {
          "address": {
            "city": "San Francisco",
            "country": "US",
            "line1": "510 Townsend Street",
            "line2": null,
            "postal_code": "94111",
            "state": "CA"
          }
        },
        "company": null,
        "created": 1656537695,
        "email": "jenny.rosen@example.com",
        "individual": null,
        "livemode": false,
        "metadata": {},
        "name": "Jenny Rosen",
        "phone_number": "+18008675309",
        "requirements": {
          "disabled_reason": null,
          "past_due": []
        },
        "spending_controls": {
          "allowed_categories": [],
          "blocked_categories": [],
          "spending_limits": [],
          "spending_limits_currency": null
        },
        "status": "active",
        "type": "individual"
      },
      "created": 1656537950,
      "currency": "usd",
      "exp_month": 5,
      "exp_year": 2025,
      "last4": "0021",
      "livemode": false,
      "metadata": {},
      "pin": null,
      "replaced_by": null,
      "replacement_for": null,
      "replacement_reason": null,
      "shipping": null,
      "spending_controls": {
        "allowed_categories": [
          "car_rental_agencies"
        ],
        "blocked_categories": null,
        "spending_limits": [
          {
            "amount": 8000,
            "categories": [],
            "interval": "per_authorization"
          }
        ],
        "spending_limits_currency": "usd"
      },
      "status": "active",
      "type": "virtual",
      "wallets": {
        "apple_pay": {
          "eligible": true,
          "ineligible_reason": null
        },
        "google_pay": {
          "eligible": true,
          "ineligible_reason": null
        },
        "primary_account_identifier": null
      }
    },
    {
      "id": "ic_1234b",
      "object": "issuing.card",
      "brand": "Visa",
      "cancellation_reason": null,
      "cardholder": {
        "id": "ich_1234a",
        "object": "issuing.cardholder",
        "billing": {
          "address": {
            "city": "San Francisco",
            "country": "US",
            "line1": "510 Townsend Street",
            "line2": null,
            "postal_code": "94111",
            "state": "CA"
          }
        },
        "company": null,
        "created": 1656537695,
        "email": "jenny.rosen@example.com",
        "individual": null,
        "livemode": false,
        "metadata": {},
        "name": "Jenny Rosen",
        "phone_number": "+18008675309",
        "requirements": {
          "disabled_reason": null,
          "past_due": []
        },
        "spending_controls": {
          "allowed_categories": [],
          "blocked_categories": [],
          "spending_limits": [],
          "spending_limits_currency": null
        },
        "status": "active",
        "type": "individual"
      },
      "created": 1656537947,
      "currency": "usd",
      "exp_month": 5,
      "exp_year": 2025,
      "last4": "0013",
      "livemode": false,
      "metadata": {},
      "pin": null,
      "replaced_by": null,
      "replacement_for": null,
      "replacement_reason": null,
      "shipping": null,
      "spending_controls": {
        "allowed_categories": null,
        "blocked_categories": null,
        "spending_limits": [
          {
            "amount": 50000,
            "categories": [],
            "interval": "daily"
          }
        ],
        "spending_limits_currency": "usd"
      },
      "status": "active",
      "type": "virtual",
      "wallets": {
        "apple_pay": {
          "eligible": true,
          "ineligible_reason": null
        },
        "google_pay": {
          "eligible": true,
          "ineligible_reason": null
        },
        "primary_account_identifier": null
      }
    }
  ],
  "has_more": false,
  "url": "/v1/issuing/cards"
}`You can see a list of cards associated with a specific cardholder by including the cardholder parameter on your Cards API GET request. Pass the specific Stripe-Account into the header and the cardholder ID into the cardholder parameter.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d cardholder=ich_1234a`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create cardholders](#create-cardholders)[Create cards](#create-cards)[Activate cards](#activate-cards)[Deactivating cards](#deactivating-cards)[See also](#see-also)[Cancel cards](#cancel-cards)[Listing cards](#listing-cards)Products Used[Issuing](/issuing)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
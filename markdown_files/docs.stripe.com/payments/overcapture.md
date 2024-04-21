htmlCapture more than the authorized amount on a payment | Stripe Documentation[Skip to content](#main-content)Capture more than the authorized amount on a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fovercapture)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fovercapture)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[Flexible payment scenarios](/docs/payments/flexible-payments)# Capture more than the authorized amount on a payment

Use overcapture to capture more than the authorized amount for a PaymentIntent.Overcapture allows you to capture with an amount that’s higher than the authorized amount for a card payment. Unlike incremental authorizations, overcapture doesn’t result in additional authorizations with the card networks. When you overcapture a PaymentIntent, your customer won’t see any immediate updates on their credit card statement. After the captured amount settles, the initial pending authorization gets updated with the final captured amount.

## Availability

When using overcapture, be aware of the following restrictions:

- Only available with Visa, Mastercard, American Express, or Discover.
- Only eligible for online card payments. For in-person card payments see how to[collect tips](/terminal/features/collecting-tips/overview).
- Card brands limit the amount that you can overcapture (generally calculated as a percentage of the authorized amount), and impose additional constraints, including country, card type, and merchant category restrictions (see below).

IC+ featureWe offer overcapture to users on IC+ pricing. If you’re on standard Stripe pricing and want access to this feature, learn more at support.stripe.com.

### Availability by card network, merchant country, and merchant category

Card brandMerchant countryMerchant categoryPercent limitVisa*GlobalTaxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas+20%GlobalCar rentalsGreater of +15% or +75 USD (or local currency equivalent)GlobalLodging; cruise lines+15%Global**All other merchant categories+15%MastercardUS***Eating places and restaurants; fast food restaurants+30%American ExpressGlobal****Eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants+30%GlobalTaxicabs and limousines; beauty and barber shops; health and beauty spas+20%GlobalLodging; car rentals; truck and utility trailer rentals; motor home and recreational vehicle rentals; grocery stores; retail stores+15%DiscoverGlobalTaxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas+20%GlobalLodging; car rentals+15%* Excludes merchants in the European Economic Area (“EEA”) where the card is also issued in the EEA

** For cardholder-initiated transactions

*** Card must also be issued in the United States

**** The percent limit for debit and prepaid card payments is 20%

### Networks with limited support (beta)

### Overcapture with Strong Customer Authentication (SCA)

If you and the cardholder are in a country that has Strong Customer Authentication (SCA) requirements, keep in mind the limitations of overcapture availability.

- Under SCA requirements, you generally need to authenticate an amount that’s greater than or equal to the amount that you eventually capture. For this reason, you need to authenticate and authorize for the highest estimated amount that you plan to capture, rather than using overcapture as outlined elsewhere on this page. Subsequently, you can capture up to the full amount authenticated, depending on the total amount for the goods or services provided. If you find it necessary to capture an amount beyond the originally authorized and authenticated amount, you must cancel the original payment and create a new one with the correct amount. However, there are some exceptions to this requirement (see below).
- There are a number of[transaction exemptions](https://support.stripe.com/questions/transaction-exemptions-for-strong-customer-authentication-%28sca%29)for SCA where overcapture might be permissible. For example, merchant-initiated transactions (MIT) where the customer isn’t physically present during the checkout flow are potentially exempt. See[when to categorize a transaction as MIT](https://support.stripe.com/questions/merchant-initiated-transactions-(mits)-when-to-categorize-a-transaction-as-mit).

You need to familiarize yourself with the complete documentation to gain a comprehensive understanding of overcapture and SCA requirements.  See our SCA guide for more information.

ComplianceYou’re responsible for your compliance with all applicable laws, regulations, and network rules when using overcapture. Make sure to review the rules for the card networks that you plan to use this feature with to make sure your sales comply with the applicable rules, which vary by network. For example, some card networks don’t allow overcapture for transactions where the final transaction amount should be known at the time of authorization.

The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

[Create and confirm an uncaptured PaymentIntent](#confirm-payment-intent)You can only perform overcapture on uncaptured payments after PaymentIntent confirmation. To indicate you want to separate the authorization and capture, specify the capture_method as manual when creating the PaymentIntent. To learn more about separate authorization and capture, see how to place a hold on a payment method.

You must specify the PaymentIntents you plan to overcapture by using if_available with the request_overcapture parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d capture_method=manual \
  -d "expand[]"=latest_charge \
  -d "payment_method_options[card][request_overcapture]"=if_available`Look at the overcapture.status field on the latest_charge in the PaymentIntent confirmation response to determine if overcapture is available for the payment based on availability. If available, the maximum_amount_capturable field indicates the maximum amount capturable for the PaymentIntent. If unavailable, the maximum_amount_capturable is the amount authorized.

`// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  "status": "requires_capture",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000
          "overcapture": {
              "status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  ...
}`[Capture the PaymentIntent](#capture-payment-intent)To capture more than the currently authorized amount on a PaymentIntent, use the capture endpoint and provide an amount_to_capture up to the maximum_amount_capturable.

If you need to capture an amount larger than the maximum_amount_capturable, perform an incremental authorization to increase the authorized amount, where available.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount_to_capture=1200 \
  -d "expand[]"=latest_charge`The amount_capturable and amount_received fields update accordingly in the PaymentIntent capture response for a successful overcapture. The captured PaymentIntent that returns has an updated amount to reflect the total monetary amount moved for this payment. Use the amount_authorized field on the associated Charge to reference the initial amount authorized for a successfully overcaptured payment.

`// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1200,
  "amount_capturable": 0,
  "amount_received": 1200,
  "status": "succeeded",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,
          "overcapture": {
              "maximum_amount_capturable": 1200,
              "status": "available" // or "unavailable"
          }
        }
      }
      ...
    }
  ...
}`## Test your integration

Use any of the below Stripe test cards with any CVC and future expiration date to request and perform overcaptures while in test mode. If overcapture is available on payments for a given network in test mode, it is also available in live mode.

Card brandNumberPayment methodVisa4242424242424242`pm_card_visa`Mastercard5555555555554444`pm_card_mastercard`Amex378282246310005`pm_card_amex`Discover6011111111111117`pm_card_discover`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Create and confirm an uncaptured PaymentIntent](#confirm-payment-intent)[Capture the PaymentIntent](#capture-payment-intent)[Test your integration](#test-your-integration)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
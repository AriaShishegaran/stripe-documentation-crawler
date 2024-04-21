# eftpos Australia

Customer geography: Australia

Payment method type: Debit, and prepaid card

Presentment currency: AUD

Disputes: Yes

Refunds and partial refunds: Yes

Recurring payments: Yes

Eftpos is Australia’s local debit card network. More than 90% of eftpos cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either network supported by the card.

[Eftpos](https://www.eftposaustralia.com.au/)

Stripe processes co-branded eftpos cards over eftpos, plus either Visa or Mastercard, in accordance with least cost routing requirements and depending on the type of transaction.

[least cost routing requirements](https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia)

[type of transaction](/payments/eftpos-australia#identify-which-network-a-payment-was-processed-on)

Eftpos-only cards (also known as “proprietary eftpos cards”) only support in-person payments and can’t be used for online transactions.

## Availability

Eftpos is available to any business that uses Stripe in Australia, with the following exceptions:

- Massage parlors (MCC 7297)

[MCC](/connect/setting-mcc)

- Financial institutions—manual cash disbursements (MCC 6010)

[MCC](/connect/setting-mcc)

- Financial institutions—merchandise and services (MCC 6012)

[MCC](/connect/setting-mcc)

- Non-financial institutions—foreign currency, money orders and travelers’ checks. (MCC 6051)

[MCC](/connect/setting-mcc)

- Remote stored value load—merchant (MCC 6530)

[MCC](/connect/setting-mcc)

- Stored value card purchase/load (MCC 6540)

[MCC](/connect/setting-mcc)

- Wires, money orders (MCC 4829)

[MCC](/connect/setting-mcc)

## Integration

If your integration can already accept card payments, you can also accept eftpos without additional updates.

[accept card payments](/payments/accept-a-payment)

Eftpos is the default network for payment. Unless you change the default network, you must inform your customers that whenever they use a dual-network debit card, their payments might be processed through the debit network, regardless of the logo that appears when they enter their payment information.

We recommend you notify your customers based on the type of payment transaction:

- For single payment transactions, display a notification to the customer before the completion of the checkout process.

- For new recurring payment transactions, display a notification to the customer at the time of setup.

- For existing recurring payment transactions, notify your customers in advance of future transactions.

You must notify your customers about how network routing functions, and how payments processing works. You can use the suggested notification message below:

Notwithstanding the payment brand logo displayed when you enter your payment information, whenever you use a dual-network debit card displaying eftpos and another payment brand, your payment (including any future recurring debit payments authorized by you) might be processed through either network. See the [Terms and Conditions] or [FAQs] for more information.

We recommend that you provide further information in your Terms and Conditions or FAQs on how network routing functions and how payments processing works. For guidelines on best practices, see the Australian Payments Network MCR Online Notification Guidelines.

[MCR Online Notification Guidelines](https://www.auspaynet.com.au/resources/cards-and-devices)

## Understand which network processes payments

Stripe dynamically routes between the international scheme (Visa or Mastercard) and eftpos, depending on the type of payment, technical availability and authorization rate considerations:

- If a payment requires placing a hold on the card (in other words, if there’s a delay between authorization and capture), or if it requires 3D Secure, Stripe always routes to the international scheme.

[placing a hold on the card](/payments/place-a-hold-on-a-payment-method)

[3D Secure](/payments/3d-secure)

- For other types of payments, Stripe generally defaults to the eftpos network.

If you require that eftpos is never the default network for any payments, please contact support.

[support](https://support.stripe.com/contact)

To identify which network a payment was processed on, inspect the network field on the Charge object associated with a successful Payment Intent:

[network](/api/charges/object#charge_object-payment_method_details-card-network)

[Charge](/api/charges/object)

[Payment Intent](/api/payment_intents/object)

## See also

- Migrating from Charges API to the Payment Intents API

[Migrating from Charges API to the Payment Intents API](/payments/payment-intents/migration)

- Available eftpos test cards

[Available eftpos test cards](/testing#cards)

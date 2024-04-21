# Create payment links with Connect

Don’t know much about Connect? Check out our Overview article.

[Connect](/connect)

[Overview](/connect)

You can create payment links for connected accounts, which support several approaches for collecting payments. You can use direct charges to create them directly on the connected account. Alternatively, you can create payment links on the platform with transfers to the connected account by using destination charges. You can also take an application fee on these payment links.

[payment links](/payment-links)

[several approaches](/connect/charges)

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

## Create a payment link using direct charges

To create an payment link that directly charges on a connected account, create a payment link while authenticated as the connected account. For this to work, you must also create the product and the price on the connected account.

[create a payment link](/api#create_payment_link)

[authenticated](/connect/authentication#stripe-account-header)

[product](/api#create_product)

[price](/api#create_price)

When you use direct charges, the connected account is responsible for the cost of the Stripe fees, refunds, and chargebacks.

## Create a payment link using destination charges

To create a payment link that charges on the platform and creates automatic transfers to a connected account, create a payment link while providing the connected account ID as the transfer_data[destination] value.

[create a payment link](/api#create_payment_link)

[value](/api/payment_links/payment_links/object#payment_link_object-transfer_data)

For this to work, you must also create the product and the price on the platform account. When using automatic transfers, the platform is the business of record.

[product](/api#create_product)

[price](/api#create_price)

When performing destination charges, Payment Links uses the brand settings of your platform account for the payment page. See the Customize branding section for more information.

[Customize branding](/connect/payment-links#customize-branding)

## Create a payment link using destination charges and on_behalf_of

You can also create a destination charge with the on_behalf_of parameter set to the connected account ID (by default, it is the platform). The on_behalf_of parameter determines the settlement merchant, which affects:

- Whose statement descriptor the end user sees

- Whose address and phone number the end user sees

- The settlement currency of the charge

- The payment page branding the customer sees

## Fulfill orders placed through payment links

After an end user pays through a payment link you need to enable your connected accounts to handle any fulfillment necessary.

Configure a webhook endpoint in the Dashboard.

[webhook](/webhooks)

[in the Dashboard](https://dashboard.stripe.com/account/webhooks)

Then create an HTTP endpoint on your server to monitor for completed payments. Make sure to replace the endpoint secret key (whsec_...) in the example with your key.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

Learn more in our fulfillment guide.

[fulfillment guide](/payments/checkout/fulfill-orders)

[OptionalCollect application fees](#collecting-fees)

## OptionalCollect application fees

[OptionalCustomize branding](#customize-branding)

## OptionalCustomize branding

[OptionalIntegrate tax calculation and collection](#connect-tax)

## OptionalIntegrate tax calculation and collection

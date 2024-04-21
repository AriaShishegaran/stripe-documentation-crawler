# Use the API to create and manage payment links

You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.

[Payment Links API](/api/payment_links/payment_links)

[Set up your product catalog](#product-catalog)

## Set up your product catalog

Payment Links use Products and Prices to model what your business is selling. To get started with Payment Links, create a product, then use that product to create a price.

[Products](/api/products)

[Prices](/api/prices)

[create a product](/api/products/create)

[create a price](/api/prices/create)

Payment Links only supports Standard pricing (charging the same price for each unit—either one time or recurring) and Customer chooses price (letting your customer specify the price). It doesn’t support advanced options like package pricing, graduated pricing, or volume pricing. Additionally, Customer choose prices currently doesn’t support recurring payments or donations.

Use Standard pricing to create a product or subscription with a fixed amount.

[Create a payment link](#create-link)

## Create a payment link

To create a payment link, pass in line_items. Each line item contains a price and quantity. Payment links can contain up to 20 line items when using Standard pricing and 1 line item when using Customer chooses price.

[line_items](/api/payment_links/payment_links/create#create_payment_link-line_items)

[price](/api/payment_links/payment_links/create#create_payment_link-line_items-price)

[quantity](/api/payment_links/payment_links/create#create_payment_link-line_items-quantity)

[Share your payment link](#share-link)

## Share your payment link

Each payment link contains a url that you can share with your customers through email, on social media, with a website link, in an app, or through other channels.

[url](/api/payment_links/payment_links/object#payment_link_object-url)

[Track payments](#tracking-payments)

## Track payments

When customers use a payment link to complete a payment, Stripe sends a checkout.session.completed webhook that you can use for fulfillment and reconciliation.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

Make sure to listen to additional webhooks in case you’ve enabled payment methods like bank debits or vouchers, which can take 2-14 days to confirm the payment. For more information, see our guide on fulfilling orders after a customer pays.

[fulfilling orders after a customer pays](/payments/checkout/fulfill-orders)

After a customer completes a purchase, you can redirect them to a URL or display a custom message by setting after_completion on the payment link.

[after_completion](/api/payment_links/payment_links/create#create_payment_link-after_completion)

[https://example.com](https://example.com)

[Deactivate a payment link](#deactivate-link)

## Deactivate a payment link

After you’ve created a payment link, you can’t delete it. What you can do is deactivate a payment link by setting the active attribute to false.

[active](/api/payment_links/payment_links/update#update_payment_link-active)

After you deactivate a link, customers can’t finalize purchases using the link anymore and are redirected to an expiration page. If you want to reuse a deactivated payment link, turn it back on by setting the active attribute to true.

[active](/api/payment_links/payment_links/update#update_payment_link-active)

[Configure payment methods](#configure-payment-method)

## Configure payment methods

By default, Stripe selects the relevant payment methods that you enabled in your Dashboard. To add supported payment methods, enable them in your Payment methods settings.

[supported payment methods](/payments/payment-methods/integration-options#payment-method-product-support)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[OptionalAllow coupons and promotion codes](#promotion-codes)

## OptionalAllow coupons and promotion codes

[OptionalCollect taxes on your payment link](#stripe-tax)

## OptionalCollect taxes on your payment link

[OptionalCollect billing and shipping addresses](#address-collection)

## OptionalCollect billing and shipping addresses

[OptionalAllow adjustable quantities](#allow-adjustable-quantities)

## OptionalAllow adjustable quantities

[OptionalCreate subscriptions](#creating-subscriptions)

## OptionalCreate subscriptions

[OptionalSpecify the payment methods you want to accept](#payment-methods)

## OptionalSpecify the payment methods you want to accept

[OptionalCollect a terms of service agreement](#terms-of-service)

## OptionalCollect a terms of service agreement

[OptionalAdd custom fields](#custom-fields)

## OptionalAdd custom fields

[OptionalCollect application fees using Connect](#application-fees)

## OptionalCollect application fees using Connect

[OptionalSend post-payment invoices](#post-payment-invoices)

## OptionalSend post-payment invoices

# Place hardware orders

Ready to buy? Browse available readers and accessories.

[available readers and accessories](https://dashboard.stripe.com/terminal/shop)

Get notified when Stripe Reader S700 is available in your country.

[Get notified](https://dashboard.stripe.com/terminal/s700_notify)

Order pre-certified readers compatible with Stripe Terminal from your Dashboard or using the Stripe API (beta). Purchase readers directly from Stripe so they’re loaded with Stripe’s payment applications and secure encryption keys.

To get started, navigate to the Readers section in your Dashboard. Click Shop to view available products.

[Readers](https://dashboard.stripe.com/terminal)

## What to buy

First, order a reader and a test card to test your full integration with physical hardware. When your integration is ready, order as many readers as you need.

[reader](https://dashboard.stripe.com/terminal/shop)

[test card](https://dashboard.stripe.com/terminal/shop)

Not sure which reader you need? See Designing an Integration to choose one for your integration.

[Designing an Integration](/terminal/designing-integration)

You can order up to 10000 of each item in a single order. If you’re interested in volume discounts, you can contact us.

[contact us](https://stripe.com/contact/sales)

The price for each reader varies by country. You can view the most updated pricing in the Dashboard.

[Dashboard](https://dashboard.stripe.com/terminal/shop)

[Stripe Reader M2](/terminal/payments/setup-reader/stripe-m2)

[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)

[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)

[Stripe Reader S700](/terminal/payments/setup-reader/stripe-reader-s700)

[Shop now](https://dashboard.stripe.com/terminal/shop)

[Shop now](https://dashboard.stripe.com/terminal/shop)

[Shop now](https://dashboard.stripe.com/terminal/shop)

[Shop now](https://dashboard.stripe.com/terminal/shop)

## Track and cancel orders

After placing an order, check its status in the Dashboard:

## Self service returns

Self service returns are for orders placed and shipped within specific countries (see countries below). See the information about returns outside of supported self service countries for all other orders.

[returns outside of supported self service countries](/terminal/fleet/placing-orders#returns-outside-of-supported-self-service-countries)

If you’ve placed an order in the Stripe Dashboard within a country supporting self service and need to return some or all of the items in your order, users with sufficient permission can initiate the return within the Stripe Dashboard. We can accept refunds for orders in original packaging (along with all accessories) within 30 days of the date of purchase. For returns past 30 days, please contact Stripe Support.

[users with sufficient permission](#self-service-return-permissions)

[Stripe Support](https://support.stripe.com/contact/login)

Going through the flow in the Dashboard produces a return shipping label. After you create the return shipping label, you can drop your package off at a local shipping carrier.

Stripe refunds the payment when our distribution facility receives the package. For credit cards, the process can take up to 10 days for the funds to be returned to the bank account.

[Selecting the Return items Button](#step-1)

## Selecting the Return items Button

To initiate a Dashboard Return, navigate to your Hardware Orders and select the order you want to return. After you select the order, click Return items to start the process. The Return items  button is available on the Terminal order details page if the hardware order has a status of Shipped  or Delivered.

[Confirming the number of units to be returned](#step-2)

## Confirming the number of units to be returned

When the popup opens, select the number of items you’d like to return for each product in the order (if you have more than one item). We’ll only show the number of items eligible for return. So, if you previously purchased three items and returned one, you’ll only be able to select up to two units to return.

[Calculating the refund amount](#step-3)

## Calculating the refund amount

The popup displays the amount to be refunded after you select the desired number of items.

Shipping fees are refunded on the first initiated return for a Terminal hardware order. For example, if you bought three readers and then returned one unit through a partial refund, then decided to return another unit, the second Dashboard return shows $0 for shipping fees to be refunded because these fees were returned in the first attempt.

[Selecting a reason for the return](#step-4)

## Selecting a reason for the return

Next, you need to select a reason for the return from the dropdown menu.

- Items arrived defective or broken—Select this option if any of the items received were damaged or defective.

- I ordered too many devices—Select this option if you ordered too many devices.

- Device setup is too complicated—Select this option if getting started with Stripe Terminal was too complicated or the product didn’t meet your expectations.

- Other - Select this option if none of the above options match your use case. A reason is required.

[Confirming and exporting the shipping label](#step-5)

## Confirming and exporting the shipping label

After you’ve confirmed the information is correct, select Submit return’—the option to download the shipping label appears after you select it. You can select View UPS Locations to find the nearest drop off location.

[Refunds](#step-6)

## Refunds

After the return is processed, you’ll be redirected back to the order details page. You can download the shipping label again from the details page if needed. Stripe issues a refund to the payment method you provided when we receive the return.

## Returns outside of supported self service countries

To return a device where self service returns isn’t available, contact support. Navigate to your order in the Dashboard and click Contact support to automatically send us your order details. We can accept refunds for orders in original packaging (along with all accessories) within 30 days of the date of purchase.

## Shipping

Stripe works with a distribution partner to fulfill Terminal orders. You can choose standard, express, or priority shipping, depending on the destination country. Hardware must be shipped to physical addresses (not PO boxes).

If you’re a Connect platform using Terminal, you can ship readers directly to your connected accounts by specifying the destination address during checkout.

[Connect platform using Terminal](/terminal/features/connect)

## User roles and permissions

The following table shows which user roles can place orders on behalf of their account via the dashboard:

[user roles](/get-started/account/teams/roles)

## Use the Hardware Orders API Beta

The Terminal Hardware Ordering API is currently in beta. To request access to the APIs, please email thor-api-feedback@stripe.com.

[thor-api-feedback@stripe.com](mailto:stripe-terminal-betas@stripe.com)

To qualify for beta access, you must:

- Have a Stripe Account manager

- Agree to monthly invoice billing

- Understand this is a beta—which might require you to make timely updates

You can use the Hardware Orders API if you’d like to: The Terminal Hardware Orders API enables you to programmatically purchase Terminal readers and accessories that can be sent directly to your users. Orders are fulfilled by Stripe’s distribution partners, so you don’t have to manage complex logistics and can instead focus on building your in-person payments business.

- Build an internal tool for your employees, such as store managers, to place orders for hardware

- Build an e-commerce ordering system for your customers to place orders for Terminal readers and accessories

To create a hardware order using the API, follow these steps:

- Retrieve available SKUs

- Retrieve available Shipping Methods

- (Optional) Preview the order

- Create the order

You must include a header in your API requests with your API version and the current version of the terminal hardware order beta: Stripe-Version: 2024-04-10;terminal_hardware_orders_beta=v4

To render an appropriate product page for users, your integration must request available items from Stripe. Each item is represented as a SKU and includes details about the product, such as the product token and price.

Each SKU is associated with a country: a reader available in the US has a different SKU from the same reader that’s available in Canada. To retrieve SKUs, you can optionally specify the country parameter when making a request to the Hardware Order SKUs endpoint:

[Hardware Order SKUs](/api/terminal/hardware_skus/list)

Each SKU is also associated with a Hardware Product. Products represent different categories of devices. If you’re building an e-commerce ordering system for your customers, make sure you only show the SKUs for the products that apply for your Terminal integration. For example, if your Terminal integration only uses the BBPOS WisePOS E, don’t make the BBPOS Chipper 2X BT reader available for purchase. To retrieve all BBPOS WisePOS E SKUs regardless of country, you can specify the optional product parameter when making a request to the Hardware Order SKUs endpoint:

[Hardware Product](/api/terminal/hardware_products/object)

[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)

[BBPOS Chipper 2X BT](/terminal/readers/bbpos-chipper2xbt)

[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)

[Hardware Order SKUs](/api/terminal/hardware_skus/list)

You can combine the country and product parameters to only get a particular product in a particular country.

SKUs and Products might become obsolete as we replace them with newer hardware. To help you manage planned obsolescence, see the SKU and Product status that indicates which are currently available or unavailable. You can’t create an Order if the SKU status is unavailable.

[SKU and Product status](/api/terminal/hardware_skus/object#terminal_hardware_sku_object-status)

[SKU status](/api/terminal/hardware_products/object#terminal_hardware_sku_object-status)

Additionally, each SKU and Product has an optional unavailable_after field that indicates when it might become unavailable. Because the availabilities of these objects change over time, we recommend using an approach to query them dynamically. You can do this either by making a query before displaying the available objects to your users, or periodically (every day, for example) and caching the results you present to your users.

[unavailable_after field](/api/terminal/hardware_skus/object#terminal_hardware_sku_object-unavailable_after)

We don’t recommend hardcoding the tokens for these objects because such an integration requires code changes when a shipping method becomes unavailable. If you don’t perform these changes in time, you might attempt to place orders with unavailable objects, causing errors.

Another required object used as an input for creating an order is the Hardware Shipping Method. This object determines the estimated shipping time for your order as well as a portion of the price. You must use a Shipping Method available in country of the shipping address when creating an order.

[Hardware Shipping Method](/api/terminal/hardware_shipping_methods/object)

Like SKUs, each Shipping Method is associated with a country: the shipping methods available in the US might be different from those available in Canada. Each Shipping Method also has a name, which denotes the basic category for this shipping method. To retrieve Shipping Methods, you can optionally specify the country and/or name parameter when making a request to the Hardware Shipping Methods endpoint:

[Hardware Shipping Methods](/api/terminal/hardware_shipping_methods/list)

Like SKUs and Products, Shipping Methods might change over time. To help you manage these changes, each Shipping Method has a status that indicates whether it’s currently available or unavailable. This mechanism works the same way as it does for SKUs and Products, as described above. As with SKUs and Products, we recommend fetching Shipping Methods periodically so your integration doesn’t become out of date.

[status](/api/terminal/hardware_skus/object#terminal_hardware_sku_object-status)

To preview a hardware order, make a request to Stripe containing the SKUs, quantities, shipping address, and Shipping Method for the order.

Previewing an order allows you to perform validation on the order and determine the overall cost of the taxes associated with the order without actually placing it, which you can use for designing an e-commerce checkout page for your customers. Calling the preview endpoint doesn’t actually create an order.

Try to minimize the time between making a request to Preview Hardware Order and Create Hardware Order to reduce the (very unlikely) chance that prices change in the interim. If you’re concerned about this issue you can save the preview and create an order using the same parameters. Then you can compare the saved preview with the order and cancel the order in the event of any changes.

[Preview Hardware Order](/api/terminal/hardware_orders/preview)

[Create Hardware Order](/api/terminal/hardware_orders/create)

To create a Terminal Hardware Order, you can make a Create Hardware Order request to Stripe that looks very similar to the Preview Hardware Order request. Include the SKUs, quantities, shipping address, and Shipping Method for the order in your request.

[Terminal Hardware Order](/api/terminal/hardware_orders/object)

[Create Hardware Order](/api/terminal/hardware_orders/create)

[Preview Hardware Order](/api/terminal/hardware_orders/preview)

The below example shows a US phone number. If the phone number provided by shipping.phone parameter is an international phone number, prefix it with an escaped version of the + sign (for example: shipping[phone]="%2B358131234567" instead of shipping[phone]="+358131234567").

The email address provided by the shipping.email parameter receives Stripe-branded update emails when the status of the order changes. Use an email address that you feel comfortable receiving Stripe-branded emails.

After creating an order, you can Retrieve a Terminal Hardware Order using the following request.

[Retrieve a Terminal Hardware Order](/api/terminal/hardware_orders/retrieve)

You can also List all Terminal Hardware Orders.

[List all Terminal Hardware Orders](/api/terminal/hardware_orders/list)

You can set up webhook events to be updated about order state transitions. We support the following webhook events:

[set up webhook events](/webhooks)

- terminal_hardware_order.created

- terminal_hardware_order.canceled

- terminal_hardware_order.ready_to_ship

- terminal_hardware_order.shipped

- terminal_hardware_order.delivered

- terminal_hardware_order.undeliverable

You can update the status of a terminal hardware order in test mode using the following endpoints in the API:

- /v1/test_helpers/terminal/hardware_orders/:hardware_order/mark_ready_to_ship

- /v1/test_helpers/terminal/hardware_orders/:hardware_order/ship

- /v1/test_helpers/terminal/hardware_orders/:hardware_order/deliver

- /v1/test_helpers/terminal/hardware_orders/:hardware_order/mark_undeliverable

You can only update the status for terminal hardware orders in test mode.

[test mode](/keys#test-live-modes)

Upon order creation, Stripe returns the tax amounts associated with the order. We calculate these amounts based on the tax owed to Stripe for the purchase. If you charge tax to your end users for orders placed using the API, you can calculate the amounts owed to you and convey those amounts to your users. The amounts owed to you might differ from those owed to Stripe.

For Italian Tax Invoices, please visit the Italian Tax Portal to view invoices.

[Italian Tax Portal](https://www.agenziaentrate.gov.it/portale/area-riservata)

During beta, Stripe sends monthly invoices for any orders created with the API. You can change the email that receives invoices in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/terminal)

As mentioned in the Shipping section, Stripe works with a distribution partner to fulfill Terminal orders. When our distribution partner gets tracking information for the order it transions to the shipped state. You can set up a webhook endpoint for the terminal_hardware_order.shipped notification to be notified when an order has a tracking number.

[Shipping](#shipping)

- Add new values (canada_post, dhl, dpd, and usps) to the Carrier enum field.

[Carrier](/api/terminal/hardware_orders/object#terminal_hardware_order_object-shipment_tracking-carrier)

- Add a new Preview Hardware Order endpoint. Remove draft and expired order statuses. Remove the /v1/terminal/hardware_orders/confirm endpoint and the confirm parameter in the Create Hardware Order endpoint.

[Preview Hardware Order](/api/terminal/hardware_orders/preview)

[Create Hardware Order](/api/terminal/hardware_orders/create)

- Add a new TerminalHardwareOrder status called ready_to_ship, which represents a state in which the order is no longer cancelable, but hasn’t yet shipped.

[TerminalHardwareOrder](/api/terminal/hardware_orders/object)

- Add new API endpoints to update the status of test mode terminal hardware orders to ready_to_ship, shipped, delivered, and undeliverable.

[ready_to_ship](/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)

[shipped](/api/terminal/hardware_orders/test_mode_ship)

[delivered](/api/terminal/hardware_orders/test_mode_deliver)

[undeliverable](/api/terminal/hardware_orders/test_mode_mark_undeliverable)

- Add a new Hardware Shipping Method object to replace the former object in the shipping_method field, as well as API endpoints for querying and retrieving these new objects.

[Hardware Shipping Method](/api/terminal/hardware_shipping_methods/object)

- Add a new Hardware Product object to replace the former product_type field, as well as API endpoints for querying and retrieving these new objects.

[Hardware Product](/api/terminal/hardware_products/object)

- Add a new, dynamic orderable field to the TerminalHardwareSku object, replacing the older max_per_order field.

[TerminalHardwareSku](/api/terminal/hardware_skus/object)

- Add status and unavailable_after fields to TerminalHardwareSku, which allow you to determine if and when a SKU becomes unavailable to order. These fields also exist on the new Hardware Shipping Method and Hardware Product objects.

[TerminalHardwareSku](/api/terminal/hardware_skus/object)

[Hardware Shipping Method](/api/terminal/hardware_shipping_methods/object)

[Hardware Product](/api/terminal/hardware_products/object)

- If you have webhooks enabled for v3 and v4 under the same mode (that is, both test mode or both live mode) at the same time, then Stripe sends the terminal_hardware_order.shipped webhook twice. We send the terminal_hardware_order.shipped webhook when an order transitions to ready_to_ship and shipped as opposed to only sending it when an order transitions to shipped. Having v3 in live mode and v4 in test mode doesn’t cause duplicate webhooks. If you need to have both v3 and v4 active under the same mode at the same time, make sure to update your integration to handle duplicate terminal_hardware_order.shipped webhooks first.

- Orders that are ready_to_ship in v4 appear as shipped in v3. You might see an order with status shipped in v3 and ready_to_ship in v4 as you’re updating your migration. This happens because the ready_to_ship concept doesn’t exist in v3; the status of these orders doesn’t actually regress.

- Update Terminal Hardware SKU and the Terminal Hardware Order line item SKU object by removing text fields such as name, description, images, and attributes.

[Terminal Hardware SKU](/api/terminal/hardware_skus/object)

[Terminal Hardware Order line item SKU object](/api/terminal/hardware_orders/object#terminal_hardware_order_object-hardware_order_items-terminal_hardware_sku)

- Make the shipping_country query parameter in Hardware Order SKUs optional and rename it to country.

[Hardware Order SKUs](/api/terminal/hardware_skus/list)

- Add the ability to query SKUs in the API by product_type and country.

- Update Terminal Hardware Order by turning total_tax_amounts.rate.jurisdiction from a structured object into a string.

[Terminal Hardware Order](/api/terminal/hardware_orders/object)

- Initial release

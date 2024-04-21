# Install Stripe Connector for Salesforce B2C Commerce Shopfront Reference Architecture

Stripe Payment Element modifies the default Commerce Cloud credit card collection and processing by using Stripe.js, a JavaScript library, to securely tokenize credit card data. Payments are then processed using the tokenized data, instead of raw credit card information.

[Payment Element](/payments/payment-element)

During checkout, the cartridge creates a PaymentIntent for any new cards or alternate payment methods that a customer enters. This tokenized data generates a Stripe Charge at the point of purchase.

When customers enter credit card or other payment information on the storefront, Stripe.js tokenizes it in interactions between Stripe and the client (browser). Unmasked credit card data is therefore never sent to the Commerce Cloud servers.

The PaymentIntent workflow guides you through the process of collecting a payment from your customer. A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and creates, at most, one successful charge.

[PaymentIntent](/api/payment_intents)

[multiple statuses](/payments/paymentintents/lifecycle)

The system creates a Stripe Charge (authorize or capture, based on Business Manager configuration) from a successfully created and submitted Basket. All Stripe Charges are created against a Stripe payment source.

Site administrators can select a variety of AVS statuses to auto fail an order for. If the Stripe charge returns any of the selected statuses for either address_line1_check or address_zip_check, the order is auto-failed and the Stripe charge reversed. You can also manage these settings on the Stripe Dashboard. Supported payment methods:

- Cards (Visa, Mastercard, American Express, Discover, Diners Club, JCB, Alipay).

- The Payment Request button element gives you a single integration for Apple Pay, Google Pay, and the browser standard Payment Request API.

## Limitations and constraints

Stripe offers a number of standard services that aren’t supported by the cartridge. These include support for subscriptions, plans, and coupons. There aren’t any known locale specific restrictions in the cartridge.

The included RELAY OCAPI configurations are included as examples only. A RELAY implementation requires additional configuration and testing along with the Stripe team. For any locale specific restrictions, see the Stripe.js documentation.

[Stripe.js documentation](/js)

## Compatibility

Available since Commerce Cloud Platform Release 16.8, SFRA version 4.4.

The cartridge is available for installation on storefronts that support both controller and SFRA SiteGenesis implementations.

## Privacy

Commerce Cloud doesn’t store any unmasked credit card data. The cartridge tokenizes all payment data within direct client-to-Stripe communications and obscures any sensitive credit card data before it arrives on the Commerce Cloud servers. Similarly, all credit card data that Commerce Cloud retrieves from the Stripe servers is either masked, tokenized, or both.

## See also

- Implementation Guide

[Implementation Guide](/connectors/salesforce-commerce-cloud/implementation-guide)

- Operations and Maintenance

[Operations and Maintenance](/connectors/salesforce-commerce-cloud/operations-and-maintenance)

- User Guide

[User Guide](/connectors/salesforce-commerce-cloud/user-guide)

- Testing

[Testing](/connectors/salesforce-commerce-cloud/testing)
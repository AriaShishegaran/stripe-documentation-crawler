# Optimizing your Radar Integration

Stripe Radar’s machine learning models use many signals to distinguish between fraudulent and legitimate payments. We compute some of these signals automatically, but many of them depend on the information that your integration provides. In general, the more data your integration provides, the more successful fraud prevention can be.

[Radar](/radar)

If you don’t collect enough information from your customers, it can reduce the effectiveness of fraud detection. Conversely, if you collect too much information, it can negatively impact the checkout experience and result in a lower conversion rate.

## Integration types

Stripe Radar leverages the power of the Stripe network to effectively detect and block fraudulent transactions, regardless of how you integrate with Stripe. However, the way you integrate with Stripe to process payments can significantly impact the completeness of the fraud signals you send us. The more information you send about a payment, the better Stripe Radar is at detecting and preventing fraud. Using one of our recommended payment integrations allows you to get the most out of Radar. If you can’t use a recommended integration, consider including as much additional data as possible, as explained in our recommendations below.

[recommendations](/radar/integration#recommendations)

[Stripe Payment Links](/payment-links)

[Stripe Checkout](/payments/checkout)

[Stripe Elements](/payments/elements)

[API](/api)

[Radar Sessions](/radar/radar-session)

[API](/api)

[API](/api)

[API](/api)

[API](/api)

## Important signals to send to Stripe

Including the following information with your payments can have a significant impact on the performance of Stripe Radar’s fraud detection models. Our recommended integrations enable you to collect this information, while direct integrations might need to explicitly include this data.

[Advanced fraud signals](/disputes/prevention/advanced-fraud-detection)

## Recommendations

We’ve tested the following recommendations to make sure that your conversion rate remains high while maximizing the performance of our machine learning models.

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you’ve completed so far.

- Collect advanced fraud signals automatically by using Payment Links, Checkout, Elements, or our mobile SDKsThe most important action you can take to guard against fraud is to collect customer payment information using one of our recommended payments integrations. Each method automatically collects important high-signal data, such as device information and IP addresses. To further improve fraud detection, collect the cardholder name, full billing address, postal code, and the card’s CVC code during checkout.You can build a seamless checkout flow within your website or app using any of these methods, and securely pass sensitive card information directly to Stripe without passing it through your servers—greatly simplifying your PCI compliance. Determine which integration makes the most sense for your business and product goals, but any of these integration methods help optimize your integration for fraud prevention.NoteIf you’re not using one of the recommended payment integrations, consider using Radar Sessions to automatically collect  advanced fraud signals to send to Stripe. You can also pass a subset of our advanced fraud signals directly using our APIs, as shown below.Command Linecurlcurl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2000 \
  -d currency=usd \
  -d "payment_method_data[type]"=card \
  -d "payment_method_data[card][number]"=4000002500003155 \
  -d "payment_method_data[card][exp_month]"=12 \
  -d "payment_method_data[card][exp_year]"=29 \
  -d "payment_method_data[card][cvc]"=123 \
  -d "payment_method_data[ip]"="62.132.141.1" \
  --data-urlencode "payment_method_data[user_agent]"="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" \
  --data-urlencode "payment_method_data[referrer]"="https://example.com/payment-page" \
  -d "payment_method_data[payment_user_agent]"="Stripe Button"Command Linecurlcurl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2000 \
  -d currency=usd \
  -d source=tok_visa \
  -d ip="62.132.141.1" \
  --data-urlencode user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" \
  --data-urlencode referrer="https://example.com/payment-page" \
  -d payment_user_agent="Stripe Button"

The most important action you can take to guard against fraud is to collect customer payment information using one of our recommended payments integrations. Each method automatically collects important high-signal data, such as device information and IP addresses. To further improve fraud detection, collect the cardholder name, full billing address, postal code, and the card’s CVC code during checkout.

[recommended payments integrations](/payments/online-payments#recommended-integrations)

You can build a seamless checkout flow within your website or app using any of these methods, and securely pass sensitive card information directly to Stripe without passing it through your servers—greatly simplifying your PCI compliance. Determine which integration makes the most sense for your business and product goals, but any of these integration methods help optimize your integration for fraud prevention.

[PCI compliance](/security/guide)

If you’re not using one of the recommended payment integrations, consider using Radar Sessions to automatically collect  advanced fraud signals to send to Stripe. You can also pass a subset of our advanced fraud signals directly using our APIs, as shown below.

[Radar Sessions](/radar/radar-session)

[advanced fraud signals](/disputes/prevention/advanced-fraud-detection)

[https://example.com/payment-page](https://example.com/payment-page)

[https://example.com/payment-page](https://example.com/payment-page)

- Create payments using the Customer object, where possibleUsing Customer objects when creating payments allows Stripe to track the payment patterns for each customer over time. This significantly increases our ability to identify irregularities in purchasing behavior. To do this, you should:Set up Payment Methods for future use and add a billing address to Customer objects and use them to create subsequent payments.Provide your customer’s email address when creating a Customer object.Provide your customer’s name when you tokenize their card information.If you ship physical goods, we also recommend collecting the customer’s shipping address and saving this to their associated Customer object.Each Customer object can also store multiple payment methods, so you can enhance your customer’s checkout experience by offering to save multiple cards. Stripe can continue to track payment patterns for each customer, regardless of which one they use.If you’re creating a PaymentIntent manually, make sure to handle declines. If you reuse the PaymentIntent, you can track repeated attempts to help counter card testing.

Using Customer objects when creating payments allows Stripe to track the payment patterns for each customer over time. This significantly increases our ability to identify irregularities in purchasing behavior. To do this, you should:

[Customer](/api#customers)

- Set up Payment Methods for future use and add a billing address to Customer objects and use them to create subsequent payments.

[Set up Payment Methods for future use](/payments/save-and-reuse)

[billing address](/api/customers/object#customer_object-address)

- Provide your customer’s email address when creating a Customer object.

[email address](/api#customer_object-email)

- Provide your customer’s name when you tokenize their card information.

[name](/api/#customer_object-name)

- If you ship physical goods, we also recommend collecting the customer’s shipping address and saving this to their associated Customer object.

[shipping address](/api#customer_object-shipping)

Each Customer object can also store multiple payment methods, so you can enhance your customer’s checkout experience by offering to save multiple cards. Stripe can continue to track payment patterns for each customer, regardless of which one they use.

[multiple payment methods](/saving-cards#multiple-payment-methods)

If you’re creating a PaymentIntent manually, make sure to handle declines. If you reuse the PaymentIntent, you can track repeated attempts to help counter card testing.

[PaymentIntent](/api/payment_intents)

[declines](/declines)

[card testing](/disputes/prevention/card-testing)

- Include Stripe.js on every page of your siteInclude Stripe.js on every page of your site, not just the checkout page where your customer enters their payment information. By doing so, Stripe can detect anomalous behavior that may be indicative of fraud as customers browse your website—providing additional signals that increase the effectiveness of our detection.<script async src="https://js.stripe.com/v3/"></script>NoteAlways load Stripe.js directly from  https://js.stripe.com/v3/. We don’t support using a local copy of Stripe.js-it can result in user-visible errors, and reduces the effectiveness of our fraud detection.

Include Stripe.js on every page of your site, not just the checkout page where your customer enters their payment information. By doing so, Stripe can detect anomalous behavior that may be indicative of fraud as customers browse your website—providing additional signals that increase the effectiveness of our detection.

[Stripe.js](/payments/elements)

[providing additional signals](/disputes/prevention/advanced-fraud-detection)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Always load Stripe.js directly from  https://js.stripe.com/v3/. We don’t support using a local copy of Stripe.js-it can result in user-visible errors, and reduces the effectiveness of our fraud detection.

- Update your privacy policy if necessaryRadar collects information on anomalous device or user behavior that might be indicative of fraud. Make sure that your own privacy policy tells your customers about this type of collection. Here’s a paragraph you could add to your policy if it doesn’t already include such a disclosure:We use Stripe for payment, analytics, and other business services. Stripe collects identifying information about the devices that connect to its services. Stripe uses this information to operate and improve the services it provides to us, including for fraud detection. You can learn more about Stripe and read its privacy policy at https://stripe.com/privacy.

Radar collects information on anomalous device or user behavior that might be indicative of fraud. Make sure that your own privacy policy tells your customers about this type of collection. Here’s a paragraph you could add to your policy if it doesn’t already include such a disclosure:

We use Stripe for payment, analytics, and other business services. Stripe collects identifying information about the devices that connect to its services. Stripe uses this information to operate and improve the services it provides to us, including for fraud detection. You can learn more about Stripe and read its privacy policy at https://stripe.com/privacy.

- Consider enabling Radar for future useRadar operates on a per-charge level, which means that during a PaymentIntent lifecycle, Radar might scan multiple charges if the payment has retries. By default, Radar doesn’t scan if you set up a Payment Method for future use without a charge. If you want to scan SetupIntents, go to the Radar settings and enable Use Radar on payment methods saved for future use.

Radar operates on a per-charge level, which means that during a PaymentIntent lifecycle, Radar might scan multiple charges if the payment has retries. By default, Radar doesn’t scan if you set up a Payment Method for future use without a charge. If you want to scan SetupIntents, go to the Radar settings and enable Use Radar on payment methods saved for future use.

[PaymentIntent lifecycle](/payments/paymentintents/lifecycle)

[set up a Payment Method for future use](/payments/save-and-reuse)

[SetupIntents](/api/setup_intents)

[Radar settings](https://dashboard.stripe.com/settings/radar)

# Set up future payments using Elements and Link

This guide walks you through how to accept payments with Link using the Setup Intents API and either the Payment Element or Link Authentication Element.

[Link](/payments/link/what-is-link)

[Setup Intents API](/api/setup_intents)

[Payment Element](/payments/payment-element)

[Link Authentication Element](/payments/elements/link-authentication-element)

There are three ways you can secure a customer email address for Link authentication and enrollment:

- Pass in an email address: You can pass an email address to the Payment Element using defaultValues. If you’re already collecting the email address and or customer’s phone number in the checkout flow, we recommend this approach.

[defaultValues](/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)

- Collect an email address: You can collect an email address directly in the Payment Element. If you’re not collecting the email address anywhere in the checkout flow, we recommend this approach.

- Link Authentication Element: You can use the Link Authentication Element to create a single email input field for both email collection and Link authentication. We recommend doing this if you use the Address Element.

[Address Element](/elements/address-element)

Collect a customer email address for Link authentication or enrollment

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, create a Stripe account or sign in.

[create a Stripe account](https://dashboard.stripe.com/register)

[sign in](https://dashboard.stripe.com/login)

Use our official libraries to access the Stripe API from your application:

[Create a CustomerServer-side](#create-customer)

## Create a CustomerServer-side

To set up a payment method for future payments, you must attach it to a Customer. Create a Customer object when your customer creates an account with your business. Customer objects allow for reusing payment methods and tracking across multiple payments.

[Customer](/api/customers)

[Create a SetupIntentServer-side](#web-create-intent)

## Create a SetupIntentServer-side

If you want to render the Payment Element without first creating a SetupIntent, see Collect payment details before creating an Intent.

[Collect payment details before creating an Intent](/payments/accept-a-payment-deferred?type=setup)

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments during a session and tracks the status of that session. Create a SetupIntent on your server with link and the other payment methods you want to support:

[SetupIntent](/api/setup_intents)

To see how to set up other payment methods, see the Set up future payments guide.

[Set up future payments](/payments/save-and-reuse)

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

[Collect customer email](#design-your-integration)

## Collect customer email

Link authenticates a customer by using their email address. Depending on your checkout flow, you have the following options: pass an email to the Payment Element, collect it directly within the Payment Element, or use the Link Authentication Element. Of these, Stripe recommends passing a customer email address to the Payment Element if available.

If any of the following apply to you:

- You want a single, optimized component for email collection and Link authentication.

- You need to collect a shipping address from your customer.

Then use the integration flow that implements these elements: the Link Authentication Element, Payment Element and optional Address Element.

A Link-enabled checkout page has the Link Authentication Element at the beginning, followed by the Address Element, and the Payment Element at the end. You can also display the Link Authentication Element on separate pages, in this same order, for multi-page checkout flows.

Create a payment form using multiple Elements

The integration works as follows:

[Set up your payment formClient-side](#web-collect-payment-details)

## Set up your payment formClient-side

Now you can set up your custom payment form with the Elements prebuilt UI components. Your payment page address must start with https:// rather than http:// for your integration to work. You can test your integration without using HTTPS. Enable HTTPS when you’re ready to accept live payments.

[Enable HTTPS](/security/guide#tls)

The Link Authentication Element renders an email address input. When Link matches a customer email with an existing Link account, it sends the customer a secure, one-time code to their phone to authenticate. If the customer successfully authenticates, Stripe displays their Link-saved addresses and payment methods automatically for them to use.

This integration also creates the Payment Element, which renders a dynamic form that allows your customer to pick a payment method type. The form automatically collects all necessary payments details for the payment method type selected by the customer. The Payment Element also handles the display of Link-saved payment methods for authenticated customers.

Install React Stripe.js and the Stripe.js loader from the npm public registry.

[npm public registry](https://www.npmjs.com/package/@stripe/react-stripe-js)

On your payment page, wrap your payment form with the Elements component, passing the client secret from the previous step. ​​If you already collect the customer’s email in another part of your form, replace your existing input with the linkAuthenticationElement​.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[the previous step](#web-create-intent)

If you don’t collect email, add the linkAuthenticationElement​ to your checkout flow. You must place the linkAuthenticationElement before the ShippingAddressElement (optional if you collect shipping addresses) and the PaymentElement for Link to autofill Link-saved details for your customer in the ShippingAddressElement and PaymentElement. You can also pass in the appearance option, customizing the Elements to match the design of your site.

[appearance option](/elements/appearance-api)

If you have the customer’s email, pass it to the defaultValues option of the linkAuthenticationElement. This prefills their email address and initiates the Link authentication process.

If you have other customer information, pass it to the defaultValues.billingDetails object for the PaymentElement. Prefilling as much information as possible simplifies Link account creation and reuse for your customers.

Then, render the linkAuthenticationElement and PaymentElement components in your payment form:

The linkAuthenticationElement, PaymentElement, and ShippingAddressElement don’t need to be on the same page. If you have a process where customer contact information, shipping details, and payment details display to the customer in separate steps, you can display each Element in the appropriate step or page. Include the linkAuthenticationElement as the email input form in the contact info collection step to make sure the customer can take full advantage of the shipping and payment autofill provided by Link.

If you collect your customer’s email with the Link Authentication Element early in the checkout flow, you don’t need to show it again on the shipping or payment pages.

You can retrieve the email address details using the onChange prop on the linkAuthenticationElement component. The onChange handler fires whenever the user updates the email field, or when a saved customer email is autofilled.

The Link Authentication Element accepts an email address. Providing a customer’s email address triggers the Link authentication flow as soon as the customer lands on the payment page using the defaultValues option.

[OptionalPrefill additional customer dataClient-side](#prefill-customer-data)

## OptionalPrefill additional customer dataClient-side

[OptionalCollect shipping addressesClient-side](#collect-shipping)

## OptionalCollect shipping addressesClient-side

[OptionalCustomize the appearanceClient-side](#customize-appearance)

## OptionalCustomize the appearanceClient-side

[Submit the SetupIntentClient-side](#web-submit-payment)

## Submit the SetupIntentClient-side

Use stripe.confirmSetup to complete the setup with the details you collected. Provide a return_url to this function so that Stripe can redirect users after they complete their setup. When a payment is successful, Stripe immediately redirects Link and card payments to the return_url.

[stripe.confirmSetup](/js/setup_intents/confirm_setup)

[return_url](/api/setup_intents/create#create_setup_intent-return_url)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

[Charge the saved payment method laterServer-side](#charge-saved-payment-method)

## Charge the saved payment method laterServer-side

When you’re ready to charge your customer, use the Customer and PaymentMethod IDs to create a PaymentIntent. To find a payment method to charge, list the payment methods associated with your customer.

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment with these parameters:

- Set the value of the PaymentIntent’s confirm property to true, which causes confirmation to occur immediately when the PaymentIntent is created.

[confirm](/api/payment_intents/create#create_payment_intent-confirm)

- Set payment_method to the ID of the PaymentMethod

[payment_method](/api#create_payment_intent-payment_method)

- Set customer to the ID of the Customer.

[customer](/api#create_payment_intent-customer)

- Set off_session to true. This causes the PaymentIntent to send an error if authentication is required when your customer isn’t actively using your site or app.

[off_session](/api/payment_intents/confirm#confirm_payment_intent-off_session)

[Test the integration](#web-test-the-integration)

## Test the integration

Don’t store real user data in test mode Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.

[test mode](/test-mode)

Currently, Link only works with credit cards, debit cards, and qualified US bank account purchases. Link requires domain registration.

[domain registration](/payments/payment-methods/pmd-registration)

You can create test mode accounts for Link using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating test mode accounts:

For testing specific payment methods, refer to the Payment Element testing examples.

[Payment Element testing examples](/payments/accept-a-payment?platform=web#additional-testing-resources)

As Stripe adds additional funding source support, you don’t need to update your integration. Stripe automatically supports them with the same transaction settlement time and guarantees as card and bank account payments.

Link supports 3D Secure 2 (3DS2) authentication for card payments. 3DS2 requires customers to complete an additional verification step with the card issuer when paying. Payments that have been successfully authenticated using 3D Secure are covered by a liability shift.

[3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)

To trigger 3DS2 authentication challenge flows with Link in test mode, use the following test card with any CVC, postal code, and future expiration date: 4000000000003220.

In test mode, the authentication process displays a mock authentication page. On that page, you can either authorize or cancel the payment. Authorizing the payment simulates successful authentication and redirects you to the specified return URL. Clicking the Failure button simulates an unsuccessful attempt at authentication.

For more details, refer to the 3D Secure authentication page.

[3D Secure authentication page](/payments/3d-secure)

When testing 3DS flows, only test cards for 3DS2 will trigger authentication on Link.

[Disclose Stripe to your customers](#disclose-cookies)

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our privacy center.

[privacy center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)

## See also

- What is Link

[What is Link](/payments/link/what-is-link)

- Link in the Payment Element

[Link in the Payment Element](/payments/link/payment-element-link)

- Explore the Link Authentication Element

[Explore the Link Authentication Element](/payments/link/link-authentication-element)

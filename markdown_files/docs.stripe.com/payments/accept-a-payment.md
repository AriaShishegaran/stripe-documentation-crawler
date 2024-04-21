htmlAccept a payment | Stripe Documentation[Skip to content](#main-content)Build a payments integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)
[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)Accept a payment# Accept a payment

Securely accept payments online.Build a payment form or use a prebuilt checkout page to start accepting online payments.

WebiOSAndroidReact NativePlugins![](https://b.stripecdn.com/docs-statics-srv/assets/ios-overview.83089c5582bf1fdc7b61fac7e8602497.png)

This integration combines all of the steps required to pay—collecting payment details and confirming the payment—into a single sheet that displays on top of your app.

Interested in displaying payment methods directly in your checkout screen?We’re exploring an integration that lets you embed a prebuilt view directly in your checkout to display payment methods. Sign up for early access.

[Set up StripeServer-sideClient-side](#react-native-setup)First, you need a Stripe account. Register now.

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`### Client-side

The React Native SDK is open source and fully documented. Internally, it uses the native iOS and Android SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

yarnnpmCommand Line`yarn add @stripe/stripe-react-native`Next, install some other necessary dependencies:

- For iOS, navigate to theiosdirectory and run`pod install`to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the StripeProvider component, or use the initStripe initialization method. Only the API publishable key in publishableKey is required. The following example shows how to initialize Stripe using the StripeProvider component.

`import { StripeProvider } from '@stripe/stripe-react-native';

function App() {
  return (
    <StripeProvider
      publishableKey="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
      merchantIdentifier="merchant.com.{{YOUR_APP_NAME}}" // required for Apple Pay
    >
      // Your app code here
    </StripeProvider>
  );
}`NoteUse your API keys for test mode while you test and develop, and your live mode keys when you publish your app.

[Enable payment methods](#react-native-enable-payment-methods)View your payment methods settings and enable the payment methods you want to support. You need at least one payment method enabled to create a PaymentIntent.

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See Payment method integration options for product and payment method support, and our pricing page for fees.

[Add an endpointServer-side](#react-native-add-server-endpoint)NoteIf you want to present the payment sheet before creating a PaymentIntent, see Collect payment details before creating an Intent.

This integration uses three Stripe API objects:

1. A PaymentIntent. Stripe uses this to represent your intent to collect payment from a customer, tracking your charge attempts and payment state changes throughout the process.


2. A Customer (optional). To set up a payment method for future payments, it must be attached to a Customer. Create a Customer object when your customer creates an account with your business. If your customer is making a payment as a guest, you can create a Customer object before payment and associate it with your own internal representation of the customer’s account later.


3. A Customer Ephemeral Key (optional). Information on the Customer object is sensitive, and can’t be retrieved directly from an app. An Ephemeral Key grants the SDK temporary access to the Customer.



NoteIf you never save cards to a Customer and don’t allow returning Customers to reuse saved cards, you can omit the Customer and Customer Ephemeral Key objects from your integration.

For security reasons, your app can’t create these objects. Instead, add an endpoint on your server that:

1. Retrieves the Customer, or creates a new one.
2. Creates an Ephemeral Key for the Customer.
3. Creates a PaymentIntent, with the[amount](/api/payment_intents/create#create_payment_intent-amount),[currency](/api/payment_intents/create#create_payment_intent-currency), and[customer](/api/payment_intents/create#create_payment_intent-customer). You can also optionally include the`automatic_payment_methods`parameter. Stripe enables its functionality by default in the latest version of the API.
4. Returns the Payment Intent’s[client secret](/api/payment_intents/object#payment_intent_object-client_secret), the Ephemeral Key’s`secret`, the Customer’s[id](/api/customers/object#customer_object-id), and your[publishable key](https://dashboard.stripe.com/apikeys)to your app.

The payment methods shown to customers during the checkout process are also included on the PaymentIntent. You can let Stripe pull payment methods from your Dashboard settings or you can list them manually. Regardless of the option you choose, know that the currency passed in the PaymentIntent filters the payment methods shown to the customer. For example, if you pass eur on the PaymentIntent and have OXXO enabled in the Dashboard, OXXO won’t be shown to the customer because OXXO doesn’t support eur payments.

Unless your integration requires a code-based option for offering payment methods, Stripe recommends the automated option. This is because Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. Payment methods that increase conversion and that are most relevant to the currency and customer’s location are prioritized.

Manage payment methods from the DashboardListing payment methods manuallyNoteYou can find a running implementation of this endpoint available on Glitch for quick testing.

You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. The PaymentIntent is created using the payment methods you configured in the Dashboard. If you don’t want to use the Dashboard or if you want to specify payment methods manually, you can list them using the payment_method_types attribute.

Command Line[curl](#)`# Create a Customer (use an existing Customer ID if this is a returning customer)
curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X "POST"

# Create an Ephemeral Key for the Customer
curl https://api.stripe.com/v1/ephemeral_keys \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Version: 2024-04-10" \
  -X "POST" \
  -d "customer"="{{CUSTOMER_ID}}" \

# Create a PaymentIntent
curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X "POST" \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "amount"=1099 \
  -d "currency"="eur" \
  # In the latest version of the API, specifying the `automatic_payment_methods` parameter
  # is optional because Stripe enables its functionality by default.
  -d "automatic_payment_methods[enabled]"=true \`[Collect payment detailsClient-side](#react-native-collect-payment-details)Before displaying the mobile Payment Element, your checkout page should:

- Show the products being purchased and the total amount
- Collect any required shipping information
- Include a checkout button to present Stripe’s UI

In the checkout of your app, make a network request to the backend endpoint you created in the previous step and call initPaymentSheet from the useStripe hook.

`export default function CheckoutScreen() {
  const { initPaymentSheet, presentPaymentSheet } = useStripe();
  const [loading, setLoading] = useState(false);

  const fetchPaymentSheetParams = async () => {
    const response = await fetch(`${API_URL}/payment-sheet`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const { paymentIntent, ephemeralKey, customer} = await response.json();

    return {
      paymentIntent,
      ephemeralKey,
      customer,
    };
  };

  const initializePaymentSheet = async () => {
    const {
      paymentIntent,
      ephemeralKey,
      customer,
      publishableKey,
    } = await fetchPaymentSheetParams();

    const { error } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      customerId: customer,
      customerEphemeralKeySecret: ephemeralKey,
      paymentIntentClientSecret: paymentIntent,
      // Set `allowsDelayedPaymentMethods` to true if your business can handle payment
      //methods that complete payment after a delay, like SEPA Debit and Sofort.
      allowsDelayedPaymentMethods: true,
      defaultBillingDetails: {
        name: 'Jane Doe',
      }
    });
    if (!error) {
      setLoading(true);
    }
  };

  const openPaymentSheet = async () => {
    // see below
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  return (
    <Screen>
      <Button
        variant="primary"
        disabled={!loading}
        title="Checkout"
        onPress={openPaymentSheet}
      />
    </Screen>
  );
}`When your customer taps the Checkout button, call presentPaymentSheet() to open the sheet. After the customer completes the payment, the sheet is dismissed and the promise resolves with an optional StripeError<PaymentSheetError>.

`export default function CheckoutScreen() {
  // continued from above

  const openPaymentSheet = async () => {
    const { error } = await presentPaymentSheet();

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else {
      Alert.alert('Success', 'Your order is confirmed!');
    }
  };

  return (
    <Screen>
      <Button
        variant="primary"
        disabled={!loading}
        title="Checkout"
        onPress={openPaymentSheet}
      />
    </Screen>
  );
}`If there is no error, inform the user they’re done (for example, by displaying an order confirmation screen).

Setting allowsDelayedPaymentMethods to true allows delayed notification payment methods like US bank accounts. For these payment methods, the final payment status isn’t known when the PaymentSheet completes, and instead succeeds or fails later. If you support these types of payment methods, inform the customer their order is confirmed and only fulfill their order (for example, ship their product) when the payment is successful.

[Set up a return URL (iOS only)Client-side](#react-native-set-up-return-url)When a customer exits your app, for example to authenticate in Safari or their banking app, provide a way for them to automatically return to your app afterward. Many payment method types require a return URL, so if you fail to provide it, we can’t present those payment methods to your user, even if you’ve enabled them.

To provide a return URL, configure a custom URL scheme or universal link and set up your root component to forward the URL to the Stripe SDK.

NoteIf you’re using Expo, set your scheme in the app.json file.

App.tsx`import React, { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}`Additionally, set the returnURL when you call the initPaymentSheet method:

`await initPaymentSheet({
  ...
  returnURL: 'your-app://stripe-redirect',
  ...
});`For more information on native URL schemes, refer to the Android and iOS docs.

[Handle post-payment events](#react-native-fulfillment)Stripe sends a payment_intent.succeeded event when the payment completes. Use the Dashboard webhook tool or follow the webhook guide to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept different types of payment methods with a single integration.

In addition to handling the payment_intent.succeeded event, we recommend handling these other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.succeeded](/api/events/types?lang=php#event_types-payment_intent.succeeded)Sent when a customer successfully completes a payment.Send the customer an order confirmation andfulfilltheir order.[payment_intent.processing](/api/events/types?lang=php#event_types-payment_intent.processing)Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a`payment_intent.succeeded`or`payment_intent.payment_failed`event in the future.Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.[payment_intent.payment_failed](/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent when a customer attempts a payment, but the payment fails.If a payment transitions from`processing`to`payment_failed`, offer the customer another attempt to pay.[Test the integration](#react-native-test)CardsBank redirectsBank debitsCard numberScenarioHow to test4242424242424242The card payment succeeds and doesn’t require authentication.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000002500003155The card payment requires[authentication](/strong-customer-authentication).Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000000000009995The card is declined with a decline code like`insufficient_funds`.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.6205500000000000004The UnionPay card has a variable length of 13-19 digits.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.See Testing for additional information to test your integration.

[OptionalEnable Link](#react-native-link)[OptionalEnable Apple Pay](#react-native-apple-pay)[OptionalEnable Google Pay](#react-native-google-pay)[OptionalEnable card scanning (iOS only)Client-side](#react-native-card-scanning)[OptionalCustomize the sheetClient-side](#react-native-customization)[OptionalHandle user logout](#react-native-logout)[OptionalComplete payment in your UI](#react-native-flowcontroller)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).[Code quickstart](/docs/payments/quickstart)On this page[Set up Stripe](#react-native-setup)[Enable payment methods](#react-native-enable-payment-methods)[Add an endpoint](#react-native-add-server-endpoint)[Collect payment details](#react-native-collect-payment-details)[Set up a return URL (iOS only)](#react-native-set-up-return-url)[Handle post-payment events](#react-native-fulfillment)[Test the integration](#react-native-test)Related Guides[Elements Appearance API](/docs/elements/appearance-api)[More payment scenarios](/docs/payments/more-payment-scenarios)[How cards work](/docs/payments/cards/overview)Products Used[Payments](/payments)[Elements](/payments/elements)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
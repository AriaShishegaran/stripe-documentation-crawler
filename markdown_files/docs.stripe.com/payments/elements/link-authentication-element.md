htmlLink Authentication Element | Stripe Documentation[Skip to content](#main-content)Link Authentication Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Felements%2Flink-authentication-element)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Felements%2Flink-authentication-element)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)# Link Authentication Element

Use the Link Authentication Element to integrate Link.Link saves and autofills customer payment and shipping information. Customers can use different funding sources to pay with Link, including credit cards, debit cards, and US bank accounts. Learn more at link.com.

Use the Link Authentication Element to create a single email input field for both email collection and Link authentication.

Customer locationUnited States (USD)SizeDesktopThemeDefaultLayoutTabsThis demo only displays Google Pay or Apple Pay if you have an active card with either wallet.To see how Link works, type in any email address into the email input.## Start with examples

To see the Link Authentication Element in action, start with one of these examples:

[QuickstartCode and instructions for accepting a payment and using the Link Authentication Element to integrate Link.](/payments/quickstart)[Clone a sample app on GitHubHTML · React · Vue](https://github.com/stripe-samples/accept-a-payment)## Before you begin

Before you start, you need to register your domain.

## Create the Link Authentication Element

The following code creates an instance of the Link Authentication Element and mounts it to the DOM:

HTML + JSReactcheckout.js`// Enable the skeleton loader UI for the optimal loading experience.
const loader = 'auto';

// Create an elements group from the Stripe instance passing in the clientSecret and enabling the loader UI.
const elements = stripe.elements({clientSecret, loader});

// Create an instance of the Link Authentication Element.
const linkAuthenticationElement = elements.create("linkAuthentication");

// Mount the Elements to their corresponding DOM node
linkAuthenticationElement.mount("#link-authentication-element");
paymentElement.mount("#payment-element");`## Retrieving email address

You can retrieve the email address details using the onChange prop on the linkAuthenticationElement component. The onChange handler fires whenever the user updates the email field, or when a saved customer email is autofilled.

`linkAuthenticationElement.on('change', (event) => {
  const email = event.value.email;
});`## Prefill customer data

The Link Authentication Element accepts an email address. Providing a customer’s email address starts the Link authentication flow as soon as the customer lands on the payment page using the defaultValues option:

checkout.js`// Create the Link Authentication Element with the defaultValues option
const linkAuthenticationElement = elements.create("linkAuthentication", {defaultValues: {email: "foo@bar.com"}});

// Mount the Link Authentication Element to its corresponding DOM node
linkAuthenticationElement.mount("#link-authentication-element");`If you want to prefill additional customer data, add the defaultValues.billingDetails object to the Payment Element. This prefills a customer’s name, phone number, and shipping addresses. By prefilling as much of your customer’s information as possible, you simplify Link account creation and reuse.

The following code shows a Payment Element with all of its values prefilled:

ReactHTML + JScheckout.js`<PaymentElement
  options={{
    defaultValues: {
      billingDetails: {
        name: 'John Doe',
        phone: '888-888-8888',
        address: {
          postal_code: '10001',
          country: 'US',
        }
      },
    },
  }}
/>;`## Combine Elements

The Link Authentication Element interoperates with other elements. For instance, the following example uses the Link Authentication Element with the Address Element and Payment Element:

![A checkout page that includes the Link Authentication Element, Address Element, and Payment Element.](https://b.stripecdn.com/docs-statics-srv/assets/lae-with-ae-pe.b70e0386757f6061d9b27c7211794173.png)

Use the Link Authentication Element with other Elements to compose your checkout page

## Appearance

You can use the Appearance API to control the style of all elements. Choose a theme or update specific details.

![Examples of light and dark modes for the payment element checkout form.](https://b.stripecdn.com/docs-statics-srv/assets/appearance_example.e076cc750983bf552baf26c305e7fc90.png)

Use the Appearance API to change the look and style of your Elements

In the following example, the “flat” theme overrides the default text color used for Elements:

index.js[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const appearance = {
  theme: 'flat'
  variables: { colorPrimaryText: '#262626' }
};`See all 10 linesWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Start with examples](#start-with-examples)[Before you begin](#before-you-begin)[Create the Link Authentication Element](#create-link-authentication-element)[Retrieving email address](#retrieving-email-address)[Prefill customer data](#prefill-customer-data)[Combine Elements](#combine-elements)[Appearance](#appearance)Related Guides[Add Link to an Elements integration](/docs/payments/link/add-link-elements-integration)Products Used[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
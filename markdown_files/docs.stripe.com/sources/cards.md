htmlCard payments with Sources | Stripe Documentation[Skip to content](#main-content)Card Sources[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fcards)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fcards)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# Card payments with SourcesDeprecated

Use Sources to accept card payments from around the world.WarningStripe recommends using the Payment Intents API instead of this API. With a PaymentIntent integration, you can use Dynamic 3D Secure, which helps you avoid declined payments due to Strong Customer Authentication regulation in Europe. To get started, follow the Accept a payment guide.

Stripe users can process card payments from customers around the world using Sources—a single integration path for creating payments using any supported method. During the payment process, your integration creates a source representing the card information. This source is then used in a charge request to debit the card and complete the payment.

Within the scope of Sources, cards are a pull-based, reusable and synchronous method of payment. This means that, after capturing the customer’s card details, you can debit arbitrary amounts from the customer’s card without them having to take any additional action and there is immediate confirmation about the success or failure of a payment.

## Handling card information

Card information is sensitive by nature. Card sources must be created client-side using Stripe.js and Elements. This ensures that no sensitive card data passes through your server so your integration can operate in a PCI compliant way.

When your customer submits their card information using your payment form, it is sent directly to Stripe, and a representative Source object is returned for you to use. The process is similar to the creation of tokens. If you’re already using Elements to tokenize card information, switching to Sources is only a small change.

[Prerequisite: Consider a flexible checkout flow if you want to accept additional payment methods](#considerations)Card payments with Sources has fewer steps and requirements than other payment methods. As it’s a synchronous method and there is no additional customer action to take, the use of webhooks isn’t necessary. If you only want to accept card payments, you can simply follow the steps within this documentation to begin accepting cards with Sources.

However, accepting other methods of payment through Sources (for example, iDEAL, SEPA Direct Debit, and so on) requires additional steps, making the use of webhooks necessary. You can refer to our best practices for developing a flexible checkout flow that supports different payment methods.

[Create a Source object](#create-source)### Stripe.js reference

This guide supplements our Stripe.js and Elements documentation with specific usage for Sources.

To create a card Source client-side, please refer to Accept a payment. You then create a Source object instead of a Token by calling the createSource instead of the createToken method.

You can also provide an optional owner dictionary containing additional cardholder information, such as their name and full billing address.

`// Create a source or display an error when the form is submitted.
const form = document.getElementById('payment-form');
const ownerInfo = {
  owner: {
    name: 'Jenny Rosen',
    address: {
      line1: 'Nollendorfstraße 27',
      city: 'Berlin',
      postal_code: '10777',
      country: 'DE',
    },
    email: 'jenny.rosen@example.com'
  },
};
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {source, error} = await stripe.createSource(card, ownerInfo);

  if (error) {
    // Inform the user if there was an error
    const errorElement = document.getElementById('card-errors');
    errorElement.textContent = error.message;
  } else {
    // Send the source to your server
    stripeSourceHandler(source);
  }
});`If your Elements payment form collects a billing postal code, it’s used as the value for the owner field address[postal_code] during source creation. This also overrides any value that is being provided separately as part of owner. If you are already collecting your customer’s billing postal code elsewhere on your checkout page, we recommend including it as part of owner and hiding the Elements postal code field—set the Element option of hidePostalCode to true.

The last steps of the Accept a payment guide remain similar and consist of submitting the source, along with any additional information that has been collected, to your server.

`const stripeSourceHandler = (source) => {
  // Insert the source ID into the form so it gets submitted to the server
  const form = document.getElementById('payment-form');
  const hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeSource');
  hiddenInput.setAttribute('value', source.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}`When the source is created, its status immediately changes to chargeable. No additional customer action is needed so the source can be used right away. Information about the card is provided within the card subhash.

`{
  "id": "src_1AhIN74iJb0CbkEwmbRYPsd4",
  "object": "source",
  "amount": null,
  "client_secret": "src_client_secret_sSPHZ17iQG6j9uKFdAYqPErO",
  "created": 1500471469,
  "currency": null,
  "flow": "none",
  "livemode": false,
  "metadata": {`See all 47 linesAs card payments are a pull-based payment method, there is no movement of funds during the creation of a source. Only when a successful charge request has been made is the customer’s card debited and you receive the funds.

### Source creation in mobile applications

If you’re building an iOS or Android app, you can implement sources using our mobile SDKs. Refer to our sources documentation for iOS or Android to learn more.

[Charge the Source](#charge-request)After creating a card Source, and before creating a charge request to complete the payment, attach it to a Customer for later reuse.

### Attaching the Source to a Customer

Attaching the Source to a Customer is required for you to reuse it for future payments. Please refer to our Sources & Customers guide for more details on how to attach Sources to new or existing Customers and how the two objects interact together. The following snippet attaches the Source to a new Customer:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode email="paying.user@example.com" \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`### Making a charge request to finalize the payment

Once attached, you can use the Source object’s ID along with the Customer object’s ID to perform a charge request and finalize the payment.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount="1000" \
  -d currency="usd" \
  -d customer=cus_AFGbOSiITuJVDs \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`A card source must be used within a few minutes of its creation as CVC information is only available for a short amount of time. Card sources do not expire, but using them after a delay can result in a charge request that is performed without CVC information. The consequences of this can be higher decline rates and increased risk of fraud.

Although the status of the source is chargeable, this does not mean that the payment is going to be successful. A charge request can still fail if the customer’s card issuer declines the payment.

[Confirm that the charge has succeeded](#charge-confirmation)Card payments are a synchronous method so confirmation of the charge’s status happens in real-time.

Your integration immediately receives the result of the charge request—either a Charge object upon success or an exception upon failure. Once the charge has been confirmed as successful, the payment has been successfully completed and you can notify your customer and fulfill the order.

If you’re making use of webhooks, your integration also receives either of the following events:

EventDescription`charge.succeeded`The charge succeeded and the payment is complete.`charge.failed`The charge has failed and the payment could not be completed.### Disputed payments

Card networks provide a process for cardholders to dispute payments made with their card. A dispute can be filed by the cardholder any time after a payment has been successful. It is still possible for a successful payment to be reversed if the card issuer investigates a dispute and decides it should be refunded.

Disputes can be made for a variety of reasons. As such, you should make the appropriate decisions regarding your business and how you manage disputes, if they occur, and how to avoid them completely.

### Updating a card source expiration date

You can update the card[exp_month] and card[exp_year] attributes of card sources, allowing you to update their expiration date:

Command Line[curl](#)`curl https://api.stripe.com/v1/sources/src_18cPLvAHEMiOZZp1YBngt6En \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d currency=usd \
  -d "card[exp_month]"=11 \
  -d "card[exp_year]"=2022`## See also

- [Declines & failed payments](/declines)
- [Other supported payment methods](/sources)
- [Sources API reference](/api#sources)
- [Best practices](/sources/best-practices)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Handling card information](#handling-card-information)[Prerequisite: Consider a flexible checkout flow if you want to accept additional payment methods](#considerations)[Create a Source object](#create-source)[Charge the Source](#charge-request)[Confirm that the charge has succeeded](#charge-confirmation)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
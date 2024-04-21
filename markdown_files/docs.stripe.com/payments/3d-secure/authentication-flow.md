htmlAuthenticate with 3D Secure | Stripe Documentation[Skip to content](#main-content)Authenticate with 3D Secure[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2F3d-secure%2Fauthentication-flow)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2F3d-secure%2Fauthentication-flow)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[3D Secure authentication](/docs/payments/3d-secure)# Authenticate with 3D Secure

Integrate 3D Secure (3DS) into your checkout flow.CautionMajor card brands no longer support 3D Secure 1. To continue using 3D Secure, adopt the Payment Intents or Setup Intents APIs. This integration:

- Takes advantage of the benefits from[Dynamic 3D Secure](/payments/3d-secure/authentication-flow#three-ds-radar).
- Supports[3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2).
- Complies with[Strong Customer Authentication](/strong-customer-authentication)regulation in Europe.

You can integrate 3D Secure (3DS) authentication into your checkout flow on multiple platforms, including Web, iOS, Android, and React Native. This integration runs 3D Secure 2 (3DS2) when supported by the customer’s bank and falls back to 3D Secure 1 otherwise. To use Stripe’s 3DS service with other processors, contact support.

WebiOSAndroid![Checkout page](https://b.stripecdn.com/docs-statics-srv/assets/3ds-flow-1-checkout-page.039294e0dee3a6dede8ea8a32185aae5.png)

The customer enters their card details.

![Loading symbol](https://b.stripecdn.com/docs-statics-srv/assets/3ds-flow-2-frictionless-flow.417618d0570c469cfb6bbc43630c7896.png)

The customer’s bank assesses the transaction and can complete 3D Secure at this step.

![Authentication modal](https://b.stripecdn.com/docs-statics-srv/assets/3ds-flow-3-challenge-flow.9052a220f336bbdb75a51799622c6477.png)

If required by their bank, the customer completes an additional authentication step.

## Control the 3DS flow

Stripe triggers 3DS automatically if required by a regulatory mandate such as Strong Customer Authentication or requested by an issuer with the soft decline code authentication_required.

You can also use Radar rules or the API to control when to prompt users to complete 3DS authentication, making a determination for each user based on the desired parameters. However, not all transactions support 3DS, for example wallets or off-session payments.

When a payment triggers 3DS, Stripe requires the user to perform authentication to complete the payment if 3DS authentication is available for a card. Depending on what frontend you use, this might require you to display the 3DS Flow.

In a typical Payment Intent API flow that triggers 3DS:

1. The user enters their payment information, which confirms a PaymentIntent, SetupIntent, or attaches a PaymentMethod to a Customer.
2. Stripe assesses if the transaction supports and requires 3DS based on regulatory mandates, Radar rules, manual API requests, issuer soft declines, and other criteria.
3. If 3DS is:  - Not required: For example, because of an[exemption](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication), Stripe attempts the charge. The PaymentIntent transitions to a status of`processing`. If requested by the issuer with a[soft decline](/declines/codes), we automatically reattempt and continue as if required.
  - Not supported: The PaymentIntent transitions to a status of`requires_payment_method`. Depending on the reason 3DS was triggered it might be permissible to continue to the authorization step for the charge. In that case, the PaymentIntent transitions to a status of`processing`.
  - Required: Stripe starts the 3DS authentication flow by contacting the card issuer’s 3D Secure Access Control Server (ACS) and starting the 3DS flow.


4. When Stripe receives 3DS flow information from the issuer, we attempt authentication. The PaymentIntent transitions to a status of`requires_action`:  - See below for how to[display the required 3DS action](#when-to-use-3d-secure). Issuers might request different 3DS flow action types, which might not always result in visibly displaying a 3DS challenge (for example, a frictionless flow).
  - If the issuer doesn’t support 3DS at all or has an outage, Stripe might attempt to complete the payment without authentication if permissible.


5. Depending on the 3DS authentication result:  - Authenticated: Stripe attempts the charge and the PaymentIntent transitions to a status of`processing`.
  - Failure: The PaymentIntent transitions to a status of`requires_payment_method`, indicating that you need to try a different payment method, or you can retry 3DS by reconfirming.
  - Other scenarios: Depending on the reason the payment triggered 3DS, it might be permissible to continue authorization for the charge in[edge cases](/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result). For example, a result of`attempt_acknowledged`leads to a charge and the PaymentIntent transitions to a status of`processing`.    - An exception is when creating[Indian e-mandates for recurring payments](/india-recurring-payments). Anything but an`authenticated`result is treated as failure.




6. The PaymentIntent transitions to one of the following statuses, depending on the outcome of the payment:`succeeded`,`requires_capture`, or`requires_payment_method`.

To track whether 3DS was supported and attempted on a card payment, read the three_d_secure property on the card information in the Charge’s payment_method_details. Stripe populates the three_d_secure property when the customer attempts to authenticate the card—three_d_secure.result indicates the authentication outcome.

### Use Radar rules in the Dashboard

Stripe provides default Radar rules to dynamically request 3DS when creating or confirming a PaymentIntent or SetupIntent. You can configure these rules in your Dashboard.

If you have Radar for Fraud Teams, you can add custom 3DS rules.

### Manually request 3DS with the API

The default method to trigger 3DS is using Radar to dynamically request 3D Secure based on risk level and other requirements. Triggering 3DS manually is for advanced users integrating Stripe with their own fraud engine.

To trigger 3DS manually, set payment_method_options[card][request_three_d_secure] to any or challenge depending on what you want to optimize for when creating or confirming a PaymentIntent or SetupIntent. This process is the same for one-time payments or when setting up a payment method for future payments. When you provide this parameter, Stripe attempts to perform 3DS and overrides any dynamic 3D Secure Radar rules on the PaymentIntent or SetupIntent.

When to provide this parameter depends on when your fraud engine detects risk. For example, if your fraud engine only inspects card details, you know whether to request 3DS before you create the PaymentIntent or SetupIntent. If your fraud engine inspects both card and transaction details, provide the parameter during confirmation—when you have more information. Then pass the resulting PaymentIntent or SetupIntent to your client to complete the process.

Explore the request_three_d_secure parameter’s usage for each case in the API reference:

- [Create a PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a PaymentIntent](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-request_three_d_secure)
- [Create a SetupIntent](/api/setup_intents/create#create_setup_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a SetupIntent](/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-card-request_three_d_secure)

Set request_three_d_secure to any to manually request 3DS with a preference for a frictionless flow, increasing the likelihood of the authentication being completed without any additional input from the customer.

Set request_three_d_secure to challenge to request 3DS with a preference for a challenge flow, where the customer must respond to a prompt for active authentication.

Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. You can find out what the ultimate authentication flow was by inspecting the authentication_flow on the three_d_secure property of the Charge or SetupAttempt. To learn more about 3DS flows, read our guide.

CautionStripe only requires your customer to perform authentication to complete the payment successfully if 3DS authentication is available for a card. If it’s not available for the given card or if an error occurred during the authentication process, the payment proceeds normally.

Stripe’s SCA rules run automatically, regardless of whether or not you manually request 3DS. Any 3DS prompts from you are additional and not required for SCA.

## Display the 3DS flow

WebiOSAndroidReact NativeStripe automatically displays the authentication UI in a pop-up modal when calling confirmCardPayment and handleCardAction. You can also redirect to the bank’s website or use an iframe.

Stripe.js collects basic device information during 3DS2 authentication and sends it to the issuing bank for their risk analysis.

### Redirect to the bank website

To redirect your customer to the 3DS authentication page, pass a return_url to the PaymentIntent when confirming on the server or on the client.

After confirmation, if a PaymentIntent has a requires_action status, inspect the PaymentIntent’s next_action. If it contains redirect_to_url, that means 3DS is required.

`next_action: {
    type: 'redirect_to_url',
    redirect_to_url: {
      url: 'https://hooks.stripe.com/...',
      return_url: 'https://mysite.com'
    }
}`In the browser, redirect the customer to the url in the redirect_to_url hash to complete authentication.

`var action = intent.next_action;
  if (action && action.type === 'redirect_to_url') {
    window.location = action.redirect_to_url.url;
  }`When the customer finishes the authentication process, the redirect sends them back to the return_url you specified when you created or confirmed the PaymentIntent. The redirect also adds payment_intent and payment_intent_client_secret URL query parameters that your application can use to identify the PaymentIntent associated with the purchase.

### Display in an iframe

You can’t customize the authentication UI on the web to match your website’s design—the bank that issued the card controls the fonts and colors.

However, you can choose how and where to show the 3D Secure UI. Most businesses show it in a modal dialog above their payment page. If you have your own modal component, you can place the 3DS frame inside of it. You can also show the authentication content inline with your payment form.

Confirm the PaymentIntentServer-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When your customer is ready to complete their purchase, you confirm the PaymentIntent to begin the process of collecting their payment.

If you want to control how to display 3DS, provide a return_url, which is where the 3DS <iframe> is redirected when authentication is complete. If your site uses a content security policy, check that it allows iframes from https://js.stripe.com, https://hooks.stripe.com, and the origin of the URL you passed to return_url.

If you’re confirming from the frontend, use the confirmCardPayment method in Stripe.js. For example, if you’re gathering card information using Stripe Elements:

`stripe.confirmCardPayment(
  '{{PAYMENT_INTENT_CLIENT_SECRET}}',
  {
    payment_method: {card: cardElement},
    return_url: 'https://example.com/return_url'
  },
  // Disable the default next action handling.
  {handleActions: false}
).then(function(result) {
  // Handle result.error or result.paymentIntent
  // More details in Step 2.
});`If you confirm from your server, provide a return_url. Depending on your integration, you might want to pass other information to confirm as well.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode return_url="https://example.com/return_url"`Check the PaymentIntent statusServer-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Next, inspect the status property property of the confirmed PaymentIntent to determine whether the payment completed successfully. The following list describes possible status values and their significance:

StatusDescription`requires_payment_method`The request failed with a`402`HTTP status code, meaning that the payment was unsuccessful. Check the[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)property and try again, collecting new payment information from the customer if necessary.`requires_capture`The request completed without authentication. You can continue to[capture the funds](/payments/place-a-hold-on-a-payment-method#capture-funds).`requires_action`An additional step such as 3DS is required to complete the payment. Ask the customer to return to your application to complete payment.`succeeded`The payment completed, creating a Charge with the supplied payment method. No further steps are required.On versions of the API before 2019-02-11, requires_payment_method appears as requires_source and requires_action appears as requires_source_action.

Render the 3DS iframeClient-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When the value of the status property is requires_action, you need to complete an additional step before processing the payment. For a card payment that requires 3DS, the PaymentIntent’s status shows as requires_action and its next_action property appears as redirect_to_url. The redirect_to_url payload contains a URL that opens in an iframe to display 3DS:

`var iframe = document.createElement('iframe');
  iframe.src = paymentIntent.next_action.redirect_to_url.url;
  iframe.width = 600;
  iframe.height = 400;
  yourContainer.appendChild(iframe);`For 3DS2, card issuers are required to support showing the 3DS content at sizes of 250x400, 390x400, 500x600, 600x400, and full screen (dimensions are width by height). You might enhance the 3DS UI by opening the iframe at exactly one of those sizes.

CautionYou can’t use the sandbox attribute on the 3DS iframe. In live mode, the card issuer controls some content inside this iframe. Some issuers’ implementations fail if they’re sandboxed, and the payment won’t succeed.

Handle the redirectClient-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

After the customer completes 3DS, the iframe redirects to the return_url you provided when confirming the PaymentIntent. That page needs to postMessage to your top-level page to inform it that 3DS authentication is complete. Your top-level page then needs to determine whether the payment succeeded or requires further action from your customer.

For example, you might have your return_url page execute:

`window.top.postMessage('3DS-authentication-complete');`Your top payment page needs to listen for this postMessage to know when authentication has finished. You then need to retrieve the updated PaymentIntent and check on the status of the payment. If the authentication failed, the PaymentIntent’s status is requires_payment_method. If the payment completed successfully, the status is succeeded. If you use separate authorize and capture, the status is requires_capture instead.

`function on3DSComplete() {
    // Hide the 3DS UI
    yourContainer.remove();

    // Check the PaymentIntent
    stripe.retrievePaymentIntent('{{PAYMENT_INTENT_CLIENT_SECRET}}')
      .then(function(result) {
        if (result.error) {
          // PaymentIntent client secret was invalid
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            // Show your customer that the payment has succeeded
          } else if (result.paymentIntent.status === 'requires_payment_method') {
            // Authentication failed, prompt the customer to enter another payment method
          }
        }
      });
  }

  window.addEventListener('message', function(ev) {
    if (ev.data === '3DS-authentication-complete') {
      on3DSComplete();
    }
  }, false);`## Test the 3DS flow

Use a Stripe test card with any CVC, postal code, and future expiration date to trigger 3DS authentication challenge flows while in test mode.

When you build an integration with your test API keys, the authentication process displays a mock authentication page. On that page, you can either authorize or cancel the payment. Authorizing the payment simulates successful authentication and redirects you to the specified return URL. Clicking the Failure button simulates an unsuccessful attempt at authentication.

WebiOSAndroidReact NativeCard numbersPaymentMethodsNumber3DS usageDescription4000000000003220RequiredThe payment must always complete 3DS2 authentication to be successful.By default, your Radar rules request 3DS authentication for this card.4000002500003155RequiredThis card requires 3DS2 authentication for off-session payments unless you[set it up](/payments/save-and-reuse)for future payments. After you set it up, off-session payments no longer require authentication.4000008400001629Required3DS authentication is required, but payments will be declinedwith a`card_declined`failure code after authentication.By default, your Radar rules request 3DS authentication for this card.4000000000003055Supported3DS authentication can still be performed, but isn’t required.By default, your Radar rules won’t request 3DS authentication for this card.4242424242424242SupportedThis card supports 3DS, but it isn’t enrolled in 3DS.This means that if your Radar rules request 3DS, the customer won’t go through additional authentication.By default, your Radar rules won’t request 3DS authentication for this card.378282246310005Not supportedThis card doesn’t support 3DS and you can’t invoke it.The PaymentIntent proceeds without performing authentication.All other Visa and Mastercard test cards don’t require authentication from the customer’s card issuer.

You can write custom Radar rules in test mode to trigger authentication on test cards. Learn more about testing your Radar rules.

## Disputes and liability shift

The liability shift rule applies to payments that are successfully authenticated using 3D Secure or an equivalent cryptogram such as Apple Pay or Google Pay in some cases. If a cardholder disputes a 3DS payment as fraudulent, the liability shifts from you to the card issuer.

If a card doesn’t support 3DS or an error occurs during the authentication process, the payment proceeds normally. When this occurs, liability doesn’t generally shift to the issuer, because a successful 3DS authentication hasn’t taken place.

In practice, this means that you won’t receive disputes marked as fraudulent if the payment was covered by the liability shift rule, but you might still receive an Early Fraud Warning. You might still receive a low percentage of fraudulent disputes, and we list a few cases below where the liability shift rule might not apply.

You might receive a dispute inquiry on a successfully authenticated payment using 3DS. This type of dispute doesn’t precipitate a chargeback because it’s only a request for information.

If you receive an inquiry for a 3D-Secure-authenticated charge, you must respond. If you don’t, the cardholder’s bank can initiate a financial chargeback known as a “no-reply” chargeback that could invalidate the liability shift. To prevent no-reply chargebacks on 3DS charges, submit sufficient information about the charge. Include information about what was ordered, how it was delivered, and who it was delivered to (whether it was physical or electronic goods, or services).

NoteIf a customer disputes a payment for any other reason (for example, product not received), then the standard dispute process applies. Make informed decisions about your business management, especially in handling and completely avoiding disputes.

Liability shift might also occur when the card network requires 3DS, but it isn’t available for the card or issuer. This can happen if the issuer’s 3DS server is down or if the issuer doesn’t support it, despite the card network requiring support. During the payment process, the cardholder isn’t prompted to complete 3DS authentication, because the card isn’t enrolled. Although the cardholder didn’t complete 3DS authentication, liability can still shift to the issuer.

Stripe returns the requested Electronic Commerce Indicator (ECI) in the electronic_commerce_indicator of the 3DS authentication outcome. This indicator can aid in determining whether a charge should adhere to the liability shift rule. As 3DS occurs subsequent to the initial payment intent response, you typically get this from a charge.succeeded webhook. A requested ECI might be degraded in the issuer response, which we don’t reveal.

Sometimes payments that are successfully authenticated using 3DS don’t fall under liability shift. This is rare and can happen, for example, if you have an excessive level of fraud on your account and are enrolled in a fraud monitoring program. Certain networks have also exempted some industries from liability shift. For example, Visa doesn’t support liability shift for businesses engaging in wire transfer or money orders, non-financial institutions offering foreign or non-fiat currency, or stored-value card purchase or load.

In rare cases, liability shift might get downgraded post-authorization, or the card networks’ dispute rejection system might fail to catch liability shift for a transaction. In these cases, if you counter the dispute, Stripe automatically adds the requested ECI and the 3DS authentication outcome for the payment to your evidence details, but we encourage you to include additional details to improve your odds of winning the dispute.

### Custom Radar rules for 3DS and liability shift

If you have Radar for Fraud Teams, you can customize your rules to control when to request 3DS and how to handle each specific authentication outcome and liability shift. Stripe’s Strong Customer Authentication (SCA) rules run automatically and independently of custom Radar rules, and block unauthenticated payments unless exempted.

## See also

- [Import 3DS results](/payments/payment-intents/three-d-secure-import)
- [Payment authentication report](/payment-authentication)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Control the 3DS flow](#controlling-when-to-present-the-3d-secure-flow)[Display the 3DS flow](#when-to-use-3d-secure)[Test the 3DS flow](#three-ds-cards)[Disputes and liability shift](#disputed-payments)[See also](#see-also)Related Guides[Strong Customer Authentication (SCA) readiness](/docs/strong-customer-authentication)[Prevent disputes and fraud](/docs/disputes/prevention)Products Used[Payments](/payments)[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
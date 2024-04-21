htmlCollect Inputs | Stripe Documentation[Skip to content](#main-content)Collect inputs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollect-inputs)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollect-inputs)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Collect InputsBeta

Use Terminal to collect inputs from your customers.Available in: 🌎 for Stripe S700 and BBPOS WisePOS E using server-driven integration, iOS SDK, or Android SDK.

NoteTo request access to the Collect Inputs beta, for server-driven, iOS SDK, or Android SDK, email us at stripe-terminal-betas@stripe.com.

Server-driveniOSAndroid[Collect inputs](#collect-inputs)In addition to collecting payments, Terminal smart readers allow you to display forms and collect information from customers. You make requests to the Stripe API, and the API communicates with the reader to display a prebuilt UI to collect customer input. Stripe notifies your backend of the customer’s responses using webhooks.

To collect inputs using Terminal’s smart readers, use the collect_inputs command. You can specify up to 5 inputs at a time, and the reader collects them in sequence. Stripe smart readers currently support six input types:

- The`selection`input type allows you to display up to 4 choices for a customer to select from.
- The`signature`input type allows you to collect a signature using the reader’s touchscreen.
- The`email`input type allows you to collect an email address from a customer.
- The`phone`input type allows you to collect a phone number from a customer.
- The`text`input type allows you to collect additional information from customers.
- The`numeric`input type allows you to collect additional information from customers.

![Supported input types.](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-form-types.9715c2bbc0105378c9c4a5e8e1c4eb59.png)

Supported input types.

You can customize the appearance and behavior of all input types:

- Set important inputs as[required](/api/terminal/readers/collect_inputs#collect_inputs-inputs-required)to make sure they’re collected. For required inputs, the skip button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using[custom_text](/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text).
- Add up to 4[toggles](/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles)that customers can enable or disable for boolean options, agreements, or opt-ins.

![Toggles in email and selection form](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-toggle.3183c0c14cc916374d588ba54ad34639.png)

Email and selection form with toggle

Additional customization is available for selection inputs. When specifying the choices you want to display to the customer, you can emphasize or de-emphasize choices using the style parameter.

![Selection choice styles](https://b.stripecdn.com/docs-statics-srv/assets/collect-inputs-choice-style.dc4d2fcb98ee649a29bc43df806c114a.png)

Primary and secondary selection choice styles

In addition to the list of inputs, you might want to include metadata in your request. The request payload includes the specified metadata, which appears in both the synchronous response and the success or failure webhooks. By including a unique identifier such as a customer ID or order ID, you can more easily identify and handle the incoming webhook.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/collect_inputs \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Version: 2024-04-10; terminal_collect_inputs_beta=v1;" \
  -d "inputs[0][type]"=signature \
  -d "inputs[0][custom_text][title]"="Rental Agreement" \
  -d "inputs[0][custom_text][description]"="Please sign below to indicate that you agree to the rental agreement." \
  -d "inputs[0][custom_text][submit_button]"=Submit \
  -d "inputs[0][required]"=true \
  -d "inputs[1][type]"=selection \
  -d "inputs[1][selection][choices][0][style]"=primary \
  -d "inputs[1][selection][choices][0][value]"=Email \
  -d "inputs[1][selection][choices][1][style]"=primary \
  -d "inputs[1][selection][choices][1][value]"=Printed \
  -d "inputs[1][selection][choices][2][style]"=secondary \
  -d "inputs[1][selection][choices][2][value]"="No thanks" \
  -d "inputs[1][custom_text][title]"=Receipt \
  --data-urlencode "inputs[1][custom_text][description]"="How would you like your receipt?" \
  -d "inputs[1][required]"=true \
  -d "inputs[2][type]"=email \
  -d "inputs[2][custom_text][title]"="Enter your email" \
  --data-urlencode "inputs[2][custom_text][description]"="We'll send updates on your order and occasional deals" \
  -d "inputs[2][required]"=true \
  -d "inputs[2][toggles][0][title]"="Opt-in for marketing emails" \
  -d "inputs[2][toggles][0][default_value]"=enabled \
  -d "metadata[order_number]"=12345`BetaYou must include the terminal_collect_inputs_beta=v1 header to use the collect_inputs preview feature. The reader object won’t include the collect_inputs object in API responses if you omit the header.

NoteDon’t use collect_inputs to collect sensitive data (including protected health information and customer payment card information), or any information restricted by law.

[Customer interaction](#customer-interaction)When the reader begins collecting inputs, it displays the first input from the list you specified to the customer. The customer must make a selection or provide a signature to proceed with required inputs. However, for optional inputs, the customer has the option to skip to the next requested input.

After the customer has either submitted or skipped all inputs, Stripe updates the reader object and sends out the terminal.reader.action_succeeded webhook.

NoteYou are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

[Receive input data](#receive-input-data)Use the curl command below as an example to create a webhook endpoint to receive the collected inputs.

Command Line`curl https://api.stripe.com/v1/webhook_endpoints \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  --header "Stripe-Version: 2023-10-16; terminal_collect_inputs_beta=v1" \
  --data-urlencode "url"="https://example.com/webhook/endpoint" \
  --data-urlencode "api_version"="2023-10-16;terminal_collect_inputs_beta=v1" \
  --data-urlencode "enabled_events[]"="terminal.reader.action_succeeded" \
  --data-urlencode "enabled_events[]"="terminal.reader.action_failed"`CautionYou must create the webhook endpoint directly with Stripe’s /v1/webhook_endpoints API. The collect_inputs object doesn’t return complete results if you create the webhook endpoint with Stripe CLI or Stripe server-side SDKs. To make sure that the collect_inputs object is present in the webhook payload, include terminal_collect_inputs_beta=v1 in the request header and set the api_version property when you create the webhook endpoint.

You won’t be able to update an existing webhook to start listening to collected inputs, you must create a new one.

When all inputs have been collected or skipped, Stripe sends a request to your webhook endpoint. The request payload is identical to the response when calling collect_inputs, but adds a few additional parameters:

- The`value`parameter is populated for each collected input.  - For signature type inputs, the[value](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-signature-value)is a[file ID](/api/files/object#file_object-id)that[retrieves](/api/files/retrieve)the signature image as an SVG.
  - For selection type inputs, the[value](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-selection-value)is the string of the selected choice’s`value`.
  - For phone, email, text, and numeric inputs, the value is the string of the customer’s response.


- If an optional input is skipped by the customer, the[skipped](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-skipped)parameter is set to`true`.
- The`value`of each toggle is populated with`enabled`or`disabled`.

Subscribe to webhooks to receive collected inputs as soon as they’re available. You can retrieve the reader with the terminal_collect_inputs_beta=v1 request header as a backup if your backend fails to consume the webhook.

Stripe sends two webhooks to notify your backend of the reader’s status:

- `terminal.reader.action_succeeded`: Sent when a`collect_inputs`action succeeds.
- `terminal.reader.action_failed`: Sent when a`collect_inputs`action fails. This includes timeouts, which occur after the reader screen isn’t touched for 2 minutes.

[Download signature images](#download-signature-images)To receive the collected signature image, retrieve the file and use your secret key to access its URL.

NoteStripe stores the signature images you collect for 7 days. If you need to use signature images more than 7 days after collecting them, download the file and store it. You are fully responsible for being aware of and complying with all laws that apply to your use, storage, and disclosure of your customers’ signatures.

## Beta SDK

If you use one of Stripe’s server-side SDKs, you must install a beta version. For installation instructions, refer to the relevant GitHub page for the server SDK you want to use.

You also need to configure your SDK’s API version to include the beta header mentioned above. View language-specific examples of how to accomplish this.

NoteToggles requires reader version 2.21 and up.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Collect inputs](#collect-inputs)[Customer interaction](#customer-interaction)[Receive input data](#receive-input-data)[Download signature images](#download-signature-images)[Beta SDK](#beta-sdk)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
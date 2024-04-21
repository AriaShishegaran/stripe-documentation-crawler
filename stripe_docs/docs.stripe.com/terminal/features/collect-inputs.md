# Collect InputsBeta

Available in: 🌎 for Stripe S700 and BBPOS WisePOS E using server-driven integration, iOS SDK, or Android SDK.

[Stripe S700](/terminal/readers/stripe-reader-s700)

[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)

[server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[iOS SDK](/terminal/payments/setup-integration?terminal-sdk-platform=ios)

[Android SDK](/terminal/payments/setup-integration?terminal-sdk-platform=android)

To request access to the Collect Inputs beta, for server-driven, iOS SDK, or Android SDK, email us at stripe-terminal-betas@stripe.com.

[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com)

[Collect inputs](#collect-inputs)

## Collect inputs

In addition to collecting payments, Terminal smart readers allow you to display forms and collect information from customers. You make requests to the Stripe API, and the API communicates with the reader to display a prebuilt UI to collect customer input. Stripe notifies your backend of the customer’s responses using webhooks.

[webhooks](/webhooks)

To collect inputs using Terminal’s smart readers, use the collect_inputs command. You can specify up to 5 inputs at a time, and the reader collects them in sequence. Stripe smart readers currently support six input types:

[collect_inputs](/api/terminal/readers/collect_inputs)

- The selection input type allows you to display up to 4 choices for a customer to select from.

- The signature input type allows you to collect a signature using the reader’s touchscreen.

- The email input type allows you to collect an email address from a customer.

- The phone input type allows you to collect a phone number from a customer.

- The text input type allows you to collect additional information from customers.

- The numeric input type allows you to collect additional information from customers.

Supported input types.

You can customize the appearance and behavior of all input types:

- Set important inputs as required to make sure they’re collected. For required inputs, the skip button is hidden.

[required](/api/terminal/readers/collect_inputs#collect_inputs-inputs-required)

- Provide context to your customer by specifying the text you want to display on the reader screen for each input using custom_text.

[custom_text](/api/terminal/readers/collect_inputs#collect_inputs-inputs-custom_text)

- Add up to 4 toggles that customers can enable or disable for boolean options, agreements, or opt-ins.

[toggles](/api/terminal/readers/collect_inputs#collect_inputs-inputs-toggles)

Email and selection form with toggle

Additional customization is available for selection inputs. When specifying the choices you want to display to the customer, you can emphasize or de-emphasize choices using the style parameter.

[selection](/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection)

[choices](/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices)

[style](/api/terminal/readers/collect_inputs#collect_inputs-inputs-selection-choices-style)

Primary and secondary selection choice styles

In addition to the list of inputs, you might want to include metadata in your request. The request payload includes the specified metadata, which appears in both the synchronous response and the success or failure webhooks. By including a unique identifier such as a customer ID or order ID, you can more easily identify and handle the incoming webhook.

[metadata](/api/terminal/readers/collect_inputs#collect_inputs-metadata)

You must include the terminal_collect_inputs_beta=v1 header to use the collect_inputs preview feature. The reader object won’t include the collect_inputs object in API responses if you omit the header.

[reader](/api/terminal/readers/object)

[collect_inputs](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs)

Don’t use collect_inputs to collect sensitive data (including protected health information and customer payment card information), or any information restricted by law.

[Customer interaction](#customer-interaction)

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list you specified to the customer. The customer must make a selection or provide a signature to proceed with required inputs. However, for optional inputs, the customer has the option to skip to the next requested input.

After the customer has either submitted or skipped all inputs, Stripe updates the reader object and sends out the terminal.reader.action_succeeded webhook.

You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

[Receive input data](#receive-input-data)

## Receive input data

Use the curl command below as an example to create a webhook endpoint to receive the collected inputs.

[https://example.com/webhook/endpoint](https://example.com/webhook/endpoint)

You must create the webhook endpoint directly with Stripe’s /v1/webhook_endpoints API. The collect_inputs object doesn’t return complete results if you create the webhook endpoint with Stripe CLI or Stripe server-side SDKs. To make sure that the collect_inputs object is present in the webhook payload, include terminal_collect_inputs_beta=v1 in the request header and set the api_version property when you create the webhook endpoint.

[/v1/webhook_endpoints](/api/webhook_endpoints/create)

[collect_inputs object](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs)

[create the webhook endpoint](/api/webhook_endpoints/create)

You won’t be able to update an existing webhook to start listening to collected inputs, you must create a new one.

When all inputs have been collected or skipped, Stripe sends a request to your webhook endpoint. The request payload is identical to the response when calling collect_inputs, but adds a few additional parameters:

[collect_inputs](/api/terminal/readers/collect_inputs)

- The value parameter is populated for each collected input.For signature type inputs, the value is a file ID that retrieves the signature image as an SVG.For selection type inputs, the value is the string of the selected choice’s value.For phone, email, text, and numeric inputs, the value is the string of the customer’s response.

- For signature type inputs, the value is a file ID that retrieves the signature image as an SVG.

[value](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-signature-value)

[file ID](/api/files/object#file_object-id)

[retrieves](/api/files/retrieve)

- For selection type inputs, the value is the string of the selected choice’s value.

[value](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-selection-value)

- For phone, email, text, and numeric inputs, the value is the string of the customer’s response.

- If an optional input is skipped by the customer, the skipped parameter is set to true.

[skipped](/api/terminal/readers/object#terminal_reader_object-action-collect_inputs-inputs-skipped)

- The value of each toggle is populated with enabled or disabled.

Subscribe to webhooks to receive collected inputs as soon as they’re available. You can retrieve the reader with the terminal_collect_inputs_beta=v1 request header as a backup if your backend fails to consume the webhook.

[retrieve the reader](/api/terminal/readers/retrieve)

Stripe sends two webhooks to notify your backend of the reader’s status:

- terminal.reader.action_succeeded: Sent when a collect_inputs action succeeds.

- terminal.reader.action_failed: Sent when a collect_inputs action fails. This includes timeouts, which occur after the reader screen isn’t touched for 2 minutes.

[Download signature images](#download-signature-images)

## Download signature images

To receive the collected signature image, retrieve the file and use your secret key to access its URL.

[retrieve the file](/api/files/retrieve)

[URL](/api/files/object#file_object-url)

Stripe stores the signature images you collect for 7 days. If you need to use signature images more than 7 days after collecting them, download the file and store it. You are fully responsible for being aware of and complying with all laws that apply to your use, storage, and disclosure of your customers’ signatures.

## Beta SDK

If you use one of Stripe’s server-side SDKs, you must install a beta version. For installation instructions, refer to the relevant GitHub page for the server SDK you want to use.

[server-side SDKs](/libraries)

You also need to configure your SDK’s API version to include the beta header mentioned above. View language-specific examples of how to accomplish this.

[language-specific examples of how to accomplish this](/api/versioning)

Toggles requires reader version 2.21 and up.

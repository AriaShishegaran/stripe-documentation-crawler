htmlExpanding responses | Stripe Documentation[Skip to content](#main-content)Expanding responses[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fexpand)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fexpand)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API# Expanding responses

Learn how to reduce the number of requests you make to the Stripe API by expanding objects in responses.This guide describes how to request additional properties from the API. You will learn to modify your requests to include:

- properties from related objects
- properties from distantly related objects
- additional properties on all objects in a list
- properties that aren’t included by default in a response

## How it works

The Stripe API is organized into resources represented by objects with state, configuration, and contextual properties. These objects all have unique IDs that you can use to retrieve, update, and delete them. The API also uses these IDs to link related objects together. A Checkout Session, for example, links to a Customer by the Customer ID.

`{
  "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
  "object": "checkout.session",
  ...
  "customer": "cus_HQmikpKnGHkNwW",
  ...
}`In cases where you need information from a linked object, you can retrieve the linked object in a new call using its ID. However, this approach requires two API requests to access just one value. If you need information from multiple linked objects, each would also require separate requests, which all adds to the latency and complexity of your application.

The API has an Expand feature that allows you to retrieve linked objects in a single call, effectively replacing the object ID with all its properties and values. For example, say you wanted to access details on a customer tied to a given Checkout Session. You would retrieve the Checkout Session and pass the customer property to the expand array, which tells Stripe to include the entire Customer object in the response:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=customer`Which returns the Checkout Session with the full Customer object instead of its ID:

`{
  "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
  "object": "checkout.session",
  ...
  "customer": {
    "id": "cus_HQmikpKnGHkNwW",
    "object": "customer",
    ...
    "metadata": {
      "user_id": "user_xyz"
    },
    ...
  }
}`NoteNot all properties can be expanded. The API reference marks expandable properties with the “Expandable” label.

## Expanding multiple properties

To expand multiple properties in one call, add additional items to the expand array. For example, if you want to expand both the customer and the payment_intent for a given Checkout Session, you would pass expand an array with both the customer and payment_intent strings:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=customer \
  -d "expand[]"=payment_intent`## Expanding multiple levels

If the value you want is nested deeply across multiple linked resources, you can reach it by recursively expanding using dot notation. For instance, if you needed to know the type of payment method that was used for a given Checkout Session, you would first retrieve the Checkout Session’s payment intent, then retrieve the payment intent’s linked payment method to get its type. With expand, you can do this in one call:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"="payment_intent.payment_method"`Which returns the Checkout Session with the full PaymentIntent and PaymentMethod objects instead of their IDs:

`{
  "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
  "object": "checkout.session",
  ...
  "mode": "payment",
  "payment_intent": {
    "id": "pi_1GkXXDLHughnNhxyLlsnvUuY",
    "object": "payment_intent",
    "amount": 100,
    ...
    "charges": {...},
    "client_secret": "pi_1GkXXDLHughnNhxyLlsnvUuY_secret_oLbwpm0ME0ieJ9Aykz2SwKzj5",
    ...
    "payment_method": {
      "id": "pm_1GkXXuLHughnNhxy8xpAdGtf",
      "object": "payment_method",
      "billing_details": {...},
      "card": {...},`See all 49 linesNoteExpansions have a maximum depth of four levels. Meaning that an expand string can contain no more than four properties: property1.property2.property3.property4.

## Expanding properties in lists

When the API returns a list of objects, you can use the data keyword to expand a given property on each object in that list. For example, say you need information about the payment methods used by one of your customers. To get this information, you would list the customer’s PaymentIntents, which returns an object with the following structure:

`{
  "object": "list",
  "data": [
    {
      "id": "pi_1GrvBKLHughnNhxy6N28q8gt",
      "object": "payment_intent",
      "amount": 1000,
      ...
      "payment_method": "pm_1GrvBxLHughnNhxyJjtBtHcc",
      ...
    },`See all 23 linesNoteAll lists returned in the API have the above structure, where the data property contains the array of objects being listed. You can use the data keyword in any position in an expand string to move the expand cursor into the list.

Rather than looping through each payment intent in the list and retrieving the linked payment methods in separate calls, you can expand all the payment methods at once using the data keyword:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "expand[]"="data.payment_method"`The list then includes the full payment method object on each payment intent:

`{
  "object": "list",
  "data": [
    {
      "id": "pi_1GrvBKLHughnNhxy6N28q8gt",
      "object": "payment_intent",
      "amount": 1000,
      ...
      "payment_method": {
        "id": "pm_1GrvBxLHughnNhxyJjtBtHcc",
        "object": "payment_method",
        "billing_details": {...},
        "card": {
          "brand": "visa",
          ...`See all 65 linesNoteExpanding responses has performance implications. To keep requests fast, try to limit many nested expansions on list requests.

## Using expansion to request includable properties

In some cases, resources have properties that aren’t included by default. One example is the Checkout Session’s line_items property, which is only included in responses if requested using the expand parameter, for example:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=line_items`NoteLike other expandable properties, the API reference marks properties that are includable with the “Expandable” label.

## Using expansion with webhooks

You can’t receive webhook events with properties auto-expanded. Objects sent in events are always in their minimal form. To access nested values in expandable properties, you must retrieve the object in a separate call within your webhook handler.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How it works](#how-it-works)[Expanding multiple properties](#multiple-properties)[Expanding multiple levels](#multiple-levels)[Expanding properties in lists](#lists)[Using expansion to request includable properties](#includable-properties)[Using expansion with webhooks](#with-webhooks)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
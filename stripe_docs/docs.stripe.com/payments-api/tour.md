# Tour of the API

The Stripe APIs are powerful and flexible if you know how to use them. This tour of the API covers key information to help you understand the APIs more deeply:

- The core concepts we use across the APIs

- The path a successful payment takes

- The objects that play a role and how to determine when they’re needed

- Common patterns and best practices for using those objects together

Understanding these patterns helps you move beyond the pre-written code in Stripe tutorials. You can migrate old integrations to use more modern patterns, combine simple patterns in novel ways, and plan for future growth.

[Core concepts](#undefined)

## Core concepts

Everything in your Stripe account is an object, whether you create it with the API or not. Your balance corresponds to a Balance object, you track customers with Customer objects, you store payment details in PaymentMethod objects, and so on.

[Balance](/api/balance)

[Customer](/api/customers)

[PaymentMethod](/api/payment_methods)

Even low-code and no-code integrations produce these objects. So do actions you perform in the Dashboard. For instance, when you manually create a customer in the Dashboard, it still creates a Customer object.

Stripe integrations handle complicated processes.

The API uses a single object to track each process. You create the object at the start of the process, and after every step you can check its status to see what needs to happen next—This is sometimes referred to as a state machine.

For instance, while completing a payment, a customer might try several payment methods. If one payment method fails, a status of requires_payment_method lets you know to prompt the customer for another.

To accept a payment, a system needs to create several core objects and manage them through several states.

Your Stripe integration is a system that handles this creation and management by communicating with Stripe.

Some integrations do a lot more than that: track customers, manage subscriptions, etc. But their core payment functionality still comes from the same objects and steps, with more objects added around that core.

[Payment objects](#payment-objects)

## Payment objects

Stripe uses a variety of related objects to facilitate payments. Before you can build an integration that suits your specific needs, you must familiarize yourself with how these objects work together.

Check out this video for an overview of payment object roles and capabilities.

To learn more about Stripe’s payment integration options, see the following guides:

- Payment Links

[Payment Links](/payment-links)

- Checkout

[Checkout](/payments/checkout)

- Subscriptions

[Subscriptions](/billing)

- Invoicing

[Invoicing](/invoicing)

- Payment Intents

[Payment Intents](/payments/payment-intents)

[The path to a payment](#path-to-a-payment)

## The path to a payment

In a modern Stripe integration, every payment uses an object called a PaymentIntent. As its name suggests, it represents your intent to collect a payment. This object tracks the steps you go through along the way to fulfilling that intent.

[PaymentIntent](/api/payment_intents)

For instance, suppose a customer clicks a Check out button with a 100 USD item in their cart. They haven’t bought it yet, and they might never buy it (maybe at some point they abandon the payment flow, or their card issuer declines the payment). But clicking Check out indicates their intent to buy—and you intend to help them. At that point, an integration creates a PaymentIntent object in the amount of 100 USD to track the rest of the process.

The PaymentIntent’s path to success goes through several statuses—here’s a simplified version:

[several statuses](/payments/paymentintents/lifecycle)

A PaymentIntent starts with the status requires_payment_method. To move it forward, Stripe needs details about the customer’s payment method—either a card number or credentials for some other payment system.

An integration represents these details using an API object called a PaymentMethod. In some integrations, you write the code that creates that object and attaches it to the PaymentIntent. In others, Stripe gathers the details and does the work for you. You can also create and save a payment method for use with future PaymentIntents using the Setup Intents API.

[PaymentMethod](/api/payment_methods)

[using the Setup Intents API](/payments/setup-intents)

The next status is requires_confirmation. In an interactive payment flow, the customer must confirm that they intend to pay—and that they intend to do it using the method they provided. In a one-time online payment, this usually happens when they click the Pay button.

When the customer clicks Pay or otherwise confirms their intent, an integration notifies Stripe with an API call. In some integrations, you write the code that makes this call. Stripe provides drop-in UI elements, called Stripe Elements, to enable this while still providing flexibility to build a custom integration. In other integrations, like a Stripe Checkout or Payment Links integration, Stripe makes the call and handles the next steps. There are many ways to integrate Stripe and combine different objects to handle your use case. Learn more about integration options for online payments.

[Stripe Elements](/payments/elements)

[Stripe Checkout](/payments/checkout)

[Payment Links](/payment-links)

[Learn more about integration options for online payments.](/payments/online-payments)

In most cases a Charge will be created when a PaymentIntent is confirmed to represent that specific attempt to move money. The Charge might succeed or fail. If it fails the payment can be retried by confirming the PaymentIntent again, usually with new payment details. Allowing retries immediately, without the need to create a new PaymentIntent, tends to increase conversion rates.

[Charge](/api/charges)

The intent’s state is now processing, and at this point Stripe attempts to process the payment.

Stripe always does this part for you—and it can have several steps. (For credit cards, these steps are part of how cards work.) As we work through the steps, we update the intent’s state with the outcome: either succeeded or back to requires_payment_method if it fails.

[how cards work](/payments/cards/overview)

When we’re done, one last object comes into play: the Event. We use Event objects to represent activity. In this case, the activity might be “the charge succeeded” or “the charge failed.” In some integrations, you write custom code to respond to events using webhooks. In others, such as Checkout or Payment Links integrations, Stripe listens for the event and provides a pre-written response.

[Event](/api/events)

[webhooks](/webhooks)

[Checkout](/payments/checkout)

[Payment Links](/payment-links)

# Display Affirm messagingDeprecated

The content in this topic refers to a Legacy feature. We recommend that you use the Payment Method Messaging Element to dynamically show your customers relevant buy now, pay later payment options for a given purchase. Stripe continues to maintain continuity for the affirmMessage Element, but has halted new feature development.

[Payment Method Messaging Element](/payments/payment-method-messaging)

Let your customers know you accept payments with Affirm by including the Affirm messaging Element on your site. We suggest adding the messaging Element to your product, cart, and payment pages. The Affirm messaging Element takes care of:

- Calculating and displaying the installments amount

- Displaying the Affirm information modal

## Include the Element

Affirm’s minimum transaction amount is 50 USD or 50 CAD. The promotional message isn’t rendered if the amount parameter is set to a number less than 50 USD or 50 CAD.

Use Stripe Elements to include the affirmMessage Element on your site.

[affirmMessage](/js/elements_object/create_element?type=affirmMessage)

If you haven’t already, include the Stripe.js script on your page by adding it to the head of your HTML file:

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create a placeholder element on your page where you want to mount the messaging Element:

On your product, cart, and payment pages, include the following code to create an instance of Stripe.js and mount the messaging Element:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

## Customize the message

There are many options available to customize the appearance and contents of the messaging Element. See the API reference for the full list of options.

[API reference](/js/elements_object/create_element?type=affirmMessage)

Use the logoColor option to choose between the following styles:

Additional configuration options allow you to use CSS to style the messaging to better fit the look and feel of your site. You can customize the fontColor, fontSize, and textAlign of the messaging:

# Display Afterpay or Clearpay messagingDeprecated

The content in this topic refers to a Legacy feature. We recommend that you use the Payment Method Messaging Element to dynamically show your customers relevant buy now, pay later payment options for a given purchase. Stripe continues to maintain continuity for the afterpayClearpayMessage Element, but has halted new feature development.

[Payment Method Messaging Element](/payments/payment-method-messaging)

Let your customers know you accept payments with Afterpay by including the Afterpay messaging Element on your site. We suggest adding the messaging Element to your product, cart, and payment pages. The afterpayClearpayMessage Element takes care of:

[afterpayClearpayMessage](/js/elements_object/create_element?type=afterpayClearpayMessage)

- Calculating and displaying the installments amount

- Displaying the Afterpay information modal

- Localizing text and currencies

## Include the Element

Use Stripe Elements to include the afterpayClearpayMessage Element on your site.

[afterpayClearpayMessage](/js/elements_object/create_element?type=afterpayClearpayMessage)

If you haven’t already, include the Stripe.js script on your page by adding it to the head of your HTML file:

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create a placeholder element on your page where you want to mount the messaging Element:

On your product, cart, and payment pages, include the following code to create an instance of Stripe.js and mount the messaging Element:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

## Customize the message

There are many options available to customize the appearance and contents of the messaging Element. See the API reference for the full list of options.

[API reference](/js/elements_object/create_element?type=afterpayClearpayMessage)

Set logoType to 'badge' and use the badgeTheme option to choose between the following styles:

Set logoType to 'lockup' and use the lockupTheme option to choose between the following styles:

Clearpay branding is displayed automatically based on the locale option. See Locale and currency for details.

[Locale and currency](#locale-and-currency)

In addition to the configuration options, use CSS to style the messaging to better fit the look and feel of your site. You can customize the font-family, font-size, and color of the messaging:

You can also control the size of the logo by setting its width and height:

## Handle ineligible items

You can’t use Afterpay for certain prohibited business categories. If you sell items in these categories, you can still display the messaging Element to clearly indicate Afterpay isn’t available.

[prohibited business categories](/payments/afterpay-clearpay#prohibited-business-categories)

Use the isEligible or isCartEligible options to indicate that the current product or cart isn’t eligible:

Afterpay also has default transactions limits for each country. When the provided amount exceeds these limits, the Element automatically displays ineligible price range messaging. You can customize this message by hiding the lower or upper limit with showLowerLimit and showUpperLimit.

[default transactions limits](/payments/afterpay-clearpay#collection-schedule)

## Locale and currency

Afterpay and clearpay support the following locales and currencies:

Supported locales: en-US, en-CA, en-AU, en-NZ, en-GB

Supported currencies: USD, CAD, AUD, NZD, GBP

Afterpay’s messaging always the appropriate number of installments a user can pay based on their locale and country. For more information, see payment collection.

[payment collection](/payments/afterpay-clearpay#collection-schedule)

Set the locale of your message by passing the locale option into the options parameter of the elements group used to create the afterpayClearpayMessage Element. You can then define your currency by passing it to the element.create options directly.

[elements group](/js/elements_object/create)

[element.create](/js/elements_object/create_element?type=afterpayClearpayMessage)

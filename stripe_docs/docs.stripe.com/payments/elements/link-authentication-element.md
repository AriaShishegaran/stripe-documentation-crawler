# Link Authentication Element

Link saves and autofills customer payment and shipping information. Customers can use different funding sources to pay with Link, including credit cards, debit cards, and US bank accounts. Learn more at link.com.

[Link](https://stripe.com/payments/link)

[link.com](https://www.link.com)

Use the Link Authentication Element to create a single email input field for both email collection and Link authentication.

[Link Authentication Element](/js/element/link_authentication_element)

## Start with examples

To see the Link Authentication Element in action, start with one of these examples:

[QuickstartCode and instructions for accepting a payment and using the Link Authentication Element to integrate Link.](/payments/quickstart)

Code and instructions for accepting a payment and using the Link Authentication Element to integrate Link.

[Clone a sample app on GitHubHTML · React · Vue](https://github.com/stripe-samples/accept-a-payment)

## Before you begin

Before you start, you need to register your domain.

[register your domain](/payments/payment-methods/pmd-registration)

## Create the Link Authentication Element

The following code creates an instance of the Link Authentication Element and mounts it to the DOM:

[creates](/js/elements_object/create_link_authentication_element)

[mounts](/js/element/mount)

## Retrieving email address

You can retrieve the email address details using the onChange prop on the linkAuthenticationElement component. The onChange handler fires whenever the user updates the email field, or when a saved customer email is autofilled.

## Prefill customer data

The Link Authentication Element accepts an email address. Providing a customer’s email address starts the Link authentication flow as soon as the customer lands on the payment page using the defaultValues option:

[defaultValues](/js/elements_object/create_link_authentication_element#link_authentication_element_create-options-defaultValues)

If you want to prefill additional customer data, add the defaultValues.billingDetails object to the Payment Element. This prefills a customer’s name, phone number, and shipping addresses. By prefilling as much of your customer’s information as possible, you simplify Link account creation and reuse.

[defaultValues.billingDetails](/js/elements_object/create_payment_element#payment_element_create-options-defaultValues-billingDetails)

[Payment Element](/payments/payment-element)

The following code shows a Payment Element with all of its values prefilled:

## Combine Elements

The Link Authentication Element interoperates with other elements. For instance, the following example uses the Link Authentication Element with the Address Element and Payment Element:

Use the Link Authentication Element with other Elements to compose your checkout page

## Appearance

You can use the Appearance API to control the style of all elements. Choose a theme or update specific details.

[Appearance API](/elements/appearance-api)

Use the Appearance API to change the look and style of your Elements

In the following example, the “flat” theme overrides the default text color used for Elements:

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

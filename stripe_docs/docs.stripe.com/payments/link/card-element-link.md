# Link in the Card Element

Stripe no longer recommends using the Card Element as part of your Web Elements integration. To integrate Link, use one of our preferred Elements: the Link Authentication Element, Express Checkout Element, or Payment Element.

Use Link in the Card Element to save and autofill payment information for your customers, so they don’t need to enter their payment details manually.

[Link](/payments/link/what-is-link)

The Card Element can take on two forms: a single line Card Element or split Elements (like Card Number, Expiry, and CVC). When referring to the Card Element, the following information applies to both forms.

[Card Element](/js/element/other_element?type=card)

[Card Number](/js/element/other_element?type=cardNumber)

[Expiry](/js/element/other_element?type=cardExpiry)

[CVC](/js/element/other_element?type=cardCvc)

## The Link flow

When Link is enabled, the card input form displays a Link button, which an authenticated customer can click to autofill their payment details. They only need to authenticate their account once every 90 days on any Link-enabled business.

Link autofilling customer payment details

If a customer hasn’t signed up for Link and they click the Link button, they’re asked to add their email address, phone number, and payment method. A customer can also enter their card details into the Card Element first, and save that card in a Link account.

A customer signing up for Link

If a returning Link customer clicks the Link button and needs to authenticate, Link asks them to do it with an SMS or email code. After the customer authenticates, Link loads their previously saved payment details, allowing them to check out faster.

Link authenticating a customer

We’re continuously optimizing Link to improve checkout conversion, and may selectively show Link when it’s most beneficial to customers at checkout. You can expect to see changes over time, including how and when Link appears.

## Link enablement

Link is supported in the Card Element globally for all businesses with granted access and doesn’t require additional fees or code changes (see note below for details). Link is fully compatible with the other features you receive from card payments.

[Card Element](/js/element/other_element?type=card)

Stripe automatically enables Link in the Card Element. If you want to turn Link off for all instances of the Card Element, visit the Link section of your payment Method settings and disable the Link in Card Element setting. This setting applies to both forms of the Card Element. To selectively disable Link in the Card Element, use the disableLink parameter. You only need to use one of these controls—if either disableLink is true or Link in the Card Element is disabled in settings, Link won’t appear in the Card Element.

[payment Method settings](https://dashboard.stripe.com/settings/payment_methods)

[disableLink](/js/elements_object/create_element?type=card#elements_create-options-disableLink)

Link isn’t visible in the Card Element if:

- The parent container that the Card Element is mounted in is too short in height or narrow in width to display the Link button.

The parent container that the Card Element is mounted in is too short in height or narrow in width to display the Link button.

- The Card Element is displayed on a browser that doesn’t support pop-ups, including in-app browsers. View information about supported browsers.

The Card Element is displayed on a browser that doesn’t support pop-ups, including in-app browsers. View information about supported browsers.

[supported browsers](#test-link-in-the-card-element)

- The Cross-Origin-Opener-Policy is set to same-origin. The Link pop-up must communicate with the page that opened it, so Link in the Card Element isn’t compatible with configurations that block this communication.

The Cross-Origin-Opener-Policy is set to same-origin. The Link pop-up must communicate with the page that opened it, so Link in the Card Element isn’t compatible with configurations that block this communication.

[Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)

We’re releasing Link in the Card Element in phases. Link for the single line Card Element was released in 2023, followed by Link in split Elements in late 2023 and early 2024. Only accounts with granted access can see Link in the Card Element in their Payment Method settings or use Link in production or test mode. Link isn’t currently supported for Stripe accounts based in India.

[single line Card Element](/js/element/other_element?type=card)

[split Elements](/js/element/other_element?type=cardNumber)

[Payment Method settings](https://dashboard.stripe.com/settings/link)

## Use the Card Element and Payment Request Button

You can also use Link with the Payment Request Button. Link in the Card Element operates independently from Link in the Payment Request button. If you use both the Payment Request Button and the Card Element, Link might appear in both during checkout. For more information on when Link appears in the Payment Request Button, see Link in the Payment Request Button.

[Payment Request Button](/payments/link/payment-request-button-link)

[Link in the Payment Request Button](/payments/link/payment-request-button-link)

## Link and Connect platforms

Link is automatically available to any accounts that access the Card Element through a Connect platform integration. Depending on a platform’s integration, a platform may be able to give its users (connected accounts) the ability to customize their own Link settings in the Dashboard:

[connected accounts](/connect/enable-payment-acceptance-guide?platform=web#create-account)

If the following conditions are all met by your platform, then your connected accounts can manage their Link settings directly in their own Dashboard.

- You use direct charges.

You use direct charges.

[direct charges](/connect/direct-charges)

- You create and charge payment methods on your connected accounts.

You create and charge payment methods on your connected accounts.

- Your connected accounts have access to the full Stripe Dashboard.

Your connected accounts have access to the full Stripe Dashboard.

To set the default state for all connected accounts on your platform:

- Click Edit settings under Your connected accounts in Payment Method settings.

Click Edit settings under Your connected accounts in Payment Method settings.

[Payment Method settings](https://dashboard.stripe.com/settings/connect/payment_methods)

- Navigate to Link in the Card Element in the Link section.

Navigate to Link in the Card Element in the Link section.

In the following cases, Link is controlled by your platform account settings, and your connected accounts can’t customize their Link settings for payments processed through your platform:

- You create payment methods on your platform and then clone payment methods to your connected accounts.

You create payment methods on your platform and then clone payment methods to your connected accounts.

[clone payment methods](/payments/payment-methods/connect#cloning-payment-methods)

- You use destination charges or separate charges and transfers.

You use destination charges or separate charges and transfers.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- Your connected accounts don’t have access to the full Stripe Dashboard.

Your connected accounts don’t have access to the full Stripe Dashboard.

To manage your platform account settings:

- Click Edit settings under Your Account in Payment Method settings.

Click Edit settings under Your Account in Payment Method settings.

[Payment Method settings](https://dashboard.stripe.com/settings/connect/payment_methods)

- Navigate to Link in the Card Element in the Link section. If you want to turn Link off for only specific connected accounts, you can use the disableLink parameter.

Navigate to Link in the Card Element in the Link section. If you want to turn Link off for only specific connected accounts, you can use the disableLink parameter.

[disableLink](/js/elements_object/create_element?type=card#elements_create-options-disableLink)

- If your platform offers you the ability to customize your Link settings for platform payments, then you can manage your Link in Card Element settings within Payment Method settings by selecting your platform from the dropdown menu at the top of the page.

If your platform offers you the ability to customize your Link settings for platform payments, then you can manage your Link in Card Element settings within Payment Method settings by selecting your platform from the dropdown menu at the top of the page.

[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods)

- If your platform isn’t able to offer you settings customization, then the platform determines Link’s availability for all payments processed through the platform, and you won’t have settings control for platform payments in your Dashboard.

If your platform isn’t able to offer you settings customization, then the platform determines Link’s availability for all payments processed through the platform, and you won’t have settings control for platform payments in your Dashboard.

- For payments you process without a platform, you can manage Link in your Payment Method settings by selecting “no platform” from the dropdown menu at the top of the page.

For payments you process without a platform, you can manage Link in your Payment Method settings by selecting “no platform” from the dropdown menu at the top of the page.

[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods)

## Test Link in the Card Element

Don’t store real user data in test mode Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.

[test mode](/test-mode)

Link works with the following browsers:

- Chrome, Chrome Mobile, and Microsoft Edge.

Chrome, Chrome Mobile, and Microsoft Edge.

- Safari on desktop and iOS (last 3 major versions).

Safari on desktop and iOS (last 3 major versions).

Link is available in both production and test mode. You can create test mode Link accounts using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating Link test mode accounts:

Enabling Link in test mode presents Link on all Card Element test mode sessions that meet the enablement requirements. In production, Link’s visibility might vary to maximize Link’s conversion benefits in each checkout session.

[enablement requirements](#enable-link)

## See also

- Stripe Web Elements

[Stripe Web Elements](/payments/elements)

- Link Authentication Element

[Link Authentication Element](/payments/elements/link-authentication-element)

- Payment Element

[Payment Element](/payments/payment-element)

# Deep links in the customer portal

With the customer portal, you can provide subscription and payment method management to your customers without building it yourself. If you want to streamline customer actions and further customize workflows between your own app and Stripe, you can create a customer portal flow.

[customer portal](/customer-management)

[flow](/api/customer_portal/session#portal_session_object-flow)

## Customer portal flows

A flow is a customizable deep link into the customer portal. Portal flows allow you to:

- Deep link directly to the page with the specified action for your customer to complete. Navigational components to access the rest of the customer portal are hidden so the customer can focus on the single action.

- Customize the redirect behavior after the customer completes the action—redirect them immediately to your own URL, to a hosted confirmation page, or back to the portal homepage.

- Personalize the flow with unique options like prefilled promotion codes or custom messages.

A flow’s type defines what single flow or action your customer will complete. Below are the currently available flow types:

[type](/api/customer_portal/sessions/create#create_portal_session-flow_data-type)

Payment method update flow

subscription_cancel

Use subscription_cancel to let your customer cancel a specific subscription.

You can customize whether the subscription cancels immediately or at the end of the period by updating your portal configuration through the API or the Dashboard.

[API](/api/customer_portal/configuration#portal_configuration_object-features-subscription_cancel-mode)

[Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)

Subscription cancel flow

subscription_update

Use subscription_update to let your customer select different update options such as upgrading or downgrading to another plan or updating the current plan quantity.

You can customize the available plans by updating your portal configuration through the API or the Dashboard.

[API](/api/customer_portal/configuration#portal_configuration_object-features-subscription_cancel-mode)

[Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)

Subscription update flow

subscription_update_confirm

Use subscription_update_confirm to let your customer confirm a specific update to their subscription.

You can use this option when you have your own pricing page but want to offload the work of displaying update details such as upcoming invoice and prorations, handling payment failures, or handling 3D Secure authentication.

[3D Secure authentication](/payments/3d-secure)

You can also specify a coupon or promotion code to apply on the subscription update. You could use this for promotional campaigns when you offer a discount for switching to another plan.

Subscription update confirm flow

[Create a flow](#create-a-flow)

## Create a flow

Customer portal flows are an extension to the customer portal API. First follow the general guide to integrate the customer portal with the API before using this guide.

[customer portal API](/api/customer_portal/sessions/create)

[integrate the customer portal with the API](/customer-management/integrate-customer-portal)

To create a flow, specify flow_data when you create a portal session.

[flow_data](/api/customer_portal/sessions/create#create_portal_session-flow_data)

Set the type of flow you want your customer to complete. Depending on the flow type, you might need to pass in additional data such as a subscription ID.

[type](/api/customer_portal/sessions/create#create_portal_session-flow_data-type)

Below are examples on how to set up each flow type.

[https://example.com/account/overview](https://example.com/account/overview)

The portal session url for the response now deep links into the flow you created. Use that URL to redirect customers to the portal flow from your site.

[Customize after completion behavior](#customize-after-completion)

## Customize after completion behavior

After your customer successfully completes the flow, they see a localized confirmation page that shows the details of their completed update. You can customize the confirmation message on this page, redirect to a URL of your choice, or redirect them back to the customer portal homepage where their full account details are visible.

To customize this behavior, set after_completion on flow_data.

[after_completion](/api/customer_portal/sessions/create#create_portal_session-flow_data-after_completion)

The following example lets your customer cancel their subscription, and redirect back to your own site afterwards:

[https://example.com/account/overview](https://example.com/account/overview)

[https://example.com/account/subscription_canceled](https://example.com/account/subscription_canceled)

The top level return_url is a link back to your website that the customer can click at any time (if they decide not to cancel, for example). The flow_data[after_completion][redirect][return_url] is a link back to your website after a customer successfully cancels their subscription.

# Viewports reference

A viewport specifies the page in the Dashboard where your view can appear. A viewport can provide an environment.objectContext object that allows you to receive context on a current page’s Stripe object. For more information, see Access Stripe objects in the Dashboard.

[Access Stripe objects in the Dashboard](/stripe-apps/build-ui#access-stripe-objects)

Available viewports for your UI extension:

[Dashboard-wide availability](#dashboard-wide-availability)

[add an app settings page](/stripe-apps/app-settings)

## Application availability

You can make your application available across all pages or specific to a single page in the Dashboard.

If your app specifies a view for the stripe.dashboard.drawer.default viewport, this view appears on every page in the Dashboard except for where you have defined page-specific views.

For example, if the ui_extension.views field in your app’s stripe-app.json manifest is as follows:

“CustomerView” would appear when the application is open on the Customer details page, and “EverywhereElseView” would appear on every other page in the Dashboard.

The stripe.dashboard.drawer.default view doesn’t receive objectContext data the way that a page-specific view does. If your app needs to access information like the id of an invoice shown on an “Invoice details” page, you need to create a view that uses the stripe.dashboard.invoice.detail viewport. For more information, see Page-specific availability.

[Page-specific availability](/stripe-apps/reference/viewports#page-specific-availability)

Page-specific views relate to the current page the user is viewing, and allow apps to receive additional context about the page through the environment property. For more information, see Access Stripe objects in the Dashboard.

[Access Stripe objects in the Dashboard](/stripe-apps/build-ui#access-stripe-objects)

For example, if your app has a view for the stripe.dashboard.product.detail viewport, when a user opens your app on the Product details page, that view appears in the app.

If your app doesn’t have either a page-specific view for the current page or an app-specific default view, the drawer displays a generic default view that shows the user how to access the app.

For example, if your app has two views on page-specific viewports, shown in the app manifest below:

When the end user opens your app on the Dashboard homepage, the application displays links to the Customers and Products pages. If the user then navigates to the Customers page, the app displays a message prompting them to select a customer to see related information in your app.

## See also

- Design your app

[Design your app](/stripe-apps/design)

- How UI extensions work

[How UI extensions work](/stripe-apps/how-ui-extensions-work)

- Permissions reference

[Permissions reference](/stripe-apps/reference/permissions)

- UI extension SDK reference

[UI extension SDK reference](/stripe-apps/reference/extensions-sdk-api)

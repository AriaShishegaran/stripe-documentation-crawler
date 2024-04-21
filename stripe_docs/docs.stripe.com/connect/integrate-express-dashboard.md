# Integrate the Express Dashboard

The Express Dashboard allows users (connected accounts) to view their available balance, see upcoming payouts, and track their earnings in real time. In this guide, you’ll learn how to redirect users to the Express Dashboard from your platform.

[payouts](/payouts)

Users can log into the Express Dashboard by clicking a link on the user interface of your website or mobile application. After they click the link, Stripe redirects your users to the Express Dashboard login page. On the login page, users must verify their identity through SMS authentication to view and manage their Express Dashboard.

Your onboarded users can also access the Express Dashboard by signing in to Stripe Express. However, we recommend providing users a link to the Express Dashboard from your platform.

[signing in to Stripe Express](/connect/express-dashboard#self-serve-access)

[Create a login link](#create-login-link)

## Create a login link

Use the Login Link API to generate a single-use URL. This URL takes users to the Express Dashboard login page.

[Login Link](/api/account/create_login_link)

When the request successfully completes, the response includes a generated login URL:

Typically, you’ll use the API to generate the URL on demand (when a user intends to visit the Express Dashboard). If users click a call to action on your application, your application creates a URL using the Login Link API and redirects them to the Express Dashboard with the URL returned by the API.

[Login Link](/api/account/create_login_link)

Don’t email, text, or otherwise send login link URLs directly to your user. Instead, redirect the authenticated user to the login link URL from within your platform’s application.

On the login page, users must enter an SMS authentication code (automatically sent from Stripe) to view their Express Dashboard. Stripe uses SMS authentication to verify a user’s identity and grant access to their Express Dashboard.

If a user no longer has access to the original phone number your platform used to create their Express Account, they can change their phone number by clicking “I no longer have access to this phone number”. Then, the user can retrieve a verification code sent to their Express Account email. The user must submit this code to add a new mobile number. Stripe redirects the user back to the login page and sends an SMS authentication code to the new number.

## See also

- Customize the Express Dashboard

[Customize the Express Dashboard](/connect/customize-express-dashboard)

- Collect payments and then pay out (if you process payments with Stripe)

[Collect payments and then pay out](/connect/collect-then-transfer-guide)

- Pay out money (if you add money from a bank account to pay out)

[Pay out money](/connect/add-and-pay-out-guide)

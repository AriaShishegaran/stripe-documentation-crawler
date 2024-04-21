# Test mode

Stripe’s test mode allows you to test your integration without making actual charges or payments. Test mode is a testing environment that simulates creating real objects without the risk of affecting real transactions or moving actual money.

In test mode, you can charge test credit cards as well as create test products and prices. You can also use test mode to simulate transactions to make sure that your integration works correctly. This feature helps to identify any bugs or errors in your Stripe implementation before you go live with actual payments.

After you create a Stripe account, you can find a set of test API keys in the Stripe Dashboard. You can use these API keys to create and retrieve simulated data by making requests to the Stripe API. To start accepting real payments, you need to activate your account, toggle off test mode, and use the live API keys in your integration.

[test API keys](/keys#obtain-api-keys)

[Stripe Dashboard](https://dashboard.stripe.com/test/apikeys)

[activate your account](/get-started/account/activate)

In the Dashboard, changing settings in test mode might also change them in live mode. Many Dashboard pages have a white notification box and disable live mode settings while in test mode. In this case, any settings still enabled are safe to use. If there’s no white callout, assume any changes made in test mode affect live mode settings (unless you see an orange test data banner).

## Test mode versus live mode

All Stripe API requests occur in either test mode or live mode. API objects in one mode aren’t accessible to the other. For instance, a test-mode product object can’t be part of a live-mode payment.

[product object](/api/products/object)

[test credit cards and accounts](/testing#cards)

[Identity](/identity)

[account objects](/api/accounts/object)

[testing process](/testing#disputes)

[payment methods](/payments/payment-methods)

The Test mode toggle in the Dashboard doesn’t affect your integration code. Your test and live mode API keys affect the behavior of your code.

## Test card numbers

Stripe provides a set of test card numbers that you can use to simulate various payment scenarios. You can use these test card numbers to create simulated payments in test mode without processing actual payments or charges.

[test card numbers](/testing#cards)

When you use test card numbers, you can enter any expiration date in the future and any three-digit CVC code to simulate a successful payment. If you want to simulate a failed payment, you can use specific test card numbers and CVC codes provided by Stripe.

Test card numbers are only valid in test mode. Don’t use them for real payments.

## Delete test data

To delete all of your test data from your Stripe account, complete the following steps:

- Log in to the Dashboard using your existing Stripe account.

[Log in to the Dashboard](https://dashboard.stripe.com/)

- While in test mode, click Developers and scroll down to the bottom of the Overview tab.

- Click Delete all test data… The ensuing dialog gives you a list of all of your existing test data objects.

- Click Start deletion to initiate the deletion process. You can’t undo the deletion of your test data.

Test mode is temporarily unusable while the deletion process occurs.

## Test email

By default, Stripe won’t send an email to customers in test mode. If you want to verify emails for invoices and receipts, you can set the email address for your Team on the Customer object or receipt_email attribute on the PaymentIntent.

[Team](https://dashboard.stripe.com/settings/team)

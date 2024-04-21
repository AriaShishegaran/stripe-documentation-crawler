# Register domains for payment methods

To use certain payment methods with Elements or Checkout’s embeddable payment form, you must register every web domain that will show the payment method. This includes registering top-level domains and subdomains. For example, if you have the domain stripe.com and subdomains like shop.stripe.com and www.stripe.com, this guide explains how to register them.

[Elements](/payments/elements)

[Checkout’s embeddable payment form](/payments/checkout/how-checkout-works?payment-ui=embedded-form)

After you register a domain, that registration applies to additional payment methods that you might add in the future.

The following payment methods require registration:

- Google Pay

- Link

- PayPal

- Apple Pay (additional verification step required)

The Apple Pay documentation describes their process of “merchant validation," which Stripe handles for you behind the scenes. You don’t need to create an Apple Merchant ID or CSR. Instead, follow the steps in this guide.

## Testing

You also need to register domains for testing. When testing locally, you can use a tool such as ngrok to get an HTTPS domain. You can either register in test mode, or register in live mode and the domain will also be registered in test mode automatically. Remember to register your domains in live mode before going live.

[ngrok](https://ngrok.com/)

You can create and manage domains in the Dashboard on the Payment method domains page for use in production and testing.

[Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains)

Connect platforms that create direct charges must use the API to manage domains for their connected accounts, not the Stripe Dashboard.

[connected accounts](#register-a-domain-using-connect)

## Register your domain

To register a domain:

- On the Payment method domains page, click Add a new domain.

[Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains)

- Enter your domain name.

- Click Save and continue.

- (Optional) To finish setting up Apple Pay, follow the steps to verify your domain.

[verify your domain](#verify-your-domain-with-apple-pay)

- (Optional) Repeat steps 1-4 for additional domains that you need to register.

After completing these steps, your domain shows up on the Payment method domains page.

## Verify your domain with Apple Pay

During registration, Stripe automatically attempts to verify your domain with Apple Pay. If the domain isn’t already verified, register your domain and then follow these steps to verify your registered domain with Apple Pay.

- Download the domain association file.

[domain association file](https://stripe.com/files/apple-pay/apple-developer-merchantid-domain-association)

- Host the file at /.well-known/apple-developer-merchantid-domain-association. For example, if you register https://example.com, make that file available at https://example.com/.well-known/apple-developer-merchantid-domain-association.

- Click Verify.

When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying allow=“payment” attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

## Manage your domain

You can see a list of all of your domains in the Dashboard.

To disable a domain, click the row action and then click Disable. If a domain is disabled, the payment methods no longer appear in Elements on that domain.

To enable a disabled domain, click the row action and then click Enable.

## Register your domain while using Connect

Connect platforms must register all domains where the Elements display the payment methods listed above. The domain where the charge is being run needs to be registered for the user running the charge.

If the platform creates direct charges, use your platform’s secret key to authenticate the request and set the Stripe-Account header to your connected account’s Stripe ID.

[direct charges](/connect/direct-charges)

If the platform creates destination charges or separate charges and transfers, use your platform’s secret key to authenticate the request and omit the Stripe-Account header.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

Learn more about Making API calls for connected accounts.

[Making API calls for connected accounts](/connect/authentication)

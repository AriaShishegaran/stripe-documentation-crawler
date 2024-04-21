# Domains and IP addresses

You can subscribe to the API announce mailing list to be notified of any changes to our IP addresses. We provide seven days’ notice through that mailing list before making changes.

[API announce mailing list](https://groups.google.com/a/lists.stripe.com/g/api-announce)

Your integration must be able to reach any of Stripe’s fully qualified domain names for it to function properly. Depending on how your integration operates, you may need add them to an allowlist.

[domain names](#stripe-domains)

To help your integration operate securely, it must also verify that it’s communicating with api.stripe.com through one of our listed IP addresses.

[IP addresses](#ip-addresses)

If your integration also receives webhooks from us, make sure these events originate from a Stripe webhook IP address.

[webhooks](/webhooks)

[webhook IP address](#webhook-notifications)

## Stripe domains

Stripe uses the following fully qualified domain names to interact with your integration:

## Stripe Terminal domains

If you use Stripe Terminal, Stripe uses the following fully qualified domain names to interact with your integration:

[Stripe Terminal](/terminal)

Stripe Terminal uses the following fully qualified domain names to sync the device date over NTP:

Stripe Terminal uses the following partially qualified domain name to interact with your integration:

## IP addresses

The full list of IP addresses that api.stripe.com may resolve to is:

The full list of IP addresses that files.stripe.com, armada.stripe.com, and gator.stripe.com may resolve to is:

Always use the api.stripe.com DNS name to contact our API—never an IP address.

## Webhook notifications

The full list of IP addresses that webhook notifications may come from is:

## Downloading IP address lists

As a convenience, these IP lists are available in other formats for import into iptables or similar tools:

- https://stripe.com/files/ips/ips_api.txt

[https://stripe.com/files/ips/ips_api.txt](https://stripe.com/files/ips/ips_api.txt)

- https://stripe.com/files/ips/ips_api.json

[https://stripe.com/files/ips/ips_api.json](https://stripe.com/files/ips/ips_api.json)

- https://stripe.com/files/ips/ips_armada_gator.txt

[https://stripe.com/files/ips/ips_armada_gator.txt](https://stripe.com/files/ips/ips_armada_gator.txt)

- https://stripe.com/files/ips/ips_armada_gator.json

[https://stripe.com/files/ips/ips_armada_gator.json](https://stripe.com/files/ips/ips_armada_gator.json)

- https://stripe.com/files/ips/ips_webhooks.txt

[https://stripe.com/files/ips/ips_webhooks.txt](https://stripe.com/files/ips/ips_webhooks.txt)

- https://stripe.com/files/ips/ips_webhooks.json

[https://stripe.com/files/ips/ips_webhooks.json](https://stripe.com/files/ips/ips_webhooks.json)

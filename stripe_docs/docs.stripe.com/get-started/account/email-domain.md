# Custom email domain

By default, when Stripe sends invoices, receipts, and failed payment notifications to your customers, it sends them from the stripe.com domain. You can change this to a custom domain.

## Set up a custom email domain

To start sending emails from your own domain, complete the following steps:

- Add your domain in the Dashboard.

[Add your domain](#adding_domain)

- Verify your domain to allow sending.

[Verify your domain](#verifying_domain)

- Set your sending domain as your domain.

[Set your sending domain](#setting_sending_domain)

To modify the look and feel of your emails, go to your Branding settings.

[Branding](https://dashboard.stripe.com/account/branding)

[Add your domain](#adding_domain)

## Add your domain

Navigate to your Customer email settings and add the domain that you want to send customer emails from.

[Customer email](https://dashboard.stripe.com/settings/emails)

[Verify your domain](#verifying_domain)

## Verify your domain

To verify your domain, you must configure the Domain Name System (DNS) records provided in the Dashboard. These DNS records are necessary to verify your domain ownership and reliable email delivery.

The procedure for adding DNS records to the DNS server for your domain depends on who provides your DNS service. Consult the documentation for your DNS service for specific instructions.

It can take up to 72 hours for DNS record changes to be confirmed. Stripe lets you know whether your domain has been verified.

If your domain hasn’t been verified after 72 hours, try the following:

- Correct any typos. You can check your domain records in the Dashboard’s Customer emails settings by clicking Verify domain to filter issues.

Correct any typos. You can check your domain records in the Dashboard’s Customer emails settings by clicking Verify domain to filter issues.

[Customer emails](https://dashboard.stripe.com/settings/emails)

- Make sure you don’t have any records that share the same name as the provided CNAME records. CNAME records must be the only record present for a record name.

Make sure you don’t have any records that share the same name as the provided CNAME records. CNAME records must be the only record present for a record name.

[only record present](https://tools.ietf.org/html/rfc2181#section-10.1)

- Make sure the added record names don’t include your domain twice. Some providers automatically append DNS record names with the domain name. For example, to create a record with the name bounce.example.com, enter only bounce in the Name field.

Make sure the added record names don’t include your domain twice. Some providers automatically append DNS record names with the domain name. For example, to create a record with the name bounce.example.com, enter only bounce in the Name field.

- Check that the DNS records are published. You can verify this by using a DNS lookup tool, which displays the published records for your domain.

Check that the DNS records are published. You can verify this by using a DNS lookup tool, which displays the published records for your domain.

[DNS lookup tool](https://dnschecker.org/all-dns-records-of-domain.php)

If you’ve tried all of our troubleshooting recommendations and are still having trouble verifying your domain, contact your DNS provider.

Each category of record that needs to be configured has a purpose.

[Sender Policy Framework (SPF)](https://tools.ietf.org/html/rfc7208)

[DomainKeys Identified Mail (DKIM)](http://www.dkim.org/)

After we verify the domain, don’t delete the provided DNS records from your domain. Stripe frequently checks these records. If a record becomes invalid or goes missing, we notify you. Also, make sure to correct DNS records within 48 hours. If you don’t, we send customer emails from stripe.com until you resolve the problem.

To use a custom email domain, you need to set up a DMARC policy for your domain. Domain-based Message Authentication, Reporting & Conformance (DMARC) shields your domain from impersonation attacks, such as phishing. Notably, major email providers like Google and Yahoo now necessitate DMARC for those sending bulk emails.

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/)

You publish DMARC policy as a DNS TXT record. The record’s name is always _dmarc, and the value comprises tag-value pairs that symbolize your policy. Additionally, you can learn about all the supported tags and their uses, but let’s cover some of the most significant tags:

[supported tags and their uses](https://dmarc.org/overview/)

If you’re new to DMARC, we suggest beginning with a p=none policy for initial monitoring, then switch to either quarantine or reject in due course. After you’ve settled on the appropriate policy, you must incorporate the following DNS record into your domain:

We don’t currently support strict SPF alignment. Make sure your DMARC policy doesn’t have aspf=s.

If you’re already using this domain to send email, use caution when adding DMARC to make sure that it doesn’t interfere with your existing configuration. Consult an email or IT professional before adding or modifying this record.

[Set your sending domain](#setting_sending_domain)

## Set your sending domain

If Stripe has verified your domain, you’ll see a Verified badge under the Verification column in your Customer email settings. Customer emails are now sent from your domain. You can send a test email by clicking the overflow menu ().

[Customer email](https://dashboard.stripe.com/settings/emails)

Whenever a customer replies to your emails, their responses are sent to the support email address you specified in your public business information.

[public business information](https://dashboard.stripe.com/settings/public)

## Change email domains

We must verify each domain that you want to set as your sending domain. To switch to a new domain, return to Add your domain. You can always switch back to sending your customer emails using stripe.com.

[Add your domain](#setup)

When you’re no longer using a domain to send customer emails, you can remove it from your Customer email settings. In the Your custom email domains section, click the overflow menu () next to the domain name and select Remove domain. After removing the domain from your Dashboard, remove the unused DNS records from your DNS service.

[Customer email](https://dashboard.stripe.com/settings/emails)

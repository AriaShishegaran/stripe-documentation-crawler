# Mexico bank transfers

## What are bank transfers?

Bank transfers are a popular way to pay in Mexico. For merchants, bank transfers help reduce customer decline rates, fraud, and chargebacks, and have lower fees than credit cards. For customers in Mexico that have access to bank transfers in their banking apps, it’s a convenient way to pay.

## Target user segments

In particular, the Stripe bank transfer product serves users that process high average order volume (AOV) and low-frequency payments. This includes B2C Marketplaces with high AOV, B2B SaaS businesses, and fintech businesses.

## Product features

Stripe’s bank transfer product is powered by Citibanamex, the local Mexico unit of Citigroup, Inc. Citibanamex is a member of the SPEI network and provides the necessary basic capabilities for processing bank transfer payments.

Our product addresses key user needs by offering automatic reconciliation and management of partial and over payments, as well as refunds. Importantly, we designed the product knowing that low-code and no-code solutions are critical for users in Mexico, and it allows them to manage bank transfer payments through low-code and no-code solutions such as invoices created in the Dashboard.

[invoices](/api/invoices)

Our bank transfer product also offers successful payment confirmation notifications. Stripe provides a message, either in an API response or in a UI message in the Dashboard, indicating that a specific payment intent has been paid. On business days, we expect to provide successful payment confirmation of most payments within 30 minutes of the transfer, and on non-business days, such as a weekend or bank holiday, we provide payment confirmation for most payments on the next business day. For certain payments, you might experience delays of up to several days. Also, in case of online system maintenance, the payment confirmation will be delayed until the system is back online.

As soon as Stripe receives the successful payment confirmation from Citibanamex (based on the timing described above), the Dashboard updates to show the credit or completed payment. Funds can get paid out to the user’s bank account as soon as 3 days after Citibanamex has confirmed the bank transfer.

Due to reporting limitations, our product doesn’t offer immediate payment confirmation notifications or settlements. As a result, our product is better suited for merchants that process high AOV, low-frequency payments, such as B2B businesses rather than consumer retail businesses.

## Get started

Get started with accepting bank transfer payments or learn more about the customer balance.

[accepting bank transfer payments](/payments/bank-transfers/accept-a-payment)

[customer balance](/payments/customer-balance)

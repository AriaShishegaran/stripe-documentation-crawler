# Requirements for online Bacs Direct Debit mandate collection

As a Stripe user you can host your own Bacs Direct Debit mandate collection forms, allowing you to provide a fully customized experience for your customers. There are specific requirements around both what you need to display and what you need to collect from your customers when obtaining a Bacs Direct Debit mandate from them. Use the information in this document to create your own Bacs Direct Debit collection form. Contact us.

[Contact us](https://support.stripe.com/contact)

## Information to be collected from the payer

Collect the following information from the payer:

- Bank or building society account number

- Sort code

- Account holder name

- Billing address (unless it has already been provided)

- Agreement from the payer that they’re the account holder and only person required to authorize debits from the account, and that they understand the merchant has partnered with Stripe to collect Direct Debit payments. You should collect this with a checkbox next to the following wording: I understand that [Merchant Name] has partnered with Stripe, who collects Direct Debits on behalf of [Merchant Name] and confirm that I am the account holder and the only person required to authorize debits from this account.

Use the following example form for a fictional company named ‘Rocket Rides’ as a reference when creating your information collection form:

## Information to be displayed to the payer

Display the following information to the payer:

- Your postal and/or customer support email address

- Your general inquiries or customer service contact number

- Notification of the advance notice period, which is 2 working days

- The company name that will appear against the Direct Debit on the payer’s bank statement

- A hyperlink or unedited copy of Stripe’s Direct Debit guarantee

[Stripe’s Direct Debit guarantee](https://stripe.com/legal/bacs-direct-debit-guarantee)

- The entered bank details so that that the payer can confirm them

- A final screen explaining that the setup of the Direct Debit Instruction is complete and that an email confirmation will follow within 3 working days

Use the following example confirmation screen for a fictional company named ‘Rocket Rides’ as a reference when creating your own form:

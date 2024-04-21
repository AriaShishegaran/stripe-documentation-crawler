htmlReceive payouts | Stripe Documentation[Skip to content](#main-content)Payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)
[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[After the payment](/docs/payments/after-the-payment)# Receive payouts

Set up your bank account to receive payouts.### Learn more

For more information, see our Payouts FAQ and pricing guide.

You receive funds when Stripe (or your platform) makes payouts to your bank account. Payout availability varies depending on your industry and country of operation. When you start processing live payments, Stripe typically schedules your initial payout for 7-14 days after you successfully receive your first payment. Your first payout might take longer, depending on your industry risk level and country of operation. Subsequent payouts follow your account’s payout schedule.

You can see a comprehensive list of your payouts and the expected dates of deposit into your bank account in the Dashboard. If you’re a Connect platform, see Connect payouts.

## Add or update your bank account

You can update your account details or add a new bank account using the Payout settings in the Dashboard. Based on your bank’s location, Stripe might require different kinds of account details to activate your bank account. To modify your banking information, click the Edit button next to the desired bank account.

Use the following table to see the required bank details for specific countries:

Albania (AL)Algeria (DZ)Angola (AO)Antigua and Barbuda (AG)Argentina (AR)Armenia (AM)Australia (AU)Austria (AT)Azerbaijan (AZ)Bahamas (BS)Bahrain (BH)Bangladesh (BD)Belgium (BE)Benin (BJ)Bhutan (BT)Bolivia (BO)Bosnia and Herzegovina (BA)Botswana (BW)Brazil (BR)Brunei (BN)Bulgaria (BG)Cambodia (KH)Canada (CA)Chile (CL)Colombia (CO)Costa Rica (CR)Côte d'Ivoire (CI)Croatia (HR)Cyprus (CY)Czech Republic (CZ)Denmark (DK)Dominican Republic (DO)Ecuador (EC)Egypt (EG)El Salvador (SV)Estonia (EE)Ethiopia (ET)Finland (FI)France (FR)Gabon (GA)Gambia (GM)Germany (DE)Ghana (GH)Gibraltar (GI)Greece (GR)Guatemala (GT)Guyana (GY)Hong Kong (HK)Hungary (HU)Iceland (IS)India (IN)Indonesia (ID)Ireland (IE)Israel (IL)Italy (IT)Jamaica (JM)Japan (JP)Jordan (JO)Kazakhstan (KZ)Kenya (KE)Kuwait (KW)Laos (LA)Latvia (LV)Liechtenstein (LI)Lithuania (LT)Luxembourg (LU)Macau (MO)Madagascar (MG)Malaysia (MY)Malta (MT)Mauritius (MU)Mexico (MX)Moldova (MD)Monaco (MC)Mongolia (MN)Morocco (MA)Mozambique (MZ)Namibia (NA)Netherlands (NL)New Zealand (NZ)Niger (NE)Nigeria (NG)North Macedonia (MK)Norway (NO)Oman (OM)Pakistan (PK)Panama (PA)Paraguay (PY)Peru (PE)Philippines (PH)Poland (PL)Portugal (PT)Qatar (QA)Romania (RO)Rwanda (RW)Saint Lucia (LC)Saudi Arabia (SA)San Marino (SM)Senegal (SN)Serbia (RS)Singapore (SG)Slovakia (SK)Slovenia (SI)South Africa (ZA)South Korea (KR)Spain (ES)Sri Lanka (LK)Sweden (SE)Switzerland (CH)Taiwan (TW)Tanzania (TZ)Thailand (TH)Trinidad & Tobago (TT)Tunisia (TN)Türkiye (TR)United Kingdom (GB)United States (US)United Arab Emirates (AE)Uruguay (UY)Uzbekistan (UZ)Vietnam (VN)Bank account informationExample dataIBANNL39RABO0300065264 (18 characters)### Supported bank account types

You have the flexibility to link various types of bank accounts for your Stripe payouts. Supported options include traditional accounts offered by established financial institutions, including checking and savings accounts. Additionally, Stripe lets you use virtual bank accounts such as N26, Revolut, Wise, and others. If you’re eligible, you can also use a debit card for instant payouts.

NoteWhile Stripe supports non-standard bank accounts, you might see higher payout failures for these accounts.

### Supported accounts and settlement currencies

In most cases, bank accounts must be located in the country where the settlement currency is the official currency. For example, SEK bank accounts must be based in Sweden. Stripe also enables you to settle and pay out to banks in select alternative currencies, or pay out to non-domestic bank accounts in the local currency, for a fee. To learn more about presenting and settling in alternative currencies, see Alternative currencies.

At times, Stripe supports international currencies that don’t incur a fee. See the following table for the list of supported free currencies per country:

Viewing supported settlement currencies for Stripe accounts in:Australia (AU)Austria (AT)Belgium (BE)Brazil (BR)Bulgaria (BG)Canada (CA)Croatia (HR)Cyprus (CY)Czech Republic (CZ)Denmark (DK)Estonia (EE)Finland (FI)France (FR)Germany (DE)Gibraltar (GI)Greece (GR)Hong Kong (HK)Hungary (HU)India (IN)Ireland (IE)Italy (IT)Japan (JP)Latvia (LV)Liechtenstein (LI)Lithuania (LT)Luxembourg (LU)Malaysia (MY)Malta (MT)Mexico (MX)Netherlands (NL)New Zealand (NZ)Norway (NO)Poland (PL)Portugal (PT)Romania (RO)Singapore (SG)Slovakia (SK)Slovenia (SI)Spain (ES)Sweden (SE)Switzerland (CH)Thailand (TH)United Arab Emirates (AE)United Kingdom (GB)United States (US)Settlement currencyCan be paid out to banks in these countriesEURAustria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United KingdomAcquiring fees, where applicable, are based on the settlement currency, and you can find these acquiring fees listed out by currency on your country’s pricing page.

### Multiple bank accounts for different settlement currencies

In some countries, Stripe users can add extra bank accounts to enable settlements and payouts in additional currencies. You can add one bank account per supported settlement currency. If you use multiple bank accounts, you must select a default settlement currency, which you can change at any time.

Charges that are presented in any enabled settlement currency settle without currency conversion. However, payments presented in a currency that you haven’t configured an additional bank account for automatically convert to your default currency.

For example, consider a Stripe user in the United Kingdom who has added both GBP and USD bank accounts, with GBP selected as the default settlement currency. USD payments (where USD is the presentment currency) are automatically paid out to the USD bank account without conversion, whereas payments in all other currencies are converted into GBP.

You can manage your bank accounts and default settlement currency by visiting Bank accounts and scheduling in the Dashboard.

## Payout schedule

### Time zone difference

All payments and payouts are processed according to UTC time except for Asia-Pacific (APAC) markets. As a result, the processed date might not be the same as your local time zone.

Your payout schedule refers to how often Stripe sends money to your bank account.

In supported countries, your default payout schedule is daily automatic. You can change this in the Dashboard to weekly automatic, monthly automatic, or manual payouts. When selecting a weekly or monthly schedule, you can specify the day of the week or month that you want payouts to arrive in your bank account.

When you select a payout schedule, it doesn’t change how long it takes your pending balance to become available. However, it allows you to control when your payouts occur. For example, if your account operates on a daily payout schedule with a 3 business day payout speed, Stripe pays out funds daily from transactions captured 3 business days earlier.

Certain countries have restrictions on payout schedules:

- In Brazil and India, payouts are always automatic and daily.
- In Japan, daily payouts aren’t available. Default payout schedule is set to weekly (Friday).

If you’re using Cross-border payouts, these payout schedule restrictions don’t apply.

### Manual payouts

If you turn off automatic payouts in the Dashboard, you must manually send funds to your bank account. You can do this either in the Dashboard or by creating payouts using the API. Manual payouts are available in all regions except Brazil and India, where payouts are always automatic and daily.

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=5000 \
  -d currency=usd`## Payout speed

While payout schedule refers to the cadence your funds are paid out on (for example, day of the week), payout speed refers to the amount of time it takes for your funds to become available. The payout speed varies per country and is typically expressed as T+X days. Some payment processors might start “T” from their internal settlement time, meaning when the funds land in their bank accounts.

In Stripe, “T” refers to the transaction time, which indicates the time of the original payment confirmation or capture, and the counting starts earlier. If your Stripe account is in a country with a T+3 standard payout speed and you use a manual payout schedule, your Stripe balance is available for payout within three business days of capturing a payment. However, if you use a daily automatic payout schedule with a T+3 speed, Stripe pays out funds daily from transactions captured 3 business days earlier.

Most banks deposit payouts into your bank account as soon as they receive them, though some might take a few extra days to make them available. The type of business and the country you’re in can also affect payout timing.

### Accelerated payout speeds

Stripe offers accelerated payout speeds for users and connected accounts where Stripe manages credit and fraud risk in Europe, the UK, Mexico, and Canada. With accelerated payout speeds, funds are available within 3 business days.

Users become eligible for accelerated payout speeds after meeting certain criteria based on risk and history with Stripe. When you’re eligible, you can choose to opt in or out of accelerated payout speeds in the Dashboard by updating your Payout settings. You remain at the starting 7 calendar day payout speed until you meet the eligibility criteria. You can configure accounts where you manage fraud and dispute liability separately. Some high risk industries might not be eligible.

### Delay behavior per account country

As the platform, you can set delay_days on your connected accounts. The delay applies as a business day or calendar day delay based on the country of the connected account. The following table shows which countries apply the delay by business or calendar day.

CountryDelay typeAustralia,India,Japan,Malaysia,New Zealand,Thailand,United Arab Emirates,United StatesBusiness day (Monday - Friday)Brazil1,Canada,Gibraltar,Hong Kong,Liechtenstein,Mexico,Norway,Singapore2,Switzerland,United Kingdom, and supported EU countriesCalendar day (Sunday - Saturday)1 Delays for Pix, Boleto, debit, and prepaid payouts in Brazil apply in business days.

2 Delays for PayNow in Singapore apply in business days.

### Payout speed by country

Use the following table to determine your country’s payout speed. High-risk businesses have a payout speed of 14 calendar days.

### Country and payout speed

## Minimum payout amounts

The minimum payout amount depends on the lowest amount we can support with our banking partners. For example, if you’re located in the US and you have less than 1 cent (0.01 of 1 dollar) USD in your Stripe account, you must wait until you accept more payments and increase your balance before you can receive a payout. If your available account balance is less than the minimum payout amount, it remains in your Stripe account until your balance increases.

If you’re in a supported country, you can use alternative currency payouts to send a payout to your local bank accounts in a foreign currency. For example, a French user can now receive a USD payout in their French bank account instead of having to pay for multiple currency exchanges.

Minimum payout amounts are typically one base unit of the local currency. See the following collapsed table for a list of countries and their minimum payout amounts:

### Minimum payout amounts per country

### Cross-border minimum payout amounts

Cross-border minimum payout amounts are typically one base unit of the local currency in the recipient country’s currency. See the following collapsed table for a list of countries and their cross-border minimum payout amounts:

### Cross-border minimum payout amounts per country

## Negative payouts

Each payout reflects your available account balance at the time it was created. In some cases, you might have a negative account balance. For example, if you receive 100 USD in payments but refund 200 USD of prior payments, your account balance would be -100 USD. If you don’t receive further payments to balance out the negative amount, Stripe creates a payout that debits your bank account.

Your bank account must support both credit and debit transactions so that Stripe can perform any required payouts.

## Payout failures

If your bank account can’t receive a payout for any reason, your bank sends the funds back to us. This returns an error with the reason for the failure. It can take up to 5 additional business days for your bank to return the payout and inform us that it failed. If this happens, you’re notified by email and in the Dashboard. To make sure that your bank account details are correct, you need to re-enter them if a payout fails. After you re-enter your bank account details, Stripe attempts to perform the payout again at the next scheduled payout interval.

CautionWhen a payout fails, it’s possible that its state initially shows as paid but then changes to failed (within 5 business days).

Make sure that the bank account information you provide is correct because Stripe sends the funds using the account information you enter. Therefore, if you provide incorrect information (for example, a mistyped account number or an incorrect routing number), Stripe might send payouts to the wrong bank account and might not be able to recover the funds.

Any fees or losses that you incur due to incorrect information fall under your responsibility. If your banking details are correct and the payout failure is for other reasons, contact your bank. After you resolve any issues with your bank, you can reactivate the payouts by clicking Resume Payouts. If you don’t receive a payout from Stripe after clicking Resume Payouts, and haven’t received a failure notification within a reasonable time frame, please contact us.

## Instant Payouts

With Instant Payouts, you can instantly send funds to a supported debit card or bank account. You can request Instant Payouts any time, including weekends and holidays, and funds usually appear in the associated bank account within 30 minutes. New Stripe users aren’t immediately eligible for Instant Payouts. You can check your eligibility in the Dashboard.

## Payout fees

Stripe’s fee structure includes payouts, which means Stripe won’t charge you anything additional to initiate payouts. One exception is if you want to settle your payments and receive a payout to a domestic bank in an alternative currency. However, Stripe supports some international currencies without an additional fee. This support depends on your bank account’s location and the currency that you want your payout denominated in. To learn more about various payout currencies and their associated fees, see Alternative currencies.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Add or update your bank account](#adding-bank-account-information)[Payout schedule](#payout-schedule)[Payout speed](#payout-speed)[Minimum payout amounts](#minimum-payout-amounts)[Negative payouts](#negative-payouts)[Payout failures](#payout-failures)[Instant Payouts](#instant-payouts)[Payout fees](#payout-fees)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`
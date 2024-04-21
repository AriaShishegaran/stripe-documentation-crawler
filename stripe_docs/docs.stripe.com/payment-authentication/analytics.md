# Analytics

The payment authentication report helps you understand how authentication impacts your payment conversion. For businesses in Europe, the report helps you understand which payments were authenticated because of SCA regulation, and how Stripe uses SCA exemptions to improve your conversion.

[payment authentication report](https://dashboard.stripe.com/authentication)

[SCA](/strong-customer-authentication)

[SCA exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

[3D Secure Conversion](#conversion)

## 3D Secure Conversion

3DS provides an additional layer of authentication for credit and debit card transactions that protects merchants from liability for fraudulent card payments. For more information on liability shift and the benefits of 3DS see Cardholder authentication using 3D Secure.

[3DS](/payments/3d-secure)

[Cardholder authentication using 3D Secure](/payments/3d-secure)

You can request transaction authentication using the API or with a Radar rule. In addition, Stripe triggers 3DS for certain regulations, such as SCA.

[API](/payments/3d-secure/authentication-flow#manual-three-ds)

[Radar rule](/radar/rules#request-3d-secure)

​​Stripe removes duplicate transactions to minimize repeated attempts. For example, it prevents a single cardholder repeatedly trying and failing a payment. Our deduplication logic looks for groups of declined payments (except for the last, potentially) with the same customer, currency, and amount​, appearing close together in time. Such groups are treated as a single unit for conversion calculations. In the Sigma table, we include all raw data, but also include a column, is_final_attempt​, that you can use to filter to a representative transaction from each group.

The Dashboard provides information on transaction attempts and completions:

- 3DS attempts: The number of times that card transactions attempted authentication. Excludes failed attempts that were retired for the same order.

3DS attempts: The number of times that card transactions attempted authentication. Excludes failed attempts that were retired for the same order.

- 3DS completed: The number of attempts where authentication was successful.

3DS completed: The number of attempts where authentication was successful.

- 3DS completion rate: The proportion of attempted transactions that successfully completed.

3DS completion rate: The proportion of attempted transactions that successfully completed.

The following section contains two views that help you understand changes to your 3D Secure completion rate over the selected time period, along with the proportion of 3D Secure outcomes.

- Completed represents transactions that completed 3DS.

- The Frictionless flow represents transactions that were completed without any additional cardholder input. This occurs when the issuer approved the 3DS request using risk signals, or the network provided a proof that 3DS was attempted.

- The Challenge flow represents transactions where the cardholder provided additional input to verify their identity to the card issuer

- The Failed outcome represents situations where the customer failed the authentication for a transaction or it was rejected by the bank.

- The Unavailable outcome means the bank doesn’t support 3DS or the issuing bank returned an error.

- Not actioned refers to instances where the customer didn’t enter the 3D Secure flow, or there was an issue with your integration and it did not action the attempt.

[SCA Exemptions](#sca-exemptions)

## SCA Exemptions

Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase.

Some transactions that are deemed low risk, based on the volume of fraud rates associated with the payment provider or bank, may be exempt from Europe’s Strong Customer Authentication requirements.

[Strong Customer Authentication](/strong-customer-authentication)

If Stripe requests an exemption for payments requiring SCA and the transaction passes through the frictionless flow, it doesn’t benefit from the liability shift. If an issuer applies the frictionless flow without being requested, liability shift generally occurs. Learn more about liability shifts.

[liability shifts](/payments/3d-secure/authentication-flow#disputed-payments)

The payment authentication report enables you to view the different type of exemptions being used, so you can access SCA impact, understand levels of enforcement, and see the value of the SCA exemptions requested on your behalf.

Payments in SCA scope is the number of all transactions where you or the card issuing bank is in one of the 32 European countries with SCA regulation. It excludes payments that were retried but failed for the same order. See When is Strong Customer Authentication required?.

[When is Strong Customer Authentication required?](https://stripe.com/guides/strong-customer-authentication#when-is-strong-customer-authentication-required)

Exempted payments is the number of those in-scope payments that were successfully exempted from SCA—either no 3D Secure was present or the payment went through the 3D Secure frictionless flow.

Exemption rate is the proportion of attempted transactions that successfully completed.

The following section contains two views that help you understand changes to your exemption rate over the selected time period, along with the proportion of payment outcomes.

- Succeeded—exempted represents payments that succeeded without requiring an authentication challenge. Either the bank didn’t support 3DS or the payment went through the 3DS frictionless flow.

- Succeeded—authenticated represents payments that succeed with a two-factor challenge, such as a 3DS challenge flow or authentication through Apple Pay or Google Pay.

- Failed represents payments that didn’t go through. Either Radar blocked the payment, the issuing bank declined it, or the customer failed the challenge authentication.

The chart displayed on your Dashboard page shows the different exemptions that were used. Use the breakdown chart to better understand SCA enforcement across your target market, as well as performance of Stripe’s optimizations.

There are two ways to claim an SCA exemption:

- Direct to authorization - where Stripe requests an exemption as part of the authorization message.

- Stripe requests frictionless authentication by asking for an exemption in the 3DS messages.

See Exemptions to Strong Customer Authentication for details on the different types of exemptions.

[Exemptions to Strong Customer Authentication](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

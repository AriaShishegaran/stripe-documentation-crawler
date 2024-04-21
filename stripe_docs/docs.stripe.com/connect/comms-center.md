# Comms Center

## Overview

Platforms that want to update the emails Stripe has on file for connected accounts can update them using the Comms Center collection flow.

[Comms Center collection flow](https://dashboard.stripe.com/connect/comms_center/collect)

## Collecting emails

After hitting Get Started you see the main page for collection and validation.

You get a template CSV like this:

For example, a filled out CSV might look like this:

The filename doesn’t matter. Only the Account ID and Email Address (please add or replace) fields matter here, the rest are only for validating your changes.

After confirming, you see the completion state. Updates can take some time, depending on how many emails you’ve uploaded. We send email updates to any webhooks you’ve configured.

## Important usage notes

- Comms Center can only currently handle CSVs with 500,000 rows. If you have more than that, break up your CSV into multiple files.

- If you get validation errors, make sure your headers on your CSV match the expected headers. The required columns are Account ID which has the acct_ tokens and Email Address (please add or replace) which has the desired email.

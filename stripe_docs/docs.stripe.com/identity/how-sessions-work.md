# How sessions work

Asynchronous verification flows are complex to manage because they depend on customer interactions that happen outside of your application. VerificationSessions simplify this by keeping track of the status of the verification flow.

[VerificationSessions](/identity/verification-sessions)

When the VerificationSession is created, it has a status of requires_input and is ready for your user to begin the verification process. We recommend creating the VerificationSession right before the start of the verification flow.

[begin the verification process](/identity/verify-identity-documents)

As soon as the user submits the session, the VerificationSession moves to processing. Most verification checks are processed in less than 1 minute.

[verification checks](/identity/verification-checks)

A VerificationSession with a status of verified means that the verification flow is complete. Processing of all the verification checks are complete and successfully verified.

If any of the verification checks fail (for example, because of a manipulated document), the VerificationSession’s status returns to requires_input. You can find an explanation for the verification failure in the last_error field of the session. If you want your user to attempt verification again, you need to Retrieve the VerificationSession to get a fresh URL or client secret.

[Retrieve the VerificationSession](/api/identity/verification_sessions/retrieve)

You may cancel a VerificationSession at any point before it’s processing or verified. This invalidates the VerificationSession for future submission attempts, and can’t be undone.

[cancel a VerificationSession](/identity/verification-sessions#cancel)

## Session events

Events are created every time a session changes status. Here’s a complete list of the VerificationSession event types:

[Events](/api/events)

[event types](/api#event_types)

[created](/identity/verification-sessions#create)

[verification checks](/identity/verification-checks)

[verification checks](/identity/verification-checks)

[canceled](/identity/verification-sessions#cancel)

[redacted](/identity/verification-sessions#redact)

[redacted](/identity/verification-sessions#redact)

[webhook endpoint](/api/webhook_endpoints)

You might want to take action in response to certain events, such as emailing your user when a verification fails or succeeds.

Stripe recommends that you listen for events with webhooks.

[webhooks](/identity/handle-verification-outcomes)

## See also

- The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions)

- Handle verification outcomes

[Handle verification outcomes](/identity/handle-verification-outcomes)

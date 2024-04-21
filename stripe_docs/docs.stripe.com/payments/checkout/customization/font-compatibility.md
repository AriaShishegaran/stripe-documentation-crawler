# Font compatibility

Each custom font is compatible with a subset of locales. You can either explicitly set the locale of a Checkout Session by passing the locale field when creating the Session, or use the default auto setting where Checkout chooses a locale based on the customer’s browser settings.

[subset of locales](/js/appendix/supported_locales)

The following table lists unsupported locales for each font. Languages in these locales might fall outside of the supported character range for a given font. In those cases, Stripe renders the Checkout page with an appropriate system fallback font. If you choose a Serif font but it’s unsupported in a locale, Stripe falls back to a Serif-based font.

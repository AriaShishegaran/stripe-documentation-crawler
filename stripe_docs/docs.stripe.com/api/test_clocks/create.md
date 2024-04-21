- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a test clockTest helper

[Create a test clock](/api/test_clocks/create)

Creates a new test clock that can be attached to new customers and quotes.

- frozen_timetimestampRequiredThe initial frozen time for this test clock.

The initial frozen time for this test clock.

- namestringThe name for this test clock.

The name for this test clock.

The newly created TestClock object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a test clockTest helper

[Retrieve a test clock](/api/test_clocks/retrieve)

Retrieves a test clock.

No parameters.

Returns the TestClock object. Otherwise, this call raises an error.

[an error](#errors)

# List all test clocksTest helper

[List all test clocks](/api/test_clocks/list)

Returns a list of your test clocks.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit test clocks, starting after starting_after. Each entry in the array is a separate test clock object. If no more test clocks are available, the resulting array will be empty.

# Delete a test clockTest helper

[Delete a test clock](/api/test_clocks/delete)

Deletes a test clock.

No parameters.

The deleted TestClock object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Advance a test clockTest helper

[Advance a test clock](/api/test_clocks/advance)

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to Ready.

- frozen_timetimestampRequiredThe time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.

The time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.

A TestClock object with status Advancing is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

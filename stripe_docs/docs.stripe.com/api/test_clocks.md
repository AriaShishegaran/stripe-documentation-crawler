- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Test ClocksTest helper

[Test Clocks](/api/test_clocks)

A test clock enables deterministic control over objects in testmode. With a test clock, you can create objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances, you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

[POST/v1/test_helpers/test_clocks](/api/test_clocks/create)

[GET/v1/test_helpers/test_clocks/:id](/api/test_clocks/retrieve)

[GET/v1/test_helpers/test_clocks](/api/test_clocks/list)

[DELETE/v1/test_helpers/test_clocks/:id](/api/test_clocks/delete)

[POST/v1/test_helpers/test_clocks/:id/advance](/api/test_clocks/advance)

# The Test Clock objectTest helper

[The Test Clock object](/api/test_clocks/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- deletes_aftertimestampTime at which this clock is scheduled to auto delete.

Time at which this clock is scheduled to auto delete.

- frozen_timetimestampTime at which all objects belonging to this clock are frozen.

Time at which all objects belonging to this clock are frozen.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- namenullable stringThe custom name supplied at creation.

The custom name supplied at creation.

- statusenumThe status of the Test Clock.Possible enum valuesadvancingIn the process of advancing time for the test clock objects.internal_failureFailed to advance time. Future requests to advance time will fail.readyAll test clock objects have advanced to the frozen_time.

The status of the Test Clock.

In the process of advancing time for the test clock objects.

Failed to advance time. Future requests to advance time will fail.

All test clock objects have advanced to the frozen_time.

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

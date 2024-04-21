# FocusView

A FocusView component can be opened from other View components and allows the developer to open a dedicated space for the end user to complete a specific task. Examples include:

- Enter details to create a new entry in a database

- Go through a wizard to decide on next steps

- Confirm that the user wants to take the action they indicated

What FocusView looks like

FocusView must be a child of ContextView. Don’t wrap the FocusView in a conditional, instead use the shown property to control its visible state. For more information, see ContextView.

[ContextView](/stripe-apps/components/contextview)

To add the FocusView component to your app:

When passing confirmCloseMessages, in order for the close confirmation dialog to work properly in every close scenario, pass the setShown prop so the FocusView can manage its shown state. To control when the close confirmation dialog displays, you can use state to conditionally pass confirmCloseMessages to the FocusView, like in the following example:

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)

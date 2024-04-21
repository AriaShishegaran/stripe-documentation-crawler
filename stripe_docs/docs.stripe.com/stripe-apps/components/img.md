# Img

To add an image to your app:

- Import the Img component:import {Img} from '@stripe/ui-extension-sdk/ui'

Import the Img component:

- Include the base URLs of any images you include in the image-src section of the content_security_policy in your app manifest.

Include the base URLs of any images you include in the image-src section of the content_security_policy in your app manifest.

[app manifest](/stripe-apps/reference/app-manifest)

The following shows a preview of an image with the respective Img tag below:

[https://images.example.com/margin.svg](https://images.example.com/margin.svg)

## SrcSet

You can use srcSet for responsive images.

[responsive images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

The example below uses the size attribute to define the maximum width of the specified image:

[https://images.example.com/daily-sales.jpg](https://images.example.com/daily-sales.jpg)

[https://images.example.com/daily-sales-large.jpg](https://images.example.com/daily-sales-large.jpg)

## Data URLs

You can co-locate images with your UI extension code and load them directly into the Img component. Supported formats are GIF, JPEG, SVG, PNG, and WEBP.

We recommend using SVG for most common use-cases like icons and other way finding illustrations.  You must include the suffix of the image in the require or import statement.

## Styling

You can achieve certain styling effects for Img components by wrapping them with a styled Box component.

[Box](/stripe-apps/components/box)

To add a border to an Img, use the CSS keyline property, along with width and display to contain the image:

[border](/stripe-apps/style#borders)

To add rounded corners to an Img, use the CSS borderRadius property, along with overflow, width, and display to contain the image:

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)

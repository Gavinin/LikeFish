# User Guide

This document provides instructions on how to use the following configuration file to set various parameters for the application.

## tolerance

- Range: 1-10
- Type: Integer

Used to set the tolerance parameter. Assign an integer value between 1 and 10 to the `tolerance` parameter. Smaller values provide higher precision, while larger values allow for more flexibility.

## hasVideo

- Range: true or false
- Type: Boolean

Used to specify whether to enable the video feature. Assign `true` to the `hasVideo` parameter to enable the video feature, or assign `false` to disable it. By default, it is set to false and is typically only enabled for debugging purposes.

### window

- Type: Object

Contains the following sub-properties to define the width and height of the window.

### width

- Type: Integer

Used to set the width of the window. Assign an integer value to the `width` parameter.

### height

- Type: Integer

Used to set the height of the window. Assign an integer value to the `height` parameter.

## userMap

- Type: Object

Used to define the user mapping configuration，example need be replaced.

### example:

- Type: Object

Defines the mapping configuration for the user "example". The name should match the name in the image, and it is case-insensitive. It is recommended to use English names.

### keyMap

- Type: Array

Used to set the shortcut keys to be executed when a successful match is found. Multiple key combinations can be specified, and the case is not significant. Supported keys include CMD, Option, Ctrl, F1-F12. This field can be empty.

### funcMap

- Type: Array

Used to set the commands or functions to be executed when a successful match is found. Currently, only hiding the process window is supported, so specify the process name. On macOS, you can use tools like htop or Activity Monitor to find the process names. This field can be empty.

## Example

Here is an example configuration file:

```yaml
# tolerance 1-10
tolerance: 4

# true or false
hasVideo: false

window:
  width: 800
  height: 600

#
userMap:
  example:
    keyMap:
      - "CMD a"
      - "cmd m"
    funcMap:
      - "Pycharm"
      - "idea"
```

Modify the values in the configuration file as needed and follow the instructions provided above for configuration.
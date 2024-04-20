# input_devices

`input_devices` is a Python library designed to provide a high-level API for interacting with various electronic input devices. This includes game controllers (such as Xbox and PlayStation controllers), joysticks, remote controllers, as well as computer peripherals like keyboards and mice. The goal of `input_devices` is to simplify the process of integrating these devices into Python projects by offering a straightforward and unified interface.

## Features

- **Game Controllers**: Support for Xbox and PlayStation controllers.
- **Joysticks**: Compatibility with various models of joysticks.
- **Remote Controllers**: Integration with different types of remote control devices.
- **Computer Peripherals**: Support for keyboards and mice, facilitating complex input handling.
- **Extensible**: Designed to be easily extendable for more types of devices.

## Installation

Install `input_devices` using pip:

```bash
pip install input_devices


Quick Start

Here is a simple example of how to use input_devices to listen for inputs from an Xbox controller:

```python

from src.xbox_controller import XboxControllerGen4
from inputs import get_gamepad

controller = XboxControllerGen4(get_gamepad())
controller.A.on_press(lambda: print("A pressed")) \
          .on_release(lambda: print("A released"), lambda: print("A released x2")) # multiple subscribers available

controller.directional_pad.up.on_press(lambda: print("D-pad up")) # interaction with different types of buttons

while True:
     controller.update()
     print(controller.left_trigger.get_y()) # get pressure-sensitive input

```

Documentation

For more detailed information about using input_devices, refer to the full documentation.
Contributing

input_devices is an open project, and contributions are welcome! If you have suggestions for improvements or new features, please feel free to fork the repository and submit a pull request, or contact me directly via email at mtik.philosopher@gmail.com.
Contact

If you have any questions or comments about input_devices, please feel free to reach out to me:

    Project by: Mark Tikhonov
    Email: mtik.philosopher@gmail.com

License

This project is licensed under the MIT License - see the LICENSE file for details.

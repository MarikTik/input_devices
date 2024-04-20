from .axis_input import CartesianAxisInput
from .button import Button
from ..utils.type_hints import range_t

class AxisTrigger(CartesianAxisInput, Button):
    """
    Represents an AxisTrigger on a controller, combining the features of both an axis input and a button. 
    This would be typically used on joystick inputs that return x-y coordinates and can be pressed.
    """

    def __init__(self,
                 horizontal_value_range: range_t,
                 vertical_value_range: range_t,
                 horizontal_axis_inverted: bool = False,
                 vertical_axis_inverted: bool = False,
                 debounce_time: float = Button.default_debounce_time) -> None:
        """
        Initializes an AxisTrigger with specific configurations for axis input and button debounce timing.

        Args:
            horizontal_value_range (range_t): The range of values for the horizontal axis.
            vertical_value_range (range_t): The range of values for the vertical axis.
            horizontal_axis_inverted (bool): Whether to invert the horizontal axis.
            vertical_axis_inverted (bool): Whether to invert the vertical axis.
            debounce_time (float): Time in seconds to ignore changes in state to prevent bounce.
        """
        CartesianAxisInput.__init__(self,
                                    horizontal_value_range=horizontal_value_range,
                                    vertical_value_range=vertical_value_range,
                                    horizontal_axis_inverted=horizontal_axis_inverted,
                                    vertical_axis_inverted=vertical_axis_inverted)
        Button.__init__(self, debounce_time)

from .axis_input import CartesianAxisInput, range_t, default_blindspot_range, default_bounds, number_t
from .button import Button

class AxisTrigger(CartesianAxisInput, Button):
    """
    Represents an AxisTrigger on a controller, combining the features of both an axis input and a button. 
    This would be typically used on joystick inputs that return x-y coordinates and can be pressed.
    """

    def __init__(self,
                 horizontal_blindspot_range: range_t = default_blindspot_range,
                 vertical_blindspot_range: range_t = default_blindspot_range,
                 horizontal_custom_bounds: range_t = default_bounds,
                 vertical_custom_bounds: range_t = default_bounds,
                 horizontal_zero: number_t = 0,
                 vertical_zero: number_t = 0,
                 horizontal_axis_inverted: bool = False,
                 vertical_axis_inverted: bool = False,
                 debounce_time: float = Button.default_debounce_time) -> None:
        """
        Initializes an AxisTrigger with specific configurations for axis input and button debounce timing.

        Args:
            horizontal_blindspot_range (range_t): Horizontal axis range where input is ignored.
            vertical_blindspot_range (range_t): Vertical axis range where input is ignored.
            horizontal_custom_bounds (range_t): Full range of horizontal axis values.
            vertical_custom_bounds (range_t): Full range of vertical axis values.
            horizontal_zero (number_t): Neutral point of the horizontal axis.
            vertical_zero (number_t): Neutral point of the vertical axis.
            horizontal_axis_inverted (bool): Whether to invert the horizontal axis.
            vertical_axis_inverted (bool): Whether to invert the vertical axis.
            debounce_time (float): Time in seconds to ignore changes in state to prevent bounce.
        """
        CartesianAxisInput.__init__(self,
                                    horizontal_blindspot_range=horizontal_blindspot_range,
                                    vertical_blindspot_range=vertical_blindspot_range,
                                    horizontal_custom_bounds=horizontal_custom_bounds,
                                    vertical_custom_bounds=vertical_custom_bounds,
                                    horizontal_zero=horizontal_zero,
                                    vertical_zero=vertical_zero,
                                    horizontal_axis_inverted=horizontal_axis_inverted,
                                    vertical_axis_inverted=vertical_axis_inverted)
        Button.__init__(self, debounce_time)

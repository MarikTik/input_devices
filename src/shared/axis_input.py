from typing import Tuple
from ..utils.functions import map, range_adjust
from ..utils.type_hints import number_t, range_t

class HorizontalAxisInput:
    """Handles the horizontal axis input settings for a controller."""
    def __init__(self, value_range: range_t, axis_inverted: bool = False) -> None:
        self.__axis_inverted = axis_inverted
        self.__value_range = value_range
        self.__x: float = 0.0

    def _set_x(self, x: number_t) -> None:
        """Internal method to set the x value directly."""
        self.__x = x

    def get_x(self) -> number_t:
        """
        Get the current horizontal axis value, considering whether it is inverted.

        Returns:
            number_t: The current horizontal axis value.
        """
        return -self.__x if self.__axis_inverted else self.__x
    
    def get_adjusted_x(self, axis_blindspot_range: range_t, axis_zero: number_t) -> number_t:
        """
        Get the adjusted horizontal axis value, applying blindspot processing and normalization based on zero.

        Args:
            axis_blindspot_range (range_t): The range within which the axis input is ignored.
            axis_zero (number_t): The value that represents zero input.

        Returns:
            number_t: The adjusted horizontal axis value.
        """
        adjusted_value = range_adjust(self.__x, axis_blindspot_range, self.__value_range, axis_zero)
        return -adjusted_value if self.__axis_inverted else adjusted_value
    
    def get_mapped_x(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Convert the horizontal axis value to a new range.

        Args:
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The horizontal axis value mapped to the new range.
        """
        mapped_value = map(self.__x, *self.__value_range, new_minimum, new_maximum)
        return -mapped_value if self.__axis_inverted else mapped_value
    
    def get_calibrated_x(self, axis_blindspot_range: range_t, axis_zero: number_t, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Get the calibrated horizontal axis value, first adjusting and then mapping it to a new range.

        Args:
            axis_blindspot_range (range_t): The range within which the axis input is ignored.
            axis_zero (number_t): The value that represents zero input.
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The calibrated horizontal axis value.
        """
        adjusted_value = self.get_adjusted_x(axis_blindspot_range, axis_zero)
        mapped_value = map(adjusted_value, *self.__value_range, new_minimum, new_maximum)
        return -mapped_value if self.__axis_inverted else mapped_value
    

class VerticalAxisInput:
    """Handles the vertical axis input settings for a controller."""

    def __init__(self, value_range: range_t, axis_inverted: bool = False) -> None:
        """
        Initialize the vertical axis input configuration.

        Args:
            value_range (range_t): The full range of vertical axis values.
            axis_inverted (bool): If True, inverts the axis values.
        """
        self.__axis_inverted = axis_inverted
        self.__value_range = value_range
        self.__y: float = 0.0
    
    def _set_y(self, y: number_t) -> None:
        """Internal method to set the y value directly."""
        self.__y = y

    def get_y(self) -> number_t:
        """
        Get the current vertical axis value, considering whether it is inverted.

        Returns:
            number_t: The current vertical axis value.
        """
        return -self.__y if self.__axis_inverted else self.__y
    
    def get_adjusted_y(self, axis_blindspot_range: range_t, axis_zero: number_t) -> number_t:
        """
        Get the adjusted vertical axis value, applying blindspot processing and normalization based on zero.

        Args:
            axis_blindspot_range (range_t): The range within which the axis input is ignored.
            axis_zero (number_t): The value that represents zero input.

        Returns:
            number_t: The adjusted vertical axis value.
        """
        adjusted_value = range_adjust(self.__y, axis_blindspot_range, self.__value_range, axis_zero)
        return -adjusted_value if self.__axis_inverted else adjusted_value
    
    def get_mapped_y(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Convert the vertical axis value to a new range.

        Args:
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The vertical axis value mapped to the new range.
        """
        mapped_value = map(self.__y, *self.__value_range, new_minimum, new_maximum)
        return -mapped_value if self.__axis_inverted else mapped_value
    
    def get_calibrated_y(self, axis_blindspot_range: range_t, axis_zero: number_t, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Get the calibrated vertical axis value, first adjusting and then mapping it to a new range.

        Args:
            axis_blindspot_range (range_t): The range within which the axis input is ignored.
            axis_zero (number_t): The value that represents zero input.
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The calibrated vertical axis value.
        """
        adjusted_value = self.get_adjusted_y(axis_blindspot_range, axis_zero)
        mapped_value = map(adjusted_value, *self.__value_range, new_minimum, new_maximum)
        return -mapped_value if self.__axis_inverted else mapped_value
    

class CartesianAxisInput(HorizontalAxisInput, VerticalAxisInput):
    """Handles combined horizontal and vertical axis inputs for a controller."""
    def __init__(self, 
                 horizontal_value_range: range_t,
                 vertical_value_range: range_t,
                 horizontal_axis_inverted: bool = False, 
                 vertical_axis_inverted: bool = False) -> None:
        """
        Initialize the Cartesian axis input configuration for managing two-dimensional control inputs.

        Args:
            horizontal_value_range (range_t): The full range of horizontal axis values.
            vertical_value_range (range_t): The full range of vertical axis values.
            horizontal_axis_inverted (bool): If True, inverts the horizontal axis values.
            vertical_axis_inverted (bool): If True, inverts the vertical axis values.

        Initializes a two-axis controller setup where each axis can be individually configured for ranges and inversion,
        enabling precise control over input handling.
        """

        HorizontalAxisInput.__init__(self, axis_inverted=horizontal_axis_inverted, value_range=horizontal_value_range)
        VerticalAxisInput.__init__(self, axis_inverted=vertical_axis_inverted, value_range=vertical_value_range)

# class HorizontalAxisInput:
#     """Handles the horizontal axis input settings for a controller."""

#     def __init__(self,
#                  blindspot_range: range_t = (-3000, 3000),
#                  custom_bounds: range_t = (-32768, 32767),
#                  zero: number_t = 0,
#                  axis_inverted: bool = False) -> None:
#         """
#         Initialize the horizontal axis input configuration.

#         Args:
#             blindspot_range (range_t): The range within which the axis input is ignored.
#             custom_bounds (range_t): The full range of axis values.
#             zero (number_t): The value that represents zero input.
#             axis_inverted (bool): If True, inverts the axis values.
#         """
#         self._horizontal_blindspot_range = blindspot_range
#         self._horizontal_custom_bounds = custom_bounds
#         self._horizontal_zero = zero
#         self._horizontal_inverted = axis_inverted
#         self._x = zero

#     def set_horizontal_blindspot_range(self, blindspot_range: range_t) -> 'HorizontalAxisInput':
#         """
#         Set the horizontal axis blindspot range.

#         Args:
#             blindspot_range (range_t): The range within which the axis input is ignored.

#         Returns:
#             HorizontalAxisInput: An instance of this class.
#         """
#         self._horizontal_blindspot_range = blindspot_range
#         return self

#     def set_horizontal_custom_bounds(self, custom_bounds: range_t) -> 'HorizontalAxisInput':
#         """
#         Set the custom bounds for the horizontal axis.

#         Args:
#             custom_bounds (range_t): The full range of axis values.

#         Returns:
#             HorizontalAxisInput: An instance of this class.
#         """
#         self._horizontal_custom_bounds = custom_bounds
#         return self

#     def set_horizontal_zero(self, zero: number_t) -> 'HorizontalAxisInput':
#         """
#         Set the zero point for the horizontal axis.

#         Args:
#             zero (number_t): The value that represents zero input.

#         Returns:
#             HorizontalAxisInput: An instance of this class.
#         """
#         self._horizontal_zero = zero
#         return self

#     def set_horizontal_axis_inverted(self, axis_inverted: bool) -> 'HorizontalAxisInput':
#         """
#         Set whether the horizontal axis is inverted.

#         Args:
#             axis_inverted (bool): If True, inverts the axis values.

#         Returns:
#             HorizontalAxisInput: An instance of this class.
#         """
#         self._horizontal_inverted = axis_inverted
#         return self

#     def get_x(self) -> number_t:
#         """
#         Get the current horizontal axis value, considering whether it is inverted.

#         Returns:
#             number_t: The current horizontal axis value.
#         """
#         return -self._x if self._horizontal_inverted else self._x

#     def get_x_adjusted(self) -> number_t:
#         """
#         Get the adjusted horizontal axis value, applying the blindspot and custom bounds.

#         Returns:
#             number_t: The adjusted horizontal axis value.
#         """
#         value = range_fit(self._x, self._horizontal_blindspot_range, self._horizontal_custom_bounds, self._horizontal_zero)
#         return -value if self._horizontal_inverted else value

#     def get_x_bounded(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
#         """
#         Convert the adjusted horizontal axis value to a new range.

#         Args:
#             new_minimum (number_t): The lower bound of the new range.
#             new_maximum (number_t): The upper bound of the new range.

#         Returns:
#             number_t: The horizontal axis value mapped to the new range.
#         """
#         return map(self.get_x_adjusted(), self._horizontal_custom_bounds[0], self._horizontal_custom_bounds[1], new_minimum, new_maximum)

# class VerticalAxisInput:
#     """Handles the vertical axis input settings for an Xbox controller."""

#     def __init__(self,
#                  blindspot_range: range_t = (-3000, 3000), 
#                  custom_bounds: range_t = (-32768, 32767),
#                  axis_inverted: bool = False,
#                  zero: number_t = 0) -> None:
#         """
#         Initialize the vertical axis input configuration.

#         Args:
#             blindspot_range (range_t): The range within which the axis input is ignored.
#             custom_bounds (range_t): The full range of axis values.
#             axis_inverted (bool): If True, inverts the axis values.
#             zero (number_t): The value that represents zero input.
#         """
#         self._vertical_blindspot_range = blindspot_range
#         self._vertical_custom_bounds = custom_bounds
#         self._vertical_inverted = axis_inverted
#         self._vertical_zero = zero
#         self._y = float()

#     def set_vertical_blindspot_range(self, blindspot_range: range_t) -> 'VerticalAxisInput':
#         """
#         Set the vertical axis blindspot range.

#         Args:
#             blindspot_range (range_t): The range within which the axis input is ignored.

#         Returns:
#             VerticalAxisInput: An instance of this class.
#         """
#         self._vertical_blindspot_range = blindspot_range
#         return self

#     def set_vertical_custom_bounds(self, custom_bounds: range_t) -> 'VerticalAxisInput':
#         """
#         Set the custom bounds for the vertical axis.

#         Args:
#             custom_bounds (range_t): The full range of axis values.

#         Returns:
#             VerticalAxisInput: An instance of this class.
#         """
#         self._vertical_custom_bounds = custom_bounds
#         return self

#     def set_vertical_axis_inverted(self, axis_inverted: bool) -> 'VerticalAxisInput':
#         """
#         Set whether the vertical axis is inverted.

#         Args:
#             axis_inverted (bool): If True, inverts the axis values.

#         Returns:
#             VerticalAxisInput: An instance of this class.
#         """
#         self._vertical_inverted = axis_inverted
#         return self

#     def set_vertical_zero(self, zero: number_t) -> 'VerticalAxisInput':
#         """
#         Set the zero point for the vertical axis.

#         Args:
#             zero (number_t): The value that represents zero input.

#         Returns:
#             VerticalAxisInput: An instance of this class.
#         """
#         self._vertical_zero = zero
#         return self

#     def get_y(self) -> number_t:
#         """
#         Get the current vertical axis value, considering whether it is inverted.

#         Returns:
#             number_t: The current vertical axis value.
#         """
#         return -self._y if self._vertical_inverted else self._y

#     def get_y_adjusted(self) -> number_t:
#         """
#         Get the adjusted vertical axis value, applying the blindspot and custom bounds.

#         Returns:
#             number_t: The adjusted vertical axis value.
#         """
#         value = range_fit(self._y, self._vertical_blindspot_range, self._vertical_custom_bounds, self._vertical_zero)
#         return -value if self._vertical_inverted else value

#     def get_y_bounded(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
#         """
#         Convert the adjusted vertical axis value to a new range.

#         Args:
#             new_minimum (number_t): The lower bound of the new range.
#             new_maximum (number_t): The upper bound of the new range.

#         Returns:
#             number_t: The vertical axis value mapped to the new range.
#         """
#         return map(self.get_y_adjusted(), self._vertical_custom_bounds[0], self._vertical_custom_bounds[1], new_minimum, new_maximum)

# class CartesianAxisInput(HorizontalAxisInput, VerticalAxisInput):
#      """Handles combined horizontal and vertical axis inputs for a controller."""
#      def __init__(self, 
#                   horizontal_blindspot_range: range_t = default_blindspot_range,
#                   vertical_blindspot_range: range_t = default_blindspot_range,
#                   horizontal_custom_bounds: range_t = default_bounds,
#                   vertical_custom_bounds: range_t = default_bounds,
#                   horizontal_axis_inverted: bool = False,
#                   vertical_axis_inverted: bool = False,
#                   horizontal_zero: number_t = zero,
#                   vertical_zero: number_t = zero
#                   ) -> None:
#           """
#              Initialize the Cartesian axis input configuration for managing two-dimensional control inputs.
     
#              Args:
#                  horizontal_blindspot_range (range_t): The horizontal axis range within which the input is ignored.
#                  vertical_blindspot_range (range_t): The vertical axis range within which the input is ignored.
#                  horizontal_custom_bounds (range_t): The full range of horizontal axis values.
#                  vertical_custom_bounds (range_t): The full range of vertical axis values.
#                  horizontal_axis_inverted (bool): If True, inverts the horizontal axis values.
#                  vertical_axis_inverted (bool): If True, inverts the vertical axis values.
#                  horizontal_zero (number_t): The value that represents zero input for the horizontal axis.
#                  vertical_zero (number_t): The value that represents zero input for the vertical axis.
     
#              Initializes a two-axis controller setup where each axis can be individually configured for blind spots, 
#              bounds, zero points, and inversion, enabling precise control over input handling.
#           """
#           HorizontalAxisInput.__init__(self, 
#                                        blindspot_range=horizontal_blindspot_range,
#                                        custom_bounds=horizontal_custom_bounds, 
#                                        axis_inverted=horizontal_axis_inverted,
#                                        zero=horizontal_zero)
#           VerticalAxisInput.__init__(self, 
#                                      blindspot_range=vertical_blindspot_range,
#                                      custom_bounds=vertical_custom_bounds,
#                                      axis_inverted=vertical_axis_inverted,
#                                      zero=vertical_zero)
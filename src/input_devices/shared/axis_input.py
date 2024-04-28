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
        return range_adjust(self.get_x(), axis_blindspot_range, self.__value_range, axis_zero)
      
    
    def get_mapped_x(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Convert the horizontal axis value to a new range.

        Args:
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The horizontal axis value mapped to the new range.
        """
        return map(self.get_x(), *self.__value_range, new_minimum, new_maximum)
    
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
        return map(adjusted_value, *self.__value_range, new_minimum, new_maximum)
         
    

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
        return range_adjust(self.get_y(), axis_blindspot_range, self.__value_range, axis_zero)
    
    def get_mapped_y(self, new_minimum: number_t, new_maximum: number_t) -> number_t:
        """
        Convert the vertical axis value to a new range.

        Args:
            new_minimum (number_t): The lower bound of the new range.
            new_maximum (number_t): The upper bound of the new range.

        Returns:
            number_t: The vertical axis value mapped to the new range.
        """
        return map(self.get_y(), *self.__value_range, new_minimum, new_maximum)
    
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
        return map(adjusted_value, *self.__value_range, new_minimum, new_maximum)
      

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
 
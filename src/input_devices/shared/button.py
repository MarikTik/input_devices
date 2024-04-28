from typing import Callable
from time import perf_counter

callback_t = Callable[[], None]  # Type alias for callback functions that take no parameters and return nothing.

class Button:
    """Encapsulates the functionality of a button on a controller, including state management and event handling."""

    default_debounce_time = 0.04  # Default debounce time set to 40 milliseconds

    def __init__(self, debounce_time=default_debounce_time) -> None:
        """
        Initializes a new Button instance with optional debounce configuration.

        Args:
            debounce_time (float): The minimum amount of time in seconds that must elapse between button state changes 
                                    to consider them valid, preventing "bouncing".
        """
        self.__press_callbacks = set()  # Set of functions to call when button is pressed.
        self.__release_callbacks = set()  # Set of functions to call when button is released.
        self.__state = bool()  # Current state of the button; False for released, True for pressed.
        self.__last_timestamp = perf_counter()  # Time of the last state change to handle debounce.
        self.__debounce_time = debounce_time  # Time threshold to ignore subsequent state changes.

    def on_press(self, *callbacks: callback_t) -> 'Button':
        """
        Registers one or more callbacks to be called when the button is pressed.

        Args:
            callbacks (callback_t): A variadic number of callback functions to register.

        Returns:
            Button: The instance of this class to allow method chaining.
        """
        self.__press_callbacks.update(callbacks)
        return self

    def on_release(self, *callbacks: callback_t) -> 'Button':
        """
        Registers one or more callbacks to be called when the button is released.

        Args:
            callbacks (callback_t): A variadic number of callback functions to register.

        Returns:
            Button: The instance of this class to allow method chaining.
        """
        self.__release_callbacks.update(callbacks)
        return self

    def pressed(self) -> bool:
        """
        Checks if the button is currently pressed.

        Returns:
            bool: True if the button is pressed, False otherwise.
        """
        return self.__state

    def released(self) -> bool:
        """
        Checks if the button is currently released.

        Returns:
            bool: True if the button is released, False otherwise.
        """
        return not self.__state

    def set_debounce_time(self, debounce_time: float) -> None:
        """
        Sets the debounce time for the button.

        Args:
            debounce_time (float): The minimum amount of time in seconds that must elapse between state changes.
        """
        self.__debounce_time = debounce_time

    def _set_state(self, state: bool) -> None:
        """
        Sets the state of the button, applying a debounce filter.

        Args:
            state (bool): The new state of the button (True for pressed, False for released).
        """
        if state == self.__state:
            return  # No state change occurred
        
        timestamp = perf_counter()
        delta_time = timestamp - self.__last_timestamp
        if delta_time < self.__debounce_time:
            return  # State change is ignored due to debounce time
        
        self.__last_timestamp = timestamp
        self.__state = state
        
        # Call the appropriate callbacks based on the new state
        for callback in (self.__press_callbacks if state else self.__release_callbacks):
            callback()

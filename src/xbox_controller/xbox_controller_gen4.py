from inputs import get_gamepad
from ..shared import Button, DirectionalPad, CartesianAxisInput, VerticalAxisInput, AxisTrigger

class XboxControllerGen4:
    """
    Represents an Xbox controller, managing button presses, joystick movements, and trigger inputs. This class encapsulates 
    the full set of controls available on an Xbox controller, organizing their interactions and state updates.
    """

    bumper_debounce_time = 0.07  # Debounce time for bumper buttons in seconds.

    def __init__(self, gamepad=get_gamepad()) -> None:
        """
        Initializes an XboxController instance linked to a specific gamepad device.

        Args:
            gamepad: The gamepad device interface from the 'inputs' library, which reads raw input events.
        """
        self.A = Button()
        self.B = Button()
        self.X = Button()
        self.Y = Button()
        self.select_button = Button()
        self.key_record_button = Button()
        self.start_button = Button()
        self.left_bumper = Button(debounce_time=self.bumper_debounce_time)
        self.right_bumper = Button(debounce_time=self.bumper_debounce_time)
        self.directional_pad = DirectionalPad()
        self.left_stick = AxisTrigger(vertical_axis_inverted=True)
        self.right_stick = AxisTrigger(vertical_axis_inverted=True)
        self.left_trigger = VerticalAxisInput(blindspot_range=(0, 0), custom_bounds=(0, 1023))  # no blindspot, representing pressure-sensitive input
        self.right_trigger = VerticalAxisInput(blindspot_range=(0, 0), custom_bounds=(0, 1023))  # same as left trigger
        self.__gamepad = gamepad

    def update(self) -> None:
        """
        Updates the state of all controller components by reading and processing all recent input events.
        """
        events = self.__gamepad.read()  # Fetch new events from the gamepad
        for event in events:
            self.__update_buttons(event)
            self.__update_triggers(event)

    def __update_buttons(self, event):
        """
        Private method to update the state of buttons based on input events.

        Args:
            event: An input event containing the event code and its state.
        """
        code = event.code
        state = event.state
        # Update button states based on event codes
        self.A._set_state(code == "BTN_SOUTH")
        self.B._set_state(code == "BTN_EAST")
        self.X._set_state(code == "BTN_NORTH")
        self.Y._set_state(code == "BTN_WEST")
        self.select_button._set_state(code == "BTN_SELECT")
        self.key_record_button._set_state(code == "KEY_RECORD")
        self.start_button._set_state(code == "BTN_START")
        self.left_bumper._set_state(code == "BTN_TL")
        self.right_bumper._set_state(code == "BTN_TR")
        
        # Update directional pad state based on joystick hat events
        dp_up_condition = code == "ABS_HAT0Y" and state == -1
        dp_down_condition = code == "ABS_HAT0Y" and state == 1
        dp_left_condition = code == "ABS_HAT0X" and state == -1
        dp_right_condition = code == "ABS_HAT0X" and state == 1

        self.directional_pad.up._set_state(dp_up_condition)
        self.directional_pad.down._set_state(dp_down_condition)
        self.directional_pad.left._set_state(dp_left_condition)
        self.directional_pad.right._set_state(dp_right_condition)
        self.left_stick._set_state(code == "BTN_THUMBL" and state == 1)
        self.right_stick._set_state(code == "BTN_THUMBR" and state == 1)

    def __update_triggers(self, event):
        """
        Private method to update the state of axis triggers based on input events.

        Args:
            event: An input event containing the event code and its state.
        """
        code = event.code
        state = event.state
        # Update axis triggers based on their respective event codes
        if code == 'ABS_X':
            self.left_stick._x = state
        if code == 'ABS_Y':
            self.left_stick._y = state
        elif code == 'ABS_RX':
            self.right_stick._x = state
        elif code == 'ABS_RY':
            self.right_stick._y = state
        elif code == 'ABS_Z':
            self.left_trigger._y = state
        elif code == 'ABS_RZ':
            self.right_trigger._y = state

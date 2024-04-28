from .button import Button

class DirectionalPad:
    """Represents the directional pad (D-pad) on an Xbox controller, consisting of four buttons: up, down, left, and right."""

    def __init__(self) -> None:
        """
        Initializes a new DirectionalPad instance with four directional buttons.
        """
        self.up = Button()  # Button instance for the "up" direction
        self.down = Button()  # Button instance for the "down" direction
        self.left = Button()  # Button instance for the "left" direction
        self.right = Button()  # Button instance for the "right" direction

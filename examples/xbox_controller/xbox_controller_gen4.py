from src.xbox_controller import XboxControllerGen4
from inputs import get_gamepad

#event subscription example
controller = XboxControllerGen4(get_gamepad())
controller.A.on_press(lambda: print("A pressed")) \
          .on_release(lambda: print("A released"), lambda: print("A released x2")) 

# interaction with different types of buttons
controller.directional_pad.up.on_press(lambda: print("D-pad up press"))
controller.directional_pad.left.on_release(lambda: print("D-pad down release"))

while True:
     # updating events and trigger states
     controller.update() 
     # getting mapped x axis value from left stick on the xbox controller
     print(controller.left_stick.get_mapped_x(), new_minimum=-1, new_maximum=1) 
     # getting raw y values from left trigger on the xbox controller
     print(controller.left_trigger.get_y()) # get pressure-sensitive input
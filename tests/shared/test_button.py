from src.shared import Button
from time import sleep

sleep_time = Button.default_debounce_time

def test_on_press_single_subscriber():
     button = Button()
     counter = 0
     def increase_counter():
          nonlocal counter 
          counter += 1
   
     button.on_press(increase_counter)
     sleep(sleep_time)
     button._set_state(True)
     assert counter == 1


def test_on_press_multiple_subscribers():
     button = Button()
     counter = 0
     def increase_counter1():
          nonlocal counter 
          counter += 1
     def increase_counter2():
          nonlocal counter 
          counter += 1

     button.on_press(increase_counter1, increase_counter2)
     sleep(sleep_time)
     button._set_state(True)
     sleep(sleep_time)
     assert counter == 2

def test_on_release_single_subscriber():
     button = Button()
     counter = 0
     def increase_counter():
          nonlocal counter 
          counter += 1

     button.on_release(increase_counter)
     sleep(sleep_time)
     button._set_state(True)
     sleep(sleep_time)
     button._set_state(False)
     assert counter == 1

def test_on_release_multiple_subscribers():
     button = Button()
     counter = 0
     def increase_counter1():
          nonlocal counter 
          counter += 1
     def increase_counter2():
          nonlocal counter 
          counter += 1

     button.on_release(increase_counter1, increase_counter2)
     sleep(sleep_time)
     button._set_state(True)
     sleep(sleep_time)
     button._set_state(False)
     sleep(sleep_time)
     assert counter == 2

def test_press_release_single_subscriber():
     button = Button()
     counter = 0
     def increase_counter():
          nonlocal counter 
          counter += 1

     button.on_press(increase_counter)
     button.on_release(increase_counter)
     sleep(sleep_time)
     button._set_state(True) # press
     sleep(sleep_time)
     button._set_state(False) # release
     assert counter == 2

def test_press_release_multiple_subscribers():
     button = Button()
     counter = 0
     def increase_counter1():
          nonlocal counter 
          counter += 1
     def increase_counter2():
          nonlocal counter 
          counter += 1

     button.on_press(increase_counter1, increase_counter2)
     button.on_release(increase_counter1, increase_counter2)
     sleep(sleep_time)
     button._set_state(True) # press
     sleep(sleep_time)
     button._set_state(False) # release
     sleep(sleep_time)
     assert counter == 4

def test_custom_debounce_time():
     custom_debounce_time = 0.5
     button = Button(custom_debounce_time)
     counter = 0
     def increase_counter():
          nonlocal counter 
          counter += 1

     button.on_press(increase_counter)
     sleep(custom_debounce_time)
     button._set_state(True)
     sleep(custom_debounce_time)
     button._set_state(False)
     sleep(custom_debounce_time)
     button._set_state(True)
     assert counter == 2

def test_quick_press_release():
     button = Button()
     counter = 0
     def increase_counter():
          nonlocal counter 
          counter += 1

     button.on_press(increase_counter)
     button.on_release(increase_counter)
     sleep(sleep_time // 2)
     button._set_state(True) # press
     button._set_state(False) # release
     assert counter == 0
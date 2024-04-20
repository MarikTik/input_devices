from src.shared import CartesianAxisInput
import pytest
from copy import copy

default_value_range = (-32768, 32767)

@pytest.fixture
def cartesian_axis_input():
     return CartesianAxisInput(
          horizontal_value_range=default_value_range, 
          vertical_value_range=default_value_range, 
          horizontal_axis_inverted=False, 
          vertical_axis_inverted=False
     )

@pytest.fixture
def cartesian_axis_input_inverted():
     return CartesianAxisInput(
          horizontal_value_range=default_value_range,
          vertical_value_range=default_value_range,
          horizontal_axis_inverted=True,
          vertical_axis_inverted=True
          )

def test_regular_get(cartesian_axis_input):
     input: CartesianAxisInput = copy(cartesian_axis_input)
     input._set_x(100)
     input._set_y(30)
     assert input.get_x() == 100
     assert input.get_y() == 30
     input._set_x(-50)
     input._set_y(-20)
     assert input.get_x() == -50
     assert input.get_y() == -20

def test_inverted_get(cartesian_axis_input_inverted):
     input: CartesianAxisInput = copy(cartesian_axis_input_inverted)
     input._set_x(100)
     input._set_y(30)
     assert input.get_x() == -100
     assert input.get_y() == -30
     input._set_x(-50)
     input._set_y(-20)
     assert input.get_x() == 50
     assert input.get_y() == 20




 
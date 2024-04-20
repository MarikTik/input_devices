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

def test_adjusted_get(cartesian_axis_input):
     input: CartesianAxisInput = copy(cartesian_axis_input)
     input._set_x(1000)
     input._set_y(1000)
     assert input.get_adjusted_x((-3000, 3000), 0) == 0 # testing blindspot ignore mode
     assert input.get_adjusted_y((-3000, 3000), 0) == 0
     input._set_x(-3001)
     input._set_y(3001)
     assert 0 > input.get_adjusted_x((-3000, 3000), 0) > -3 #estimated value after blindspot range adjustment
     assert 0 < input.get_adjusted_y((-3000, 3000), 0) < 3
     input._set_x(10000)
     input._set_y(-10000)
     assert input.get_adjusted_x((-3000, 3000), axis_zero=1000) - 8471 < 1 # testing zero shift
     assert input.get_adjusted_y((-3000, 3000), axis_zero=-1000) + 8471 < 1




 
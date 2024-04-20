from src.shared import CartesianAxisInput, HorizontalAxisInput, VerticalAxisInput
from pytest import fixture

@fixture
def sample_horizontal_axis_input():
     return HorizontalAxisInput(custom_bounds=(-1, 1), zero=0, axis_inverted=False, blindspot_range=(-0.3, 0.3))

@fixture
def sample_vertical_axis_input():
     return VerticalAxisInput(custom_bounds=(-1, 1), zero=0, axis_inverted=False, blindspot_range=(-0.3, 0.3))


 

def test_horizontal_range_general(sample_horizontal_axis_input):
     axis_input: HorizontalAxisInput = sample_horizontal_axis_input

     axis_input._x = -1
     assert axis_input.get_x() == -1.0
     axis_input._x = 1
     assert axis_input.get_x() == 1.0

def test_horizontal_range_blindspot(sample_horizontal_axis_input):
     axis_input: HorizontalAxisInput = sample_horizontal_axis_input
     axis_input._x = 0
     assert axis_input.get_x_adjusted() == 0
     axis_input._x = 0.2
     assert axis_input.get_x_adjusted() == 0
     axis_input._x = -0.2
     assert axis_input.get_x_adjusted() == 0
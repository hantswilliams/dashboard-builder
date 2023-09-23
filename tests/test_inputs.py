from dashboard_builder.components.inputs import BaseInput
from dashboard_builder.components.inputs import InputSlider_Categorical
from dashboard_builder.components.inputs import InputDropdown
from dashboard_builder.components.inputs import InputRadio

def test_base_input_initialization():
    input_component = BaseInput(name="test", default_value="default")
    assert input_component.name == "test"
    assert input_component.default_value == "default"
    assert input_component.value == "default"

def test_input_slider_categorical_initialization():
    slider = InputSlider_Categorical(name="slider_test", label="Label Test", categories=["A", "B", "C"])
    assert slider.name == "slider_test"
    assert slider.label == "Label Test"
    assert slider.categories == ["A", "B", "C"]
    assert slider.default_value == "Select All"

def test_input_dropdown_initialization():
    dropdown = InputDropdown(name="dropdown_test", label="Label Dropdown", options=["Option1", "Option2"])
    assert dropdown.name == "dropdown_test"
    assert dropdown.label == "Label Dropdown"
    assert dropdown.options == ["Option1", "Option2"]
    assert dropdown.default_value == "Select All"


def test_input_radio_initialization():
    radio = InputRadio(name="radio_test", label="Label Radio", options=["Radio1", "Radio2"])
    assert radio.name == "radio_test"
    assert radio.label == "Label Radio"
    assert radio.options == ["Radio1", "Radio2"]
    assert radio.default_value == "Select All"

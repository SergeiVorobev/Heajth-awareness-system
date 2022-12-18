# forms.py
from django import forms
from django_range_slider.fields import RangeSliderField

class SliderForm(forms.Form):
    name_range_field = RangeSliderField(minimum=30,maximum=300,name="TestName") # with name inside the input field (no label)
    range_field = RangeSliderField(minimum=10,maximum=102) # without name or label
    label_range_field = RangeSliderField(label="TestLabel",minimum=1,maximum=10) # with label (no name)
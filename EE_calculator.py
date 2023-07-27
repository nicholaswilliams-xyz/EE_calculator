"""
Calculate the resistance and tolerances of a resistor based on the chosen colour bands.
Currently works with Python interpreter 3.10
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import re

__author__ = 'Nicholas Williams'

AMPLIFIERS = {"Op-amp": 0,
              "In-amp": 1,
              "Trans-imp-amp": 2}

RLC = {"RC": 0,
       "RL": 1,
       "RLC": 2}

KIRCHHOFF_OHM_WATT = {"Kirchhoff": 0,
                      "Ohm": 1,
                      "Watt": 2}

LED = {"Current limiting resistor": 0}


class EECalculatorApp(App):
    """EECalculatorApp is a Kivy app for electrical and electronics engineers"""
    amplifiers = ListProperty()
    rlc = ListProperty()
    kirchhoff_ohm_watt = ListProperty()
    led = ListProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "EE calculator 1.0"
        self.root = Builder.load_file('EE_calculator.kv')
        self.amplifiers = AMPLIFIERS
        self.rlc = RLC
        self.kirchhoff_ohm_watt = KIRCHHOFF_OHM_WATT
        self.led = LED

        Window.size = (1200, 1000)

        return self.root

    def set_selected_spinner_colour(self, instance):
        """Colour selected spinner and make all other spinners grey."""
        self.root.ids.led_spinner.background_color = 'grey'
        self.root.ids.amplifiers_spinner.background_color = 'grey'
        self.root.ids.rlc_spinner.background_color = 'grey'
        self.root.ids.kirchhoff_ohm_watt_spinner.background_color = 'grey'
        instance.background_normal = ''  # Enable background colours to appear normal, not greyed
        instance.background_color = "green"


EECalculatorApp().run()

from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder


Builder.load_string(
   """
<vehicle parts>:
    name: 'Vehicle Parts'
    MDLabel:
        bold:True
        pos_hint:{"center_x": .5}
        adaptive_size: True
        text: "Sign Left"
        padding: "4dp", "4dp"
        allow_selection: True
        allow_copy: True
        font_size: "48dp"
    MDScrollView:
        orientation:'vertical'
        adaptive_height:True
        pos_hint:{'center_x':.5}
        MDCard:
            orientation:'vertical'
            radius:15
            padding:'15dp'
            spacing:'30dp'
            adaptive_height:True
            pos_hint:{'center_x':.5,}
            MDTextField:
                id: tires
                MDTextFieldHintText:
                    text: "Tires:"
            MDTextField:
                id: car batteries
                MDTextFieldHintText:
                    text: "Car Batteries:"
            MDTextField:
                 id: engine parts
                MDTextFieldHintText:
                    text: "Engine Parts:"
            MDTextField:
                id: car cleaning supplies
                MDTextFieldHintText:
                    text: "Car Cleaning Supplies:"
            MDTextField:
                id: car accessories
                MDTextFieldHintText:
                    text: "Car Accessories:"
            MDBoxLayout:
                adaptive_width: True
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5}
                spacing: "5dp"
            MDButton:
                pos_hint: {"center_x":.5}
                size_hint_y: None
                radius:"4dp"
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
"""
)


class Vehicle_Parts(Screen):
    pass

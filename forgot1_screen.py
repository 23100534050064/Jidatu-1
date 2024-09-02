from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_string(
   """
<Forgot1>:
    name: 'forgot1'
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
                id: email
                MDTextFieldHintText:
                    text: "Email:"
                MDTextFieldHelperText:
                    text: "Remember your password here"
            MDBoxLayout:
                adaptive_width: True
                size_hint: .55, None
                height: "380dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                spacing: "5dp"
                MDCheckbox:
                    id:cd
                    size_hint: None, None
                    width:"30dp"
                    height: "30dp"
                    pos_hint: {"center_x":.5}
                    on_press:
                        passw.password = False if passw.password == True else True
                        passw1.password = False if passw1.password == True else True
                MDLabel:
                    text: "[ref=Show Password]Show Password[/ref]"
                    markup: True
                    pos_hint: cd.pos_hint
                    on_ref_press:
                        cd.active = False if cd.active == True else True
                        passw.password = False if passw.password == True else True
                        passw1.password = False if passw1.password == True else True
            MDButton:
                pos_hint: {"center_x":.5}
                size_hint_y: None
                radius:"4dp"
                on_press: app.change_screen('forgot2')
                MDButtonText:
                    text:"Submit"

                MDButtonIcon:
                    icon:"login"

            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5,"center_y": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_release: app.change_screen('login')
                MDIcon:
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Don't have an account? Sign Up"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
"""
)


class Forgot1(Screen):
    pass

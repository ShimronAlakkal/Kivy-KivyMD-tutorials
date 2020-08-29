from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen

# texxt field using the md code

# class App(MDApp):
#
#     def build(self):
#         main_window = Screen()

        # text field inside the screen
#         field = MDTextField(text='Username',
#                             pos_hint={'center_x': 0.5,
#                                       'center_y': 0.5},
#                             size_hint_x = 0.5,  # horizontal distance of the line  The reatio
#                             size_hint_y = 0.1,  # vertical distance between the line and the text in the field
#                             width=500)  # number of pixels to which the line remains a constant when size_hint_x = None
#
#         main_window.add_widget(field)
#         return main_window
#
# App().run()


# text field with animations using kivy lang

from kivy.lang import Builder


string_to_be_loaded ='''
MDTextField:
    hint_text:'Username'
    helper_text:'Enter your username to  '
    helper_text_mode:'persistent'        # helper text mode is of 2 type on_focus and persistent 
    pos_hint:{'center_x':0.5,'center_y':0.5}
    icon_right:'android'
    icon_right_color:app.theme_cls.primary_color    
    size_hint_x:None
    size_hint_y:None
    width:350
'''
class Builder_app(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Green'
        main_window = Screen()

        builder_field = Builder.load_string(string_to_be_loaded)
        main_window.add_widget(builder_field)
        return main_window

Builder_app().run()
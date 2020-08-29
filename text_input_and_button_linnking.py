from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton , MDFlatButton
from kivymd.uix.dialog import MDDialog

string = '''
MDTextField:
    hint_text:'username'
    helper_text:'enter your username here '
    helper_text_mode:'on_focus'
    icon_right:'eye'
    icon_right_color:app.theme_cls.primary_color
    size_hint_x:0.4
    pos_hint:{'center_x':0.5,'center_y':0.5}
'''

class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()
        self.Username = Builder.load_string(string)

        btn = MDRectangleFlatButton(text='Login',
                                    pos_hint={'center_x':0.5,
                                              'center_y':0.4},
                                    on_release=self.bind_btn)
        screen.add_widget(self.Username)
        screen.add_widget(btn)
        return screen

    def bind_btn(self,obj):
        close = MDFlatButton(text='Close',
                             on_release=self.close_dialogue)

        if self.Username.text == '':
            self.dialog_box = MDDialog(text='Please enter a valid username ... ',
                              title='User check',
                              size_hint_x=0.6,
                              size_hint_y=0.6,
                                   buttons = [close])
        else:
            self.dialog_box = MDDialog(text=self.Username.text
                                  ,title='User check',
                                  size_hint_x=0.6,
                                  size_hint_y=0.6,
                                       buttons = [close])
        self.dialog_box.open()

    def close_dialogue(self,obj):
        self.dialog_box.dismiss()
App().run()
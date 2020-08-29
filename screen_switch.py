from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.core.window import Window
Window.size = (325,600)

main_string = '''

ScreenManager:
    MenuScreen:
    ProfileScreen:
    
<MenuScreen>:
    name:'main_screen'
    MDFlatButton:
        text:'Time screen'
        on_release: root.manager.current = 'time_screen'

<ProfileScreen>:
    name:'time_screen'
        MDLabel:
            text:'Heythere'
            pos_hint:{'center_x':0.5,'center_y':0.5}
        MDFlatButton:
            text:'return'
            on_release:root.manager.current = 'main_screen'
'''

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass  # as there is nothing to be done using code in here because its all done above in the mulitiline string

screen_manager =ScreenManager()
screen_manager.add_widget(MenuScreen(name='main_screen'))
screen_manager.add_widget(ProfileScreen(name='time_screen'))

class App(MDApp):

    def build(self):

        return Builder.load_string(main_string)


App().run()
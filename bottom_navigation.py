from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget

Window.size = (325, 600)

# promo must contain an image of your's and a navigation drawer
# the Invite screen must contain a text , which is the name of the org , once clicked go to the other screen < use boxlayout >

main_string = '''
MDBottomNavigation:
    MDBottomNavigationItem:
        text:'Home'
        name:'main_screen_home'
        icon:'home'
        MDBoxLayout:
            orientation:'vertical'
            MDLabel:
                text : 'WELCOME HOME' 

    MDBottomNavigationItem:
        text:'Task'
        name:'main_screen_task'
        icon:'library'
        MDBoxLayout:
            orientation:'vertical'
            MDLabel:


'''


class App(MDApp):

    def build(self):
        return Builder.load_string(main_string)
    # def on_start(self):
    #     for i in range(20):
    #         list = TwoLineAvatarListItem(text='Jhonny' + str(i))
    #         image = ImageLeftWidget(source=r'C:\Users\hp\Desktop\ml\data\panda.png')
    #         list.add_widget(image)
    #         self.root.ids.list_of_lists.add_widget(list)


App().run()

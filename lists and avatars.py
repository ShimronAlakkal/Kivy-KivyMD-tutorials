from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.list import ImageLeftWidget

helper_string = '''
Screen :
    ScrollView:
        MDList:
            id:list_of_lists 
'''


class App(MDApp):

    def build(self):
        load_variable = Builder.load_string(helper_string)

        return load_variable

    def on_start(self):
        for i in range(17):
            list = TwoLineIconListItem(text='Jhonny' + str(i))
            image = ImageLeftWidget(source=r'C:\Users\hp\Desktop\ml\data\panda.png')
            list.add_widget(image)
            self.root.ids.list_of_lists.add_widget(list)


App().run()

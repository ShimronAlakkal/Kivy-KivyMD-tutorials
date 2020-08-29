from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.menu import  MDDropdownMenu,MDMenuItem

# this part is currently in research by me ,
# i have to know the documentation about hoew this is going to work
# bsaically how to add a dropdown item to a dropadown menu like in a list





from kivymd.uix.dropdownitem import MDDropDownItem


menu='''
BoxLayout:
    MDToolbar:
        right_action_items:[['dots-horizontal',lambda x: app.dropdown_open()]]
        title:'dropdown'
        # for the bg colour of the tool bar
        md_bg_color : app.theme_cls.primary_color
        
        
 
'''

class App(MDApp):
    def build(self):
        return Builder.load_string(menu)

    def dropdown_open(self):
        self.dd = MDDropdownMenu()
        self.menu_item = MDMenuItem(text='item 1')
        self.dd.add_widget(self.menu_item)
        self.dd.open()


App().run()
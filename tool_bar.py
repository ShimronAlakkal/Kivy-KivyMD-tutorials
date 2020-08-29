from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350,600)

string = '''
Screen:
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'ToolBar'
            halign:'center'
            theme_text_color:'Primary'
            left_action_items:[['human',lambda x:app.nav_release()]]
            elevation : 10
            
        MDLabel:
            text:'TRENSTANCE'
            font_style :'H4'
            halign:'center'
            theme_text_color:'Secondary'
        
        MDBottomAppBar:
            MDToolbar:
                left_action_items:[['home',lambda x:app.nav_release()],['library-video',lambda x:app.nav_release()]]
                type:'bottom'
                mode:'end'
                icon:'human'
                on_action_button:app.nav_release()
'''
count=1
class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette ='Yellow'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = "Light"
        builder_string = Builder.load_string(string)

        return builder_string
    def nav_release(self):
        global count
        print('cliked the menu icon ',count,' times ')
        count += 1
App().run()
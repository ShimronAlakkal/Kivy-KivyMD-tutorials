from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
Window.size = (350,600)

nav = '''
Screen:
    NavigationLayout:   
    
        MDNavigationDrawer:
            id:drw_nav  # what this basically does is that it actually incorporates the action button with the movement of the navigation drwawer 
            BoxLayout :
                orientation: 'vertical'
                spacing:'0dp'
                padding:'20dp'
                Image:
                    source : r'C:\\Users\\hp\\Desktop\\ml\\data\\panda.png'
                BoxLayout:
                    orientation:'vertical'
                    padding:'-29dp'
                    spacing:'8dp'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:'Logout'
                                secondary_text:'Hey man how is it going today'
                                IconLeftWidget:
                                    icon: 'logout'
                            OneLineIconListItem:
                                text:'History'  
                                IconLeftWidget:
                                    icon: 'history'

                MDLabel:
                    text:'Shimron'
                    font_style :'Subtitle1'
                    theme_text_color:'Custom'
                    text_color:(0/123.0,0/234.0,0/231.9,1)
                    size_hint_x:None
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:
                    text:'shimron.alakkal1804@gmail.com'
                    font_style :'Caption'
                    theme_text_color:'Secondary'
                    size_hint_y:None
                    height:self.texture_size[1]
        
        ScreenManager:
            Screen:
            
                MDTextField:
                    id:username
                    hint_text:'Username'
                    helper_text:'Enter your username  '
                    helper_text_mode:'on_focus'        # helper text mode is of 2 type on_focus and persistent 
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    icon_right:'human'
                    icon_right_color:app.theme_cls.primary_color    
                    size_hint_x:0.7
                    size_hint_y:None
                    width:350
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Nav Draw'
                        left_action_items :[['menu',lambda x : drw_nav.toggle_nav_drawer()]]
                        elevation:10
                    
                    
                    MDBottomAppBar:
                        MDToolbar:
                            mode:'end'
                            type:'bottom'
                            on_action_button: app.main_btn()
                    
                    Widget:
'''

class App(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Pink'
        bilder = Builder.load_string(nav)
        return bilder
    def main_btn(self):
        on_close = MDFlatButton(text='Close',
                                on_release=self.on_close_flat)
        self.log = MDDialog(title='Main_button',
                            text='you are logged in as '+str(self.root.ids.username.text),
                            size_hint_x=0.8,
                            size_hint_y=0.8,
                            buttons=[on_close])

        self.log.open()

    def on_close_flat(self,obj):
        self.log.dismiss()

App().run()
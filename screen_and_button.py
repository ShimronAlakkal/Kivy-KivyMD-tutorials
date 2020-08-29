# this is a topic on screen and buttons
'''
screens can be thoght as the window of your android/ios app > the main window
'''

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton , MDIconButton , MDRectangleFlatButton ,MDFloatingActionButton
from kivymd.uix.screen import Screen

class App(MDApp):

    def build(self):
        main_window = Screen()
        button_on_screen = MDIconButton(icon='language-python',
                                        pos_hint = {'center_x':0.5,       # position hint : buttons position in X axis
                                                    'center_y':0.5})      # in the Y axis
        flat_button = MDFlatButton(text='Login using your ID',
                                   pos_hint = {'center_x':1,
                                               'center_y':1})
        rect_button = MDRectangleFlatButton(text = 'Submit',
                                            pos_hint = {'center_x':0,
                                                        'center_y':0})
        floaticon_button = MDFloatingActionButton(icon='library-video',
                                                  pos_hint={'center_x':0.2,
                                                            'center_y':0.2})

        '''
        quick note : pos_hint ={center_x:point_on_x_axis , center_y : position_on_the_y_axis }
         '''

        main_window.add_widget(button_on_screen)
        main_window.add_widget(flat_button)
        main_window.add_widget(rect_button)
        main_window.add_widget(floaticon_button)
        return main_window

App().run()
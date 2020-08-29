# create a kivymd app that has got data tables in it to show , obviously , data

from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
Window.size = (350,600)

class APP(MDApp):

    def build(self):

        screen_root = Screen()
        data_table_in_screen = MDDataTable(
            column_data = [
                ('Employee',dp(40)),
                ('Age',dp(10)),
                ('position',dp(30))
            ],
            row_data = [
                ('Shawn','17','CDO'),
                ('Jaiden John','16','ML/AI head'),
                ('Sanand G Dev','17','Algorithms expert'),
                ('Yan Chummar','17','Software Dev'),
                ('Sahil','17','IDK'),
                ('Sharoon','18','Analytics head'),
                ('Nived','17','Web Dev')
            ],
            check=True,
            pos_hint = {'center_x':0.5,
                        'center_y':0.5},
            size_hint_x=0.9,
            size_hint_y=0.6,
            rows_num = 7
        )

        data_table_in_screen.bind(on_check_press = self.check_press)
        data_table_in_screen.bind(on_row_press=self.row_press)

        screen_root.add_widget(data_table_in_screen)
        return screen_root

    # def check_press(self,instance_table,current_row):
    #     self.dlog = MDDialog(title='Check Press',
    #                          text=self.current_row[0].text)
    #     self.dlog.open()
    #
    # def row_press(self,instance_row,instance_table):
    #     self.dlog = MDDialog(title=self.current_row[0].text,
    #                          text ='hey there I am using shimron\'s app' )
    #     self.dlog.open()

# APP().run()

    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)

    def row_press(self,instace_table,instace_row):
        print(instace_row)
APP().run()
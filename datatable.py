from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#kv codes
Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustomLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5

<CustomLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')

class DataTable(BoxLayout):
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)

        data = {
            '1':{0:'TESTa',1:'Sample1a',2:'Sample2a',3:'Sample3a'},
            '2':{0:'TESTb',1:'Sample1b',2:'Sample2b',3:'Sample3b'},
            '3':{0:'TESTc',1:'Sample1c',2:'Sample2c',3:'Sample3c'},
        } #data store

        column_titles = [x for x in data.keys()]
        rows_length = len(data[column_titles[0]])
        self.columns = len(column_titles)

        table_data = []
        for y in column_titles:
            table_data.append({'text':str(y),'size_hint_y':None,'height':30,'bcolor':(.05,.30,.80,1)}) #append the data

        for z in range(rows_length):
            for y in column_titles:
                table_data.append({'text':str(data[y][z]),'size_hint_y':None,'height':20,'bcolor':(.06,.25,.50,1)}) #append the data

        self.ids.table_floor_layout.cols = self.columns #define value of cols to the value of self.columns
        self.ids.table_floor.data = table_data #add table_data to data value

class DataTableApp(App):
    def build(self):
        return DataTable()

if __name__=='__main__':
    DataTableApp().run()
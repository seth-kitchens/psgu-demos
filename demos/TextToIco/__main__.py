import PySimpleGUI as sg
import psgu
from psgu import ge

import cairo

info_main_window = ge.InfoBuilder() \
    .text('To Be Added')

class MainWindow(psgu.AbstractBlockingWindow):
    def __init__(self) -> None:
        super().__init__(title='TextToIco')
    
    def get_layout(self):
        layout = [
            [sg.Graph(canvas_size=(300, 300), graph_bottom_left=(0, 0), graph_top_right=(300, 300), key='ImagePreview')],
            [
                sg.Text('Text'),
                sg.Input('', key='TextInput')
            ],
            [
                sg.Text('Text Color'),
                sg.Input('', key='TextColor')
            ]
        ]
        return layout
    
    def define_events(self):
        super().define_events()
        self.event_value_exit(sg.WIN_CLOSED)
    
def main():
    main_window = MainWindow()
    window_context = psgu.WindowContext()
    wrc = main_window.open(window_context)
    if wrc.check_success():
        pass

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label

KV = '''
<MainScreen>:
    orientation: 'vertical'
    padding: 15
    spacing: 12

    Label:
        text: '[b]TIKSPARK v3.4 PRO[/b]\\nلوحة إدارة الحسابات'
        markup: True
        font_size: '22sp'
        size_hint_y: None
        height: '80dp'

    Label:
        id: path_label
        text: 'لم يتم اختيار ملف الحسابات'
        text_size: self.width, None
        halign: 'center'
        size_hint_y: None
        height: '60dp'

    Button:
        text: 'اختيار ملف الحسابات'
        size_hint_y: None
        height: '50dp'
        on_release: root.pick_file()

    Button:
        text: 'قراءة الحسابات'
        size_hint_y: None
        height: '50dp'
        on_release: root.read_file()

    Label:
        id: status
        text: 'الحالة: جاهز'
        size_hint_y: None
        height: '45dp'

    ScrollView:
        GridLayout:
            id: results
            cols: 1
            size_hint_y: None
            height: self.minimum_height
'''

class MainScreen(BoxLayout):
    file_path = ''

    def pick_file(self):
        chooser = FileChooserListView(
            path='/storage/emulated/0/Download',
            filters=['*.txt', '*'],
            dirselect=False
        )
        layout = BoxLayout(orientation='vertical', spacing=8)
        layout.add_widget(chooser)
        buttons = BoxLayout(size_hint_y=None, height='48dp')
        popup = Popup(title='اختر ملف الحسابات',
                      content=layout, size_hint=(0.95, 0.85))
        cancel = Button(text='إلغاء')
        choose = Button(text='اختيار')
        buttons.add_widget(cancel)
        buttons.add_widget(choose)
        layout.add_widget(buttons)
        cancel.bind(on_release=popup.dismiss)

        def select_file(*args):
            if chooser.selection:
                self.file_path = chooser.selection[0]
                self.ids.path_label.text = self.file_path
                self.ids.status.text = 'تم اختيار الملف'
            popup.dismiss()

        choose.bind(on_release=select_file)
        popup.open()

    def read_file(self):
        self.ids.results.clear_widgets()
        if not self.file_path:
            self.ids.status.text = 'اختر ملف الحسابات أولاً'
            return
        try:
            with open(self.file_path, encoding='utf-8-sig') as f:
                lines = [x.strip() for x in f if ':' in x]
            users = [x.split(':', 1)[0].strip() for x in lines]
            users = [u for u in users if u]
            for i, username in enumerate(users, 1):
                self.ids.results.add_widget(Label(
                    text=f'{i}. {username}',
                    size_hint_y=None, height='38dp'
                ))
            self.ids.status.text = f'تمت قراءة {len(users)} حساباً'
        except Exception as e:
            self.ids.status.text = f'تعذر فتح الملف: {e}'

class TikSparkApp(App):
    def build(self):
        self.title = 'TIKSPARK Dashboard'
        Builder.load_string(KV)
        return MainScreen()

if __name__ == '__main__':
    TikSparkApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class RafiqRemote(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        title = Label(text='RAFIQ REMOTE CONTROL', font_size=24)
        m20 = Button(text='Connect Samsung M20')
        redmi = Button(text='Connect Redmi 12')
        status = Label(text='Status: Waiting for connection')
        layout.add_widget(title)
        layout.add_widget(m20)
        layout.add_widget(redmi)
        layout.add_widget(status)
        return layout

RafiqRemote().run()

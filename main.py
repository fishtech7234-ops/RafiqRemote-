from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class RafiqRemote(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=25
        )

        title = Label(
            text='REMOTE CONTROL',
            font_size=28
        )

        m20 = Button(
            text='Connect M20',
            font_size=22
        )

        redmi = Button(
            text='Connect Redmi',
            font_size=22
        )

        status = Label(
            text='Status: Ready',
            font_size=18
        )

        layout.add_widget(title)
        layout.add_widget(m20)
        layout.add_widget(redmi)
        layout.add_widget(status)

        return layout

RafiqRemote().run()

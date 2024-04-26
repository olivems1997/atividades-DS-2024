from kivy.app import App
from kivy.uix.boxlayout import boxt.ayout
from kivy.uix.label import Label

class RotuloApp (App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.labl = Label(
            text = 'senai',color=[1, 0, 0, 1],
            foot_size=40, bold=True
        )
         self.lab2 = Label(
            text = 'sesi',color=[0, 1, 0, 1],
            foot_size=40, italic=True
        )
         self.lab3 = Label(
            text = 'Enem',color=[0, 0, 0, 1],
            foot_size=40, font_name='arial',
            underline=True
        )
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return Label(text="Olá senai!", font_size=100, font_name='arial',
             halign='left',
             valign='top',
             size_hint=(None, None),
             size=(150, 50),
             text_size=(150, None)
        )
if __name__ == "__main__":
     MinhaApp().run()
    
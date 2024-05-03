from kivy.app import App
from kivy.uix.switch import switch 
class MinhaApp(App):
    def build(self):
        return switch(active=false)

if __name__ == "__main__":
    MinhaApp().run()
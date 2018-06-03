from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel

class Tabla(TabbedPanel):
    pass


class VentanaTablaApp(App):
    def build(self):
        return Tabla()


if __name__ == '__main__':
    VentanaTablaApp().run()

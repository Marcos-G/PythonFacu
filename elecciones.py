from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel

class SelectorFacultades(TabbedPanel):
    pass

class VentanaTablaApp(App):
    def build(self):
        return SelectorFacultades()


if __name__ == '__main__':
    VentanaTablaApp().run()

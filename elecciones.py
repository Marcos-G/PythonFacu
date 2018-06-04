from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ListProperty

class SelectorFacultades(TabbedPanel):
    tabla=[[[[0 for q in range(10)] for w in range(5)] for e in range(5)] for r in range(13)]
    data=ListProperty(tabla)
    pass

class VentanaTablaApp(App):
    def build(self):
        return SelectorFacultades()


if __name__ == '__main__':
    VentanaTablaApp().run()

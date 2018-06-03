from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string("""

<Test>:
    do_default_tab: False

    TabbedPanelItem:
        text: 'FAD'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FCA'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    TabbedPanelItem:
        text: 'FCAI'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))
    TabbedPanelItem:
        text: 'FCE'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FCEN'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FCM'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FCPyS'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FD'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FE'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FFyL'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FI'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'FO'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'Rectorado'
        Label:
            text: 'First tab content area'

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()

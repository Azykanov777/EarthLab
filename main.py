import kivy
from kivymd.app import MDApp
from kivy.uix.label import *
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["clock",lambda x: app.clock_draw()]]
            elevation: 15

        MDLabel:
            text: 'Hello World'
            halign: 'center'


        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["coffee",lambda x: app.clock_draw()]]
                mode: 'end'
                type: 'bottom'
                no_action_button: app.clock_draw()





"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(seif):
        print("Hi")

    def clock_draw(self):
        print("clock")


DemoApp().run()
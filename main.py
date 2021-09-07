import os
os.environ["KIVY_TEXT"] = "pil"

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class PreSplashScreen(MDScreen):
    
    def login_screen_call(self, dt):
        self.manager.current = 'login_screen'
        


class LoginScreen(MDScreen):

    def on_enter_button(self):
        #self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'


class HomeScreen(MDScreen):
    pass



class FaithSchedulerApp(MDApp):
    def build(self):
        Builder.load_file('mainscreen.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget((PreSplashScreen(name='pre_splash')))
        screen_manager.add_widget((LoginScreen(name='login_screen')))
        screen_manager.add_widget((HomeScreen(name='home_screen')))

        return screen_manager



if __name__ == '__main__':

    FaithSchedulerApp().run()

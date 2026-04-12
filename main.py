from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
import os

class SplashScreen(Screen):
    def on_enter(self):
        # طلب الأذونات اللي اتفقنا عليها
        request_permissions([
            Permission.RECORD_AUDIO, 
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE
        ])
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="NOVA AI", font_size='80sp', color=(0, 1, 1, 1)))
        layout.add_widget(Label(text="Welcome Malek Al-Hacker", font_size='25sp', color=(1, 1, 1, 1)))
        self.add_widget(layout)
        Clock.schedule_once(self.go_to_main, 5)

    def go_to_main(self, dt):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # زرار حرف الـ N (محرك نوفا)
        self.btn_n = Button(text="N", size_hint=(None, None), size=(250, 250),
                           pos_hint={'center_x': 0.5}, font_size='100sp',
                           background_color=(0, 0.7, 0.9, 1))
        self.btn_n.bind(on_press=self.nova_engine)
        
        # أزرار الأدوات (تطبيقات وملفات)
        tools = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_apps = Button(text="APPS", background_color=(0.2, 0.2, 0.2, 1))
        btn_files = Button(text="FILES", background_color=(0.2, 0.2, 0.2, 1))
        
        btn_apps.bind(on_press=lambda x: os.system("am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER"))
        btn_files.bind(on_press=lambda x: os.system("am start -a android.intent.action.GET_CONTENT -t */*"))

        tools.add_widget(btn_apps)
        tools.add_widget(btn_files)
        
        layout.add_widget(Label(text="NOVA SYSTEM ACTIVE", font_size='25sp', color=(0, 1, 1, 1)))
        layout.add_widget(self.btn_n)
        layout.add_widget(tools)
        self.add_widget(layout)

    def nova_engine(self, instance):
        # تشغيل المايك
        os.system("am start -a android.speech.action.RECOGNIZE_SPEECH")

class NovaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    NovaApp().run()
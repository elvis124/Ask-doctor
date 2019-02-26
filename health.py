from __future__ import unicode_literals
from kivy.app import App
from kivy.config import Config
Config.set('input', 'multitouchscreen1', 'tuio,192.168.2.22:3306')
Config.set('postproc','desktop','1')
Config.set('kivy','exit_on_escape','1')
Config.set('kivy','log_enable','1')
Config.set('kivy', 'log_maxfiles', '-1')
Config.set('widgets', 'scroll_friction','float')
Config.set('widgets', 'scroll_distance', '4')
Config.set('graphics','borderless','0')
Config.set('graphics','rotation','0')
Config.set('graphics','full_screen','1')
Config.set('graphics','allow_screensaver','1')
Config.set('graphics','kivy_clock','free_all')
Config.set('widgets', 'scroll_distance', '4')
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor=(0,0,0,0)
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen,WipeTransition, SwapTransition
import os
import sys
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.listview import ListItemButton, ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.interactive import InteractiveLauncher
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.core.image import Image
from kivy.graphics import Color,Rectangle, Line
from kivy.uix.actionbar import ActionBar,ActionView,ActionGroup,ActionButton,ActionPrevious, ActionView,ActionOverflow, ContextualActionView
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.loader import Loader
from kivy.support import install_twisted_reactor
from kivy.adapters.models import SelectableDataItem

#Homepage 
class Homepage(Screen):
    def __init__(self, **kwargs):
        super(Homepage, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    #function for gprs calculation
    def n_profile(self, *args):
        data = 'Range: Max 2km range longitude: 12345435 lat: 2435436643'
        self.ids['n_location'].text=data
    #function for loading lsit of doctors of patients
    def listofcon(self, **kwargs):
        self.text = TextInput(multline=False, size_hint=(.2, .2))
        self.ids['listview'].add_widget(self.text)
    #list for loading messages
    def messages(self, *args):
        self.msg = TextInput(multline=False, size_hint=(.2, .2))
        self.ids['listview'].add_widget(self.msg)
    #list for loading the chats
    def n_chats(self, *args):
        self.chats = Label(text='fhfhfhfhfh', size_hint=(.2, .2))
        self.ids['listview'].add_widget(self.chats)

#class for image selection
class Imagesel(GridLayout):
    def __init__(self, **kwargs):
        super(Imagesel, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    cancel = ObjectProperty(None)
    def loading(self, path, filename):
        with open(os.path.join(path, filename[0])) as image:
            self.sound = Image(source=image)
            return self.sound
#class for profile settings 
class My_profile(Screen):
    def __init__(self, **kwargs):
        super(My_profile, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    def __init__(self, **kwargs):
        super(My_profile, self). __init__(**kwargs)
        with self.canvas.before:
            Color(1,1,1,0)
    def profile_photo(self, *args):
        from kivy.factory import Factory
        self.image = Button(text='image', size_hint=(.2, .1), on_press=self.photo)
        self.label = Label(text='proffesion', size_hint=(.1, .1))
        self.text  = TextInput(multline=False, size_hint=(1,.1),hint_text='lab tech: Mr.luke, surgeon: Dr.ian, pedetrician, nurse, artist')
        self.hobbies = Label(text='Hobbies', size_hint=(.1,.1))
        self.text_in = TextInput(multline=False, size_hint=(1,.1), hint_text='football, swimming, karate, boxing, wacthing, praying, singing ')
        self.but = Button(text='update', size_hint=(.2, .1), on_press=self.update)
        for data in [self.image, self.label, self.text, self.hobbies, self.text_in, self.but]:
            self.ids['display_layout'].add_widget(data)
    def photo(self,*args):
        im = Imagesel()
        self.pop = Popup(title='iamge', title_align='center',content = im, size_hint=(1,1) )
        self.pop.open()
    def update(self, *args):
        self.ids['display_layout'].clear_widgets()
        print('jhgygyfg')
    def status(self, *args):
        self.text = TextInput(multline=False, hint_text='Status: Today am feelings good, thanks to my creator', size_hint=(1, .1))
        self.but = Button(text='push_online', size_hint=(.2, .1), background_color=[0,1,0,1], on_press=self.up)
        for s in [self.text, self.but]:
            self.ids['display_layout'].add_widget(s)
    def up(self, *args):
        self.ids['display_layout'].clear_widgets()
        print('still in process')
    def privacy(self, *args):
        self.la = Label(text='My_status', size_hint=(.2, .1))
        self.spinner = Spinner(text='public', values=('private', 'only_me'), size_hint=(.2, .1))
        self.lla = Label(text='profile', size_hint=(.2, .1))
        self.sspinner = Spinner(text='public', values=('private', 'only_me'), size_hint=(.2, .1))
        self.dla = Label(text='location', size_hint=(.2, .1))
        self.dspinner = Spinner(text='public', values=('private', 'only_me'), size_hint=(.2, .1))
        self.pla = Label(text='proffesion', size_hint=(.2, .1))
        self.pspinner = Spinner(text='public', values=('private', 'only_me'), size_hint=(.2, .1))
        self.hla = Label(text='hobbies', size_hint=(.2, .1))
        self.hspinner = Spinner(text='public', values=('private', 'only_me'), size_hint=(.2, .1))
        self.but = Button(text='update', size_hint=(.2, .1), pos_hint={'top': .1},on_press=self.updater)
        for privacy in [self.la, self.spinner, self.lla, self.sspinner, self.dla, self.dspinner, self.pla, self.pspinner, self.hla, self.hspinner, self.but]:
            self.ids['display_layout'].add_widget(privacy)
    def updater(self, *args):
        print('okay we will do the backend ')
        self.ids['display_layout'].clear_widgets()
    def about(self,*args):
        self.text = TextInput(hint_text='location', size_hint=(1, .9))
        self.e = Button(text='exit', size_hint=(.1, .1), on_press=self.dis, background_color=[1,1,1,0])
        for value in [self.text, self.e]:
            self.ids['display_layout'].add_widget(value)
    def dis(self, *args):
        self.ids['display_layout'].clear_widgets()


#class containing the patient details
class Patient_details(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(Patient_details, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos

    def n_Register(self, *args):
        for data in  str(self.ids['n_username'].text) and str(self.ids['n_full_name'].text) and str(self.ids['n_email_address'].text) and str(self.ids['n_postion'].text) and str(self.ids['n_password'].text) and str(self.ids['n_confirm_password'].text):
            if True:
                from kivy.storage.jsonstore import JsonStore
                store = JsonStore('patient.json')
                store.put('data', data=data)
            else: 
                raise ImportError



#classs for capturing doctors detials
class Doctors_details(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(Doctors_details, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rect.size = self.size
        self.rect.pos= self.pos
    def nn_Register(self, *args):
        print('sjcnaihnkb')

#patients registration
class Registering(GridLayout):
    def __init__(self, **kwargs):
        super(Registering, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        self.cols=1
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
        self.label = Label(text='validating your details')
        self.add_widget(self.label)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
#class for registering doctors
class Doctors_section(StackLayout):
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Doctors_section, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        self.cols=1
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
        self.label = TextInput(hint_text='code send to phone',size_hint=(1, .5), is_focusable=True)
        self.but = Button(text='verfy', size_hint=(1, .5), on_press=self.validating)
        for widgets in [self.label, self.but]:
            self.add_widget(widgets)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    def validating(self, *args):
        Doc = Docone(cancel=self.dismiss)
        self._p = Popup(title='connecting.......................................................', title_align='center', content=Doc,  size_hint=(1, 1))
        self._p.open()
        Clock.schedule_once(self.dismiss, 10)
    def dismiss(self, *args):
        self._p.dismiss()
#backend of doctors registration process
class Docone(GridLayout):
    cancel = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Docone, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.after:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
            data = 'sfgnruibgdjvnek'
            self.ids['doctors_registration'].text=data
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos

#class for registering 
class Register_patients(Screen):
    def __init__(self, **kwargs):
        super(Register_patients, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    def n_Register(self, *args):
        contentpopone = Registering(cancel=self.dismissone)
        self.contentpop = Popup(title='capruring', title_align='center', content=contentpopone, size_hint=(1 ,1))
        self.contentpop.open()
        Clock.schedule_once(self.dismissone, 10)
        self.manager.current='loginpage'
    def dismissone(self, *args):
        self.contentpop.dismiss()


#section for doctors details
class Register_Doctors_details(Screen):
    def __init__(self, **kwargs):
        super(Register_Doctors_details, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos
    def nn_Register(self, *args):
        connone = Doctors_section(cancel=self.dismissme)
        self.conn = Popup(title='Registering ', title_align='center', content=connone, size_hint=(.2,.2))
        self.conn.open()
        Clock.schedule_once(self.dismissme, 10)
        self.manager.current='loginpage'
    def dismissme(self, *args):
        self.conn.dismiss()
#login page 
class Loginpage(Screen):
    def __init__(self, **kwargs):
        super(Loginpage, self). __init__(**kwargs)
        self.bind(size=self.update_rec, pos=self.update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rec = Rectangle(size=self.size, pos=self.pos)
    def update_rec(self, *args):
        self.rec.size=self.size
        self.rec.pos = self.pos

    def verifycredentials(self):
            print('waiting for backend')
            self.manager.current='homepage'

    def n_register(self, *args):
        print('prepare your documents')
        self.manager.current='register'
    def register_as_doc(self, *args):
        print('hallpow')
        self.manager.current='doctors_section'

    def screen_postion():
        print('Hllo')



#screen ,manager
class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('health.kv')
class healthApp(App):
    def build(self):
        self.icon = 'icons/watch.png'
        return kv_file



             

if __name__ =='__main__':
    healthApp().run()

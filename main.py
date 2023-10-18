from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import instaloader

class InstagramDownloaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        self.label = Label(text='Enter Instagram Username:', font_size=16)
        self.username_input = TextInput(hint_text='Username', multiline=False, font_size=16)
        self.download_button = Button(text='Download Profile Picture', font_size=16)
        self.download_button.bind(on_press=self.download_profile_pic)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.download_button)
        
        return self.layout

    def download_profile_pic(self, instance):
        username = self.username_input.text

        if not username:
            return  # Don't proceed if the input is empty

        try:
            loader = instaloader.Instaloader()
            loader.download_profile(username, profile_pic_only=True)
            message = f'Profile picture for {username} downloaded successfully!'
        except Exception as e:
            message = f'Error: {str(e)}'

        self.label.text = message

if __name__ == '__main__':
    InstagramDownloaderApp().run()

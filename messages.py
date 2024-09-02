from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import RoundedRectangle, Color

class ShopProfile(BoxLayout):
    def __init__(self, shop_name, profile_image, profile_desc, message_count, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5
        self.padding = [10, 10, 10, 5]

        # Profile section
        profile_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=100)
        profile_img = Image(source=profile_image, size_hint=(None, None), size=(80, 80))
        profile_desc_label = Label(text=profile_desc, size_hint=(None, None), size=(200, 80), text_size=(200, None), valign='middle', halign='left')
        
        profile_layout.add_widget(profile_img)
        profile_layout.add_widget(profile_desc_label)

        # Message count section
        message_count_label = Label(
            text=f"Total Messages: {message_count}",
            size_hint_y=None,
            height=40,
            font_size='16sp',
            color=(0, 0, 0, 1)  # Text color
        )
        
        # Add profile and message count to main profile layout
        self.add_widget(profile_layout)
        self.add_widget(message_count_label)

class MessagesScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        shops = {
            'Shop 1': {
                'messages': ['Unauza shilingi 1000...', 'Unauza shilingi 2000...', 'Unauza shilingi 3000...'],
                'profile_image': 'shop1_profile.jpg',
                'profile_desc': 'Shop 1: Best deals in town!'
            },
            'Shop 2': {
                'messages': ['Unauza shilingi 4000...', 'Unauza shilingi 5000...', 'Unauza shilingi 6000...'],
                'profile_image': 'shop2_profile.jpg',
                'profile_desc': 'Shop 2: Quality products guaranteed.'
            },
            'Shop 3': {
                'messages': ['Unauza shilingi 7000...', 'Unauza shilingi 8000...', 'Unauza shilingi 9000...'],
                'profile_image': 'shop3_profile.jpg',
                'profile_desc': 'Shop 3: Friendly service.'
            },
            'Shop 4': {
                'messages': ['Unauza shilingi 10000...', 'Unauza shilingi 11000...', 'Unauza shilingi 12000...'],
                'profile_image': 'shop4_profile.jpg',
                'profile_desc': 'Shop 4: Great prices and variety.'
            },
            'Shop 5': {
                'messages': ['Unauza shilingi 13000...', 'Unauza shilingi 14000...', 'Unauza shilingi 15000...'],
                'profile_image': 'shop5_profile.jpg',
                'profile_desc': 'Shop 5: Your one-stop shop.'
            },
        }

        # ScrollView for better view if many shops
        scroll_view = ScrollView(size_hint=(1, 1))
        grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for shop_name, details in shops.items():
            shop_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
            shop_layout.height = 350

            # Add shop profile
            profile = ShopProfile(
                shop_name,
                details['profile_image'],
                details['profile_desc']
            )
            shop_layout.add_widget(profile)

            # Add messages
            for message in details['messages']:
                message_btn = MessageButton(text=message)
                shop_layout.add_widget(message_btn)

            # Add shop layout to grid layout
            grid_layout.add_widget(shop_layout)

        scroll_view.add_widget(grid_layout)
        self.add_widget(scroll_view)

class MessagesApp(App):
    def build(self):
        return MessagesScreen()

if __name__ == '__main__':
    MessagesApp().run()


from kivy.uix.button import Button

class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.font_size = '24sp'
        self.size_hint = (1, 0.1)
        self.background_color = (0.2, 0.2, 0.2, 1)  # Dark grey background
        self.color = (1, 1, 1, 1)  # White text color

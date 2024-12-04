import reflex as rx

class ChatState(rx.State):
    form_data: dict = {}

    @classmethod
    def get_form_data(cls):
        return cls.form_data

    @rx.event
    def update_text(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
    
    
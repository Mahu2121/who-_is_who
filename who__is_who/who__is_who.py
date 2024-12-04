import reflex as rx

from who__is_who import style

from rxconfig import config


class ChatState(rx.State):
    form_data: dict = {}

    @rx.event
    def update_text(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
    
    @classmethod
    def get_form_data(cls):
        return cls.form_data



def chat():
    return rx.vstack(
        rx.form(
            rx.hstack(

                rx.input(
                    name="question",
                    placeholder = "Introduce la característica a buscar",   
                    style = style.chat_style,
                ),

                rx.button(
                    "Enviar", 
                    type="submit",
                    style = style.button_style,
                ),
        ),
        on_submit=ChatState.update_text,
        reset_on_submit=True,
        margin_top = "80%",
    ),
    )
    
def index():
    return rx.container(
        rx.heading("Bienvenido al Who is Who",font_size = "10px" , as_ = "h1"),
        chat(),
),


app = rx.App()
app.add_page(index)



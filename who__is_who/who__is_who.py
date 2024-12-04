import reflex as rx

from who__is_who import style

from rxconfig import config

from .estado import ChatState

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



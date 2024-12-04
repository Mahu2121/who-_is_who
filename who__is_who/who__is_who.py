import reflex as rx

from who__is_who import style

from rxconfig import config

from .estado import ChatState

from .reconocer_caracteristicas import depurar_personajes 

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
        on_submit= handle_form_submit, 
        reset_on_submit=True,
        margin_top = "80%",
    ),
    )

def handle_form_submit(form_data):

    ChatState.update_text(form_data)
    
    depurar_personajes()
    
def index():
    return rx.container(
        rx.heading("Bienvenido al Who is Who",font_size = "10px" , as_ = "h1"),
        chat(),
),


app = rx.App()
app.add_page(index)



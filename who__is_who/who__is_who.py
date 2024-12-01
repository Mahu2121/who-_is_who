import reflex as rx

from who__is_who import style

from rxconfig import config


class ChatState(rx.State):
    text: str = ""

    @rx.event
    def update_text(self, new_text:str):
        self.text = new_text


def chat() -> rx.Component:
    return rx.container(
        rx.hstack(

            rx.input(default_value=ChatState.text, 
                placeholder = "Haz una pregunta sobre tu personaje en mente",   
                on_change=ChatState.update_text,
                style = style.chat_style,
                ),

            rx.button("Enviar", 
                on_click=lambda: ChatState.update_text(ChatState.text),
                style = style.button_style,
                ),
        ),margin_top = "80%",
    )

def index():
    return rx.container(
    rx.heading("Bienvenido al Who is Who",font_size = "10px" , as_ = "h1"),
    chat(),
    )

app = rx.App()
app.add_page(index)



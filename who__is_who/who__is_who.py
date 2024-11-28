import reflex as rx

from who__is_who import style

from rxconfig import config

def chat() -> rx.Component:
    return rx.vstack(
        rx.input(placeholder="Haz una pregunta sobre tu personaje en mente", style=style.chat_style),
        margin_top="850px"
    )

def index():
    return rx.container(
    rx.heading("Bienvenido al Who is Who",font_size="10px" , as_="h1"),
    chat()
    )

app = rx.App()
app.add_page(index)



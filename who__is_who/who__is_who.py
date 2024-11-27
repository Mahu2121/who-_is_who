import reflex as rx

from rxconfig import config


def index():
    return rx.heading("Bienvenido al Who is Who",font_size="10px" , as_="h1")




app = rx.App()
app.add_page(index)



import reflex as rx

from rxconfig import config


def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="10px" , as_="h1"),
            rx.grid(
                rx.foreach(
                rx.Var.range(24),lambda i: rx.card(height="28vh", width="140px" ),
                    
                    ),
                    columns="8",    
                    spacing="3",
                    width="65%",
                    margin_left="230px",
                    
                    
            )
    )


app = rx.App()
app.add_page(index)



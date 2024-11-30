import reflex as rx
from who__is_who.randomizer import randomizer
from who__is_who.estado import State

def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="9px" , as_="h1"),
    rx.box(
            rx.grid(
                rx.foreach(
                rx.Var.range(24),lambda i: rx.card(height="28vh", width="140px" ),
                    
                    ),
                    columns="8",
                    spacing="3",
                    width="65%",
                    margin_left="300px",
                    margin_top="70px",
                    on_click=State.randomizer,
            )
    )
    )

app = rx.App()
app.add_page(index)
app._compile()


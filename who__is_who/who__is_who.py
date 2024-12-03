import reflex as rx
from who__is_who.estado import State
def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="9px" , as_="h1"),
    rx.box(
            rx.grid(
                
                
                rx.card( height="28vh",width="140px" ,color_scheme="tomato"),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                rx.card(height="28vh", width="140px" ),
                    
                    
                    columns="8",
                    spacing="6",
                    width="65%",
                    margin_left="300px",
                    margin_top="5px",
                    on_click=State.randomizer,
            ),
    ),
    ),
    
app = rx.App()
app.add_page(index)
app._compile()
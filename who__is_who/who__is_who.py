import reflex as rx
from who__is_who.estado import state


def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="9px" , as_="h1"),
    rx.box(
            rx.grid(
                
                
                rx.card(rx.image(src="/alex.png"),height="28vh",width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/alfred.png"),height="28vh", width="140px",background_color="tomato" ),
                rx.card(rx.image(src="/anita.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/anne.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/bernard.png"),height="28vh", width="140px",background_color="tomato" ),
                rx.card(rx.image(src="/bill.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/charles.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/claire.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/david.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/eric.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/frans.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/george.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/hernan.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/joe.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/maria.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/max.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/paul.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/peter.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/philip.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/richard.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/robert.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/sam.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/susan.png"),height="28vh", width="140px" ,background_color="tomato"),
                rx.card(rx.image(src="/tom.png"),height="28vh", width="140px",background_color="tomato" ),
                    
                    columns="8",
                    spacing="6",
                    width="65%",
                    margin_left="300px",
                    margin_top="5px",
                    on_click=state.randomizer
            ),
    ),
    ),
    
app = rx.App()
app.add_page(index)
app._compile()

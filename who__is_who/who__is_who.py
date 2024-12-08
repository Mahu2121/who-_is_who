import reflex as rx
from who__is_who.estado import state


def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="60px" , margin_top="20px",as_="h1",text_align="center"),
    rx.box(
            rx.grid(
                
                
                rx.card(rx.cond(state.empezar,rx.image(src="/alex.png")),height="24vh",width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/alfred.png")),height="24vh", width="115px",background_color="tomato" ),
                rx.card(rx.cond(state.empezar,rx.image(src="/anita.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/anne.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/bernard.png")),height="24vh", width="115px",background_color="tomato" ),
                rx.card(rx.cond(state.empezar,rx.image(src="/bill.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/charles.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/claire.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/david.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/eric.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/frans.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/george.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/hernan.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/joe.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/maria.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/max.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/paul.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/peter.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/philip.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/richard.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/robert.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/sam.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/susan.png")),height="24vh", width="115px" ,background_color="tomato"),
                rx.card(rx.cond(state.empezar,rx.image(src="/tom.png")),height="24vh", width="115px",background_color="tomato" ),
                    
                    
                    columns="8",
                    spacing="6",
                    width="65%",
                    margin_left="300px",
                    margin_top="40px",
                    
                    
            ),

                rx.button("Empezar",padding="10px",position="absolute",top="800px",background_color="tomato",on_click=[state.ponerImagenes,state.randomizer]),
                
                rx.cond(state.empezar,
                        rx.fragment(
                
                rx.input(on_change=state.set_texto_input,placeholder = "Adivina el personaje aqui", width="550px",margin_left="60%",border_width="3px",margin_top="30px",)
                ,rx.button(
                    "Adivinar",
                    on_click=state.adivinar,
                    position="absolute",
                    left="1700px",
                    top="820px",
                ),
                    rx.text(state.adivinaste),    ),



                ),),)

app = rx.App()
app.add_page(index)
app._compile()
import reflex as rx
from who__is_who.estado import state
from .diccionario_caracteristicas2 import diccionario
from who__is_who import style
import pydeps



def index():
    return rx.box(rx.heading("Bienvenido al Who is Who",font_size="60px" , margin_top="20px",as_="h1",text_align="center"),
    rx.box(
    rx.grid(
        *[
            rx.card(
                rx.cond(
                    state.empezar,
                    rx.image(src=f"/{nombre.lower()}.png")  
                ),
                height="24vh",
                width="115px",
                background_color= rx.cond(state.keys.contains(nombre) ,"tomato","blue"),
                
            )
            for nombre in diccionario().keys()
        ], 
        columns="8",
        spacing="6",
        width="65%",
        margin_left="300px",
        margin_top="40px",
                    
    )
),

                rx.button("Empezar",padding="10px",position="absolute",top="800px",background_color="tomato",on_click=[state.randomizer, state.ponerImagenes]),
                
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
                    rx.text(state.adivinaste),
                    rx.vstack(
        rx.form(
            rx.hstack(

                rx.input(
                    name="question",
                    placeholder = "Introduce la característica a buscar",
                    style = style.chat_style,
                ),

                
        ),
        on_submit= state.handle_submit,
        reset_on_submit=True,
        
    ),
    ),),
                    


                ),
    
)



app = rx.App()
app.add_page(index)
app._compile()
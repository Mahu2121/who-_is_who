import reflex as rx



from rxconfig import config


from .diccionario_caracteristicas2 import diccionario

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
        on_submit= ChatState.handle_submit, 
        reset_on_submit=True,
        margin_top = "80%",
    ),
    )

        
class ChatState(rx.State):
    form_data: dict = {}
    datos: dict = diccionario()

    def handle_submit(self,form_data: dict):
        self.update_text(form_data)
        self.depurar_personajes(form_data.get("question"))


    @rx.event
    def update_text(self, form_data: dict):
        print(form_data)
        self.form_data = form_data

    @rx.event
    def depurar_personajes(self,caracteristica: str):

        diccionario_nuevo = {}

        for personaje, caracteristicas in self.datos.items():

            if  caracteristica in caracteristicas:
                diccionario_nuevo.update({personaje:caracteristicas})

        self.datos = diccionario_nuevo

    
        print(self.datos)

    
def index():
    return rx.container(
        rx.heading("Bienvenido al Who is Who",font_size = "10px" , as_ = "h1"),
        chat(),
),



app = rx.App()
app.add_page(index)



import reflex as rx

from .diccionario_caracteristicas import diccionario

class ChatState(rx.State):
    form_data: dict = {}


    @rx.event
    def update_text(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
        

    def depurar_personajes(self) :

        datos = diccionario()
        caracteristica_buscada = ChatState.form_data

        encontrados = []
        no_encontrados = []

        for personaje, caracteristicas in datos.items():

            if caracteristica_buscada in caracteristicas:
                encontrados.append(personaje)
    
            else:
                no_encontrados.append(personaje)

        print(encontrados)
        print(no_encontrados)

        return encontrados, no_encontrados
    
        
    
    
import reflex as rx

from .estado import ChatState

from diccionario_caracteristicas import diccionario





def depurar_personajes():

    caracteristica_buscada = ChatState.get_form_data()

    encontrados = []
    no_encontrados = []

    for personaje, caracteristicas in diccionario.items():

        if caracteristica_buscada in caracteristicas:
            encontrados.append(personaje)
    
        else:
            no_encontrados.append(personaje)
        
    print(encontrados)

    print(no_encontrados)
    

        
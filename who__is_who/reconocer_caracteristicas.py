import reflex as rx

from .estado import ChatState

from .diccionario_caracteristicas import diccionario

datos = diccionario()
caracteristica_buscada = ChatState.imput.form_data
def depurar_personajes() :

    encontrados = []
    no_encontrados = []

    for personaje, caracteristicas in datos.items():

        if caracteristica_buscada in caracteristicas:
            encontrados.append(personaje)
    
        else:
            no_encontrados.append(personaje)
    print(encontrados)
    print(no_encontrados)
    
        

from .who__is_who import ChatState

from diccionario_caracteristicas import diccionario


encontrados = []
no_encontrados = []

def depurar_personajes():
    for personaje, caracteristicas in diccionario.items():

        if form_data in caracteristicas:
            encontrados.append(personaje)
    
        else:
            no_encontrados.append(personaje)

print(encontrados)

print(no_encontrados)

        
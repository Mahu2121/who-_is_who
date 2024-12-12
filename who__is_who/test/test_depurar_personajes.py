from who__is_who.diccionario_caracteristicas2 import diccionario

def depurar_personajes(caracteristica : str):

        
        datos = diccionario()

        diccionario_nuevo = {}

        caracteristicas_personaje = datos.get("David")


        print("caracteristicas personaje final:", caracteristicas_personaje)

        if caracteristica not in caracteristicas_personaje:

            personas_eliminadas = []
            for personas in datos:
                if caracteristica in datos[personas]:
                    personas_eliminadas.append(personas)

            for personas in personas_eliminadas:
                del datos[personas]



        for personaje, caracteristicas in datos.items():

            if  caracteristica in caracteristicas:
                diccionario_nuevo.update({personaje:caracteristicas})

        datos = diccionario_nuevo
        return datos 
        

if __name__ == "__main__":
    resultado = depurar_personajes("rubio")
    print("Test segun el imput'rubio':", resultado)

    resultado2 = depurar_personajes("castaño")
    print("Test segun el imput 'castaño':", resultado2)

    resultado3 = depurar_personajes("barba")
    print("Test segun el imput 'barba':", resultado3)

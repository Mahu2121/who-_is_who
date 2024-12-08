from diccionario_caracteristicas import diccionario

def depurar_personajes(self) :

        datos = diccionario()
        caracteristica_buscada = self.form_data.get("question")

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
    
import reflex as rx

from who__is_who.diccionario_caracteristicas2 import diccionario
import random
from who__is_who.randomizer import randomizer






class state(rx.State):
    name_diccionarioo= diccionario()
    form_data: dict = {}
    datos: dict = diccionario()

    personaje: str = ""
    final: str = ""
    adivinaste: str = ""
    texto_input: str = ""
    empezar: bool = False
    guess: bool = False
    def ponerImagenes(self):
        self.empezar = not self.empezar

    def randomizer(self):
        self.final = random.choice(list(self.name_diccionarioo.keys()))
        self.adivinaste = ""

    texto_input: str=""
    def adivinar(self):
        self.guess = not self.guess
        if self.texto_input.lower() == self.final.lower():
            self.adivinaste = f"¡Ganaste! El personaje era {self.final}."
            
        else:
            self.adivinaste = f"Perdiste. El personaje era {self.final}."
            

    def handle_submit(self,form_data: dict):
        self.update_text(form_data)
        self.depurar_personajes(form_data.get("question"))

    @rx.var
    def keys(self):       #*lista de keys del diccionario*
        return list(self.datos.keys())   #conversión de las claves de un diccionario a una lista

    
    @rx.event
    def update_text(self, form_data: dict):
        print(form_data)
        self.form_data = form_data

    @rx.event
    def depurar_personajes(self,caracteristica: str):

        diccionario_nuevo = {}
        caracteristicas_personaje = self.datos.get(self.final)     #dentro del diccionario coje el personaje seleccionado por el random

        print(caracteristicas_personaje)
        if caracteristica not in caracteristicas_personaje:         #se asegura que la caractristica(imput) está dentro de del los valores del personaje seleccionado por el random

            print("El personaje no tiene esta caracteristica")      #si no está -> printea eso

            return

        for personaje, caracteristicas in self.datos.items():       #bucle for por cada "key de personaje (nombre de personaje) y sus valores" en los items(key:value) del diccionario

            if  caracteristica in caracteristicas:                  #si la caracteristica(imput) está en los valores del personaje, añade al diccionario el personaje con sus valores
                diccionario_nuevo.update({personaje:caracteristicas})

        self.datos = diccionario_nuevo                              #iguala el diccionario inicializado por la clase de estado al diccionario nuevo para solo almacenar los que cumplen el if (los que tienen su caracteristica dentro de los valores del personaje seleccionado por random)

    
        print(self.datos)                                       
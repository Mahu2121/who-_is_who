import reflex as rx

from who__is_who.diccionario_caracteristicas2 import diccionario
import random







class state(rx.State):
    name_diccionarioo= diccionario()
    form_data: dict = {}
    datos: dict = diccionario()
    personas_eliminadas:list = []
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
    def keys(self) -> list:
        return list(self.datos.keys())

    
    @rx.event
    def update_text(self, form_data: dict):
        
        self.form_data = form_data

    @rx.event
    def depurar_personajes(self,caracteristica: str):

        diccionario_nuevo = {}
        caracteristicas_personaje = self.datos.get(self.final)

        
        if caracteristica not in caracteristicas_personaje:

            self.personas_eliminadas = []
            for personas in self.datos:
                if caracteristica in self.datos[personas]:
                    self.personas_eliminadas.append(personas)

            for personas in self.personas_eliminadas:
                del self.datos[personas]

                
            return

        for personaje, caracteristicas in self.datos.items():

            if  caracteristica in caracteristicas:
                diccionario_nuevo.update({personaje:caracteristicas})

        self.datos = diccionario_nuevo

    
        




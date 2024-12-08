import reflex as rx

from who__is_who.diccionario_caracteristicas import diccionario
import random
from who__is_who.randomizer import randomizer






class state(rx.State):
    name_diccionarioo= diccionario()

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
            
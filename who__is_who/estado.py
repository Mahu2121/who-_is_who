import reflex as rx

from who__is_who.diccionario_caracteristicas import diccionario
import random
from who__is_who.randomizer import randomizer






class state(rx.State):
    name_diccionarioo={"Susan":["mujer","blanco", "largo"], "Claire":["mujer","pelirroja","corto","gafas","sombrero",], "David":["hombre","rubio","corto","barba"], "Anne":["mujer","castaño","corto","pendientes"],
                "Robert":["hombre","castaño","corto"], "Anita":["mujer","rubia","largo"], "Joe":["hombre","rubio","corto","gafas"], "George":["hombre","blanco","corto","sombrero"],
                "Bill": ["hombre","pelirrojo","semicalvo","perilla"], "Alfred":["hombre","pelirrojo","largo","bigote"], "Max":["hombre","castaño","corto","bigote"],"Tom":["hombre","castaño","semicalvo","gafas"],
                "Alex": ["hombre","castaño","corto","bigote"], "Sam": ["hombre","blanco","semicalvo","gafas"], "Richard": ["hombre","castaño","semicalvo","barba"], "Paul":["hombre","blanco","corto","gafas"] ,
                "Maria":["mujer","castaño","largo","boina","pendientes"], "Frans":["hombre","pelirrojo","corto"], "Herman": ["hombre", "pelirrojo", "semicalvo"], "Bernard":["hombre","castaño","corto","gorro"],
                "Philip":["hombre","castaño","corto","barba"],"Eric":["hombre","rubio","corto","gorra"], "Charles":["hombre","rubio","corto","bigote"], "Peter":["hombre","blanco","corto"]}

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
            
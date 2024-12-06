import reflex as rx

from who__is_who.diccionario_caracteristicas import diccionario
import random
from who__is_who.randomizer import randomizer
class state(rx.State):
    personaje: str=""
    empezar: bool = False

    def ponerImagenes(self):
        self.empezar = not self.empezar

    def randomizer(self):
        info_perso=diccionario()
        random.choice(list(info_perso.keys()))
        

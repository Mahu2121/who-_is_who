
import pytest

from who__is_who.depurar_personajes import depurar_personajess

diccionario_test = {
    "Susan": ["mujer", "blanco", "largo"],
    "David": ["hombre", "rubio", "corto", "barba"],
    "Joe": ["hombre", "rubio", "corto", "gafas"]
}


def test_depurar_personajes_rubio():
    datos = diccionario_test.copy()  
    resultado = depurar_personajess("rubio", datos)
    assert resultado == {
        "David": ["hombre", "rubio", "corto", "barba"],
        "Joe": ["hombre", "rubio", "corto", "gafas"]
    }


def test_depurar_personajes_barba():
    datos = diccionario_test.copy()  
    resultado = depurar_personajess("barba", datos)
    assert resultado == {
        "David": ["hombre", "rubio", "corto", "barba"]
    }

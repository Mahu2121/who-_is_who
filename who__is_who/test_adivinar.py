import reflex as rx
import unittest
from who__is_who.estado import state
import pytest

class TestAdivinar(unittest.TestCase):

    def setUp(self):
        
        self.state = state()


    def test_ganaste(self):

        self.state.final = "Sam"
        self.state.texto_input = "sam"
        self.state.adivinar()
        self.assertEqual(
            self.state.adivinaste,
            "¡Ganaste! El personaje era Sam."

        )

    def test_perdiste(self):

        self.state.final = "Bernard"
        self.state.texto_input = "pablo"
        self.state.adivinar()
        self.assertEqual(
            self.state.adivinaste,
            "Perdiste. El personaje era Bernard"
        )



if __name__ == "__main__":
    unittest.main()
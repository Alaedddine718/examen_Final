import unittest
import os
from proceso import Proceso
from repositorio import RepositorioProcesos

class TestRepositorio(unittest.TestCase):
    def test_agregar_proceso(self):
        repo = RepositorioProcesos()
        p = Proceso("X", 4, 1)
        repo.agregar(p)
        self.assertEqual(len(repo.listar()), 1)

  

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

    def test_pid_duplicado(self):
        repo = RepositorioProcesos()
        p1 = Proceso("X", 4, 1)
        p2 = Proceso("X", 3, 2)
        repo.agregar(p1)
        with self.assertRaises(ValueError):
            repo.agregar(p2)

    def test_guardar_y_cargar_json(self):
        repo = RepositorioProcesos()
        repo.agregar(Proceso("A", 5, 1))
        repo.guardar_json("test.json")

        nuevo_repo = RepositorioProcesos()
        nuevo_repo.cargar_json("test.json")
        self.assertEqual(len(nuevo_repo.listar()), 1)
        os.remove("test.json")

if __name__ == "__main__":
    unittest.main() 

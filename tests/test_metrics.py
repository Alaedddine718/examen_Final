import unittest
from proceso import Proceso
from metrics import calcular_metricas

class TestMetrics(unittest.TestCase):
    def test_metricas(self):
        p1 = Proceso("P1", 4, 1)
        p2 = Proceso("P2", 2, 1)
        p1.tiempo_inicio = 0
        p1.tiempo_fin = 4
        p2.tiempo_inicio = 4
        p2.tiempo_fin = 6

        metricas = calcular_metricas([p1, p2])
        self.assertAlmostEqual(metricas["respuesta_media"], 2.0)
        self.assertAlmostEqual(metricas["retorno_media"], 3.0)
        self.assertAlmostEqual(metricas["espera_media"], 1.0)

if __name__ == "__main__":
    unittest.main()

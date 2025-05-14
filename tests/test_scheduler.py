import unittest
from proceso import Proceso
from scheduler import FCFSScheduler, RoundRobinScheduler

class TestScheduler(unittest.TestCase):
    def test_fcfs(self):
        p1 = Proceso("A", 4, 1)
        p2 = Proceso("B", 3, 1)
        scheduler = FCFSScheduler()
        resultado = scheduler.planificar([p1, p2])
        self.assertEqual(resultado, [("A", 0, 4), ("B", 4, 7)])



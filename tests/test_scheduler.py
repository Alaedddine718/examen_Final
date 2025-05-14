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
    def test_round_robin(self):
        p1 = Proceso("P1", 4, 1)
        p2 = Proceso("P2", 3, 1)
        scheduler = RoundRobinScheduler(2)
        resultado = scheduler.planificar([p1, p2])
        pids = [e[0] for e in resultado]
        self.assertIn("P1", pids)
        self.assertIn("P2", pids)
        self.assertGreaterEqual(len(resultado), 3)  # debe haber varias entradas

if __name__ == "__main__":
    unittest.main()

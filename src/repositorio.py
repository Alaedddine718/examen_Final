import json
import csv
from proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = []

    def agregar(self, proceso):
        for p in self.procesos:
            if p.pid == proceso.pid:
                raise ValueError("PID duplicado")
        self.procesos.append(proceso)

    def listar(self):
        return self.procesos

    def eliminar(self, pid):
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def obtener(self, pid):
        for p in self.procesos:
            if p.pid == pid:
                return p
        return None

    def guardar_json(self, archivo):
        datos = []
        for p in self.procesos:
            datos.append({
                "pid": p.pid,
                "duracion": p.duracion,
                "prioridad": p.prioridad
            })
        with open(archivo, 'w') as f:
            json.dump(datos, f)

    
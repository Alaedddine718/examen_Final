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

    def cargar_json(self, archivo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
        self.procesos = []
        for d in datos:
            proceso = Proceso(d["pid"], d["duracion"], d["prioridad"])
            self.procesos.append(proceso)

    def guardar_csv(self, archivo):
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, archivo):
        with open(archivo, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.procesos = []
            for fila in reader:
                proceso = Proceso(fila['pid'], int(fila['duracion']), int(fila['prioridad']))
                self.procesos.append(proceso)

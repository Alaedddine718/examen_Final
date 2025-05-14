from proceso import Proceso
from scheduler import FCFSScheduler, RoundRobinScheduler
from repositorio import RepositorioProcesos
from metrics import calcular_metricas

def mostrar_procesos(procesos):
    for p in procesos:
        print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}")

def main():
    repo = RepositorioProcesos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar proceso")
        print("2. Listar procesos")
        print("3. Guardar en JSON")
        print("4. Cargar desde JSON")
        print("5. Ejecutar FCFS")
        print("6. Ejecutar Round Robin")
        print("0. Salir")
        opcion = input("> ")

        if opcion == "1":
            pid = input("PID: ")
            dur = int(input("Duración: "))
            prio = int(input("Prioridad: "))
            proceso = Proceso(pid, dur, prio)
            repo.agregar(proceso)

    

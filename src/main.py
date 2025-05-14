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

        elif opcion == "2":
            mostrar_procesos(repo.listar())

        elif opcion == "3":
            repo.guardar_json("procesos.json")
            print("Guardado en procesos.json")

        elif opcion == "4":
            repo.cargar_json("procesos.json")
            print("Cargado desde procesos.json")

        elif opcion == "5":
            scheduler = FCFSScheduler()
            gantt = scheduler.planificar(repo.listar())
            print("Diagrama de Gantt:", gantt)
            print("Métricas:", calcular_metricas(repo.listar()))

        elif opcion == "6":
            q = int(input("Quantum: "))
            scheduler = RoundRobinScheduler(q)
            gantt = scheduler.planificar(repo.listar())
            print("Diagrama de Gantt:", gantt)
            print("Métricas:", calcular_metricas(repo.listar()))

        elif opcion == "0":
            break

if __name__ == "__main__":
    main()

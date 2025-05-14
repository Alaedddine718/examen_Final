class Proceso:
    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser positiva.")
       

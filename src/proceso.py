class Proceso:
    def __init__(self, pid, duracion, prioridad):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser positiva.")
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None



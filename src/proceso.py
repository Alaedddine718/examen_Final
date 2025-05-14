class Proceso:
    def __init__(self, pid, duracion, prioridad):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser positiva.")
      



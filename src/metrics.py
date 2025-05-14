def calcular_metricas(procesos):
    suma_respuesta = 0
    suma_espera = 0
    suma_retorno = 0
    n = len(procesos)

    for p in procesos:
        respuesta = p.tiempo_inicio - p.tiempo_llegada
        retorno = p.tiempo_fin - p.tiempo_llegada
        espera = retorno - p.duracion

        suma_respuesta += respuesta
        suma_retorno += retorno
        suma_espera += espera
    
    return {
        "respuesta_media": suma_respuesta / n if n > 0 else 0,
        "retorno_media": suma_retorno / n if n > 0 else 0,
        "espera_media": suma_espera / n if n > 0 else 0
    }

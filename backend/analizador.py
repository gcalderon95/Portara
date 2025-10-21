# analizador.py
from collections import deque, Counter
from generador import generar_evento

MAX_EVENTOS = 100
eventos = deque(maxlen=MAX_EVENTOS)

def agregar_evento(evento):
    
    eventos.append(evento)

def generar_evento_agregar():
    
    evento = generar_evento()
    agregar_evento(evento)
    return evento

def obtener_metricas():
    
    estados_counts = Counter()
    ip_counts = Counter()
    auth_failures = 0

    for e in eventos:
        estados_counts[e['status_code']] += 1
        ip_counts[e['ip']] += 1
        if e['status_code'] == 400:
            auth_failures += 1

    metricas = {
        "total_eventos": len(eventos),
        "estados_counts": dict(estados_counts),
        "ip_counts": dict(ip_counts),
        "auth_failures": auth_failures
    }
    return metricas

if __name__ == "__main__":
    import time
    while True:
        e = generar_evento_agregar()
        print(e)
        time.sleep(0.5)

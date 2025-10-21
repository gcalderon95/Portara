from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analizador import agregar_evento, generar_evento_agregar, obtener_metricas
import threading
import time

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generador_trasero():
    while True:
        generar_evento_agregar()  
        time.sleep(0.5)


threading.Thread(target=generador_trasero, daemon=True).start()


@app.get("/metricas")
def metricas():
    return obtener_metricas()

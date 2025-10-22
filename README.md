# 🛰️ Portara

**Portara** es una aplicación web de monitorización y análisis de actividad de seguridad. Fue desarrollada como prueba técnica para un proceso de selección.  

Integra **backend en Python con FastAPI** y **frontend en Vue.js con Vite**.

---

## 📁 Estructura del Proyecto
```
Portara/
├── backend/
│ ├── analizador.py # Analiza logs y métricas
│ ├── generador.py # Genera datos de prueba
│ └── main.py # Servidor FastAPI
├── frontend/
│ ├── index.html
│ ├── package.json
│ └── src/
│ ├── components/
│ │ ├── GraficoErrores.vue
│ │ ├── TablaIP.vue
│ │ ├── TablaLoginFail.vue
│ │ └── TarjetasMetricas.vue
│ └── views/
│ └── Dashboard.vue
└── README.md
```

---

## ⚡ Funcionalidades

### Backend
- Servidor FastAPI en **Python 3.10.12**.
- Endpoints para métricas de actividad.
- Procesamiento y análisis de logs.
- Generación de datos de prueba.

### Frontend
- Dashboard interactivo construido con **Vue.js 3**.
- Componentes visuales: gráficos de errores, intentos de login fallidos, métricas clave.
- Estilos modernos con **TailwindCSS**.
- Compatible con **Node.js v20.19.5**.

---

## 🔗 Endpoint Principal (Backend)

| Método | Ruta       | Descripción                    |
|--------|------------|--------------------------------|
| GET    | /metrics   | Devuelve métricas para el dashboard |

---

## Tecnologías
- Python 3.10.12 + FastAPI
- JavaScript + Vue.js 3
- Vite como bundler
- TailwindCSS para estilos
- Componentes modulares Vue (SFC)

---

## 🚀 Instalación y Ejecución

### Backend
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```
### Frontend
```bash
cd frontend
npm install
npm run dev
```








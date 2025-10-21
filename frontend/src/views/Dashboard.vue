<template>
  <div class="dashboard">
    <h1>Security Logs Dashboard</h1>

    <!-- Métricas -->
    <div class="metrics">
      <TarjetasMetricas title="Total Líneas Analizadas" :value="metrics.total_eventos" class="primary"/>
      <TarjetasMetricas title="Total Errores" :value="metrics.estados_counts?.['500'] || 0" class="error"/>
      <TarjetasMetricas title="Intentos Fallidos Login" :value="metrics.auth_failures" class="warning"/>
    </div>

    <!-- Tablas y gráfico -->
    <div class="middle">
      <TablaIP :data="ipData" class="left"/>
      <GraficoErrores :data="errorData" class="right"/>
    </div>

    <TablaLoginFail :data="loginData" class="full-width"/>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import TarjetasMetricas from '../components/TarjetasMetricas.vue'
import TablaIP from '../components/TablaIP.vue'
import TablaLoginFail from '../components/TablaLoginFail.vue'
import GraficoErrores from '../components/GraficoErrores.vue'

export default {
  components: { TarjetasMetricas, TablaIP, TablaLoginFail, GraficoErrores },
  setup() {
    const metrics = ref({})
    const ipData = ref([])
    const loginData = ref([])
    const errorData = ref([])

    const fetchMetrics = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/metricas')
        const data = await res.json()
        metrics.value = data
        ipData.value = Object.entries(data.ip_counts || {}).map(([ip, count]) => ({ ip, count }))
        loginData.value = [{ user: 'demo', fails: data.auth_failures || 0 }]
        errorData.value = Object.entries(data.estados_counts || {}).map(([status, count]) => ({ status, count }))
      } catch (err) {
        console.error(err)
      }
    }

    onMounted(() => {
      fetchMetrics()
      setInterval(fetchMetrics, 5000)
    })

    return { metrics, ipData, loginData, errorData }
  }
}
</script>

<style scoped>
/* Variables para Tema Oscuro */
:root {
    --bg-main: #1e1e2f; /* Fondo principal oscuro */
    --bg-card: #27293d; /* Fondo de tarjetas */
    --text-main: #e0e0e0; /* Color de texto principal */
    --text-secondary: #9a9a9a; /* Color de texto secundario */
    --accent-red: #eb5757; /* Rojo para errores */
    --accent-green: #27ae60; /* Verde para éxito/acceso */
    --accent-blue: #5688e4; /* Azul para información */
    --accent-yellow: #f2c94c; /* Amarillo para advertencia */
    --border-color: #3f4158; /* Color de borde y separadores */
    --shadow-dark: rgba(0, 0, 0, 0.4);
}

/* Contenedor principal */
.dashboard {
    max-width: 1400px; /* Aumentamos el ancho para más espacio */
    margin: 0 auto;
    padding: 30px 20px;
    font-family: 'Inter', sans-serif; /* Recomendable usar una fuente moderna */
    background-color: var(--bg-main);
    color: var(--text-main);
    min-height: 100vh;
}

/* Encabezado */
.dashboard h1 {
    text-align: left; /* Título alineado a la izquierda */
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 30px;
    color: white; /* Blanco puro para el título */
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 15px;
}

/* Tarjetas métricas */
.metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 columnas iguales */
    gap: 20px;
    margin-bottom: 30px;
}
.metrics > * {
    /* Aquí se aplican los estilos base de la tarjeta */
    flex: 1; 
    background-color: var(--bg-card); /* Fondo oscuro de la tarjeta */
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px var(--shadow-dark);
    transition: all 0.3s ease;
    border: 1px solid var(--border-color); /* Borde sutil */
}

/* Adaptación de clases de color a la nueva estética */
.primary, .error, .warning { 
    background-color: var(--bg-card); /* Mismo fondo para todos, solo cambiamos el acento */
    color: var(--text-main); 
    /* Necesitarás pasar una prop para el color del valor,
       o usar CSS para apuntar a un elemento dentro de TarjetasMetricas */
}

/* Contenedor de tabla IP y gráfico */
.middle {
    display: grid;
    grid-template-columns: 1fr 2fr; /* Columna Izquierda (Tabla) más pequeña, Derecha (Gráfico) más grande */
    gap: 20px;
    margin-bottom: 30px;
}
.middle > * {
    background-color: var(--bg-card);
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px var(--shadow-dark);
    border: 1px solid var(--border-color);
}
.middle .left { 
    /* La tabla IP ahora ocupa 1/3 del espacio */
    grid-column: span 1; 
}
.middle .right { 
    /* El gráfico ahora ocupa 2/3 del espacio */
    grid-column: span 1;
}

/* Tabla login fail */
.full-width {
    width: 100%;
    padding: 25px;
    background-color: var(--bg-card);
    border-radius: 10px;
    box-shadow: 0 4px 15px var(--shadow-dark);
    border: 1px solid var(--border-color);
}

/* --- Responsive Layout --- */
@media (max-width: 1024px) {
    .metrics {
        grid-template-columns: 1fr; /* Una columna en tablet */
    }
    .middle {
        grid-template-columns: 1fr; /* Una columna en tablet */
    }
}

@media (max-width: 600px) {
    .dashboard h1 {
        font-size: 1.8rem;
    }
    .dashboard {
        padding: 15px;
    }
}


</style>

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Valor del Cliente", page_icon="💳")

# -----------------------------
# BASE DE CLIENTES (SIMULADA)
# -----------------------------
clientes = [
    {"id": 1, "nombre": "Carlos Ruiz", "total_gasto": 150, "frecuencia": 3, "ticket_promedio": 50},
    {"id": 2, "nombre": "Ana Torres", "total_gasto": 800, "frecuencia": 12, "ticket_promedio": 67},
    {"id": 3, "nombre": "Luis Gómez", "total_gasto": 2600, "frecuencia": 34, "ticket_promedio": 76},
    {"id": 4, "nombre": "Marta Silva", "total_gasto": 5000, "frecuencia": 58, "ticket_promedio": 86},
    {"id": 5, "nombre": "Javier Soto", "total_gasto": 980, "frecuencia": 22, "ticket_promedio": 44},
    {"id": 6, "nombre": "Elena Prado", "total_gasto": 12000, "frecuencia": 120, "ticket_promedio": 100},
    {"id": 7, "nombre": "Fabian León", "total_gasto": 320, "frecuencia": 6, "ticket_promedio": 53},
    {"id": 8, "nombre": "Lucía Ramos", "total_gasto": 1800, "frecuencia": 29, "ticket_promedio": 62},
    {"id": 9, "nombre": "Diego Núñez", "total_gasto": 4500, "frecuencia": 41, "ticket_promedio": 109},
    {"id": 10, "nombre": "Gabriela Vega", "total_gasto": 750, "frecuencia": 16, "ticket_promedio": 47},
]

clientes_df = pd.DataFrame(customers := clientes)

# -----------------------------
# FUNCIÓN DE PREDICCIÓN SIMPLE
# -----------------------------
def predecir_valor(total, frecuencia, ticket):
    score = (
        (total / 2000) * 0.5 +
        (frecuencia / 50) * 0.3 +
        (ticket / 100) * 0.2
    )

    if score < 0.3:
        return "BAJO"
    elif score < 0.6:
        return "MEDIO"
    else:
        return "ALTO"


# -----------------------------
# INTERFAZ STREAMLIT
# -----------------------------
st.title("💳 Clasificador del Valor del Cliente")
st.write("Selecciona un cliente para analizar su valor y ver recomendaciones.")

# Dropdown para elegir cliente
opciones = {c["nombre"]: c for c in clientes}
nombre_cliente = st.selectbox("Cliente:", list(opciones.keys()))
cliente = opciones[nombre_cliente]

st.subheader("📊 Datos del Cliente Seleccionado")
st.metric("Total gastado", f"${cliente['total_gasto']}")
st.metric("Frecuencia de compras", f"{cliente['frecuencia']} compras")
st.metric("Ticket promedio", f"${cliente['ticket_promedio']}")

# Mini gráfico
st.write("Historial simulado de compras del cliente:")
historial = pd.DataFrame({
    "Compra": list(range(1, cliente["frecuencia"] + 1)),
    "Monto": [random.randint(20, cliente["ticket_promedio"] + 40)
              for _ in range(cliente["frecuencia"])]
})

st.line_chart(historial, x="Compra", y="Monto")

# -----------------------------
# BOTÓN PARA PREDECIR
# -----------------------------
if st.button("🔮 Predecir Valor del Cliente"):
    
    pred = predecir_valor(cliente["total_gasto"], cliente["frecuencia"], cliente["ticket_promedio"])
    
    st.subheader("🎯 Resultado de la Predicción")
    st.write(f"**Valor estimado del cliente:** `{pred}`")

    # Recomendaciones
    st.subheader("💡 Recomendación")

    if pred == "BAJO":
        st.warning("📉 Cliente BAJO → Ofrécele un cupón del 15% para aumentar su retención.")
    elif pred == "MEDIO":
        st.info("⚡ Cliente MEDIO → Excelente para fidelización. Recomienda upgrade o membresía.")
    else:
        st.success("🏆 Cliente ALTO → Ofrece beneficios VIP y prioridad personalizada.")

import streamlit as st
import pandas as pd
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# --- CARA A: DISEÑO DE LA PANTALLA WEB ---
st.set_page_config(page_title="Farmacología Cuántica", page_icon="💊")
st.title("💊 Optimizador Cuántico de Medicación")
st.write("Sistema de apoyo clínico basado en Qiskit para encontrar combinaciones seguras de fármacos.")
with st.expander("ℹ️ ¿Cómo funciona esta herramienta?", expanded=True):
    st.markdown("""
    * **Objetivo:** Encontrar la combinación de fármacos más eficaz y segura usando cúbits.
    * **Uso:** Cambia los números de la tabla haciendo doble clic y pulsa el botón azul de abajo.
    """)


st.sidebar.header("⚙️ Parámetros del Paciente")
max_pastillas = st.sidebar.slider("Número exacto de fármacos a recetar:", 1, 3, 2)
evitar_choque = st.sidebar.checkbox("Bloquear choque tóxico (Antibiótico A + Antiviral D)", value=True)

# Tabla editable para que el médico pueda probar distintos valores
st.subheader("1. Catálogo de Fármacos Candidatos")
datos_iniciales = pd.DataFrame({
    'Codigo_Qubit': list(range(4)),
    'Farmaco': ['Antibiotico_A', 'Antiinflamatorio_B', 'Protector_C', 'Antiviral_D'],
    'Eficacia_Curacion': list((85, 70, 40, 90)),
    'Riesgo_Higado': list((30, 50, 10, 40))
})

tabla_editada = st.data_editor(datos_iniciales, hide_index=True)

# --- BOTÓN DE EJECUCIÓN CUÁNTICA ---
if st.button("🚀 Calcular Receta Óptima con Cúbits"):
    
    # --- CARA B: MOTOR CUÁNTICO (QISKIT) ---
    qc = QuantumCircuit(4, 4)
    for q in range(4):
        qc.h(q)
    qc.measure(range(4), range(4))
    
    simulador = AerSimulator()
    resultados = simulador.run(qc, shots=1000).result().get_counts()
    
    # --- FILTRO CLÍNICO Y TRADUCCIÓN ---
    mejor_puntuacion = -999
    receta_ganadora = ""
    farmacos_ganadores = []
    
    for combinacion in resultados.keys():
        bits = combinacion[::-1]
        if bits.count('1') == max_pastillas:
            if evitar_choque and bits[0] == '1' and bits[3] == '1':
                continue
                
            eficacia = 0
            riesgo = 0
            nombres = []
            for i in range(4):
                if bits[i] == '1':
                    eficacia += tabla_editada.loc[i, 'Eficacia_Curacion']
                    riesgo += tabla_editada.loc[i, 'Riesgo_Higado']
                    nombres.append(tabla_editada.loc[i, 'Farmaco'])
                    
            puntuacion = eficacia - riesgo
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                receta_ganadora = bits
                farmacos_ganadores = nombres
                
    # --- RESULTADOS EN PANTALLA ---
    st.subheader("2. Diagnóstico del Procesador Cuántico")
    if farmacos_ganadores:
        st.success(f"✅ **Combinación Óptima:** {', '.join(farmacos_ganadores)}")
        col1, col2 = st.columns(2)
        col1.metric("Puntuación Clínica Neta", f"{mejor_puntuacion} pts")
        col2.metric("Estado de Cúbits Ganador", receta_ganadora)
    else:
        st.warning("⚠️ No se encontró ninguna combinación válida con esas restricciones.")

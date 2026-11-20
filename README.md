# 💊 Optimizador Cuántico de Medicación (Polifarmacia)

Aplicación web interactiva que combina **computación cuántica (IBM Qiskit)** y **análisis de datos en Python** para apoyar la toma de decisiones farmacológicas, encontrando combinaciones de medicamentos con máxima eficacia y mínimo riesgo hepático.

🔗 **Prueba la aplicación en vivo aquí:** https://optimizador-farmacos-cuantico-zuk6vhvcwfpz8fzoxtqdhw.streamlit.app/

<img width="1324" height="882" alt="Captura de pantalla 2026-11-19 212602" src="https://github.com/user-attachments/assets/9fc3b3ab-ffcd-413b-8cdb-515c0673ddda" />


## 🧠 ¿Qué problema resuelve?
En pacientes con tratamientos complejos (polifarmacia), evaluar múltiples fármacos a la vez y evitar interacciones tóxicas entre ellos supone un reto combinatorio. Este prototipo asigna cada fármaco a un **cúbit** para explorar todas las combinaciones simultáneamente mediante superposición cuántica y filtrar las opciones seguras.

## 🛠️ Tecnologías utilizadas
* **Python 3:** Lógica de negocio y filtrado clínico.
* **IBM Qiskit & Qiskit Aer:** Creación del circuito cuántico de 4 cúbits con compuertas Hadamard (`H`).
* **Pandas:** Gestión dinámica de tablas farmacológicas.
* **Streamlit:** Interfaz web interactiva para usuarios sin conocimientos técnicos.

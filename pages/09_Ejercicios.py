import streamlit as st
import random

st.title("Ejercicios Streamlit")

# =====================================================
st.subheader("Ejercicio 1: Saludo Simple")

nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.success(f"¡Hola, {nombre}!")

st.divider()

# =====================================================
st.subheader("Ejercicio 1: Calculadora Básica")

# Opción para usar decimales
usar_decimales = st.checkbox("Usar decimales")

if usar_decimales:
    num1 = st.number_input("Número 1", value=0.0)
    num2 = st.number_input("Número 2", value=0.0)
else:
    num1 = st.number_input("Número 1", value=0, step=1)
    num2 = st.number_input("Número 2", value=0, step=1)

# ⚠️ WARNING números grandes
if num1 > 100 or num2 > 100:
    st.warning("Números grandes")

operacion = st.selectbox(
    "Selecciona la operación",
    ["Sumar", "Restar", "Multiplicar", "Dividir"]
)

if operacion == "Sumar":
    resultado = num1 + num2
elif operacion == "Restar":
    resultado = num1 - num2
elif operacion == "Multiplicar":
    resultado = num1 * num2
elif operacion == "Dividir":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "No se puede dividir entre 0"

st.write(f"Resultado: {resultado}")

st.divider()

# =====================================================
st.subheader("Ejercicio 3: Convertidor de Temperatura")

opcion = st.radio(
    "Tipo de conversión",
    ["Celsius a Fahrenheit", "Fahrenheit a Celsius"]
)

temp = st.number_input("Temperatura", value=0.0)

if opcion == "Celsius a Fahrenheit":
    resultado = (temp * 9/5) + 32
    st.write(f"Resultado: {resultado:.2f} °F")
else:
    resultado = (temp - 32) * 5/9
    st.write(f"Resultado: {resultado:.2f} °C")

st.divider()

# =====================================================
st.subheader("Ejercicio 4: Galería de Mascotas")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.image("https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg")
    if st.button("Me gusta ", key="gato"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://images.dog.ceo/breeds/retriever-golden/n02099601_3004.jpg")
    if st.button("Me gusta ", key="perro"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/32/House_sparrow04.jpg")
    if st.button("Me gusta                    ", key="ave"):
        st.toast("Te gusta esta mascota")

# =====================================================
st.subheader("Ejercicio 5: Caja de Comentarios")

with st.form("comentarios"):
    asunto = st.text_input("Asunto")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")

    if enviar and mensaje:
        st.json({"asunto": asunto, "mensaje": mensaje})

st.divider()

# =====================================================
st.subheader("Ejercicio 6: Login Simulado")

if "logueado" not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if user == "admin" and password == "1234":
            st.session_state.logueado = True
            st.success("Login exitoso")
        else:
            st.error("Credenciales incorrectas")
else:
    st.success("Ya estás logueado")
    if st.button("Cerrar sesión"):
        st.session_state.logueado = False
        st.rerun()

st.divider()

# =====================================================
st.subheader("Ejercicio 7: Lista de Compras")

if "lista" not in st.session_state:
    st.session_state.lista = []

producto = st.text_input("Producto")

col1, col2 = st.columns(2)

with col1:
    if st.button("Agregar") and producto:
        st.session_state.lista.append(producto)

with col2:
    if st.button("Limpiar Lista"):
        st.session_state.lista = []

st.write("Lista de compras:")
st.write(st.session_state.lista)

st.divider()

# =====================================================
st.subheader("Ejercicio 8: Gráfico Interactivo")

N = st.slider("Cantidad de datos", 10, 100, 20)

datos = [random.randint(0, 100) for _ in range(N)]

st.line_chart(datos)

if st.button("Regenerar datos"):
    st.rerun()
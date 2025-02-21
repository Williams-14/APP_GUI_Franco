import flet as ft

def extract_numeric_values(text):
    # Verifica si el texto contiene comas
    if isinstance(text, str) and ',' in text:
        # Divide el texto por comas y convierte a float
        return [float(value) for value in text.split(',') if value.strip().isdigit()]
    elif isinstance(text, str):
        # Convierte el valor único a float
        return [float(text)] if text.strip().isdigit() else []
    else:
        return []

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_700
    page.title = "Tiempo de operaciones REG & LOG"
    page.window.width = 1000
    page.window.height = 750
    
    # Columna 1    
    # Parte 1
    texto_1 = ft.Text("Ingreso de datos generales", size=20)
    produnfidad_de_pozo = ft.TextField(label="Profundidad del pozo", value="4000")
    
    contenedor_general = ft.Column(
        controls=[produnfidad_de_pozo],
        width=250
    )
    
    # Parte 2
    texto_2 = ft.Text("Herramientas y pozo", size=20)
    
    herramienta_valor = ft.Text(value="", size=20)
    profundidad_valor = ft.Text(value="", size=20)
    intervalos_valor = ft.Text(value="", size=20)
    pasada_valor = ft.Text(value="", size=20)
    estaciones_valor = ft.Text(value="", size=20)
    tiempo_medicion_PLT_valor = ft.Text(value="", size=20)
    tiempo_medicion_NS_valor = ft.Text(value="", size=20)
    
    def actualizar_herramienta(e):
        herramienta_valor.value = cinta_herramienta.value
        page.update()
    
    def actualizar_profundidad(e):
        profundidad_valor.value = produnfidad_de_pozo.value
        page.update()
    
    def actualizar_intervalos(e):
        intervalos_valor.value = intervalos_interes.value
        page.update()
    
    def actualizar_pasada(e):
        pasada_valor.value = pasada_de_PLT.value
        page.update()
    
    def actualizar_estaciones(e):
        estaciones_valor.value = esatciones_de_PLT.value
        page.update()
    
    def actualizar_tiempo_medicion_PLT(e):
        tiempo_medicion_PLT_valor.value = tiempo_de_medicion_PLT.value
        page.update()
    
    def actualizar_tiempo_medicion_NS(e):
        tiempo_medicion_NS_valor.value = tiempo_de_medicion_NS.value
        page.update()
    
    cinta_herramienta = ft.Dropdown(
        label="Herramienta",
        width=250,
        hint_text="Opciones",
        options=[
            ft.dropdown.Option("MLPT-MFTS"),
            ft.dropdown.Option("NS"),
            ft.dropdown.Option("Ambas")
        ],
        on_change=actualizar_herramienta
    )
    
    cinta_pozo = ft.Dropdown(
        label="Estado del pozo",
        width=250,
        hint_text="Opciones",
        options=[
            ft.dropdown.Option("Abierto"),
            ft.dropdown.Option("Cerrado"),
            ft.dropdown.Option("Ambos")   
        ]
    )
    
    intervalos_interes = ft.TextField(
        label="Intervalo de interés  (m)", 
        helper_text="Valores separados por coma", 
        width=250, 
        on_change=actualizar_intervalos
    )
    
    pasada_de_PLT = ft.TextField(label="Pasada PLT (m/min)", helper_text="Valores separados por coma", width=250, on_change=actualizar_pasada)
    esatciones_de_PLT = ft.TextField(label="Estaciones PLT(m/s)", helper_text="Valores separados por coma", width=250, on_change=actualizar_estaciones)
    
    tiempo_de_medicion_PLT = ft.TextField(label="Tiempo de medición estación de PLT(min)", width=250, value="8", on_change=actualizar_tiempo_medicion_PLT)
    tiempo_de_medicion_NS = ft.TextField(label="Tiempo de medición estación de NS(min)", width=250, value="1", on_change=actualizar_tiempo_medicion_NS)
    
    columna_izquierda = ft.Column(
        controls=[
            texto_1, 
            contenedor_general, 
            texto_2, 
            cinta_herramienta,
            cinta_pozo,
            intervalos_interes,
            pasada_de_PLT,
            esatciones_de_PLT,
            tiempo_de_medicion_PLT,
            tiempo_de_medicion_NS
        ],
        spacing=16
    )
    
    # Columna derecha
    columna_derecha = ft.Column(
        controls=[
            ft.Text(value=" ", size=20),
            ft.Text("Herramienta seleccionada:"),
            herramienta_valor,
            ft.Text("Profundidad del pozo:"),
            profundidad_valor,
            ft.Text("Intervalos de interés:"),
            intervalos_valor,
            ft.Text("Pasada PLT:"),
            pasada_valor,
            ft.Text("Estaciones PLT:"),
            estaciones_valor,
            ft.Text("Tiempo de medición PLT:"),
            tiempo_medicion_PLT_valor,
            ft.Text("Tiempo de medición NS:"),
            tiempo_medicion_NS_valor
        ],
        spacing=18
    )
    
    # Layout principal
    layout_principal = ft.Row(
        controls=[
            columna_izquierda,
            columna_derecha
        ],
        expand=True
    )
    
    page.add(layout_principal)

    def procesar_valores(e):
        # Extraer valores numéricos de los TextField solo si no están vacíos
        if intervalos_interes.value:
            intervalos_interes_values = extract_numeric_values(intervalos_interes.value)
            print(f"Intervalos de interés: {intervalos_interes_values}")
        
        if pasada_de_PLT.value:
            pasada_de_PLT_values = extract_numeric_values(pasada_de_PLT.value)
            print(f"Pasada PLT: {pasada_de_PLT_values}")
        
        if esatciones_de_PLT.value:
            esatciones_de_PLT_values = extract_numeric_values(esatciones_de_PLT.value)
            print(f"Estaciones PLT: {esatciones_de_PLT_values}")

    # Botón para procesar los valores
    boton_procesar = ft.ElevatedButton(text="Procesar valores", on_click=procesar_valores)
    page.add(boton_procesar)

ft.app(target=main)

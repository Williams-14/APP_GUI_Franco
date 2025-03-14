import flet as ft
from Control_flow.extract import *

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.title = "Tiempo de operaciones REG & LOG 1.0"
    page.window.width = 1000
    page.window.height = 750
    
    # Columna 1    
    ensamble_equipo = 45  # minutos
    estabilizacion = 180  # minutos
    calibracion = 25
    # Velocidades de intervalo de herramienta a intervalo de interés
    velocidad_plt = 15  # m/min
    velocidad_ns = 15
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
    
    # def actualizar_profundidad(e):
    #     profundidad_valor.value = produnfidad_de_pozo.value
    #     page.update()
    
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
        controls=[ft.Text("TIEMPOS")],
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
    
    # ! Pagina para los resultados a imprimir ne pantalla
    armado_alinedo = ensamble_equipo * 2
    estabilizacion_pozo = estabilizacion * 2
    viaje_calibracion = (int(produnfidad_de_pozo.value) / calibracion) * 2
    
    def procesar_valores(e):
        # Extraer valores numéricos de los TextField solo si no están vacíos
        if intervalos_interes.value:
            intervalos_interes_values = extract_numeric_values(intervalos_interes.value)
            arribo_a_intevalo_PLT = intervalos_interes_values[0] / calibracion
            
        if pasada_de_PLT.value:
            pasada_de_PLT_values = extract_numeric_values(pasada_de_PLT.value)
            
        if esatciones_de_PLT.value:
            esatciones_de_PLT_values = extract_numeric_values(esatciones_de_PLT.value)
            
        pasada_PLT = sum(((intervalos_interes_values[1] - intervalos_interes_values[0]) / velocidad) * 2 for velocidad in pasada_de_PLT_values)
        estaciones_para_PLT = (len(esatciones_de_PLT_values) * int(tiempo_de_medicion_PLT.value)) + sum((esatciones_de_PLT_values[i] - esatciones_de_PLT_values[i -1]) / 3 for i in range(1, len(esatciones_de_PLT_values)))
        recuperacion_PLT = esatciones_de_PLT_values[-1] / velocidad_plt
        
        NS = intervalos_interes_values[0] / calibracion
        pasada_de_NS = ((intervalos_interes_values[1] - intervalos_interes_values[0]) / 3 + (intervalos_interes_values[1] - intervalos_interes_values[0]) * 1) * 2
        arribo_regreso_NS = intervalos_interes_values[0] / calibracion
        tiemp_total = (armado_alinedo + estabilizacion_pozo + viaje_calibracion + arribo_a_intevalo_PLT + pasada_PLT + estaciones_para_PLT + recuperacion_PLT + NS + pasada_de_NS + arribo_regreso_NS)
        Horas = tiemp_total / 60
        
        # Actualizar la columna derecha con los valores calculados
        columna_derecha.controls = [
            ft.Text(f"Armado y alineado: {armado_alinedo} minutos"),
            ft.Text(f"Estabilización del pozo: {estabilizacion_pozo} minutos"),
            ft.Text(f"Viaje de calibración: {viaje_calibracion} minutos"),
            ft.Text(f"Arribo a intervalo PLT: {arribo_a_intevalo_PLT} minutos"),
            ft.Text(f"Pasada PLT: {round(pasada_PLT,3)} minutos"),
            ft.Text(f"Estaciones para PLT: {round(estaciones_para_PLT,3)} minutos"),
            ft.Text(f"Recuperación PLT: {round(recuperacion_PLT,3)} minutos"),
            ft.Text(f"NS: {round(NS,2)} minutos"),
            ft.Text(f"Pasada de NS: {round(pasada_de_NS,3)} minutos"),
            ft.Text(f"Arribo y regreso NS: {round(arribo_regreso_NS,3)} minutos"),
            ft.Text(f"Tiempo total: {round(tiemp_total,3)} minutos"),
            ft.Text(f"Horas: {round(Horas,3)} horas")
        ]
        page.update()

    # Botón para procesar los valores 
    boton_procesar = ft.ElevatedButton(text="Procesar valores", on_click=procesar_valores)
    page.add(boton_procesar)

ft.app(target=main)


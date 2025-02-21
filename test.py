# Datos generales
pozo_prof = 4000
ensamble_equipo = 45  # minutos
estabilizacion = 180  # minutos

# Herramienta usada
herramientas = ['MLPT-MFTS', 'NS']  # Puede variar

# Pozo
pozo = ['Abierto', 'Cerrado']  # Puede afectar los tiempos de trabajo de acuerdo a su condición

# Intervalos de interés para el control de tiempos
intervalos = [3800, 3919]  # Puede variar

# Velocidad de viaje de calibración es fija
calibr = 25  # m/min

# Velocidades de intervalo de herramienta a intervalo de interés
velocidad_plt = 15  # m/min
velocidad_ns = 15

pasada_plt_mts = [3, 6, 10]  # m/s
pasada_ns = 1

estaciones_plt = [3810, 3836, 3845, 3855, 3900, 3919]  # m

tiempo_medido_PLT = 8  # minutos
tiempo_medido_NS = 1

# Resultados de tiempos operativos
armado_alineado = ensamble_equipo * 2
estabilizacion_pozo = estabilizacion * 2
viaje_calibracion = (pozo_prof / calibr) * 2
arribo_a_intervalo_PLT = intervalos[0] / calibr

pasada_PLT = sum(((intervalos[1] - intervalos[0]) / velocidad) * 2 for velocidad in pasada_plt_mts)
estaciones_para_PLT = (len(estaciones_plt) * tiempo_medido_PLT) + sum((estaciones_plt[i] - estaciones_plt[i - 1]) / 3 for i in range(1, len(estaciones_plt)))
recuperacion_PLT = estaciones_plt[-1] / velocidad_plt

NS = intervalos[0] / calibr
pasada_de_NS = ((intervalos[1] - intervalos[0]) / 3 + (intervalos[1] - intervalos[0]) * 1) * 2
arribo_regreso_NS = intervalos[0] / calibr

tiempo_total = (armado_alineado + estabilizacion_pozo + viaje_calibracion + arribo_a_intervalo_PLT +
                pasada_PLT + estaciones_para_PLT + recuperacion_PLT + NS + pasada_de_NS + arribo_regreso_NS)
HORAS = tiempo_total / 60

print(f'''
Armado y alineado de equipo: {armado_alineado} minutos
Estabilización de pozo: {estabilizacion_pozo} minutos
Viaje de calibración: {viaje_calibracion:.2f} minutos
Arribo al intervalo de interés PLT: {arribo_a_intervalo_PLT:.2f} minutos
Pasada PLT: {pasada_PLT:.2f} minutos
Estaciones PLT: {estaciones_para_PLT:.2f} minutos
Recuperación PLT: {recuperacion_PLT:.2f} minutos
NS: {NS:.2f} minutos
Pasada NS: {pasada_de_NS:.2f} minutos
Arribo de regreso de NS: {arribo_regreso_NS:.2f} minutos
Tiempo Total: {tiempo_total:.2f} minutos
HORAS: {HORAS:.2f} h
''')

nombre = input("Nombre de la tarea: ")
horas = float(input("Horas estimadas: "))
prioridad = int(input("Prioridad (1-5): "))

minutos_totales = int(horas*60)
horas_totales = minutos_totales // 60
minutos_sobrantes = minutos_totales % 60

es_urgente = prioridad >= 4 and horas <= 2

print (f"El nombrede la tarea es: {nombre}")
print (f"Duración: {horas_totales} horas y {minutos_sobrantes} minutos")
print (f"La prioridad es: {prioridad}")
print (f"Es urgente?: {es_urgente}")
print(type(nombre), type(horas), type(prioridad))
# =========================================
# FASE 5 - EVALUACION FINAL POA
# Problema 5
# =========================================

empleados = [
    ["Ana",8,8,9,8,8],
    ["Carlos",10,9,8,9,8],
    ["Luisa",7,8,7,8,7],
    ["Pedro",9,9,9,9],
]

def calcular_horas(horas):

    total = sum(horas)

    if total > 40:
        estado = "Sobretiempo"
    else:
        estado = "Horario Estandar"

    return total, estado


print("===================================")
print(" REPORTE DE HORAS TRABAJADAS ")
print("===================================")

for empleado in empleados:

    nombre = empleado[0]
    horas = empleado[1:]

    total, estado = calcular_horas(horas)

    print("\nEmpleado:", nombre)
    print("Total Horas:", total)
    print("Estado:", estado)

print("\n===================================")
print(" FIN DEL PROGRAMA ")
print("===================================")
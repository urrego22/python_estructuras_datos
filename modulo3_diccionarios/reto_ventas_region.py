# reto modulo 3 - diccionarios
# analisis de ventas trimestrales por region
# estructura: { region: { Q1, Q2, Q3, Q4 } }

ventas_por_region = {
    "Norte":  {"Q1": 45000, "Q2": 52000, "Q3": 48000, "Q4": 61000},
    "Sur":    {"Q1": 38000, "Q2": 41000, "Q3": 44000, "Q4": 39000},
    "Este":   {"Q1": 55000, "Q2": 60000, "Q3": 58000, "Q4": 72000},
    "Oeste":  {"Q1": 30000, "Q2": 35000, "Q3": 33000, "Q4": 40000},
    "Centro": {"Q1": 62000, "Q2": 58000, "Q3": 65000, "Q4": 70000},
}

# calcula el total anual de cada region
def calcular_totales(ventas):
    totales = {}
    for region, trimestres in ventas.items():
        totales[region] = sum(trimestres.values())
    return totales

# encuentra la region con mas ventas
def region_mayor_ventas(totales):
    return max(totales, key=lambda r: totales[r])

# suma las ventas de cada trimestre en todas las regiones
def ventas_por_trimestre(ventas):
    acumulado = {}
    for trimestres in ventas.values():
        for trimestre, monto in trimestres.items():
            acumulado[trimestre] = acumulado.get(trimestre, 0) + monto
    return acumulado

# calcula el porcentaje de cada region sobre el total general
def calcular_porcentajes(totales):
    gran_total = sum(totales.values())
    porcentajes = {region: round(total / gran_total * 100, 1) for region, total in totales.items()}
    return porcentajes

# imprime el reporte ordenado de mayor a menor
def imprimir_reporte(totales, porcentajes, por_trimestre):
    gran_total = sum(totales.values())

    print("\n---- reporte de ventas por region ----")
    print(f"{'region':<10} {'total':>12} {'porcentaje':>12}")
    print("-" * 38)
    for region, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"{region:<10} ${total:>11,} {porcentajes[region]:>10.1f}%")
    print("-" * 38)
    print(f"{'total general':<10} ${gran_total:>11,}")

    print("\nventas por trimestre:")
    for trimestre, monto in sorted(por_trimestre.items()):
        print(f"  {trimestre}: ${monto:,}")

# programa principal
print("=== analisis de ventas por region ===\n")

totales       = calcular_totales(ventas_por_region)
top           = region_mayor_ventas(totales)
por_trimestre = ventas_por_trimestre(ventas_por_region)
porcentajes   = calcular_porcentajes(totales)

print(f"region con mayores ventas: {top} (${totales[top]:,})")
imprimir_reporte(totales, porcentajes, por_trimestre)
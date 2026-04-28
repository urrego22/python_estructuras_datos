# reto modulo 5 - comprehensions
# analizador de ventas usando list, dict y set comprehension

ventas = [
    {"producto": "laptop",     "categoria": "tecnologia", "unidades": 20, "precio": 800.00},
    {"producto": "teclado",    "categoria": "tecnologia", "unidades": 50, "precio":  25.00},
    {"producto": "mouse",      "categoria": "tecnologia", "unidades": 30, "precio":  15.00},
    {"producto": "monitor",    "categoria": "tecnologia", "unidades": 10, "precio": 200.00},
    {"producto": "silla",      "categoria": "muebles",    "unidades":  5, "precio": 350.00},
    {"producto": "escritorio", "categoria": "muebles",    "unidades":  3, "precio": 450.00},
    {"producto": "audifonos",  "categoria": "audio",      "unidades": 40, "precio":  45.00},
    {"producto": "bocina",     "categoria": "audio",      "unidades": 15, "precio":  80.00},
]

# 1. list comp: valor total por producto (unidades x precio)
valor_total = [v["unidades"] * v["precio"] for v in ventas]

# 2. list comp con filtro: productos con valor total mayor a 1000
alto_valor = [v["producto"] for v in ventas if v["unidades"] * v["precio"] > 1000]

# 3. dict comp: nombre del producto -> su valor total y unidades
producto_info = {
    v["producto"]: {"valor": v["unidades"] * v["precio"], "unidades": v["unidades"]}
    for v in ventas
}

# 4. dict comp con filtro: solo productos con precio mayor a 50, ordenados por valor
ranking_premium = dict(
    sorted(
        {v["producto"]: v["unidades"] * v["precio"] for v in ventas if v["precio"] > 50}.items(),
        key=lambda x: x[1],
        reverse=True
    )
)

# 5. set comp: categorias unicas y productos baratos (precio <= 50)
categorias_unicas = {v["categoria"] for v in ventas}
productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}

# 6. gran total con sum() y resumen por producto
gran_total = sum(valor_total)
resumen = {v["producto"]: v["unidades"] * v["precio"] for v in ventas}

# programa principal
print("=== analizador de ventas con comprehensions ===\n")

print("1. valor total por producto (list comp):")
for v, total in zip(ventas, valor_total):
    print(f"   {v['producto']:<15} ${total:,.2f}")

print(f"\n2. productos con valor > $1000 (list comp + filtro):")
print(f"   {alto_valor}")

print("\n3. producto_info (dict comp):")
for prod, info in producto_info.items():
    print(f"   {prod:<15} valor: ${info['valor']:,.2f}  unidades: {info['unidades']}")

print("\n4. ranking premium - precio > $50 (dict comp + sorted):")
for i, (prod, val) in enumerate(ranking_premium.items(), 1):
    print(f"   {i}. {prod:<15} ${val:,.2f}")

print(f"\n5. categorias unicas (set comp):   {categorias_unicas}")
print(f"   productos baratos <= $50:       {productos_baratos}")

print("\n6. resumen general:")
for prod, val in resumen.items():
    print(f"   {prod:<15} ${val:,.2f}")
print(f"\n   gran total: ${gran_total:,.2f}")
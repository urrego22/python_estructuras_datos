# reto modulo 4 - conjuntos
# analisis de catalogos de tiendas y recomendacion de peliculas

# -- parte 1: tiendas --

# 1. sets de productos por tienda
tienda_centro = {"laptop", "teclado", "mouse", "monitor", "auriculares", "webcam", "impresora"}
tienda_norte  = {"laptop", "teclado", "tablet", "smartphone", "auriculares", "smartwatch", "router"}
tienda_sur    = {"mouse", "monitor", "tablet", "impresora", "auriculares", "camara", "tripode"}

# 2. catalogo completo y productos comunes
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

# 3. exclusivos de cada tienda
solo_centro = tienda_centro.difference(tienda_norte, tienda_sur)
solo_norte  = tienda_norte.difference(tienda_centro, tienda_sur)
solo_sur    = tienda_sur.difference(tienda_centro, tienda_norte)

# verifico si hay tiendas sin productos en comun
sin_comun_cn = tienda_centro.isdisjoint(tienda_norte)
sin_comun_ns = tienda_norte.isdisjoint(tienda_sur)

print("=== analisis de tiendas ===\n")
print(f"catalogo completo ({len(catalogo_completo)} productos): {sorted(catalogo_completo)}")
print(f"\nproductos en las 3 tiendas: {productos_comunes}")
print(f"\nexclusivos centro: {solo_centro}")
print(f"exclusivos norte:  {solo_norte}")
print(f"exclusivos sur:    {solo_sur}")
print(f"\ncentro y norte sin productos en comun: {sin_comun_cn}")
print(f"norte y sur sin productos en comun:    {sin_comun_ns}")

# -- parte 2: peliculas --

# 4. sets de generos por usuario
usuario1 = {"accion", "ciencia ficcion", "aventura", "thriller"}
usuario2 = {"comedia", "drama", "ciencia ficcion", "romance"}
usuario3 = {"accion", "aventura", "fantasia", "animacion"}

# 5. operaciones con & | - ^
comunes_u1_u2    = usuario1 & usuario2
todos_los_generos = usuario1 | usuario2 | usuario3
solo_usuario1    = usuario1 - usuario2 - usuario3
solo_uno_de_dos  = usuario1 ^ usuario2

# 6. verifico subconjunto con <=
base = {"accion", "aventura"}
u1_tiene_base = base <= usuario1
u2_tiene_base = base <= usuario2

# generos que gustan a por lo menos 2 usuarios
populares = set()
for a, b in [(usuario1, usuario2), (usuario1, usuario3), (usuario2, usuario3)]:
    populares |= (a & b)

print("\n=== recomendaciones de peliculas ===\n")
print(f"usuario1: {usuario1}")
print(f"usuario2: {usuario2}")
print(f"usuario3: {usuario3}")
print(f"\ngeneros en comun u1 y u2: {comunes_u1_u2}")
print(f"todos los generos:        {todos_los_generos}")
print(f"generos solo de u1:       {solo_usuario1}")
print(f"generos en uno pero no en ambos (u1^u2): {solo_uno_de_dos}")
print(f"\nu1 tiene accion y aventura: {u1_tiene_base}")
print(f"u2 tiene accion y aventura: {u2_tiene_base}")
print(f"\ngeneros populares (gustan a 2 o mas usuarios): {populares}")
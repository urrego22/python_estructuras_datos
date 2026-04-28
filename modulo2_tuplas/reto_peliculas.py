# reto modulo 2 - tuplas
# catalogo de peliculas con tuplas inmutables
# cada pelicula es: (titulo, director, anio, puntuacion)

catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("Interestelar", "Christopher Nolan", 2014, 8.6),
    ("El Senor de los Anillos", "Peter Jackson", 2001, 8.8),
    ("Parasitos", "Bong Joon-ho", 2019, 8.5),
    ("Inception", "Christopher Nolan", 2010, 8.7),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8),
)

# muestra todas las peliculas desempaquetando cada tupla
def mostrar_catalogo(catalogo):
    print("\n---- catalogo de peliculas ----")
    for titulo, director, anio, puntuacion in catalogo:
        print(f"{titulo} ({anio}) - director: {director} - puntuacion: {puntuacion}")

# busca peliculas por director y devuelve tupla con resultados
def buscar_por_director(catalogo, director):
    resultado = tuple(p for p in catalogo if p[1].lower() == director.lower())
    return resultado

# retorna minima, maxima y promedio de puntuaciones
def obtener_estadisticas(catalogo):
    puntuaciones = [p[3] for p in catalogo]
    minima = min(puntuaciones)
    maxima = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    return minima, maxima, promedio

# programa principal
print("=== sistema de peliculas ===")

mostrar_catalogo(catalogo)

# separo la primera pelicula del resto con *
primera, *resto = catalogo
titulo, director, anio, puntuacion = primera
print(f"\nprimera pelicula: {titulo} ({anio})")
print(f"quedan {len(resto)} peliculas en el resto")

# busqueda por director
director_buscar = "Christopher Nolan"
encontradas = buscar_por_director(catalogo, director_buscar)
print(f"\npeliculas de {director_buscar}:")
for titulo, director, anio, punt in encontradas:
    print(f"  - {titulo} ({anio}) - {punt}")

# desempaqueto las estadisticas directamente
minima, maxima, promedio = obtener_estadisticas(catalogo)
print(f"\nestadisticas de puntuacion:")
print(f"  minima:   {minima}")
print(f"  maxima:   {maxima}")
print(f"  promedio: {promedio:.2f}")
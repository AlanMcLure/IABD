import random
from functools import reduce

# Generar datos aleatorios para 20 registros
regiones = ["Norte", "Sur", "Este", "Oeste"]
data = [(random.choice(regiones), random.randint(1, 100)) for _ in range(20)]

print("Datos aleatorios generados:")
print(data)

# 1. Conteo
print("\nFase: Conteo")
map_count = list(map(lambda x: (x[0], 1), data))  # Asigna 1 por cada elemento
print("Resultados de map (conteo):", map_count)

reduce_count = reduce(lambda acc, x: acc + x[1], map_count, 0)  # Suma los '1'
print("Total de elementos (conteo):", reduce_count)

# 2. Suma
print("\nFase: Suma")
map_sum = list(map(lambda x: (x[0], x[1]), data))  # Transforma a (región, valor)
print("Resultados de map (suma):", map_sum)

reduce_sum = reduce(lambda acc, x: acc + x[1], map_sum, 0)  # Suma valores
print("Total de suma (valores):", reduce_sum)

# 3. Regiones (agrupación y suma por región)
print("\nFase: Regiones")
map_regions = list(map(lambda x: (x[0], x[1]), data))  # Mantiene datos originales
print("Resultados de map (regiones):", map_regions)

reduce_regions = reduce(
    lambda acc, x: {**acc, x[0]: acc.get(x[0], 0) + x[1]}, map_regions, {}
)
print("Suma por región:", reduce_regions)

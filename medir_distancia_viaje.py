# Importar bibliotecas necesarias
from geopy.distance import geodesic
from datetime import timedelta

# Diccionario de ciudades y sus coordenadas
ciudades = {
    # Ciudades de Chile
    "arica": (-18.4783, -70.3126),
    "iquique": (-20.2208, -70.1431),
    "antofagasta": (-23.6509, -70.3975),
    "copiapo": (-27.3668, -70.3319),
    "coquimbo": (-29.9533, -71.3395),
    "valparaiso": (-33.0458, -71.6197),
    "santiago": (-33.4489, -70.6693),
    "rancagua": (-34.1708, -70.7445),
    "talca": (-35.4264, -71.6485),
    "chillan": (-36.6066, -72.1034),
    "concepcion": (-36.8201, -73.0440),
    "temuco": (-38.7359, -72.5903),
    "valdivia": (-39.8142, -73.2459),
    "osorno": (-40.5735, -73.1332),
    "puerto montt": (-41.4718, -72.9362),
    "coyhaique": (-45.5712, -72.0683),
    "punta arenas": (-53.1638, -70.9171),

    # Ciudades de Argentina
    "buenos aires": (-34.6037, -58.3816),
    "cordoba": (-31.4201, -64.1888),
    "rosario": (-32.9468, -60.6393),
    "mendoza": (-32.8908, -68.8272),
    "tucuman": (-26.8083, -65.2176),
    "salta": (-24.7829, -65.4125),
    "santa fe": (-31.6333, -60.7000),
    "san juan": (-31.5375, -68.5364),
    "corrientes": (-27.4698, -58.8302),
    "neuquen": (-38.9516, -68.0591),
    "bahia blanca": (-38.7196, -62.2724),
    "san luis": (-33.3017, -66.3378),
    "mardel plata": (-38.0023, -57.5575),
    "ushuaia": (-54.8019, -68.3020),
    "rawson": (-43.3002, -65.1023),
    "formosa": (-26.1775, -58.1781),
    "posadas": (-27.3671, -55.8961),
    "jujuy": (-24.1855, -65.2995)
}

# Función para calcular la distancia y duración del viaje
def calcular_distancia_duracion(ciudad_origen, ciudad_destino, medio_transporte):
    if ciudad_origen not in ciudades or ciudad_destino not in ciudades:
        print("Ciudades no válidas.")
        return

    origen_coords = ciudades[ciudad_origen]
    destino_coords = ciudades[ciudad_destino]

    # Calcular distancia en kilómetros
    distancia_km = geodesic(origen_coords, destino_coords).kilometers

    # Calcular duración del viaje (ejemplo de duración)
    velocidad_promedio_kph = {
        "auto": 100,   # ejemplo de velocidad en km/h para cada medio de transporte
        "avion": 800,
        "tren": 120,
        "barco": 50
    }

    if medio_transporte.lower() not in velocidad_promedio_kph:
        print("Medio de transporte no válido.")
        return

    velocidad_kph = velocidad_promedio_kph[medio_transporte.lower()]
    duracion_horas = distancia_km / velocidad_kph
    duracion_viaje = timedelta(hours=duracion_horas)

    # Mostrar resultados en kilómetros
    print(f"\nDistancia entre {ciudad_origen.capitalize()} y {ciudad_destino.capitalize()}:")
    print(f"- Kilómetros: {distancia_km:.2f} km")
    print(f"- Duración del viaje en {medio_transporte.capitalize()}: {duracion_viaje}")

    # Mostrar narrativa del viaje
    print("\nNarrativa del viaje:")
    print(f"Viajando desde {ciudad_origen.capitalize()} hasta {ciudad_destino.capitalize()} en {medio_transporte}, llegarás en aproximadamente {duracion_viaje}. ¡Buen viaje!")

# Función principal
def main():
    print("Bienvenido al sistema de cálculo de distancia y duración de viaje.")

    while True:
        ciudad_origen = input("\nIngrese la ciudad de origen (o 's' para salir): ").strip().lower()
        if ciudad_origen == 's':
            print("Saliendo del programa...")
            break
        
        ciudad_destino = input("Ingrese la ciudad de destino: ").strip().lower()
        medio_transporte = input("Ingrese el medio de transporte (auto, avion, tren, barco): ").strip().lower()

        calcular_distancia_duracion(ciudad_origen, ciudad_destino, medio_transporte)

# Ejecutar la función principal si se ejecuta directamente el script
if __name__ == "__main__":
    main()

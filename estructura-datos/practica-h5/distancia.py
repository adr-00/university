import random
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

def obtener_coordenadas(ciudad, geolocator):
    location = geolocator.geocode(f"{ciudad}, Murcia, España")
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"No se encontraron coordenadas para {ciudad}")

def generar_distancias(ciudades, nombre_archivo="distancias_murcia.txt"):
    geolocator = Nominatim(user_agent="grafo_murcia")
    coordenadas = {}

    print("Obteniendo coordenadas...")
    for ciudad in ciudades:
        try:
            coordenadas[ciudad] = obtener_coordenadas(ciudad, geolocator)
            time.sleep(1)  # Evita bloqueo del servidor de geocodificación
        except ValueError as e:
            print(e)
            return

    print("Calculando distancias...")

    pares = []
    for i in range(len(ciudades)):
        for j in range(i + 1, len(ciudades)):
            pares.append((ciudades[i], ciudades[j]))

    random.shuffle(pares)

    with open(nombre_archivo, "w") as archivo:
        for ciudad1, ciudad2 in pares:
            dist = geodesic(coordenadas[ciudad1], coordenadas[ciudad2]).meters
            archivo.write(f"{ciudad1} {ciudad2} {int(dist)}\n")

    print(f"Archivo '{nombre_archivo}' generado con {len(pares)} conexiones.")

# Lista de 50 ciudades de la Región de Murcia
lista_de_ciudades = [
    "Murcia", "Cartagena", "Lorca", "Molina de Segura", "Cieza", "Yecla", "Mazarrón",
    "Caravaca de la Cruz", "San Javier", "Alcantarilla", "Águilas", "Jumilla",
    "Totana", "La Unión", "Torre-Pacheco", "Archena", "Los Alcázares", "Fuente Álamo",
    "San Pedro del Pinatar", "Alhama de Murcia", "Cehegín", "Bullas", "Mula",
    "Beniel", "Abarán", "Ceutí", "Calasparra", "Fortuna", "Blanca", "Campos del Río",
    "Librilla", "Ricote", "Villanueva del Río Segura", "Ojós", "Ulea", "Albudeite",
    "Pliego", "Lorquí", "Abanilla", "Santomera", "Torre de la Horadada", "Sucina",
    "La Manga", "El Palmar", "Cabezo de Torres", "Sangonera la Verde", "La Alberca",
    "Puente Tocinos", "Beniaján", "El Esparragal"
]

generar_distancias(lista_de_ciudades)

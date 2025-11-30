import requests
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OWM_API_KEY")


def unixstamp_to_uft_date(timestamp:int):
    date_utc = datetime.utcfromtimestamp(timestamp)
    formate_date = date_utc.strftime("%d/%m/%Y")
    return formate_date

def obtener_lat_lon(ciudad:str, api_key:str)->tuple:
    url_latitud = f'http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&appid={api_key}'
    try:
        response = requests.request('get', url_latitud)
    except:
        return None

    if response.status_code == 200:
        datos = response.json()
        if not datos:
            return None
        lon = float(datos[0]["lon"])
        lat = float(datos[0]["lat"])
        return lat, lon
    else:
        return None
    
def air_pollution(lat:float, lon:float, api_key:str):
    url_air_pollution = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}'

    try:
        response = requests.request('get', url_air_pollution)
    except:
        return None
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def get_summary_response(data_weather, ciudad):
    for i in range(len(data_weather["list"])):
        data_weather["list"][i]["dt"] = unixstamp_to_uft_date(data_weather["list"][i]["dt"])
    
    datos_interes = {}
    
    for reg_data in data_weather["list"]:
        if reg_data["dt"] in datos_interes:
            datos_interes[reg_data["dt"]]["count"] += 1
            datos_interes[reg_data["dt"]]["aqi_medio"] += reg_data["main"]["aqi"]
            datos_interes[reg_data["dt"]]["co"] += reg_data["components"]["co"]
            datos_interes[reg_data["dt"]]["no2"] += reg_data["components"]["no2"]
            datos_interes[reg_data["dt"]]["o3"] += reg_data["components"]["o3"]
            datos_interes[reg_data["dt"]]["pm2_5"] += reg_data["components"]["pm2_5"]
            datos_interes[reg_data["dt"]]["pm10"] += reg_data["components"]["pm10"]
        else:
            datos_interes[reg_data["dt"]] = {
                "count": 1,
                "aqi_medio": reg_data["main"]["aqi"],
                "co": reg_data["components"]["co"],
                "no2": reg_data["components"]["no2"],
                "o3": reg_data["components"]["o3"],
                "pm2_5": reg_data["components"]["pm2_5"],
                "pm10": reg_data["components"]["pm10"],
            }
    for date, vals in datos_interes.items():
        c = vals.pop("count")
        
        datos_interes[date]["aqi_medio"] /= c
        datos_interes[date]["co"] /= c
        datos_interes[date]["no2"] /= c
        datos_interes[date]["o3"] /= c
        datos_interes[date]["pm2_5"] /= c
        datos_interes[date]["pm10"] /= c
    
    final_output = {
        "ciudad" : ciudad,
        "dias":datos_interes
    }
    return final_output


def graficar_tabla(summary_data, ciudad):
    fechas = list(summary_data["dias"].keys())
    aquis = [summary_data["dias"][fecha]["aqi_medio"] for fecha in fechas]
    no2s = [summary_data["dias"][fecha]["no2"] for fecha in fechas]
    o3s = [summary_data["dias"][fecha]["o3"] for fecha in fechas]
    pm2_5s = [summary_data["dias"][fecha]["pm2_5"] for fecha in fechas]
    pm10s = [summary_data["dias"][fecha]["pm10"] for fecha in fechas]

    print("*"*20 + f"TABLA RESUMEN {ciudad.upper()}" + "*"*20)
    print(f"{'Fecha':<12} {'AQI Medio':<10} {'NO2':<10} {'O3':<10} {'PM2.5':<10} {'PM10':<10}")
    for i in range(len(fechas)):
        print(f"{fechas[i]:<12} {aquis[i]:<10.2f} {no2s[i]:<10.2f} {o3s[i]:<10.2f} {pm2_5s[i]:<10.2f} {pm10s[i]:<10.2f}")

def graficar_aqi(summary_data, ciudad):
    fechas = list(summary_data["dias"].keys())
    aquis = [summary_data["dias"][fecha]["aqi_medio"] for fecha in fechas]

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, aquis, marker='o')
    plt.title(f'Índice de Calidad del Aire (AQI) en {ciudad}')
    plt.xlabel('Fecha')
    plt.ylabel('AQI Medio')
    plt.grid()
    plt.savefig(f'aqi_{ciudad}.png')

if __name__ == "__main__":
    ciudad = str(input("Introduce el nombre de la ciudad: "))
    ciudades = ciudad.split(";")
    
    for c in ciudades:
        lat_lon = obtener_lat_lon(c, API_KEY)
        if lat_lon:
            lat, lon = lat_lon
            data_weather = air_pollution(lat, lon, API_KEY)
        else:
            print("No se pudo obtener la latitud y longitud de la ciudad.")
        if data_weather:
            summary = get_summary_response(data_weather, c)
            graficar_tabla(summary, c)
        else:
            print("No se pudo obtener los datos de contaminación del aire.")
        opcion_grafica = str(input(f"¿Deseas guardar la gráfica del AQI para {c}? (s/n): ")).lower()
        if opcion_grafica == 's':
            graficar_aqi(summary, c)
            print(f'Gráfica guardada como aqi_{c}.png')
        

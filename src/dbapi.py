import flet as ft
import requests, json
from datetime import date

#---CONFIGURACIÓN A LA CONEXIÓN DE LAS API's---
#---URLs---
URL_API_APOD="https://api.nasa.gov/planetary/apod?"  # URL de la API APOD
URL_API_NEOWS="https://api.nasa.gov/neo/rest/v1/feed?" # URL de la API NeoWs

#---key para acceso---
api_key = "c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq"

#---Parametros de busqueda---
now= date.today() # Fecha actual tomada del servidor

def handle_change(e): #---Función busqueda por fecha---
        #selected_date= e.control.value.strftime('%Y/%m/%d')
        #return selected_date
        pass

def handle_dismissal(e):#---Función cierre de busqueda---
        pass

def apod(): # Conexión con la API APOD (Astronomy Picture of the Day)
        try:
        # Parámetros de busqueda
                params= {
                   "api_key":api_key,
                   "date":now,
                }
                # Solicitud GET a la API
                response = requests.get(URL_API_APOD, params= params)

                if response.status_code == 200:
                        apod_data = response.json()  # Se convierte la respuesta a JSON
                        return apod_data # Retorno resultado
                
        except requests.exceptions.RequestException as e:
                return f"Error: {str(e)} en conexión con la API´s" #---Error de conexión con la api---
        except json.JSONDecodeError as e:
                return f"Error al decodificar JSON:{str(e)}" #---Manejo de errores al decodificar JSON---

def neows(): # Conexión con la API NeoWs (Near Earth Object Web Service)
        try:
        # Parámetros de busqueda
                params= {
                        "api_key":api_key,
                        "start_date":now,
                        "end_date":'2025-12-12',
                }
        # Intenta realizar la solicitud GET a la API
                response = requests.get(URL_API_NEOWS, params= params)

                if response.status_code == 200:
                        neows_data = response.json() # Se convierte la respuesta a JSON
                        return neows_data # Retorno resultado

        except requests.exceptions.RequestException as e:
                return f"Error al conectar con la API NeoWs: {str(e)}" # Error de conexión con la api

        except json.JSONDecodeError as e:
                return f"Error al decodificar JSON: {str(e)}"  # Maneja errores al decodificar JSO
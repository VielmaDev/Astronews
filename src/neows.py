import flet as ft
import requests, json
from datetime import date, timedelta

#---URL's---
URL_API_APOD="https://api.nasa.gov/planetary/apod?"  # URL API APOD
URL_API_NEOWS="https://api.nasa.gov/neo/rest/v1/feed?" # URL API NeoWs

#---key---
api_key = "c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq"

#---Parámetros---
now= date.today() #---Fecha actual---
before= now - timedelta(days=1) #---Fecha anterior---

#---Función neows_now (Fecha actual)
def neows_now():
        try:
        #---Parámetros de busqueda---
                params= {
                        "api_key":api_key,
                        "start_date":now,
                        "end_date":before,
                }
        #---Intenta realizar la solicitud GET a la API---
                response = requests.get(URL_API_NEOWS, params= params)

                if response.status_code == 200: #---Validación de status---
                        neows_data = response.json() #---Se convierte la respuesta a JSON---
                        return neows_data #---Retorno de resultado---
                
        #---Error de conexión con la api---
        except requests.exceptions.RequestException as e:
                neows_data= f"Error: {str(e)} al conectar con la API NeoWs."
                return neows_data #---Retorno de resultado---
         
        #---Maneja errores al decodificar JSO---
        except json.JSONDecodeError as e:
                neows_data= f"Error: {str(e)} al decodificar JSON."
                return neows_data #---Retorno de resultado---

#---Función neows_api (Fecha por busqueda)
def neows_api(s, e):
        try:
                start_dates= s  #---Variable parámetro (fecha inicio)---
                end_dates= e  #---Variable parámetro (fecha final)--- 

        #---Parámetros de busqueda---
                params= {
                        "api_key":api_key,
                        "start":start_dates,
                        "end":end_dates,
                }
        #---Intenta realizar la solicitud GET a la API---
                response = requests.get(URL_API_NEOWS, params= params)

                if response.status_code == 200: #---Validación de status---
                        neows_data = response.json() #---Se convierte la respuesta a JSON---
                        return neows_data #---Retorno de resultado---
                
        #---Error de conexión con la api---
        except requests.exceptions.RequestException as e:
                neows_data= f"Error: {str(e)} al conectar con la API NeoWs."
                return neows_data #---Retorno de resultado---
         
        #---Maneja errores al decodificar JSO---
        except json.JSONDecodeError as e:
                neows_data= f"Error: {str(e)} al decodificar JSON."
                return neows_data #---Retorno de resultado---
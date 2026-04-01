import flet as ft
import requests, json
from datetime import date

#---URL's---
URL_API_APOD="https://api.nasa.gov/planetary/apod?"  #---URL API APOD---
URL_API_NEOWS="https://api.nasa.gov/neo/rest/v1/feed?" #---URL API NeoWs---

#---API key---
api_key = "c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq"

#---Parámetro (Fecha actual)---
now= date.today()

#---Función apod_now (Fecha actual)
def apod_now(): 
        try:
        #---Parámetros de busqueda---
                params= {
                   "api_key":api_key,
                   "date":now,
                }
                #---Solicitud GET a la API---
                response = requests.get(URL_API_APOD, params= params)

                if response.status_code == 200: #---Validación de status---
                        apod_data = response.json()  #---Respuesta en formato JSON---
                        return apod_data #---Retorno de resultado---
                       
        #---Error de conexión con la API---      
        except requests.exceptions.RequestException as e: 
                apod_data = f"Error: {str(e)} en conexión."
                return apod_data #---Retorno de resultado---
        
        #---Manejo de errores al decodificar JSON--- 
        except json.JSONDecodeError as e:
                apod_data = f"Error: {str(e)} al decodificar JSON."
                return apod_data #---Retorno de resultado---

#---Función apod_api (busqueda por fecha)---
def apod_api(d):
        try:
            dates= d  #---Variable parámetro (fecha de busqueda)---  
            
            #---Parámetros de busqueda---
            params= {
                   "api_key":api_key,
                   "date":dates,
            }

            #---Solicitud GET a la API---
            response = requests.get(URL_API_APOD, params= params)

            if response.status_code == 200: #---Validación de status---
                    apod_data = response.json()  #---Respuesta en formato JSON---
                    return apod_data #---Retorno de resultado---
                
        #---Error de conexión con la API---      
        except requests.exceptions.RequestException as e: 
                apod_data = f"Error: {str(e)} en conexión."
                return apod_data #---Retorno de resultado---
        
        #---Manejo de errores al decodificar JSON--- 
        except json.JSONDecodeError as e:
                apod_data = f"Error: {str(e)} al decodificar JSON."
                return apod_data #---Retorno de resultado--


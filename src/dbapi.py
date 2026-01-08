import flet as ft
import requests, json
from datetime import date

#---CONFIGURACIÓN DE CONEXIÓN---
#---URL's---
URL_API_APOD="https://api.nasa.gov/planetary/apod?"  # URL API APOD
URL_API_NEOWS="https://api.nasa.gov/neo/rest/v1/feed?" # URL API NeoWs
#---key---
api_key = "c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq"
#---Parámetros---
now= date.today() #---Fecha actual---

def apod(): # Conexión API APOD (Astronomy Picture of the Day)
        try:
        #---Parámetros de busqueda---
                params= {
                   "api_key":api_key,
                   "date":now,
                }
                #---Solicitud GET a la API---
                response = requests.get(URL_API_APOD, params= params)

                if response.status_code == 200: #---Validación de status---
                        apod_data = response.json()  #---Se convierte la respuesta a JSON---
                        return apod_data #---Retorno de resultado---
                else: #---falla en validación de status---
                       apod_data = f"Falla en conexión con la API APOD."
                       return apod_data #---Retorno de resultado--- 
                
        #---Error de conexión con la api---      
        except requests.exceptions.RequestException as e: 
                apod_data = f"Error: {str(e)} en conexión con la API's."
                return apod_data #---Retorno de resultado---
        
        #---Manejo de errores al decodificar JSON--- 
        except json.JSONDecodeError as e:
                apod_data = f"Error: {str(e)} al decodificar JSON."
                return  apod_data #---Retorno de resultado---
        
def handle_change(e): #---Busqueda por fecha---
        #selected_date= e.control.value.strftime('%Y/%m/%d')
        #return selected_date
        pass

def handle_dismissal(e):#---Cierre de busqueda---
        pass

def neows(): # Conexión API NeoWs (Near Earth Object Web Service)
        try:
        #---Parámetros de busqueda---
                params= {
                        "api_key":api_key,
                        "start_date":now,
                        "end_date":'2026-01-06'
                }
        #---Intenta realizar la solicitud GET a la API---
                response = requests.get(URL_API_NEOWS, params= params)

                if response.status_code == 200: #---Validación de status---
                        neows_data = response.json() #---Se convierte la respuesta a JSON---
                        return neows_data #---Retorno de resultado---
                else: #---falla en validación de status---
                       neows_data = f"Falla en conexión con la API NeoWs."
                       return neows_data #---Retorno de resultado--- 
                
        #---Error de conexión con la api---
        except requests.exceptions.RequestException as e:
                neows_data= f"Error: {str(e)} al conectar con la API NeoWs."
                return neows_data #---Retorno de resultado---
         
        #---Maneja errores al decodificar JSO---
        except json.JSONDecodeError as e:
                neows_data= f"Error: {str(e)} al decodificar JSON."
                return neows_data #---Retorno de resultado---
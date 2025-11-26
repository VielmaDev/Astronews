import flet as ft
from flet import TextField, ElevatedButton, Column, Row, Text, Container, alignment, Dropdown, dropdown, Colors, Image, DataRow, DataCell, DataTable, DataColumn, DatePicker
import dbapi
import datetime
from time import strftime

# ---CONFIGURACIÓN DE FORMATOS ---
ORIGINAL_API_FORMAT = "%Y-%m-%d" #Formato ISO 
API_DATE_FORMAT = "%d-%m-%Y" #Nuevo formato fecha a convertir.

#---Conexión con módulo dbapi--- 
Apod= dbapi.apod()
Neows= dbapi.neows()

class myapp:
    def __init__(self, page: ft.Page):
        page.title = "ASTRO NEWS"
        page.bgcolor = Colors.BLACK26
        page.theme_mode = "dark"
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        def check_item_clicked(e):  #---Función selector de item del menú principal---
            # El ítem de menú actual que fue clickeado (e.control)
            item_click = e.control
            
            #--Obtención de la lista de items del PopupMenuButton,
            #--Asumiendo que el PopupMenuButton es el último action del AppBar
            menu_items = page.appbar.actions[-1].items
            
            #---Los items de contenido son el índice 0 ("APOD") y el 2 ("Asteroids NeoWs")
            apod_item = menu_items[0]
            neows_item = menu_items[2]

            #---Alternar las propiedades checked y disabled
            item_click.checked = True
            item_click.disabled = True

            if item_click.text == "APOD":
                #---Si se hizo clic en "APOD", desmarcamos y deshabilitamos "Asteroids NeoWs"
                neows_item.checked = False
                neows_item.disabled = False
                
                #---Actualizar el AppBar y el contenido de la página
                page.appbar.title = Text("APOD")
                page.appbar.leading = ft.Icon(ft.Icons.NEWSPAPER)
                page.remove(asteroid_container)
                page.add(news_container)
                
            elif item_click.text == "Asteroids NeoWs":
                #---Si se hizo clic en "Asteroids NeoWs", desmarcamos y deshabilitamos "APOD"
                apod_item.checked = False
                apod_item.disabled = False
                
                #---Actualizar el AppBar y el contenido de la página
                page.appbar.title = Text("Asteroids NeoWs")
                page.appbar.leading = ft.Icon(ft.Icons.EXPLORE) #---Cambiamos el icono para el ejemplo
                page.remove(news_container)
                page.add(asteroid_container)
            
        def handle_change(e):  #---Función fecha seleccionada---
            #page.add(ft.Text(f"Date changed: {e.control.value.strftime('%m/%d/%Y')}"))
            selected_date = e.control.value.strftime('%Y/%m/%d')
            dbapi.search_date_picker(selected_date)
        
        def handle_dismissal(e): 
            #page.add(ft.Text(f"DatePicker dismissed"))
            pass
        
        def date_picker(e):  #---Calendario (DatePicker)---
            page.open(ft.DatePicker(
                            first_date=datetime.datetime
                                    (year=2000, month=10, day=1),
                            last_date=datetime.datetime
                                    (year=2030, month=12, day=31),
                            on_change=handle_change,
                            on_dismiss=handle_dismissal
                        )
                    )
            
       #---Control de alerta falla en conexión con las API's
        dlg= ft.AlertDialog(
                        title=Text("Alert"),
                        content=Text("No connection to the API network!"),
                        alignment=alignment.center,
                        on_dismiss=lambda e: print("Dialog dismissed!"),
                        title_padding=ft.padding.all(25),
                    )
        page.add(dlg)
            
        #---Barra principal del menú---
        page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.NEWSPAPER),
        leading_width=35,
        title=Text("APOD"),
        center_title=False,
        bgcolor=Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.CALENDAR_MONTH, 
                          on_click=date_picker,
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="APOD", 
                                     checked=False,
                                     disabled=True,
                                     on_click=check_item_clicked,
                    ),
                    ft.PopupMenuItem(), # divider
                    ft.PopupMenuItem(text="Asteroids NeoWs", 
                                     checked=False,
                                     disabled=False,
                                    on_click=check_item_clicked,
                    ), 
                ], 
            ), 
        ],   
    )

        #---Widget menú APOD---
        #---Resultados de conexón con la API APOD---
        if Apod: #---Si la conexión es éxitosa---
            #---Título de la publicación---        
            label = Text(f"{Apod['title']}", 
                            size=25,
                            color=ft.Colors.BLUE,
                            text_align=ft.TextAlign.CENTER)
            apod_label = Row(
                            controls=[label],
                            alignment="center",
                        )
            
            #---Convertidor de la cadena date en un objeto 'datetime'---
            #date_objeto = datetime.strptime(Apod['date'], ORIGINAL_API_FORMAT) 

            #---Formatea el objeto 'datetime' al nuevo formato de cadena---
            #date_format = date_objeto.strftime(API_DATE_FORMAT)

            #---Fecha de la publicación---
            dates = Text(Apod['date'],
                            size=17,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER)
            apod_date = Row(
                            controls=[dates],
                            alignment="center",
                        )

            #---Imagen de la publicación---
            imagen = Image(src=f"{Apod['url']}", width=380, height=380)
            apod_imagen = Row(
                            controls=[imagen],
                            alignment="center", #---Alineación horizontal---
                            vertical_alignment="center"  #---Alineación vertical---
                        )
            #---Contenido de la publicación---
            apod_content = ft.Container(
                    content=ft.Column([
                            ft.Text(f"{Apod['explanation']}"
                                    ,size=16,
                                    color=ft.Colors.WHITE,
                                    text_align=ft.TextAlign.JUSTIFY),
                        ]),
                    padding=20)
        else: #---Si la conexión es fallida---
            label = ft.Text(f'Error: conexión fallida con el servidor', 
                            size=40,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
            apod_label = Row(
                            controls=[label],
                            alignment="center",
                        )
        #---Contenedor widgets Apod---
        if Apod: #---Si la conexión es éxitosa---
            news_container = Container(
                    content=Column(
                        controls=[
                            apod_label,
                            apod_date,
                            apod_imagen,
                            apod_content
                        ],
                    ),padding=20 
                )  
        else: #---Si la conexión es fallida---
            label = Text(f"Astronomy Picture of the Day", 
                            size=20,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
            apod_label = Row(
                            controls=[label],
                            alignment="center",
                        )
            news_container = Container(
                    content=Column(
                        controls=[
                            apod_label,
                        ],
                    ),padding=20 
                )
            page.open(dlg)  

        #---Widget Asteriod NeoWs---
        label = Text("Near Earth Object Web Service", #---Encabezado principal de Asteroid NeoWs---
                            size=20,
                            color=ft.Colors.RED, 
                            text_align=ft.TextAlign.CENTER)
        neows_label = Row(
                        controls=[label],
                        alignment="center",
                    )
        # ---Definición de las Columnas de la DataTable ---
        columns=[
                DataColumn(ft.Text("Neo id"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Name"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Magnitude"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Diameter Km"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Velocity (Km/Hrs)"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Distance / Astronomical"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Orby"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Closet date full"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Hazardous"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
            ]
        #---Resultados de conexón con la API NeoWs---
        if Neows: #---Si la conexión es éxitosa---
            #---Contador de elementos widget Ateroid---
            count = Text(f"Elements: {Neows['element_count']}",
                            size=16,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER)
            neows_count = Row(
                        controls=[count],
                        alignment="center", #---Alineación horizontal---
            )

            #---Fecha de la publicación---
            start_date = list(Neows['near_earth_objects'].keys())[1] # Fecha de inicio de la busqueda
            end_date= list(Neows['near_earth_objects'].keys())[0] # Fecha final de la busqueda

            dates = Text(f"From: " + str(start_date) + " / To: " + str(end_date),
                            size=16,
                            color=ft.Colors.YELLOW,
                            text_align=ft.TextAlign.CENTER)
            neows_date = Row(
                            controls=[dates],
                            alignment="center",
                        )
            
            # Lista para acumular todas las DataRow generadas.
            all_rows= [] 
            
            #---El bucle for itera sobre cada diccionario 'Neows'---
            for neos_list in Neows['near_earth_objects'].values():
                for neo_data in neos_list:
                        for approach_data in neo_data['close_approach_data']:

                        # ---Definición de las Filas (Rows) de la DataTable ---
                            rows=DataRow(
                                        cells=[
                                                # El id de referncia
                                                DataCell(ft.Text(f"{neo_data['neo_reference_id']}")),
                                                # El nombre del asteroide
                                                DataCell(ft.Text(f"{neo_data['name']}")),
                                                # La magnitud absoluta
                                                DataCell(ft.Text(f"{neo_data['absolute_magnitude_h']}")),
                                                # E diámetro máximo
                                                DataCell(ft.Text(f"{neo_data['estimated_diameter']['kilometers']['estimated_diameter_max']}")),
                                                # La velocidad
                                                DataCell(ft.Text(f"{approach_data['relative_velocity']['kilometers_per_hour']}")),
                                                # La distancia astronómica
                                                DataCell(ft.Text(f"{approach_data['miss_distance']['astronomical']}")),
                                                # El cuerpo orbitante
                                                DataCell(ft.Text(f"{approach_data['orbiting_body']}")),
                                                # La fecha cerrada de aproximación
                                                DataCell(ft.Text(f"{approach_data['close_approach_date_full']}")),
                                                # Potencial peligro
                                                DataCell(ft.Text(f"{neo_data['is_potentially_hazardous_asteroid']}")),
                                            ],
                                        )
                            # --- Añade la nueva fila a la lista de todas las filas ---      
                            all_rows.append(rows) 

            #---Rows tabla de widget Asteroids NeoWs---
            table= DataTable(
                columns=columns,
                rows=all_rows,
                width=1200, 
                border=ft.border.all(1, ft.Colors.BLUE_500),
                border_radius=6,
                vertical_lines=ft.border.BorderSide(2, ft.Colors.BLUE_500),
                horizontal_lines=ft.border.BorderSide(2, ft.Colors.BLUE_500),
                heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_500),
                data_text_style=ft.TextStyle(color=ft.Colors.WHITE),
                column_spacing=15,
            )
            neows_table= Row(
                        controls=[table],
                        alignment="center", #---Alineación horizontal---
                    )

        #---Contenedor widgets NeoWs---
        if Neows:#---Si la conexión es éxitosa---
            asteroid_container = Container(
                        content=Column(
                                controls=[
                                    neows_label,
                                    neows_count,
                                    neows_date,
                                    neows_table,
                            ],
                    ),padding=10 
                )
        else: #---Si la conexión es fallida---
            asteroid_container = Container(
                        content=Column(
                                controls=[
                                    neows_label,
                            ],
                    ),padding=10 
                )

        page.add(news_container)
        page.update()

if __name__ == "__main__":
    ft.app(target = myapp)



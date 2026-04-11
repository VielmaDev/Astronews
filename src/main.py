import flet as ft
from flet import DatePicker,Text, Colors
import apod, neows
import datetime

#---Conexión con módulos---
apod_now= apod.apod_now() #--Módulo apod_now (Fecha actual)
neows_now= neows.neows_now() #---Modulo neows_now (Fecha actual)---

class myapp:
    def __init__(self, page: ft.Page):
        page.title = "ASTRO NEWS"
        page.bgcolor = Colors.BLACK26
        page.theme_mode = "dark"
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #---Función selector de item del menú principal---
        def check_item_clicked(e):  
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
                page.remove(app_neows)
                page.add(app_apod)
                
            elif item_click.text == "Asteroids NeoWs":
                #---Si se hizo clic en "Asteroids NeoWs", desmarcamos y deshabilitamos "APOD"
                apod_item.checked = False
                apod_item.disabled = False
                
                #---Actualizar el AppBar y el contenido de la página
                page.appbar.title = Text("Asteroids NeoWs")
                page.appbar.leading = ft.Icon(ft.Icons.EXPLORE) #---Cambiamos el icono para el ejemplo
                page.remove(app_apod)
                page.add(app_neows)

       #---Función selección de fecha---         
        def handle_change(e: DatePicker):
                d= e.control.value.strftime('%Y-%m-%d') #---Formato (AAAA-mm-dd)---
                select_date.value= f"{d}" #---Actualización de fecha seleccionada---
                apod.apod_api(d) #---Ejecución de la función apod_api (Modulo apod)---
                apod_content= apod.apod_api(d)#---Instanciación con resultado de la función apod_api

                #---Actualización de widget APOD---
                title.value= apod_content['title']
                imagen.src= apod_content['url']
                content.value= apod_content['explanation']
                page.update() #---Actualización de page---
        
        #---Función cierre de calendario---
        def handle_dismissal(e: DatePicker):
            message= ft.Text(f"DatePicker dismissed")
        
        #---Calendario de la app---
        def date_picker(e): 
            page.open(DatePicker(
                            first_date=datetime.datetime
                                    (year=2000, month=10, day=1),
                            last_date=datetime.datetime
                                    (year=2030, month=12, day=31),
                            on_change= handle_change,
                            on_dismiss=handle_dismissal,
                        )
                    )
        
        #-------------Widget de la app APOD----------------------------
        apod_calendar = ft.ElevatedButton(
                        "Calendario",
                        icon=ft.Icons.CALENDAR_MONTH,
                        on_click= date_picker)
        #---Fecha de la publicación---
        select_date= ft.Text(f"{apod_now['date']}",
                            size=18,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER)
        app_date = ft.Row(
                        controls=[select_date],
                        alignment="center",
                    )
        #---Titulo de la publicación---
        title= ft.Text(f"{apod_now['title']}", 
                        size=27,
                        color=ft.Colors.BLUE,
                        text_align=ft.TextAlign.CENTER)
        app_title = ft.Row(
                            controls=[title],
                            alignment="center",
                            )
        #---Imagen de la publicación---
        imagen = ft.Image(src="{apod_now['url']}", 
                            width=380, 
                            height=380
                            )
        app_imagen = ft.Row(
                            controls=[imagen],
                            alignment="center", #---Alineación horizontal---
                            #vertical_alignment="center"  #---Alineación vertical---
                        )
        #---Contenido de la publicación---
        content= ft.Text(f"{apod_now['explanation']} ",
                        size=16,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.JUSTIFY)
        app_content = ft.Column(
                            controls=[content],
                            alignment="center",
                            )
        
        #--------Contenedor de widget app APOD-------
        app_apod = ft.Container(
                            content=ft.Column(
                                 controls=[
                                    app_date, #---Date---
                                    app_title, #--Titulo---
                                    app_imagen, #---Imagen---
                                    app_content, #---Contenido---
                                ]
                            ), padding=25,
                        )

        #-------------Widget de la app Neows----------------------------
        if isinstance(neows_now, dict): #---Validación de diccionario de datos---
        
            # ---Definición de las Columnas DataTable ---
            columns=[
                    ft.DataColumn(ft.Text("Neo id"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Name"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Magnitude"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Diameter Km"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Velocity (Km/Hrs)"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Distance / Astronomical"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Orby"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Closet date full"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                    ft.DataColumn(ft.Text("Hazardous"), 
                                heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                ]
            
            #---Contador de elementos widget Ateroid---
            count = ft.Text(f"Elementos: {neows_now['element_count']}",
                                size=16,
                                color=ft.Colors.BLUE,
                                text_align=ft.TextAlign.CENTER)
            neows_count = ft.Row(
                            controls=[count],
                            alignment="center", #---Alineación horizontal---
                )

            #---Fecha de la publicación---
            start_date = list(neows_now['near_earth_objects'].keys())[1] # Fecha de inicio de la busqueda
            end_date= list(neows_now['near_earth_objects'].keys())[0] # Fecha final de la busqueda
            dates = ft.Text(f"From: " + str(start_date) + " / To: " + str(end_date),
                                size=16,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER)
            neows_date = ft.Row(
                                controls=[dates],
                                alignment="center",
                            )
                
            # Lista Row DataTable.
            all_rows= [] 
                
            #---El bucle for itera sobre cada diccionario 'Neows'---
            for neos_list in neows_now['near_earth_objects'].values():
                    for neo_data in neos_list:
                            for approach_data in neo_data['close_approach_data']:
                            # ---Definición de las Filas (Rows) de la DataTable ---
                                rows=ft.DataRow(
                                            cells=[
                                                    # El id de referncia
                                                    ft.DataCell(ft.Text(f"{neo_data['neo_reference_id']}")),
                                                    # El nombre del asteroide
                                                    ft.DataCell(ft.Text(f"{neo_data['name']}")),
                                                    # La magnitud absoluta
                                                    ft.DataCell(ft.Text(f"{neo_data['absolute_magnitude_h']}")),
                                                    # E diámetro máximo
                                                    ft.DataCell(ft.Text(f"{neo_data['estimated_diameter']['kilometers']['estimated_diameter_max']}")),
                                                    # La velocidad
                                                    ft.DataCell(ft.Text(f"{approach_data['relative_velocity']['kilometers_per_hour']}")),
                                                    # La distancia astronómica
                                                    ft.DataCell(ft.Text(f"{approach_data['miss_distance']['astronomical']}")),
                                                    # El cuerpo orbitante
                                                    ft.DataCell(ft.Text(f"{approach_data['orbiting_body']}")),
                                                    # La fecha cerrada de aproximación
                                                    ft.DataCell(ft.Text(f"{approach_data['close_approach_date_full']}")),
                                                    # Potencial peligro
                                                    ft.DataCell(ft.Text(f"{neo_data['is_potentially_hazardous_asteroid']}")),
                                                ],
                                            )
                                # --- Añade la nueva fila a la lista de todas las filas ---      
                                all_rows.append(rows) 

            #---Rows tabla de widget Asteroids NeoWs---
            table= ft.DataTable(
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
            neows_table= ft.Row(controls=[table],
                        alignment="center", #---Alineación horizontal---
                    )

        #-------Contenedor widget App NeoWs-------
        app_neows= ft.Container(
                        content=ft.Column(
                                controls=[
                                    neows_count, #---Count elements--
                                    neows_date, #---Date---
                                    neows_table, #---DataTable---
                            ]
                    ),padding=25
                )
        
        #---Barra principal del menú---
        page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.NEWSPAPER),
        leading_width=35,
        title=Text("APOD"),
        center_title=False,
        bgcolor=Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="APOD", 
                                     checked=False,
                                     disabled=False,
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
        
        page.add(
            apod_calendar,
            app_apod
        )
        page.update()
        
if __name__ == "__main__":
    ft.app(target = myapp)
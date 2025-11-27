import flet as ft
import dbapi

#---Conexión con módulo dbapi ---función neows--- 
Neows= dbapi.neows()

def neows_pages():
        if Neows: #---Si la conexión es éxitosa---
            #---Encabezado principal de Asteroid NeoWs---
            label = ft.Text("Near Earth Object Web Service", 
                            size=20,
                            color=ft.Colors.RED, 
                            text_align=ft.TextAlign.CENTER)
            neows_label = ft.Row(
                        controls=[label],
                        alignment="center",
                    )
            
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
            count = ft.Text(f"Elements: {Neows['element_count']}",
                            size=16,
                            color=ft.Colors.BLUE,
                            text_align=ft.TextAlign.CENTER)
            neows_count = ft.Row(
                        controls=[count],
                        alignment="center", #---Alineación horizontal---
            )

            #---Fecha de la publicación---
            start_date = list(Neows['near_earth_objects'].keys())[1] # Fecha de inicio de la busqueda
            end_date= list(Neows['near_earth_objects'].keys())[0] # Fecha final de la busqueda
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
            for neos_list in Neows['near_earth_objects'].values():
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
            
            return [neows_label, neows_count, neows_date, neows_table]
        
        else:
            #---Encabezado principal de Asteroid NeoWs---
            label = ft.Text("Near Earth Object Web Service", 
                            size=20,
                            color=ft.Colors.RED, 
                            text_align=ft.TextAlign.CENTER)
            neows_label = ft.Row(
                        controls=[label],
                        alignment="center",
                    )
            
            return [neows_label]
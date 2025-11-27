import flet as ft
import dbapi

#---Conexión con módulo dbapi ---función apod--- 
Apod= dbapi.apod() 

def apod_page():
    if Apod:  #---Si la conexión es éxitosa---  
            label = ft.Text(f"Astronomy Picture of the Day", 
                            size=20,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
            apod_label = ft.Row(
                            controls=[label],
                            alignment="center",
                        )  
            
            title= ft.Text(f"{Apod['title']}", 
                            size=27,
                            color=ft.Colors.BLUE,
                            text_align=ft.TextAlign.CENTER)
            apod_title = ft.Row(
                            controls=[title],
                            alignment="center",
                        )
            
            dates = ft.Text(Apod['date'], #---Fecha de la publicación---
                            size=18,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER)
            apod_date = ft.Row(
                            controls=[dates],
                            alignment="center",
                        )
            #---Imagen de la publicación---
            imagen = ft.Image(src=f"{Apod['url']}", width=380, height=380)
            apod_imagen = ft.Row(
                            controls=[imagen],
                            alignment="center", #---Alineación horizontal---
                            vertical_alignment="center"  #---Alineación vertical---
                        )

            #---Contenido de la publicación---
            content= ft.Text(f"{Apod['explanation']}",
                                    size=16,
                                    color=ft.Colors.WHITE,
                                    text_align=ft.TextAlign.JUSTIFY)
            apod_content = ft.Column(
                                controls=[content],
                                alignment="center",
                        )
            
            return [apod_label, apod_title, apod_date, apod_imagen, apod_content]
    
    else: #---Si la conexión es fallida---
            label = ft.Text(f"Astronomy Picture of the Day", 
                            size=20,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
            apod_label = ft.Row(
                            controls=[label],
                            alignment="center",
                        )
            return apod_label
          

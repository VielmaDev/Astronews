import flet as ft
import dbapi

def apod_page():
    #--Widget principal del menú APOD---
    label = ft.Text(f"Astronomy Picture of the Day", 
                            size=20,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
    apod_label = ft.Row(
                            controls=[label],
                            alignment="center",
                        ) 
    
    apod= dbapi.apod() #---Conexión con módulo dbapi---
    
    while apod:#---Si la conexión es éxitosa---
        #---Titulo de la publicación---
        title= ft.Text(f"{apod['title']}", 
                            size=27,
                            color=ft.Colors.BLUE,
                            text_align=ft.TextAlign.CENTER)
        apod_title = ft.Row(
                            controls=[title],
                            alignment="center",
                        )

        #---Fecha de la publicación---  
        dates = ft.Text(apod['date'], 
                                size=18,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER)
        apod_date = ft.Row(
                            controls=[dates],
                            alignment="center",
                            )
            
        #---Imagen de la publicación---
        imagen = ft.Image(src=f"{apod['url']}", width=380, height=380)
        apod_imagen = ft.Row(
                            controls=[imagen],
                            alignment="center", #---Alineación horizontal---
                            vertical_alignment="center"  #---Alineación vertical---
                            )

        #---Contenido de la publicación---
        content= ft.Text(f"{apod['explanation']}",
                                        size=16,
                                        color=ft.Colors.WHITE,
                                        text_align=ft.TextAlign.JUSTIFY)
        apod_content = ft.Column(
                                controls=[content],
                                alignment="center",
                            )
        
        #---Contenedor widget APOD---
        apod_container = ft.Container(
                    content=ft.Column(
                        controls=[
                            apod_label, #---Identificador---
                            apod_title, #---Title---
                            apod_date, #---Date---
                            apod_imagen, #---Imagen---
                            apod_content, #---Content---
                        ],
                    ),padding=20 
                )
                
        return apod_container #---Retorno---
    
    else:
        #---Aviso de falla en conexión con la red APOD---
        dlg = ft.page.open(ft.AlertDialog(
                    title=ft.Text("Warning"),
                    content=ft.Text("No connection to the API network!"),
                    alignment=ft.alignment.center,
                    on_dismiss=lambda e: print("Dialog dismissed!"),
                    title_padding=ft.padding.all(25),
                )
            )
        return dlg #---Retorno---
    

import flet as ft
import dbapi

def apod_page(): #---Identificador de página---
    #--Widget principal del menú APOD---
    label = ft.Text(f"Astronomy Picture of the Day", 
                            size=20,
                            color=ft.Colors.RED,
                            text_align=ft.TextAlign.CENTER)
    apod_label = ft.Row(
                        controls=[label],
                        alignment="center",
                        ) 
    
    #---Contenedor widget APOD---
    apod_identifier= ft.Container(
                        content=ft.Column(
                            controls=[
                                apod_label, #---Identificador---
                            ],
                        ),padding=20 
                    )
    return apod_identifier #---Retorno---

def apod_content():
    #---Variable de conexión con el módulo dbapi apod---
    search= dbapi.apod() 

    #---Validación de diccionario de datos---
    if isinstance(search, dict): 
            #---Titulo de la publicación---
            title= ft.Text(f"{search['title']}", 
                                    size=27,
                                    color=ft.Colors.BLUE,
                                    text_align=ft.TextAlign.CENTER)
            apod_title = ft.Row(
                                controls=[title],
                                alignment="center",
                                )

            #---Fecha de la publicación---  
            dates = ft.Text(f"{search['date']}", 
                                    size=18,
                                    color=ft.Colors.WHITE,
                                    text_align=ft.TextAlign.CENTER)
            apod_date = ft.Row(
                                controls=[dates],
                                alignment="center",
                                    )
                    
                #---Imagen de la publicación---
            imagen = ft.Image(src= search['url'], 
                                        width=380, 
                                        height=380
                                        )
            apod_imagen = ft.Row(
                                controls=[imagen],
                                alignment="center", #---Alineación horizontal---
                                vertical_alignment="center"  #---Alineación vertical---
                                )

            #---Contenido de la publicación---
            content= ft.Text(f"{search['explanation']}",
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
                                    apod_title, #---Title---
                                    apod_date, #---Date---
                                    apod_imagen, #---Imagen---
                                    apod_content, #---Content---
                                ],
                            ),padding=20 
                        )
            return apod_container #---Retorno---
    
    else:  
        dialog= ft.AlertDialog(
                    title=ft.Text("Aviso:"), #---Aviso de falla en conexión---
                    content=ft.Text(f"{search}"),
                    open=True,
                )
        
        #---Contenedor widget APOD---
        apod_container = dialog
        return apod_container #---Retorno---
    

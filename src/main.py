import flet as ft
from flet import Column, Text, Container, Colors, DatePicker
import dbapi, apod, neows
import datetime

#---Conexión con módulos--- 
Alert= dbapi.alert() # Llama a la función control de falla de conexión API´s
apod_module= apod.apod_page() #---Módulo apod---
neows_module= neows.neows_pages() #---Módulo neows---

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
            
        #---Widget Calendario---
        def handle_change(e):  #---Función fecha seleccionada---
            #page.add(ft.Text(f"Date changed: {e.control.value.strftime('%m/%d/%Y')}"))
            selected_date = e.control.value.strftime('%Y/%m/%d')
            dbapi.search_date_picker(selected_date)
        def handle_dismissal(e): 
            #page.add(ft.Text(f"DatePicker dismissed"))
            pass
        def date_picker(e):  #---Calendario (DatePicker)---
            page.open(DatePicker(
                            first_date=datetime.datetime
                                    (year=2000, month=10, day=1),
                            last_date=datetime.datetime
                                    (year=2030, month=12, day=31),
                            on_change=handle_change,
                            on_dismiss=handle_dismissal
                        )
                    )
            
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

        #---Widget del menú APOD---
        if apod_module: #---Si la conexión es éxitosa---
                news_container = Container(
                    content=Column(
                        controls=[
                            apod_module[0], #---Etiqueta---
                            apod_module[1], #---Title---
                            apod_module[2], #---Date---
                            apod_module[3], #---Imagen---
                            apod_module[4], #---Content---
                        ],
                    ),padding=20 
                )          
        else: #---Si la conexión es fallida---
            page.add(Alert)
            page.open(Alert)
            news_container = Container(
                    content=Column(
                        controls=[
                            apod_module[0], #---Etiqueta---
                        ],
                    ),padding=18 
                )

        #---widgets del menú NeoWs---
        if neows_module:#---Si la conexión es éxitosa---
            asteroid_container = Container(
                        content=Column(
                                controls=[
                                    neows_module[0], #---Title---
                                    neows_module[1], #---Count elements--
                                    neows_module[2], #---Date---
                                    neows_module[3], #---DataTable---
                            ],
                    ),padding=10 
                )
        else: #---Si la conexión es fallida---
            asteroid_container = Container(
                        content=Column(
                                controls=[
                                    neows_module[0], #---Title---
                            ],
                    ),padding=10 
                )

        page.add(news_container)
        page.update()

if __name__ == "__main__":
    ft.app(target = myapp)



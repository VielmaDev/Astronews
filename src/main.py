import flet as ft
from flet import Text, Colors, DatePicker
import dbapi, apod, neows
import datetime

#---Conexión con módulos--- 
apod_module= apod.apod_page() #---Módulo apod_page---
apod_content= apod.apod_content() #---Módulo apod_content---
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
                page.remove(neows_module)
                page.add(apod_module)
                
            elif item_click.text == "Asteroids NeoWs":
                #---Si se hizo clic en "Asteroids NeoWs", desmarcamos y deshabilitamos "APOD"
                apod_item.checked = False
                apod_item.disabled = False
                
                #---Actualizar el AppBar y el contenido de la página
                page.appbar.title = Text("Asteroids NeoWs")
                page.appbar.leading = ft.Icon(ft.Icons.EXPLORE) #---Cambiamos el icono para el ejemplo
                page.remove(apod_module)
                page.add(neows_module)

        #---Calendario (DatePicker)---
        def date_picker(e): 
            page.open(DatePicker(
                            first_date=datetime.datetime
                                    (year=2000, month=10, day=1),
                            last_date=datetime.datetime
                                    (year=2030, month=12, day=31),
                            on_change= dbapi.handle_change,
                            on_dismiss=dbapi.handle_dismissal,
                        )
                    ),
            page.add(apod_content) 

        #---Barra principal del menú---
        page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.NEWSPAPER),
        leading_width=35,
        title=Text("APOD"),
        center_title=False,
        bgcolor=Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.CALENDAR_MONTH,
                          on_click= date_picker,
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

        page.update()
        page.add(apod_module)
        
if __name__ == "__main__":
    ft.app(target = myapp)

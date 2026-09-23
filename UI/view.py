import flet as ft


class View:
    def __init__(self, page: ft.Page):
        self._page = page
        self._page.title = "Programmazione avanzata - Compagnie aeree"
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None
        self.txt_result = None

    def load_interface(self):
        title = ft.Text("Concorrenza tra compagnie aeree", color="blue", size=24)
        self._page.controls.append(title)

        self.txtNumAeroporti = ft.TextField(
            label="Numero minimo di aeroporti", width=260
        )
        self.btnCreaGrafo = ft.ElevatedButton(
            text="Crea grafo", on_click=self._controller.handle_creaGrafo
        )
        self._page.controls.append(
            ft.Row(
                [self.txtNumAeroporti, self.btnCreaGrafo],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.ddCompagnia = ft.Dropdown(
            label="Compagnia aerea",
            width=330,
            disabled=True
        )
        self.btnCompagnieConcorrenti = ft.ElevatedButton(
            text="Compagnie concorrenti",
            width=210,
            disabled=True,
            on_click=self._controller.handle_compagnieConcorrenti,
        )
        self._page.controls.append(
            ft.Row(
                [self.ddCompagnia, self.btnCompagnieConcorrenti],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.txtNumCompagnie = ft.TextField(
            label="Lunghezza della sequenza", width=260, disabled=True
        )
        self.btnCercaSequenza = ft.ElevatedButton(
            text="Cerca sequenza",
            disabled=True
        )
        self._page.controls.append(
            ft.Row(
                [self.txtNumCompagnie, self.btnCercaSequenza],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.txt_result = ft.ListView(
            expand=1, spacing=10, padding=20, auto_scroll=True
        )
        self._page.controls.append(self.txt_result)
        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        self._page.open(ft.AlertDialog(title=ft.Text(message)))
        self._page.update()

    def update_page(self):
        self._page.update()

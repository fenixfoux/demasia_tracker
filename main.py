import flet as ft
import threading
from test import locationCoordinates

class Tracker:
    def __init__(self):
        self.track_status = False
        self.buttons = ft.Column()
        self.content_page = ft.Column()

    def create_buttons_section(self):
        self.buttons.controls.append(
            ft.Row(controls=[
                ft.ElevatedButton('start', on_click=lambda ev: self.start_tracking()),
                ft.ElevatedButton('stop', on_click=lambda ev: self.stop_tracking())
            ])
        )

    def start_tracking(self):
        self.track_status = True
        threading.Thread(target=self._tracking_thread).start()

    def _tracking_thread(self):
        while self.track_status:
            locationCoordinates()

    def stop_tracking(self):
        self.track_status = False
        print("=" * 20 + f"TRACKING STOPPED" + "=" * 20)

    def main(self):
        self.create_buttons_section()
        self.content_page.controls.append(self.buttons)
        self.content_page.controls.append(ft.Text('asdasdasd'))
        return self.content_page


def main(page: ft.Page):
    page.add(Tracker().main())


ft.app(target=main)

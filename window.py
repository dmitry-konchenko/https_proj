from PyQt5.QtWidgets import QMainWindow
from window_ui import Ui_MainWindow
from static_maps_api import get_map
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._map_zoom = 5
        self._map_ll = 37.977751, 55.757718
        self._map_l = 'map'
        self._init_ui()

    def _init_ui(self) -> None:
        ...

    def _refresh_map(self) -> None:
        image_data = get_map(ll=self._map_ll, zoom=self._map_zoom, map_type=self._map_l)
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        self.map_label.setPixmap(pixmap)
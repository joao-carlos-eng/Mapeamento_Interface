# pyuic5 design.ui -o design.py

import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import kmz_analiser

analizer = kmz_analiser.Application()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, kmz=analizer):
        super().__init__()
        self.setupUi(self)
        self.kmz = kmz

        self.carregarArquivo.clicked.connect(self.select_file)

    def next_placemark(self):
        if self.current_placemark < len(self.placemarks) - 1:
            self.current_placemark += 1
            self.show_placemark()

    def previous_placemark(self):
        if self.current_placemark > 0:
            self.current_placemark -= 1
            self.show_placemark()

    def select_file(self):
        self.kmz.select_file()
        self.kmz.load_placemarks()

        self.exibir_dados()

    def exibir_dados(self):
        place = self.kmz.show_placemark()
        if place.get('picture_path') is not None:
            self.image_area.setPixmap(QPixmap(place['picture_path'].strip()))
            self.image_area.setScaledContents(True)
            self.image_area.adjustSize()
        if place.get('name') is not None:
            self.lineEdit_name.setText(place['name'])
        if place.get('coordinates') is not None:
            self.lineEdit_coordinates.setText(place['coordinates'])
        if place.get('description') is not None:
            self.description.setText(place['description'])
        if place.get('1.altura') is not None:
            self.line_altura.setText(place['1.altura'])
        if place.get('0.tipo') is not None:
            self.line_tipo.setText(place['0.tipo'])
        if place.get('2.esforco') is not None:
            self.line_esforco.setText(place['2.esforco'])
        if place.get('3.rede') is not None:
            self.line_rede.setText(place['3.rede'])
        if place.get('4.casa') is not None:
            self.line_casa.setText(place['4.casa'])
        if place.get('5.comercio') is not None:
            self.line_comercio.setText(place['5.comercio'])
        if place.get('6.predio') is not None:
            self.line_industria.setText(place['6.predio'])
        if place.get('7.equipamento') is not None:
            self.line_equipamento.setText(place['7.equipamento'])
            self.line_codigo.setText(place['8.codigo'])
        if place.get('9.ocupante') is not None:
            self.line_ocupante.setText(place['9.ocupante'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

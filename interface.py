# pyuic5 design.ui -o design.py
import os.path
import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
import kmz_analiser

analizer = kmz_analiser.Application()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, kmz=analizer):
        super().__init__()
        self.setupUi(self)
        self.kmz = kmz

        self.carregarArquivo.clicked.connect(self.select_file)
        self.next.clicked.connect(self.next_placemark)
        self.previous.clicked.connect(self.previous_placemark)

        self.image_area = QLabel(self)

    def next_placemark(self):
        if self.kmz.current_placemark < len(self.kmz.placemarks) - 1:
            self.kmz.current_placemark += 1
            self.exibir_dados()

    def previous_placemark(self):
        if self.kmz.current_placemark > 0:
            self.kmz.current_placemark -= 1
            self.exibir_dados()

    def select_file(self):
        self.kmz.select_file()
        self.kmz.load_placemarks()

        self.exibir_dados()

    def exibir_dados(self):
        self.image_area.clear()
        place = self.kmz.show_placemark()

        if place.get('picture_path') is not None:
            self.exibir_imagem(place['picture_path'])
        else:
            self.exibir_imagem([])

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
            self.line_predio.setText(place['6.predio'])
        if place.get('7.equipamento') is not None:
            self.line_equipamento.setText(place['7.equipamento'])
        if place.get('8.codigo') is not None:
            self.line_codigo.setText(place['8.codigo'])
        else:
            self.line_codigo.setText('Não informado')
        if place.get('9.ocupante') is not None:
            self.line_ocupante.setText(place['9.ocupante'])

    def exibir_imagem(self, list_of_images):
        layout = QGridLayout()

        pixmaps = []
        for path in list_of_images:
            if os.path.exists(path.strip()):
                pixmap = QPixmap(path.strip())
                pixmaps.append(pixmap)
            else:
                print(f"Imagem não encontrada: {path}")

        row_count = 2
        col_count = (len(pixmaps) + 1) // 2
        layout.addWidget(self.image_area, 0, 0, row_count, col_count)
        for i, pixmap in enumerate(pixmaps):
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            row = i // col_count
            col = i % col_count
            layout.addWidget(image_label, row + 1, col)

        self.scrollArea.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

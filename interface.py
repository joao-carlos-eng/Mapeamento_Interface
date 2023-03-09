# pyuic5 design.ui -o design.py
import os.path
import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QHBoxLayout
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

        self.image_widgets = []  # lista de widgets de imagem
        self.image_area = QWidget(self.scroll_Area)  # widget que contém as imagens
        self.image_layout = QHBoxLayout(self.image_area)  # layout para as imagens

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
        place = self.kmz.show_placemark()

        if place.get('picture_path') is not None:
            self.exibir_imagem(place['picture_path'])
        else:
            self.exibir_imagem([])

        if place.get('name') is not None:
            self.lineEdit_name.setText(place['name'])
        else:
            self.lineEdit_name.setText('Sem nome')
        if place.get('coordinates') is not None:
            self.lineEdit_coordinates.setText(place['coordinates'])
        else:
            self.lineEdit_coordinates.setText('ponto invalido')
        if place.get('description') is not None:
            self.description.setText(place['description'])
        else:
            self.description.setText('')
        if place.get('1.altura') is not None:
            self.line_altura.setText(place['1.altura'])
        else:
            self.line_altura.setText('')
        if place.get('0.tipo') is not None:
            self.line_tipo.setText(place['0.tipo'])
        else:
            self.line_tipo.setText('')
        if place.get('2.esforco') is not None:
            self.line_esforco.setText(place['2.esforco'])
        else:
            self.line_esforco.setText('')
        if place.get('3.rede') is not None:
            self.line_rede.setText(place['3.rede'])
        else:
            self.line_rede.setText('')
        if place.get('4.casa') is not None:
            self.line_casa.setText(place['4.casa'])
        else:
            self.line_casa.setText('')
        if place.get('5.comercio') is not None:
            self.line_comercio.setText(place['5.comercio'])
        else:
            self.line_comercio.setText('')
        if place.get('6.predio') is not None:
            self.line_predio.setText(place['6.predio'])
        else:
            self.line_predio.setText('')
        if place.get('7.equipamento') is not None:
            self.line_equipamento.setText(place['7.equipamento'])
        else:
            self.line_equipamento.setText('')
        if place.get('8.codigo') is not None:
            self.line_codigo.setText(place['8.codigo'])
        elif place.get('7.equipamento') and not place.get('8.codigo'):
            self.line_codigo.setText('Não informado')
        else:
            self.line_codigo.setText('')
        if place.get('9.ocupante') is not None:
            self.line_ocupante.setText(place['9.ocupante'])
        else:
            self.line_ocupante.setText('')

    def exibir_imagem(self, list_of_images):
        # Limpa o layout anterior
        for image_widget in self.image_widgets:
            self.image_layout.removeWidget(image_widget)
            image_widget.deleteLater()
        self.image_widgets.clear()

        # Adiciona as novas imagens
        for path in list_of_images:
            if os.path.exists(path.strip()):
                pixmap = QPixmap(path.strip())
                image_label = QLabel(self)
                image_label.setPixmap(pixmap)
                self.image_widgets.append(image_label)
                self.image_layout.addWidget(image_label)

        # Define o layout do widget de scroll como sendo o layout que contém as imagens
        self.scroll_Area.setLayout(self.image_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

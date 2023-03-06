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

    def abrir_imagem(self):
        self.imagem = QFileDialog.getOpenFileName(self, 'Abrir Imagem', filter='Imagens (*.png *.jpg *.bmp)')[0]
        if self.imagem:
            self.label_14.setPixmap(QPixmap(self.imagem))
            self.label_14.setScaledContents(True)
            self.label_14.adjustSize()

    def next_placemark(self):
        if self.current_placemark < len(self.placemarks) - 1:
            self.current_placemark += 1
            self.show_placemark()

    def previous_placemark(self):
        if self.current_placemark > 0:
            self.current_placemark -= 1
            self.show_placemark()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

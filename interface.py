# pyuic5 design.ui -o design.py

import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

    def abrir_imagem(self):
        self.imagem = QFileDialog.getOpenFileName(self, 'Abrir Imagem', filter='Imagens (*.png *.jpg *.bmp)')[0]
        if self.imagem:
            self.label_14.setPixmap(QPixmap(self.imagem))
            self.label_14.setScaledContents(True)
            self.label_14.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

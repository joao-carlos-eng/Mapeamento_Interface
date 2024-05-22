# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QStatusBar, QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 897)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_esforco = QLabel(self.centralwidget)
        self.label_esforco.setObjectName(u"label_esforco")

        self.gridLayout.addWidget(self.label_esforco, 4, 0, 1, 1)

        self.anterior = QPushButton(self.centralwidget)
        self.anterior.setObjectName(u"anterior")

        self.gridLayout.addWidget(self.anterior, 8, 6, 1, 1)

        self.line_esforco = QLineEdit(self.centralwidget)
        self.line_esforco.setObjectName(u"line_esforco")

        self.gridLayout.addWidget(self.line_esforco, 4, 1, 1, 1)

        self.proximo = QPushButton(self.centralwidget)
        self.proximo.setObjectName(u"proximo")

        self.gridLayout.addWidget(self.proximo, 8, 7, 1, 1)

        self.label_codigo = QLabel(self.centralwidget)
        self.label_codigo.setObjectName(u"label_codigo")

        self.gridLayout.addWidget(self.label_codigo, 5, 2, 1, 1)

        self.label_rede = QLabel(self.centralwidget)
        self.label_rede.setObjectName(u"label_rede")

        self.gridLayout.addWidget(self.label_rede, 5, 0, 1, 1)

        self.descricao = QTextEdit(self.centralwidget)
        self.descricao.setObjectName(u"descricao")

        self.gridLayout.addWidget(self.descricao, 2, 5, 5, 3)

        self.label_comercio = QLabel(self.centralwidget)
        self.label_comercio.setObjectName(u"label_comercio")

        self.gridLayout.addWidget(self.label_comercio, 2, 2, 1, 1)

        self.label_ocupante = QLabel(self.centralwidget)
        self.label_ocupante.setObjectName(u"label_ocupante")

        self.gridLayout.addWidget(self.label_ocupante, 6, 2, 1, 1)

        self.line_rede = QLineEdit(self.centralwidget)
        self.line_rede.setObjectName(u"line_rede")

        self.gridLayout.addWidget(self.line_rede, 5, 1, 1, 1)

        self.line_casa = QLineEdit(self.centralwidget)
        self.line_casa.setObjectName(u"line_casa")

        self.gridLayout.addWidget(self.line_casa, 6, 1, 1, 1)

        self.label_casa = QLabel(self.centralwidget)
        self.label_casa.setObjectName(u"label_casa")

        self.gridLayout.addWidget(self.label_casa, 6, 0, 1, 1)

        self.line_codigo = QLineEdit(self.centralwidget)
        self.line_codigo.setObjectName(u"line_codigo")

        self.gridLayout.addWidget(self.line_codigo, 5, 3, 1, 1)

        self.line_predio = QLineEdit(self.centralwidget)
        self.line_predio.setObjectName(u"line_predio")

        self.gridLayout.addWidget(self.line_predio, 3, 3, 1, 1)

        self.label_nome = QLabel(self.centralwidget)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout.addWidget(self.label_nome, 1, 4, 1, 1)

        self.line_tipo = QLineEdit(self.centralwidget)
        self.line_tipo.setObjectName(u"line_tipo")

        self.gridLayout.addWidget(self.line_tipo, 2, 1, 1, 1)

        self.label_tipo = QLabel(self.centralwidget)
        self.label_tipo.setObjectName(u"label_tipo")

        self.gridLayout.addWidget(self.label_tipo, 2, 0, 1, 1)

        self.lineEdit_nome = QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")

        self.gridLayout.addWidget(self.lineEdit_nome, 1, 5, 1, 3)

        self.label_altura = QLabel(self.centralwidget)
        self.label_altura.setObjectName(u"label_altura")

        self.gridLayout.addWidget(self.label_altura, 3, 0, 1, 1)

        self.line_altura = QLineEdit(self.centralwidget)
        self.line_altura.setObjectName(u"line_altura")

        self.gridLayout.addWidget(self.line_altura, 3, 1, 1, 1)

        self.label_predio = QLabel(self.centralwidget)
        self.label_predio.setObjectName(u"label_predio")

        self.gridLayout.addWidget(self.label_predio, 3, 2, 1, 1)

        self.line_equipamento = QLineEdit(self.centralwidget)
        self.line_equipamento.setObjectName(u"line_equipamento")

        self.gridLayout.addWidget(self.line_equipamento, 4, 3, 1, 1)

        self.label_equipamento = QLabel(self.centralwidget)
        self.label_equipamento.setObjectName(u"label_equipamento")

        self.gridLayout.addWidget(self.label_equipamento, 4, 2, 1, 1)

        self.line_ocupante = QLineEdit(self.centralwidget)
        self.line_ocupante.setObjectName(u"line_ocupante")

        self.gridLayout.addWidget(self.line_ocupante, 6, 3, 1, 1)

        self.carregar_arquivo = QPushButton(self.centralwidget)
        self.carregar_arquivo.setObjectName(u"carregar_arquivo")

        self.gridLayout.addWidget(self.carregar_arquivo, 8, 5, 1, 1)

        self.label_descricao = QLabel(self.centralwidget)
        self.label_descricao.setObjectName(u"label_descricao")

        self.gridLayout.addWidget(self.label_descricao, 4, 4, 1, 1)

        self.reprovar = QPushButton(self.centralwidget)
        self.reprovar.setObjectName(u"reprovar")

        self.gridLayout.addWidget(self.reprovar, 7, 7, 1, 1)

        self.label_extendedData = QLabel(self.centralwidget)
        self.label_extendedData.setObjectName(u"label_extendedData")
        self.label_extendedData.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_extendedData, 1, 0, 1, 4)

        self.refazer = QPushButton(self.centralwidget)
        self.refazer.setObjectName(u"refazer")

        self.gridLayout.addWidget(self.refazer, 7, 6, 1, 1)

        self.aprovar = QPushButton(self.centralwidget)
        self.aprovar.setObjectName(u"aprovar")

        self.gridLayout.addWidget(self.aprovar, 7, 5, 1, 1)

        self.line_comercio = QLineEdit(self.centralwidget)
        self.line_comercio.setObjectName(u"line_comercio")

        self.gridLayout.addWidget(self.line_comercio, 2, 3, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_Area = QWidget()
        self.scroll_Area.setObjectName(u"scroll_Area")
        self.scroll_Area.setGeometry(QRect(0, 0, 718, 628))
        self.scrollArea.setWidget(self.scroll_Area)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 8)

        self.label_coords = QLabel(self.centralwidget)
        self.label_coords.setObjectName(u"label_coords")

        self.gridLayout.addWidget(self.label_coords, 8, 0, 1, 1)

        self.coordinates = QLineEdit(self.centralwidget)
        self.coordinates.setObjectName(u"coordinates")

        self.gridLayout.addWidget(self.coordinates, 8, 1, 1, 1)

        self.salvar_arquivo = QPushButton(self.centralwidget)
        self.salvar_arquivo.setObjectName(u"salvar_arquivo")

        self.gridLayout.addWidget(self.salvar_arquivo, 8, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_esforco.setText(QCoreApplication.translate("MainWindow", u"2.esforco", None))
        self.anterior.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.proximo.setText(QCoreApplication.translate("MainWindow", u"Proximo", None))
        self.label_codigo.setText(QCoreApplication.translate("MainWindow", u"8.codigo", None))
        self.label_rede.setText(QCoreApplication.translate("MainWindow", u"3.rede", None))
        self.label_comercio.setText(QCoreApplication.translate("MainWindow", u"5.comercio", None))
        self.label_ocupante.setText(QCoreApplication.translate("MainWindow", u"9.ocupante", None))
        self.label_casa.setText(QCoreApplication.translate("MainWindow", u"4.casa", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_tipo.setText(QCoreApplication.translate("MainWindow", u"0.tipo", None))
        self.label_altura.setText(QCoreApplication.translate("MainWindow", u"1.altura", None))
        self.label_predio.setText(QCoreApplication.translate("MainWindow", u"6.predio", None))
        self.label_equipamento.setText(QCoreApplication.translate("MainWindow", u"7.equipamento", None))
        self.carregar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.label_descricao.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">descri\u00e7\u00e3o/Notas</span></p></body></html>",
                                                                None))
        self.reprovar.setText(QCoreApplication.translate("MainWindow", u"Reprovar", None))
        self.label_extendedData.setText(QCoreApplication.translate("MainWindow", u"ExtendedData", None))
        self.refazer.setText(QCoreApplication.translate("MainWindow", u"Refazer", None))
        self.aprovar.setText(QCoreApplication.translate("MainWindow", u"Aprovar", None))
        self.label_coords.setText(QCoreApplication.translate("MainWindow", u"Coordenadas", None))
        self.salvar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

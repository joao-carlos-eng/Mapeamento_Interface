import os
import shutil
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from design import Ui_MainWindow
from auto_save import AutoSave
import kmz_analiser

analizer = kmz_analiser.Application()


def gerar_pixmaps(path):
    image = QPixmap(path)
    new_image = image.scaled(688, 620)
    return new_image


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, kmz=analizer):
        super().__init__()
        self.setupUi(self)
        self.kmz = kmz
        self.auto_save = AutoSave()

        self.carregar_arquivo.clicked.connect(self.select_file)
        self.proximo.clicked.connect(self.next_placemark)
        self.anterior.clicked.connect(self.previous_placemark)
        self.aprovar.clicked.connect(self.aprovar_place)
        self.refazer.clicked.connect(self.refazer_place)
        self.reprovar.clicked.connect(self.reprovar_place)
        self.salvar_arquivo.clicked.connect(self.salvar_alteracoes)

        self.image_widgets = []  # lista de widgets de imagem
        self.image_area = QWidget(self.scroll_Area)  # widget que contém as imagens
        self.image_layout = QHBoxLayout(self.image_area)  # layout para as imagens

        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_analizar_step)

    def select_file(self):
        self.kmz.select_file()

        estado_salvo = self.auto_save.load_state(self.kmz.filename)
        if estado_salvo:
            if self.perguntar_retomar_estado():
                self.kmz.current_placemark = estado_salvo['current_placemark']
            else:
                self.kmz.current_placemark = 0

        self.kmz.load_placemarks()
        self.auto_analizar()  # Realiza a análise automática
        self.exibir_dados()

    def perguntar_retomar_estado(self):
        resposta = QMessageBox.question(self, "Retomar Estado",
                                        "Encontrado um estado salvo para este arquivo. Deseja retomar?",
                                        QMessageBox.Yes | QMessageBox.No)
        return resposta == QMessageBox.Yes

    def next_placemark(self):
        if self.kmz.current_placemark < len(self.kmz.placemarks) - 1:
            self.kmz.current_placemark += 1
            self.exibir_dados()
            self.save_state()

    def previous_placemark(self):
        if self.kmz.current_placemark > 0:
            self.kmz.current_placemark -= 1
            self.exibir_dados()
            self.save_state()

    def aprovar_place(self):
        self.kmz.aprovados.append(self.kmz.placemarks[self.kmz.current_placemark])
        self.next_placemark()

    def refazer_place(self):
        self.kmz.a_refazer.append(self.kmz.placemarks[self.kmz.current_placemark])
        self.next_placemark()

    def reprovar_place(self):
        self.kmz.reprovados.append(self.kmz.placemarks[self.kmz.current_placemark])
        self.next_placemark()

    def exibir_dados(self):
        place = self.kmz.show_placemark()

        if place.get('picture_path') is not None:
            self.exibir_imagem(place['picture_path'])
        else:
            self.exibir_imagem([])

        self.lineEdit_nome.setText(place.get('name', 'Sem nome'))
        self.coordinates.setText(place.get('coordinates', 'ponto invalido'))
        self.descricao.setText(place.get('description', ''))
        self.line_altura.setText(place.get('1.altura', ''))
        self.line_tipo.setText(place.get('0.tipo', ''))
        self.line_esforco.setText(place.get('2.esforco', ''))
        self.line_rede.setText(place.get('3.rede', ''))
        self.line_casa.setText(place.get('4.casa', ''))
        self.line_comercio.setText(place.get('5.comercio', ''))
        self.line_predio.setText(place.get('6.predio', ''))
        self.line_equipamento.setText(place.get('7.equipamento', ''))
        self.line_codigo.setText(place.get('8.codigo', 'Não informado'))
        self.line_ocupante.setText(place.get('9.ocupantes', ''))

    def exibir_imagem(self, list_of_images):
        for image_widget in self.image_widgets:
            self.image_layout.removeWidget(image_widget)
            image_widget.deleteLater()
        self.image_widgets.clear()

        for path in list_of_images:
            path.strip()
            if os.path.exists(path):
                if self.kmz.file_images.get(path):
                    image = self.kmz.file_images[path]
                else:
                    image = gerar_pixmaps(path)
                    self.kmz.file_images[path] = image
                image_label = QLabel(self)
                image_label.setPixmap(image)
                self.image_widgets.append(image_label)
                self.image_layout.addWidget(image_label)

        self.scroll_Area.setLayout(self.image_layout)

    def salvar_alteracoes(self):
        path_to_save = QFileDialog.getExistingDirectory(self, 'Selecione o diretório para salvar os arquivos')
        if not path_to_save:
            return

        result = self.kmz.save_to_kmz()
        if result is None:
            QMessageBox.warning(self, "Erro", "Não foi possível salvar o arquivo KMZ.")
            return

        shutil.copyfile(result, os.path.join(path_to_save, os.path.basename(result)))

        self.kmz.aprovados = []
        self.kmz.reprovados = []
        self.kmz.a_refazer = []
        self.kmz.current_placemark = 0

    def save_state(self):
        estado = {'current_placemark': self.kmz.current_placemark}
        self.auto_save.save_state(self.kmz.filename, estado)

    def auto_analizar(self):
        self.timer.start(300)  # Intervalo de 500ms

    def auto_analizar_step(self):
        if self.kmz.current_placemark >= len(self.kmz.placemarks) - 1:
            self.timer.stop()
            QMessageBox.information(self, "Análise Automática", "Análise Automática Concluída")
            return

        placemark = self.kmz.placemarks[self.kmz.current_placemark]
        placemark_atributos = self.kmz.get_placemark_data(placemark)
        status = kmz_analiser.auto_analisar(placemark_atributos)
        if status == 'aprovado':
            self.aprovar.click()
        elif status == 'a_refazer':
            self.refazer.click()
        elif status == 'reprovado':
            self.reprovar.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

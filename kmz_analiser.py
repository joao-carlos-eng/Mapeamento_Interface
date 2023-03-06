import os
import shutil
import tempfile
import zipfile
from tkinter import filedialog
from xml.etree import ElementTree as ET


def extract_kml(kmz_path):
    # Cria uma pasta temporária
    temp_dir = tempfile.mkdtemp()

    # Extrai o arquivo.kml do KMZ para a pasta temporária
    with zipfile.ZipFile(kmz_path, 'r') as zip_ref:
        zip_ref.extract('doc.kml', temp_dir)

    # Cria uma pasta "files" na pasta temporária
    files_dir = os.path.join(temp_dir, 'files')
    os.mkdir(files_dir)

    # Extrai todos os arquivos.jpg da pasta "files" no KMZ para a pasta "files" na pasta temporária
    with zipfile.ZipFile(kmz_path, 'r') as zip_ref:
        for zip_info in zip_ref.infolist():
            if zip_info.filename.startswith('files/') and zip_info.filename.endswith('.jpg'):
                filename = os.path.basename(zip_info.filename)
                target_path = os.path.join(files_dir, filename)
                with zip_ref.open(zip_info) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)

    # Retorna o caminho para o arquivo.kml e a pasta "files"
    return os.path.join(temp_dir, 'doc.kml'), files_dir


class Application:

    def __init__(self):
        self.placemarks = []
        self.current_placemark = 0
        self.filename = ''
        self.tmp_folder = ''

    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecione um arquivo KMZ",
                                                   filetypes=[("KMZ files", "*.kmz")])
        self.tmp_folder = extract_kml(self.filename)

    def load_placemarks(self):
        # Analisa o arquivo KML usando a biblioteca Etree e encontra todos os placemarks pontos com extensões de dados.
        tree = ET.parse(self.tmp_folder[0])
        root = tree.getroot()
        placemarks = root.findall(
            ".//{http://www.opengis.net/kml/2.2}Placemark[{http://www.opengis.net/kml/2.2}Point]/{"
            "http://www.opengis.net/kml/2.2}ExtendedData")
        for placemark in placemarks:
            self.placemarks.append(placemark)

        self.current_placemark = 0

        self.show_placemark()

    def show_placemark(self):
        # Cria uma janela interativa que exibe as informações dos placemarks encontrados.
        if self.current_placemark < len(self.placemarks):
            placemark = self.placemarks[self.current_placemark]
            # Adicione um código para mostrar as informações do placemark.
            placemark_atributos = {}
            for data in placemark.findall(r".//{http://www.opengis.net/kml/2.2}Data"):
                name = data.attrib['name']
                try:
                    value = data.find(r"{http://www.opengis.net/kml/2.2}value").text
                except AttributeError:
                    continue
                placemark_atributos[name] = value
                print(placemark_atributos)
            if placemark_atributos.get('pictures') is not None:
                picture = placemark_atributos.get('pictures')
                picture_path = os.path.join(self.tmp_folder[1], picture)
                print(self.current_placemark, picture_path)
        else:
            ...
            # Adicione um código para mostrar uma mensagem de que todos os placemarks foram analisados.

    def move_placemark(self, category):
        # Adicione um código para mover o placemark para a pasta aprovados ou reprovados, dependendo da categoria.
        placemark = self.placemarks[self.current_placemark]
        category_folder = os.path.join(os.path.dirname(self.filename), category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        move_folder = os.path.join(category_folder, placemark.get('id') + ".kml")
        with open(move_folder, 'wb') as f:
            f.write(ET.tostring(placemark))

    def next_placemark(self):
        if self.current_placemark < len(self.placemarks) - 1:
            self.current_placemark += 1
            self.show_placemark()

    def previous_placemark(self):
        if self.current_placemark > 0:
            self.current_placemark -= 1
            self.show_placemark()


app = Application()
app.select_file()
app.load_placemarks()


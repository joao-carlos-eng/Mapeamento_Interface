import os
import shutil
import tempfile
import zipfile
from tkinter import filedialog
from xml.etree import ElementTree as Et


# Função para extrair o arquivo.kml e a pasta "files" do KMZ
def extract_kmz(kmz_path):
    # Cria uma pasta temporária
    temp_dir = tempfile.mkdtemp()

    # Extrai o arquivo.kml do KMZ para a pasta temporária
    with zipfile.ZipFile(kmz_path, 'r') as zip_ref:
        zip_ref.extract('doc.kml', temp_dir)

    # Cria uma pasta "files" na pasta temporária
    files_dir = os.path.join(temp_dir, 'files')
    os.mkdir(files_dir)

    # Extrai todos os arquivos.jpg da pasta "files" ou "images" no KMZ para a pasta "files" na pasta temporária
    with zipfile.ZipFile(kmz_path, 'r') as zip_ref:
        for zip_info in zip_ref.infolist():
            if (zip_info.filename.startswith('files/') or zip_info.filename.startswith('images/')) and zip_info.filename.endswith('.jpg'):
                filename = os.path.basename(zip_info.filename)
                target_path = os.path.join(files_dir, filename)
                with zip_ref.open(zip_info) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target, 1024 * 8)

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
        self.tmp_folder = extract_kmz(self.filename)

    def load_placemarks(self):
        # Analisa o arquivo KML usando a biblioteca Etree e encontra todos os placemarks pontos com extensões de dados.
        tree = Et.parse(self.tmp_folder[0])
        root = tree.getroot()
        placemarks = root.findall(
            ".//{http://www.opengis.net/kml/2.2}Placemark[{http://www.opengis.net/kml/2.2}Point]")

        for placemark in placemarks:
            self.placemarks.append(placemark)

    def show_placemark(self):
        if self.current_placemark < len(self.placemarks):
            placemark = self.placemarks[self.current_placemark]
            placemark_atributos = {}

            name = placemark.find(".//{http://www.opengis.net/kml/2.2}name").text
            coordinates = placemark.find(".//{http://www.opengis.net/kml/2.2}coordinates").text
            description = placemark.find(".//{http://www.opengis.net/kml/2.2}description").text if placemark.find(
                ".//{http://www.opengis.net/kml/2.2}description") is not None else ''
            placemark_atributos['name'] = name
            placemark_atributos['coordinates'] = coordinates
            placemark_atributos['description'] = description

            for data in placemark.findall(".//{http://www.opengis.net/kml/2.2}ExtendedData/{"
                                          "http://www.opengis.net/kml/2.2}Data"):
                name = data.attrib['name']
                try:
                    value = data.find("{http://www.opengis.net/kml/2.2}value").text
                except AttributeError:
                    continue
                placemark_atributos[name] = value

            if placemark_atributos.get('pictures') is not None:
                picture = placemark_atributos.get('pictures')
                picture_path = os.path.join(self.tmp_folder[1], picture)
                placemark_atributos['picture_path'] = picture_path

            print(placemark_atributos)
            return placemark_atributos

    def move_placemark(self, category):
        # Adicione um código para mover o placemark para a pasta aprovados ou reprovados, dependendo da categoria.
        placemark = self.placemarks[self.current_placemark]
        category_folder = os.path.join(os.path.dirname(self.filename), category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        move_folder = os.path.join(category_folder, placemark.get('id') + ".kml")
        with open(move_folder, 'wb') as f:
            f.write(Et.tostring(placemark))


if __name__ == '__main__':
    app = Application()
    app.select_file()
    app.load_placemarks()
    placemark = app.show_placemark()
    print(placemark)

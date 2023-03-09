import os
import re
import tempfile
import zipfile
from tkinter import filedialog
from xml.etree import ElementTree as Et


def tratar_picture_path(picture_path, tmp_folder):
    padrao = r'<img src="([^"]+)"\/>'
    matches = re.findall(padrao, picture_path)

    lista_imagens = []
    if len(matches) > 0:
        for match in matches:
            lista_imagens.append(os.path.join(tmp_folder, match))

    return lista_imagens


def extract_files_from_kmz(kmz_path):
    # extrai todos os arquivos do kmz para uma pasta temporária
    tmp_folder = tempfile.mkdtemp()
    with zipfile.ZipFile(kmz_path, 'r') as zip_ref:
        if 'doc.kml' in zip_ref.namelist():
            zip_ref.extract('doc.kml', tmp_folder)
        for file in zip_ref.namelist():
            if file.endswith('.jpg') or file.endswith('.JPG'):
                try:
                    zip_ref.extract(file, tmp_folder)
                except Exception as e:
                    print('Imagem corrompida: ', file)
                    pass
                continue

    kml_path = os.path.join(tmp_folder, 'doc.kml')

    return kml_path, tmp_folder


class Application:

    def __init__(self):
        self.placemarks = []
        self.current_placemark = 0
        self.filename = ''
        self.tmp_folder = ''

    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecione um arquivo KMZ",
                                                   filetypes=[("KMZ files", "*.kmz")])
        self.tmp_folder = extract_files_from_kmz(self.filename)

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
                picture_path = tratar_picture_path(picture, self.tmp_folder[1])
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

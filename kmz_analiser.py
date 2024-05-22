# kmz_analiser.py
import os
import re
import tempfile
import zipfile
from tkinter import filedialog, messagebox
from xml.etree import ElementTree as Et
from pprint import pprint


def tratar_picture_path(picture_path, tmp_folder):
    padrao = r'<img src="([^"]+)"\/>'
    matches = re.findall(padrao, picture_path)

    lista_imagens = []
    if len(matches) > 0:
        for match in matches:
            lista_imagens.append(os.path.join(tmp_folder, match))

    return lista_imagens


def extract_files_from_kmz(kmz_path):
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

    return {'kml_path': kml_path, 'images_folder': tmp_folder}


def auto_analisar(placemark):
    altura = placemark.get('1.altura')
    tracao = placemark.get('2.esforco')
    pictures = placemark.get('picture_path')
    codigo = placemark.get('8.codigo')
    equipamento = placemark.get('7.equipamento')

    if not any([altura, tracao, pictures]):
        return 'reprovado'

    if not altura or not tracao:
        return 'a_refazer'

    if not pictures:
        return 'a_refazer'

    if equipamento and not codigo:
        return 'a_refazer'

    return 'aprovado'


class Application:

    def __init__(self):
        self.placemarks = []
        self.current_placemark = 0
        self.filename = ''
        self.tmp_folder = {}
        self.file_images = {}
        self.aprovados = []
        self.reprovados = []
        self.a_refazer = []

    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecione um arquivo KMZ",
                                                   filetypes=[("KMZ files", "*.kmz")])
        self.tmp_folder = extract_files_from_kmz(self.filename)

    def load_placemarks(self):
        tree = Et.parse(self.tmp_folder['kml_path'])
        root = tree.getroot()
        placemarks = root.findall(
            ".//{http://www.opengis.net/kml/2.2}Placemark[{http://www.opengis.net/kml/2.2}Point]")

        for place in placemarks:
            self.placemarks.append(place)

    def show_placemark(self):
        if self.current_placemark < len(self.placemarks):
            placemark = self.placemarks[self.current_placemark]
            placemark_atributos = self.get_placemark_data(placemark)
            pprint(placemark_atributos)
            return placemark_atributos

    def move_placemark(self, category):
        placemark = self.placemarks[self.current_placemark]
        category_folder = os.path.join(os.path.dirname(self.filename), category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        move_folder = os.path.join(category_folder, placemark.get('id') + ".kml")
        with open(move_folder, 'wb') as f:
            f.write(Et.tostring(placemark))

    def save_to_kmz(self):
        if not self.filename:
            # exibe uma mensagem de erro
            messagebox.showerror("Erro", f"Nenhum arquivo selecionado: {self.filename}")
            return None

        doc = Et.parse(self.tmp_folder['kml_path'])
        root = doc.getroot()

        aprovados_folder = Et.Element('Folder')
        aprovados_folder.set('id', 'Aprovados')
        reprovados_folder = Et.Element('Folder')
        reprovados_folder.set('id', 'Reprovados')
        refazer_folder = Et.Element('Folder')
        refazer_folder.set('id', 'A refazer')

        for place in self.aprovados:
            aprovados_folder.append(place)
        for place in self.reprovados:
            reprovados_folder.append(place)
        for place in self.a_refazer:
            refazer_folder.append(place)

        root[0].append(aprovados_folder)
        root[0].append(reprovados_folder)
        root[0].append(refazer_folder)

        doc.write(self.tmp_folder['kml_path'])

        kmz_path = self.filename.replace('.kmz', '_new.kmz')
        with zipfile.ZipFile(kmz_path, 'w') as zip_ref:
            zip_ref.write(self.tmp_folder['kml_path'], 'doc.kml')

            for file in os.listdir(self.tmp_folder['images_folder']):
                if file.endswith('.jpg') or file.endswith('.JPG'):
                    zip_ref.write(os.path.join(self.tmp_folder['images_folder'], file), file)

        return kmz_path

    def processar_placemarks(self):
        for placemark in self.placemarks:
            placemark_atributos = self.get_placemark_data(placemark)
            status = auto_analisar(placemark_atributos)
            if status == 'aprovado':
                self.aprovados.append(placemark)
            elif status == 'a_refazer':
                self.a_refazer.append(placemark)
            elif status == 'reprovado':
                self.reprovados.append(placemark)

    def get_placemark_data(self, placemark):
        placemark_atributos = {}

        name_element = placemark.find(".//{http://www.opengis.net/kml/2.2}name")
        coordinates_element = placemark.find(".//{http://www.opengis.net/kml/2.2}coordinates")
        description_element = placemark.find(".//{http://www.opengis.net/kml/2.2}description")

        name = name_element.text if name_element is not None else None
        coordinates = coordinates_element.text if coordinates_element is not None else None
        description = description_element.text if description_element is not None else ''

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
            picture_path = tratar_picture_path(picture, self.tmp_folder['images_folder'])
            placemark_atributos['picture_path'] = picture_path
            self.file_images.update({path: None for path in picture_path})

        return placemark_atributos

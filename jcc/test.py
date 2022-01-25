import xml.etree.ElementTree as P
import requests


URL = "https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml"
response = requests.get(URL)
with open("velo.xml", 'wb') as fichier:
    fichier.write(response.content)


fichier = "velo.xml"
print(fichier)
tree = P.parse(fichier)
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
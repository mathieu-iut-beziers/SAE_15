from os import read
import requests
from lxml import etree 
import time

temps=int(time.time())
print(temps)

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 

f1=open("parkings","w", encoding='utf8')

liste_des_parking = []
for i in range(len(parkings)):
    liste_provisoir = []
    url="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
    print(url)
    response=requests.get(url)
    tree = etree.fromstring(response.content)
    for user in tree.xpath("Name"):
        print('Nom du parking :',user.text)
        f1.write(f"Nom du parking : {user.text}\n")
        liste_provisoir.append(user.text)
    for user in tree.xpath("Total"):
        place = user.text
        print('Nombre total de places :',user.text)
        f1.write(f"Nombre total de places : {user.text}\n")
        liste_provisoir.append(user.text)
    for user in tree.xpath("Free"):
        place_libre = user.text
        print('Nombre de places libres :',user.text)
        f1.write(f"Nombre de places libres : {user.text}\n")
        liste_provisoir.append(user.text)
    liste_des_parking.append(liste_provisoir)
    print(place,place_libre)
    place_libre = int(place_libre)
    place = int(place)
    pour_cent = str(round((place_libre * 100)/place))
    print("Pourcentage de place libre : "+pour_cent+" %")
    f1.write(f"Pourcentage de place libre : "+pour_cent+" %\n")
f1.close() 

print(liste_des_parking)
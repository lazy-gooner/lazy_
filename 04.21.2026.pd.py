import json
import csv

with open("uzd2.json","r",encoding="utf-8")as datne:
  dati=json.load(datne)
pilsetas=["Rīga","Daugavpils","Liepāja","Jelgava","Jūrmala","Ventspils","Rēzekne","Valmiera","Ogre","Jēkabpils"]
pensionaru_ipastsvars=[]
for pilsetas in pensionaru_ipastsvars:
 with open("rezultati.csv", "w", encoding="utf-8") as save:
  procentos = csv.writer(save)
  procentos.writerow(["Pilsēta", "pensionāru_īpastsvars"])
  for i in range(len(pilsetas)):
    pilsetas = pensionaru_ipastsvars[i]
    print()
    Normunda Zujeva darbs
    



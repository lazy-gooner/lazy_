import json
import csv

with open("uzd2.json","r",encoding="utf-8")as datne:
  dati=json.load(datne)
pilsētas=["Rīga","Daugavpils","Liepāja","Jelgava","Jūrmala","Ventspils","Rēzekne","Valmiera","Ogre","Jēkabpils"]
pensionāru_īpastsvars=[]
for pilsētas in pensionāru_īpastsvars:
with open("rezultati.csv", "w", encoding="utf-8") as save:
  rakstitajs = csv.writer(save)
  rakstitajs.writerow(["Pilsēta", "pensionāru_īpastsvars"( %)"])
  for i in range(len(pilsētas)):
    pilsētas = pensionāru_īpastsvars[i]
    



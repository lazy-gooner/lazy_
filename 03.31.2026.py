import pyjokes
import pyfiglet
import cowsay

joks=pyjokes.get_joke()
parv=pyfiglet.figlet_format(joks,font="bubble")

print(cowsay.ghostbusters(parv))

import csv
#nolasu
datne=open("kontakti.csv",encoding="utf-8")
saturs=list(csv.reader(datne))#parveidoju par sarakstu
datne.close()
print(saturs)#saraksts

#izvade pa 1

for cilveks in saturs:
    print(cilveks[0],"\t",cilveks[-2])

#saraksts
galvene=["vārds","uzvārds","tel.","Pilsēta"]

#saglabāšana
with open("k1.csv","w",newline="", encoding="utf-8") as fails:
    i=csv.writer(fails, delimiter="\t")
    i.writerow(galvene)
    i.writerows(saturs)

    print(galvene,"\t",saturs)

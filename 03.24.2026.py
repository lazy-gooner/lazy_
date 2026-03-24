import re
with open("klienti.txt","r",emcoding="UTF-8")as datne:
   dati=datne.read()

epasts=re.findall(r"\w+@\w+\.\w+",dati)
print("E-pasti: ",epasts)
telfonanum=re.findall(r"\d{8}")
print(telfonanum)

blehbleh=re.sub(r"\d{8}","✆",dati)
print(blehbleh)
datne=open("klienti.txt","W",emcoding="utf-8")
datne.write(blehbleh)


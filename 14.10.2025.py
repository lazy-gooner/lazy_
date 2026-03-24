import re
with open("klienti.txt","r",emcoding="UTF-8")as datne:
   dati=datne.read()

epasts=re.findall(r"\w+@\w+\.\w+",dati)
print("E-pasti: ",epasts)




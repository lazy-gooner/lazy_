temp=[]
datne=open("temperatura.txt","r",encoding="utf+8")
dati=datne.read()
datne.close()
temo=dati.split("")
print(temp[0],temp[12],temp[22])
print(f"{float(temp[8]*9/5+32)} {float(temp[12]*9/5+32)} {float(temp[16]*9/5+32)} ")
print(f"videja {float(temp[0]),{float(temp[6]),{float(temp[12]),{float(temp[18])  ")

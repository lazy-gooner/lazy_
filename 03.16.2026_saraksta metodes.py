vardi=[]

datne=open("vardi.txt","r",encoding="utf-8")
dati=datne.read()

print(type(dati))
vardi=dati.split(", ")
vardi.sort()
for i in vardi:
    if i.startswith("R"):
       print(i)
       with open("r.txt","w",encoding="utf-8") as f:
           f.write(i)

datne.close()


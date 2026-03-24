import random
sk=[-24, -10, 2, 6]
skaitlis=[]
for i in range(7):
    sk1=random.randint(-7, 7)
    skaitlis.insert(i,sk1)
print(skaitlis)
skaitlis+=sk
skaitlis.extend(sk)
# noinspection PyUnboundLocalVariable
skaitlis.insert(0, sk1)
print(skaitlis)
skaitlis.append(-23)
skaitlis.insert(2,-19)
print(skaitlis)
skaitlis.remove(skaitlis[5])
print(skaitlis)
"-------------------------------------------------------------------------------------------------------------"
datne=open("skaitlis.txt","w",encoding="utf-8")
datne.write(str(skaitlis))
datne.close()
print(f"min={min(skaitlis)}, max={max(skaitlis)},vid={sum(skaitlis)/len(skaitlis)}")
"___________________________________________________________________________________________________________________"
fails=open("vardi.txt","r",encoding="utf-8")
dati=fails.read().split(", ")
dati.sort()
print(type(dati))
for i in dati:
    if i.startswith("R")==True:
        print(i)
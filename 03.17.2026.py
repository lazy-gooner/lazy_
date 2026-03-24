import json

datne2 = open("priekšmetu.txt", "r", encoding="utf-8")
x = json.load(datne2)
datne2.close()

print(x)
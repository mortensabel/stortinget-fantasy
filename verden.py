#--Tester--
import json

f = open("politikere.json")

data = json.load(f)
f.close()


for politiker in data["representanter_oversikt"]["representanter_liste"]["representant"]:
    print(f"{politiker['fornavn']} {politiker['etternavn']}")
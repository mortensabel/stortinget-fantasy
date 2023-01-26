#--Tester--
from verden import Verden
import json
from lag import Lag
from politiker import Politiker

f = open("politikere.json")
politiker_liste = json.load(f)
f.close()


for politiker in politiker_liste["representanter_oversikt"]["representanter_liste"]["representant"]:
    print(f"{politiker['fornavn']} {politiker['etternavn']} {politiker['parti']['navn']}")


erna = Politiker("Erna", "Solberg", "Høyre")

print(erna)





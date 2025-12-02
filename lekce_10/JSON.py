## Formát JSON

"""
import json

with open("lekce_10/absolventi.json", encoding="utf-8") as file:
    absolvents = json.load(file)
print(absolvents)

print(absolvents[3]["prijmeni"])
"""

"""
import json

hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open("lekce_10/hodiny.json", "w", encoding="utf-8") as file:
    json.dump(hours, file)
"""

"""
import json

data = {"řeřicha": "Česká Třebová"}
with open("lekce_10/rericha.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4) 

# výstupní JSON v plném kódování UTF-8 --> volitelný parametr ensure_ascii=False.
"""

"""
import json

with open('lekce_10/absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)
absolvents_output = []
for item in absolvents:
    #item.pop("dochazka")
    if item["vyznamenani"] == True:
        absolvents_output.append(item)
with open("lekce_10/absolventi_output.json", "w", encoding="utf-8") as file:
    json.dump(absolvents_output, file, indent=4, ensure_ascii=False)
"""

## Složitější JSON struktury

import json
with open("lekce_10/zavod.json", encoding="utf-8") as file:
    runners = json.load(file)
# print(runners[0]["jmeno"])
cas_zlaty = runners[0]["casy"]["oficialni"]
cas_stribrny = runners[1]["casy"]["oficialni"]
print(cas_zlaty)
print(cas_stribrny)
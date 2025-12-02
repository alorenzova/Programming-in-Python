"""import requests
response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()
print(data)"""

# Cvičení
## Seznam lidí

"""
import json
import requests

response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()

total_people = len(data)
print(f"Seznam obsahuje celkem {total_people} lidí")

if data:
    keys = data[0].keys()
    print("Info o osobách:", keys)

gender_count = {}
for person in data:
    gender_count[person["gender"]] = gender_count.get(person["gender"], 0) + 1

print("V souboru je můžů a žen:", gender_count)
"""

"""
import json
import requests
from collections import Counter # pro druhou moznost

response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()

print(len(data))
print(data[0].keys())

gender_count = {}
for item in data:
    gender_count[item["gender"]] = gender_count.get(item["gender"], 0) + 1
print(gender_count)

# druha moznost
gender = [person[*gender*] for person in data] # list comprehension
gender_count = Counter(genders)

for gender, count in gender_count.items():
    print(f*{gender}: {count} lidí*)
"""

## Kočky

import json
import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()
data.pop("length")

cat_fact = {"fact": data["fact"]}

with open("lekce_10/cat_fact.json", "w", encoding="utf-8") as file:
    json.dump(cat_fact, file, ensure_ascii=False, indent=4)
"""
with open('mereni.txt', encoding='utf-8') as file:
    text = file.read()

print(text)
"""

"""
lines = []
with open("mereni.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)
print(lines)
"""

"""
lines = []
with open("mereni.txt", encoding="utf-8") as file:
    for line in file:
        # line: po\t17.3\n
        # line_split: ["po", "17.3\n"]
        line_split = line.split("\t")
        lines.append(line_split)
print(lines)
"""

"""
lines = []
with open("lekce_9/mereni.txt", encoding="utf-8") as file:
    for line in file:
        # line: po\t17.3\n
        # line_split: ["po", "17.3\n"]
        line_split = line.split()
        line_split[1] = float(line_split[1])
        lines.append(line_split)
print(lines)
"""

"""
temparatures = []
with open("lekce_9/mereni.txt", encoding="utf-8") as file:
    for line in file:
        # line: po\t17.3\n
        # line_split: ["po", "17.3\n"]
        line_split = line.split()
        temp = float(line_split[1])
        temparatures.append(temp)
print(temparatures)
"""


"""
temparatures = []
with open("lekce_9/mereni.txt", encoding="utf-8") as file:
    for line in file:
        # line: po\t17.3\n
        # day = "po"
        # temp = "17.3\n"
        day, temp = line.split()
        temp = float(temp)
        temparatures.append(temp)
print(temparatures)
"""

"""names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open("lekce_9/soubor.txt", "w", encoding="utf-8") as output_file:
    for item in names:
        print(item, file=output_file)"""

"""names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
nazev_soubor = "lekce_9/soubor.txt"
with open(nazev_soubor, "w", encoding="utf-8") as output_file:
    for item in names:
        print(item, file=output_file)"""

## Cviceni
### Vyplata presneji
"""lines = []
vykazy = []

with open('vykaz.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            vykazy.append(float(line))"""

"""hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
celkova_mzda = hodinova_mzda * sum(vykazy)"""

"""hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
celkova_mzda = 0
    
for vykaz in vykazy:
    celkova_mzda += hodinova_mzda * vykaz"""

"""print(celkova_mzda)
print(celkova_mzda/len(vykazy))"""

"""print("Celková mzda za rok je:", celkova_mzda)
print("Průměrná měsíční mzda je:", celkova_mzda/len(vykazy))"""

### Kryptomeny
"""lines = []

rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}

total_usd = 0

with open("transaction_list.csv", encoding="utf-8") as file:
    for line in file:
        date, amount, currency = line.split(",")
        amount = float(amount)
        currency = currency.strip()

        total_usd += amount * rates[currency]

print(f"Hodnota úspor Markéty je {int(total_usd)} dolarů.")"""


"""
rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}

total_usd = 0

with open("transaction_list.csv", encoding="utf-8") as file:

    for line in file:
        date, amount_str, crypto_with_newline = line.split(";")

        # množství kryptoměny jako číslo
        amount = float(amount_str)

        # název měny bez \n na konci
        crypto = crypto_with_newline.strip()

        # kurz dané měny
        rate = rates[crypto]

        # přičtu hodnotu této transakce v dolarech
        total_usd += amount * rate

# převedu na celé dolary (můžeš použít int nebo round)
total_usd_int = round(total_usd)

print(f"Hodnota úspor Markéty je {total_usd_int} dolarů.")
"""

### Dny v mesici
"""pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("kalendar1.txt", encoding="utf-8", mode="w") as file:
    for dny in pocty_dni:
        print(dny, file=file)

### Vytvoreni souboru
file_name = input("Zadej název souboru: ")
text = input("Zadej text: ")

with open(file_name, mode="w", encoding="utf-8") as output_file:
    print(text, file=output_file)"""

### Rozepsana vyplata
vyplata_po_mesicich = []

hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
#hodinova_mzda = float(input("Napiš hodinovou mzdu v Kč: ")) #test

with open('vykaz.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        vyplata = float(radek) * hodinova_mzda
        vyplata_po_mesicich.append(vyplata)
        print(vyplata)

with open("vyplata_po_mesicich.txt", "w", encoding="utf-8") as soubor:
    for hodnota in vyplata_po_mesicich:
        print(hodnota, file=soubor)
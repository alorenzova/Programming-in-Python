# Komplexní příklad: Game of Thrones

"""radky = []

SLOUPEC_ATTACKER_1 = 5
SLOUPEC_ATTACKER_2 = 6

with open("lekce_11/battles.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radky.append(radek.split("\t"))
# ["Battle of the Golden Tooth", "298", "1", "Joffrey/Tommen Baratheon"]

# Pracujeme s první bitvou při číslování od 1
utocici_rod_bitva_1 = radky[1][SLOUPEC_ATTACKER_1]
utocici_rod_bitva_2 = radky[1][SLOUPEC_ATTACKER_2]
print(utocici_rod_bitva_1)"""

"""radky = []

with open("lekce_11/battles.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radky.append(radek.split("\t"))

zahlavi = radky[0]
cisla_sloupcu_utocnici = []
for cislo_sloupce, nazev_sloupce in enumerate(zahlavi):
    if "attacker_" in nazev_sloupce and len(nazev_sloupce) == len("attacker_1"):
        cisla_sloupcu_utocnici.append(cislo_sloupce)
print(cisla_sloupcu_utocnici)"""

"""radky = []

with open("lekce_11/battles.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radky.append(radek.split("\t"))

zahlavi = radky[0]
cisla_sloupcu_utocnici = [] # [5, 6, 7, 8]
for cislo_sloupce, nazev_sloupce in enumerate(zahlavi):
    if "attacker_" in nazev_sloupce and len(nazev_sloupce) == len("attacker_1"):
        cisla_sloupcu_utocnici.append(cislo_sloupce)

pocet_utoku = {} # klíč = rod, hodnota = počet útoků
for radek in radky[1:]:
    for cislo_sloupce in cisla_sloupcu_utocnici:
        # if len(radek[cislo_sloupce]) > 0:
        if radek[cislo_sloupce]:
            # Chci vypsat útočící rod
            print(radek[cislo_sloupce])"""

"""radky = []

with open("lekce_11/battles.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radky.append(radek.split("\t"))

zahlavi = radky[0]
cisla_sloupcu_utocnici = [] # [5, 6, 7, 8]
for cislo_sloupce, nazev_sloupce in enumerate(zahlavi):
    if "attacker_" in nazev_sloupce and len(nazev_sloupce) == len("attacker_1"):
        cisla_sloupcu_utocnici.append(cislo_sloupce)

pocet_utoku = {} # klíč = rod, hodnota = počet útoků
for radek in radky[1:]:
    for cislo_sloupce in cisla_sloupcu_utocnici:
        # if len(radek[cislo_sloupce]) > 0:
        if radek[cislo_sloupce]:
            rod = radek[cislo_sloupce]
            if rod not in pocet_utoku:
                pocet_utoku[rod] = 0
            pocet_utoku[rod] += 1"""

## Cvičení
### Skvělí velitelé
"""
Nyní je naším úkolem vytvořit seznam velitelů, kteří zvítězili v boji proti přesile, tj. jejich armáda 
byla slabší než armáda soupeřů a oni přesto zvítězili. Budeme k tomu potřebovat sloupečky s výsledkem bitvy 
(attacker_outcome), informacemi o síle útočníků a obránců (attacker_size a defender_size) a se jmény velitelů.

Před začátkem psaní kódu si sepiš kroky, které jsou k řešení potřeba. Poté začni s programováním a postupuj 
podle svého plánu. V případě problémů můžeš vyzkoušet debugger.
"""
#### Kroky
"""
1. najít indexy potřebných sloupců - určit indexy sloupců pro 
- výsledek bitvy (attacker_outcome), 
- velikost útočníka (attacker_size), 
- velikost obránce (defender_size)
- jména velitelů (commander?)

2. vytvořit seznam, kam uložím jména velitelů, kteří zvítězili proti přesile

3. projít všechny řádky s daty

4. zkontrolovat kritéria vítězství proti přesile - kontrola podmínek
- útočník musel zvítězit (attacker_outcome je win?)
- velikost armády: Velikost útočníkovy armády (attacker_size) musela být menší než velikost armády obránce (defender_size)
- data jsou platná, sloupce attacker_size a defender_size musí obsahovat platné číselné hodnoty a musí být převeditelné na celé číslo

5. pokud jsou všechna kritéria splněna, z příslušného sloupce s velitelem (commander) získat jméno velitele a přidat ho do seznamu "top velitelů"

6. print seznam velitelů
"""

#### Řešení
# magická čísla
"""
V Pythonu se "magická čísla" (magic numbers) obvykle vztahují k speciálním, skrytým konstantám,
které používá samotný interpreter (např. při interním ukládání dat a operacích), ale častěji se 
v kontextu programování jedná o nezdokumentovaná čísla (jako 0xDEADBEEF, 42, 666), která mají 
pro programátora nějaký význam (nebo jsou jen výplň), což se nedoporučuje (lepší jsou pojmenované konstanty). 
Další kontext může být "magické datum" (násobek měsíce a dne rovný poslednímu dvojčíslí roku) v úlohách 
pro začátečníky, nebo skryté interní chování, jako je semínko (seed) pro generování náhodných čísel. 
"""

with open("lekce_11/battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

attacker_size_idx = 17
defender_size_idx = 18
attacker_outcome_idx = 13
attacker_commander_idx = 19
defender_commander_idx = 20

commanders = []

# Procházíme řádky kromě prvního (ten je hlavička)
for radek in radky[1:]:
    # Rozdělíme řádek na jednotlivé hodnoty podle tabulátoru
    radek = radek.strip().split("\t")
    # Podmínka: musí být zadaná síla útočníků i obránců (sloupečky nesmí být prázdné)
    if radek[attacker_size_idx] != "" and radek[defender_size_idx] != "":
        attacker_size = float(radek[attacker_size_idx])
        defender_size = float(radek[defender_size_idx])
        attacker_outcome = radek[attacker_outcome_idx] #sem ukladame vysledek bitvy
        # PŘÍPAD: Útočníci byli SLABŠÍ, ale VYHRÁLI
        if attacker_size < defender_size and attacker_outcome == "win":
            commanders += radek[attacker_commander_idx].split(", ") ## Velitelé utocniku (může jich být více, oddělených čárkou)
        # PŘÍPAD: Útočníci byli SILNĚJŠÍ, ale PROHRÁLI
        if attacker_size > defender_size and attacker_outcome == "loss":
            commanders += radek[defender_commander_idx].split(", ")
            
print("Počet bitev proti přesile:", len(commanders))
print("Velitelé:", commanders)
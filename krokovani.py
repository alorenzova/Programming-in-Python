# Obsluha vyjimek
## Krokovani
### Click to add a breakpoint - najet na cislo radku a kliknout na cervenou tecku (prvni prikaz , ktery neudela)
### Run - start debugging (F5) - select debugger (PYthon) - python file
#### Kontrola? --> variables - local - lines - neni tam avg_sales
### Tlacitko Step Over (F10) - pokracovat na dalsi radek

"""
lines = [
    "2904,4",
    "7390,7",
    "6950,8",
    "3300,4",
    "10570,8",
    "1310,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    line = line.split(",")
    avg = int(line[0]) / int(line[1])
    avg_sales.append(avg)

print(avg_sales)
"""
"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"]

avg_sales = []
for line in lines:
    line = line.split(",")
    try:
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except ZeroDivisionError:
        print("Délka směny nesmí být 0.")

print(avg_sales)
"""
"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    try:
        line = line.split(",")
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except Exception as e:
        print(f"Zpracování se nepodařilo kvůli chybě: {e}")

print(avg_sales)
"""

"""
lines = [
    "6950,0",
    "73907",
    2904,
    "3300;4",
    "10570,4,4",
    "a,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    try:
        line = line.split(",")
        if len(line) > 2:
            print("Na řádku mají být dvě hodnoty")
            avg_sales.append("chyba")
        else:
            avg = int(line[0]) / int(line[1])
            avg_sales.append(avg)
    except Exception as e:
        print(f"Zpracování se nepodařilo kvůli chybě: {e}")
        avg_sales.append("chyba")

print(avg_sales)
"""

"""
if len(line) > 2:
            print("Na řádku mají být dvě hodnoty")
            avg_sales.append("chyba")
            # raise Exception("Na řádku mají být dvě hodnoty")
        else:
            avg = int(line[0]) / int(line[1])
            avg_sales.append(avg)
"""

## Cviceni
### Knihy
knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
index = input("Zadej index knihy: ")
index = int(index)
print(knihy[index])

"""
value error a index error
"""


knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

try:
    index = input("Zadej index knihy: ")
    index = int(index)
    print(knihy[index])
except Exception:
    print("Nastala chyba")

### Knizni serie (bonus)
knihy = {
    "1984": 328, # jen jedno číslo (počet stran knihy)
    "Pán Prstenů": [423, 352, 416],  # seznam knih v sérii
    "Hornblower": [256, 352, 288, 304],
    "Problém tří těles": [400, 512, 608]
}

nazev = input("Zadej název knižní série: ")
stranek_za_den = int(input("Kolik stran přečteš každý den? "))
stranek_celkem = sum(knihy[nazev]) ### Funkce sum() v Pythonu sečítá všechny prvky v nějakém iterovatelném objektu – typicky v seznamu

pocet_dni = stranek_celkem / stranek_za_den
pocet_dni = round(pocet_dni)
print(f"Celou sérii přečteš za {pocet_dni} dní.")


#oprava

knihy = {
    "1984": 328,
    "Pán Prstenů": [423, 352, 416],
    "Hornblower": [256, 352, 288, 304],
    "Problém tří těles": [400, 512, 608]
}

try:
    nazev = input("Zadej název knižní série: ")
    stranek_za_den = int(input("Kolik stran přečteš každý den? "))

    if stranek_za_den <= 0:
        raise ValueError("Počet stran na den musí být větší než 0.")

    hodnota = knihy[nazev]

    if isinstance(hodnota, int):
        stranek_celkem = hodnota
    else:
        stranek_celkem = sum(hodnota)

    pocet_dni = stranek_celkem / stranek_za_den
    pocet_dni = round(pocet_dni)

    print(f"Celou sérii přečteš za {pocet_dni} dní.")

except KeyError:
    print("Tuto knihu nebo sérii neznáme.")

except ValueError as e:
    print("Chyba ve vstupu:", e)

except Exception as e:
    print("Nastala neočekávaná chyba:", e)
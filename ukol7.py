# 1. Která chyba vždy způsobí, že program nejde vůbec spustit, tj. neprovede se žádný příkaz?
#* SyntaxError

# 2. Chceme, aby program vypsal text "Je třeba zadat číslo!", pokud uživatel nezadá do terminálu číslo. Co je potřeba na programu opravit?
try:
    print("Nákup lístků na představení Věc Makropulos.")
    pocet = int(input("Zadejte počet lístků: "))
    cena = pocet * 360
    print(f"Cena je {cena} Kč.")
except TypeError:
    print("Je třeba zadat číslo!")

#* except TypeError je potřeba nahradit except ValueError

# 3. Co platí, pokud máme u bloku try více bloků except? (To jsme si na lekci neukazovali, ale jistě dokážeš odpověď snadno zjistit.)
#* Python v případě chyby prochází bloky except postupně a provede příkazy v prvním bloku, který vyhovuje chybě, která se objevila

# 4. Krokuješ následující program. Aktuálně jsi na řádku 4. Jaký bude další řádek, který bude spuštěný?
promenna_1 = 5
promenna_2 = "7"
try:
    soucet = promenna_1 + promenna_2  #promenna_1 = 5,
    print(f"Výsledek scítání je {soucet}.")
except TypeError:
    print("Čísla nejde sečíst")

#* 6

# 5. Jaký bude výsledek následujícího programu?
promenna_1 = 5
promenna_2 = "7"
try:
    soucet = promenna_1 + promenna_2
    print(f"Výsledek scítání je {soucet}.")
except ZeroDivisionErrorr:
    print("Čísla nejde sečíst")

#* Program skončí s neodchycenou chybou

# 6. Krokuješ následující program. Program se zastavil na řádku 6. Stiskneš tlačítko Step over. Na jakém řádku se program zastaví?
cisla = [1, 2, -2, -2, 1]
kladna = 0
zaporna = 0 #zaporna = 0
for c in cisla: # cisla = [1, 2, -2, -2, 1]
    if c > 0: # c= 1
        kladna = kladna + 1 # kladna = 0
    elif c < 0:
        zaporna = zaporna + 1
print(f"Máme {kladna} kladných a {zaporna} záporných čísel.")

#* 4

# 7. Existuje koncept obsluhy výjimek i v jiných programovacích jazycích?
#* Ano, ale někde se používají jiná klíčová slova, např. try a catch.

# 8. Pokud mi Python hlásí chybu SyntaxError, co je nejlepší způsob, jak ji opravit?
#* Opravit syntaktickou chybu v kódu.
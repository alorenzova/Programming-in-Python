# Domácí úkoly - Úkol 1 (povinný)
## Zadání povinné části úkolu
"""
Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. 
Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, 
bytové a komerční prostory. Výše daně se odvíjí od několika faktorů, např. typu 
nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.
"""
# from pydantic import BaseModel, PositiveInt, field_validator --> ma smysl?

### 1) Třída Locality s atributy name a locality_coefficient
"""
V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, 
kde se nemovitost nachází. Třída bude mít atributy name (název katastru/obce) 
a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).
"""

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self) -> str:
        return f"Lokalita: {self.name}, místní koeficient: {self.locality_coefficient}"
 
    #def get_locality_info_(self) -> str:
        #return f"Lokalita: {self.name}, místní koeficient: {self.locality_coefficient}"
        # !!! tato cast nefunguje, smazat

"""
#### Praha, Brno
praha = Locality("Praha", 6.4)
brno = Locality("Brno", 2.3)
"""
"""
praha = Locality(name="Praha", locality_coefficient=6.4)
brno = Locality(name="Brno", locality_coefficient=2.3)
"""
"""
print(praha)
print(brno)

print("Koeficient pro Brno: ", brno.locality_coefficient)
"""

### 2) třída Property s atributem locality
"""
Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. 
Třída bude mít atribut locality (lokalita, kde se pozemek nachází, 
bude to objekt třídy Locality).
"""

class Property:
    def __init__(self, locality: Locality):
    #def __init__(self, locality: Locality, size: float):
        self.locality = locality
        # self.size = size --> uvest navic i m², aby to davalo vetsi smysl? --> bude nize
    def __str__(self) -> str:
        return f"Nemovitost se nachází v lokalitě s názvem {self.locality.name}." 

    #def __str__(self) -> str:
        #return f"Nemovitost o velikosti {self.size} m² se nachází v lokalitě {self.locality.name}"

"""
#### Dům, byt
dum_v_praze = Property(locality=praha)
byt_v_brne = Property(locality=brno)

print(dum_v_praze)
print(byt_v_brne)

print(f"Místní koeficient pro dům v Praze je: {dum_v_praze.locality.locality_coefficient}")
"""

### 3) třída Estate (potomek Property) s atributy locality, estate_type, area
"""
Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku 
v metrech čtverečních). 
"""

# kod nize, kde je doplnen o krok 4)
    
"""
#### Zahrádka u Brna
brno = Locality(name="Brno", locality_coefficient=6.66)

zahradka_brno = Estate(
    locality=brno,
    estate_type="zahradka",
    area=123.21
)

print(zahradka_brno)
"""

### 4) Třída Estate - metoda calculate_tax()
"""
Dále přidej metodu calculate_tax(), která spočítá výši daně 
pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() 
z modulu math). 

Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu 
pozemku (atribut estate_type) * místní koeficient. U atributu estate_type 
následující hodnoty a koeficienty:

- land (zemědělský pozemek) má koeficient 0.85.
- building site (stavební pozemek) má koeficient 9.
- forrest (les) má koeficient 0.35,
- garden (zahrada) má koeficient 2. 

Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě 
s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.
"""
from math import ceil

class Estate(Property):
    estate_coefficients = {
    "land": 0.85,
    "building site": 9.0,
    "forrest": 0.35,
    "garden": 2.0
    }
    def __init__(self, locality: Locality, estate_type: str, area: float):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self) -> int:
        return ceil(
            self.area * # kam se pise *, kdyz nechci vse na jednom radku?
            self.estate_coefficients[self.estate_type] *
            self.locality.locality_coefficient
        )
    def __str__(self) -> str:
        return (f"Pozemek typu {self.estate_type} o rozloze {self.area} m² "
                f"v lokalitě s názvem {self.locality.name}.")

# bez importu ceil problem, napsat jinak?
# co kdyz se jako input zada blbost?

#### Vypocty
loc1 = Locality("Praha", 2.8)
loc2 = Locality("Brno", 1.1)
loc3 = Locality("Test", 3.6)

estate1 = Estate(loc1, "building site", 170)
estate2 = Estate(loc2, "garden", 210)
estate3 = Estate(loc3, "forrest", 999)
estate4 = Estate(loc1, "land", 100)

print("Daň estate1:", estate1.calculate_tax())
print("Daň estate2:", estate2.calculate_tax())
print("Daň estate3:", estate3.calculate_tax())
print("Daň estate4:", estate4.calculate_tax())

# vyzkouset nesmysly, dlouhe cislo apod.

### 5) Třída Residence (potomek Property) s atributy locality, area, commercial
"""
Vytvoř třídu Residence, která reprezentuje byt, dům či jinou stavbu a je potomkem 
třídy Property. Třída bude mít atributy locality, area (podlahová plocha bytu nebo 
domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost 
používanou k podnikání). 
"""

# kod nize, pridan k nemu krok 6)

"""
#### Nemovitosti  
locality_prague = Locality("Praha", 2.8)

my_flat = Residence(
    locality=locality_prague, 
    area=75.5, 
    commercial=False
)

my_office = Residence(
    locality=locality_prague, 
    area=670.0, 
    commercial=True
)

print(my_flat)
print(my_office)
"""

### 6) Třída Residence - metoda calculate_tax()
"""
Dále přidej metodu calculate_tax(), která spočítá výši daně 
pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: 
podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru 
commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů 
čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. 
Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.
"""

class Residence(Property):
    BASE_TAX_RATE = 15
    def __init__(self, locality: Locality, area: float, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self) -> float:
        base_tax = (
            self.area 
            * self.locality.locality_coefficient 
            * self.BASE_TAX_RATE
        )
        final_tax = base_tax
        if self.commercial:
            final_tax *= 2
        return final_tax
    def __str__(self) -> str: #str?
        if self.commercial:
            use = "Komerční/k podnikání"
        else:
            use = "Obytné"
        return (f"Stavba s atributy:" # zjistit, jak rozdelit na radky
                f" lokalita: {self.locality.name} (koeficient {self.locality.locality_coefficient}),"
                f" podlahová plocha: {self.area} m²,"
                f" využití: {use}.")

#### Výpočet daně

locality_test = Locality("testovaci", 3.0)
area_test = 60.0

flat_residence = Residence(locality_test, area_test, commercial=False)
tax_residence = flat_residence.calculate_tax()

print(f"Byt ({area_test} m²):")
print(f" výpočet: {area_test} * {locality_test.locality_coefficient} * {Residence.BASE_TAX_RATE} = 2700,")
print(f" vypočtená daň: **{tax_residence}** Kč,")
print(f" test: {'passed' if tax_residence == 2700.0 else 'failed'}")


office_residence = Residence(locality_test, area_test, commercial=True)
tax_commercial = office_residence.calculate_tax()
print(f"Komerční nemovitost ({area_test} m²):")
print(f" výpočet: 2700 * 2 = 5400,")
print(f" vypočtená daň: **{tax_commercial}** Kč,")
print(f" test: {'passed' if tax_commercial == 5400.0 else 'failed'}")

### 7) Zkoušky výpočtů
"""
Vyzkoušej svůj program pomocí následujících nemovitostí:
"""

#### A) Zemědělský pozemek
"""
- Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín 
s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
"""

#### B) Dům
"""
- Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín 
s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
"""

#### C) Kancelář
"""
- Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů 
čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti 
je 90 * 3 * 15 * 2 = 8100.
"""

## Bonusy
"""
Tyto bonusy jsou nepovinné a záleží čistě na tobě, zda se do nich pustíš. 
Jednotlivé části jsou nezávislé, můžeš si tedy vybrat libovolné odrážky a ty vyřešit.
"""

### Výpisy informací
"""
- Ke třídě Estate a Residence přidej výpisy informací do metody __str__(). 
Např.: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, 
daň 765 Kč.
"""

### Úprava třídy Property
"""
- Uprav třídu Property na abstraktní třídu. Tato třída totiž nereprezentuje žádnou 
konkrétní nemovitost, nemovitost totiž musí být pozemek nebo stavba.
"""

### Třída TaxReport
"""
- Přidej třídu TaxReport, která bude reprezentovat daňové přiznání. Třída bude mít 
atributy name (jméno osoby, která přiznání podává) a property_list, což je seznam 
nemovitostí, které jsou v přiznání uvedeny.
"""

#### Metoda add_property()
"""
Dále přidej metodu add_property(), 
která bude mít jako parametr objekt (nemovitost, která je součástí přiznání) 
a vloží ji do seznamu property_list. 
"""

#### Metoda calculate_tax()
"""
Dále přidej metodu calculate_tax(), 
která vypočte daň ze všech nemovitostí v seznamu property_list.
"""

### Enum třídy
"""
- Podívej se na to, jak fungují tzv. enum třídy. Můžeš si přečíst například tento 
text (link: https://www.geeksforgeeks.org/enum-in-python/). Zkus vytvořit třídu pro typy pozemků (zemědělský pozemek, stavební pozemek, 
les, zahrada) a použít ji ve třídě Estate. Použití této třídy zabrání, aby byl 
vytvořen pozemek s neexistujícím typem.
"""
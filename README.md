# Programování v Pythonu
## Obsah kurzu
* Úvod: Opakování základů, slicing, metody, moduly
* Slovníky: Ukládání informací do slovníků – struktur umožňujících přehledně uložit větší množství informací
* GitHub: Webová platforma pro správu verzí a hosting softwarových projektů
* Coding style: Pravidla a konvence, které určují, jak by měl být napsán zdrojový kód
* Čtení a zápis textových souborů
* Obsluha výjimek
* AI nástroje ve vývoji
* Instalace balíčků pomocí pip
* Funkce
* Objektově orientované programování (OOP): Základní úvod do OOP, dědičnost, rozdíly mezi objektově orientovaným programování v Pythonu od ostatních programovacích jazyků
* Datum a čas
* API: Propojení aplikace s jinými aplikacemi a automatizace nudných úkolů
* Regulární výrazy: Umožní z nepřehledného textu vytáhnout zajímavé a důležité informace nebo kontrolovat, zda uživatelé nezadávají do aplikace nesmyslné hodnoty

## Zadání 1. domácího úkolu
Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, bytové a komerční prostory. Výše daně se odvíjí od několika faktorů, např. typu nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.

V rámci aplikace nejprve vytvoř třídu **Locality**, která označuje lokalitu, kde se nemovitost nachází. Třída bude mít atributy **name** (název katastru/obce) a **locality_coefficient** (tzv. místní koeficient, který se používá k výpočtu daně).

Vytvoř třídu **Property**, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut **locality** (lokalita, kde se pozemek nachází, bude to objekt třídy **Locality**).

Dále vytvoř třídu **Estate**, která reprezentuje pozemek a je potomkem třídy **Property**. Třída bude mít atributy **locality**, **estate_type** (typ pozemku), **area** (plocha pozemku v metrech čtverečních). Dále přidej metodu **calculate_tax()**, která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci **ceil()** z modulu **math**). Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut **estate_type**) * místní koeficient. U atributu **estate_type** následující hodnoty a koeficienty:

- land (zemědělský pozemek) má koeficient 0.85.
- building site (stavební pozemek) má koeficient 9.
- forrest (les) má koeficient 0.35,
- garden (zahrada) má koeficient 2. 

Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.

Vytvoř třídu **Residence**, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy **Property**. Třída bude mít atributy **locality**, **area** (podlahová plocha bytu nebo domu) a **commercial** (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). Dále přidej metodu **calculate_tax()**, která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru **commercial** True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.

Vyzkoušej svůj program pomocí následujících nemovitostí:

- Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
- Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
- Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.

### Bonusy
Tyto bonusy jsou nepovinné a záleží čistě na tobě, zda se do nich pustíš. Jednotlivé části jsou nezávislé, můžeš si tedy vybrat libovolné odrážky a ty vyřešit.

- Ke třídě **Estate** a **Residence** přidej výpisy informací do metody **__str__()**. Např.: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, daň 765 Kč.
- Uprav třídu **Property** na abstraktní třídu. Tato třída totiž nereprezentuje žádnou konkrétní nemovitost, nemovitost totiž musí být pozemek nebo stavba.
- Přidej třídu **TaxReport**, která bude reprezentovat daňové přiznání. Třída bude mít atributy **name** (jméno osoby, která přiznání podává) a **property_list**, což je seznam nemovitostí, které jsou v přiznání uvedeny. Dále přidej metodu **add_property()**, která bude mít jako parametr objekt (nemovitost, která je součástí přiznání) a vloží ji do seznamu property_list. Dále přidej metodu **calculate_tax()**, která vypočte daň ze všech nemovitostí v seznamu **property_list**.
- Podívej se na to, jak fungují tzv. enum třídy. Můžeš si přečíst například [tento text](https://www.geeksforgeeks.org/enum-in-python/). Zkus vytvořit třídu pro typy pozemků (zemědělský pozemek, stavební pozemek, les, zahrada) a použít ji ve třídě **Estate**. Použití této třídy zabrání, aby byl vytvořen pozemek s neexistujícím typem.

## Řešení 1. domácího úkolu
[Link](https://github.com/alorenzova/Programming-in-Python/blob/main/povinny-ukol-1.py)

## Zadání 2. domácího úkolu
Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.

### Část 1
V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektui. Nejprve se pomocí funkce `input()` zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. S využitím modulu `requests` odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, kde `ICO` nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu `.replace()`, operátor `+` atd. Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle `textovaAdresa`). Získané informace vypiš na obrazovku.

Například pro IČO 22834958 by tvůj program měl vypsat následující text.

```
Czechitas z.ú.
Krakovská 583/9, Nové Město, 110 00 Praha 1
```

### Část 2
Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.

V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. Request typu POST pošleme tak, že namísto funkce `requests.get()` použijeme funkci `requests.post()`. K requestu musíme přidat hlavičku (parametr `headers`), který určí formát výstupních dat. Použij slovník níže.

```
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
```

Dále přidáme parametr `data`, do kterého vložíme řetězec, který definuje, co chceme vyhledávat. Data vkládáme jako řetězec, který má JSON formát. Pokud chceme například vyhledat všechny subjekty, které mají v názvu řetězec `"moneta"`, použijeme následující řetězec.

```
data = '{"obchodniJmeno": "moneta"}'
```

Níže je příklad odeslání requestu:

```
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "moneta"}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
```

Tentokrát API vrátí počet nalezených subjektů (`pocetCelkem`) a seznam nalezených subjektů `ekonomickeSubjekty`. Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou. Příklad výstupu pro `"moneta"` je níže.

```
Nalezeno subjektů: 13
MONETA PARTNERS s.r.o., 01590952
Moneta Sinkovská, 05170443
Nadace MONETA Clementia, 10730443
Juno Moneta, z.s., 22741461
Moneta Investment, s.r.o., 24227625
Moneta SPV, s. r. o. "v likvidaci", 25355163
MONETA Money Bank, a.s., 25672720
Moneta Praha s.r.o., 26424720
Moneta holding s.r.o., 28660463
JK MONETA, s.r.o., 29242746
MONETA Stavební Spořitelna, a.s., 47115289
MONETA Auto, s.r.o., 60112743
MONETA Leasing, s.r.o., 60751606
```

Ve tvém programu musíš nahradit řetězec `moneta` proměnnou, která obsahuje řetězec zadaný uživatelem.

### Bonus
Ke každému subjektu je v databázi uložena jeho právní forma. Ta se nachází pod klíčem `pravniForma`. Není tam přímo název subjektu, ale číselný kód, jehož význam je uložený v tzv. číselníku. Pomocí požadavku na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat si můžeme stáhnout celý číselník a poté tam příslušný kód vyhledat. Přidej do programu požadavek na tuto adresu. Půjde o požadavek typu POST, parametr `headers` zůstane stejný a jako parametr `data` zadej:

```
data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
```

Číselník je v seznamu pod klíčem `ciselniky`. Dále použij počáteční hodnotu ze seznamu (dotaz vrátí pouze jeden číselník, v seznamu je tedy pouze jedna položka). Touto hodnotou je opět slovník, ve kterém je pod klíčem `polozkyCiselniku` seznam všech kódů a jejich hodnot.

Poté napiš funkci `find_legal_form`, která bude přijímat dva parametry - hledaný kód a seznam `polozkyCiselniku`. Například pro kód `"112"` by funkce měla vrátit řetězec `"Společnost s ručením omezeným"`.

Nyní uprav část programu, která vypisuje všechny aplikace podle názvu, aby spolu s obchodním jménem a identifikačním číslem vypsala i právní normu. Napříkad pro `"moneta"` by výstup mohl vypadat takto:

```
Nalezeno subjektů: 13
MONETA PARTNERS s.r.o., 01590952, Společnost s ručením omezeným
Moneta Sinkovská, 05170443, Fyzická osoba podnikající dle živnostenského zákona
Nadace MONETA Clementia, 10730443, Nadace
Juno Moneta, z.s., 22741461, Spolek
Moneta Investment, s.r.o., 24227625, Společnost s ručením omezeným
Moneta SPV, s. r. o. "v likvidaci", 25355163, Společnost s ručením omezeným
MONETA Money Bank, a.s., 25672720, Akciová společnost
Moneta Praha s.r.o., 26424720, Společnost s ručením omezeným
Moneta holding s.r.o., 28660463, Společnost s ručením omezeným
JK MONETA, s.r.o., 29242746, Společnost s ručením omezeným
MONETA Stavební Spořitelna, a.s., 47115289, Akciová společnost
MONETA Auto, s.r.o., 60112743, Společnost s ručením omezeným
MONETA Leasing, s.r.o., 60751606, Společnost s ručením omezeným
```

### Diakritika
Na splnění úkolu stačí, aby tvůj program dobře fungoval pro vyhledávání řetězců bez diakritiky.

Pokud bys chtěl(a) vyhledat nějaký název, který obsahuje diakritiku, je nutné řetězec zakódovat. K tomu slouží metoda `encode()`, Protože chceme použít kódování UTF-8, je třeba toto kódování doplnit do volání metody. Pokud název diakritiku neobsahuje, není to nutné.

```
data = '{"obchodniJmeno": "škoda"}'
data = data.encode("utf-8")
```

Tip: Protože v hodnotě `data` jsou složené závorky, namísto formátovaných řetězců je jednodušší spojit řetězec dohromady z jednotlivých částí s využitím +. Alternativně můžeš využít metodu `.dumps()`, která slovník uloží jako řetězec.

## Řešení 2. domácího úkolu
Link
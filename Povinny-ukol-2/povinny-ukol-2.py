## ---------------------------------
# Povinný domácí úkol 2
## ---------------------------------

## ---------------------------------
#  Část 1
## ---------------------------------
#  Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.
## ---------------------------------

## ---------------------------------
# 1) V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). 
# Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektu. 
# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. 
## ---------------------------------
import requests
import json

# validace - číslo a počet znaků
def je_validni_ico_jednoduche(ico: str) -> bool: # chci true/false v return
    ico = ico.strip()
    if ico.isdigit() and len(ico) == 8:
        return True
    else:
        print("Zadané IČO je neplatné.")
        return False

## ---------------------------------
# 2) S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, 
# kde ICO nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). 
# S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd. Text, který API vrátí, 
# převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). 
## ---------------------------------
def info_o_subjektu(): # získání informací o subjektu
    while True: # py while loop
        ico_input = input("Zadejte IČO subjektu: ")
        
        if je_validni_ico_jednoduche(ico_input):
            ico = ico_input
            break
        else:
            print("-" * 30) # oddělovač

    # sestavení URL a volání API
    api_url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    print(f"\nKontrolní message: Input je validní, odesílání požadavku na ARES: {api_url}")

## ---------------------------------
# 3) Získané informace vypiš na obrazovku. Testovací IČO: 22834958
## ---------------------------------
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status() 
        data = response.json() 

        jmeno = data.get('obchodniJmeno', 'Neznámé obchodní jméno')
        adresa = data.get('sidlo', {}).get('textovaAdresa', 'Neznámá adresa sídla')

        print("\n--- Zjištěné informace ---")
        print(f"IČO: {ico}")
        print(jmeno)
        print(adresa)
        print("--------------------------")

    except requests.exceptions.RequestException as e:
        print(f"\nNastala chyba při komunikaci s API: {e}")
        print(f"Zkontrolujte, zda IČO {ico} v rejstříku opravdu existuje.") # více error messages k různým status codes?
        
    except json.JSONDecodeError:
        print("\nChyba: Odpověď z API nebyla ve správném formátu JSON.")

if __name__ == "__main__":
    info_o_subjektu()

## ---------------------------------
# Část 2
## ---------------------------------
# Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. 
## ---------------------------------

## ---------------------------------
# 1) Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.
## ---------------------------------
def vyhledej_subjekty_podle_jmena():
    nazev = input("Zadejte název nebo část názvu subjektu pro vyhledání: ").strip() 
    # jak vyhledávat i podle části slova? '%nazev%'? 
    # # jak nabízet možnosti? m...
    if not nazev:
        print("Pole pro název nesmí být prázdné.")
        return

## ---------------------------------
# 2) V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. 
# Request typu POST pošleme tak, že namísto funkce requests.get() použijeme funkci requests.post(). K requestu musíme přidat hlavičku (parametr headers), 
# který určí formát výstupních dat. 
## ---------------------------------
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

## ---------------------------------
# 3) Dále přidáme parametr data, do kterého vložíme řetězec, který definuje, co chceme vyhledávat. Data vkládáme jako řetězec, který má JSON formát. 
# Pokud chceme například vyhledat všechny subjekty, které mají v názvu řetězec "moneta", použijeme následující řetězec.
## ---------------------------------
    request_body = {"obchodniJmeno": nazev} # Ve tvém programu musíš nahradit řetězec moneta proměnnou, která obsahuje řetězec zadaný uživatelem.
    data_json_string = json.dumps(request_body)

    api_url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"  # URL pro vyhledávání

    print(f"\nKontrolní message: Odesílání POST requestu na: {api_url}")

    try: # POST
        response = requests.post(
            api_url, 
            headers=headers, 
            data=data_json_string,
            timeout=60 # moc/málo času?
        )

        response.raise_for_status() # http requests --> pokud 4xx, 5xx

        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Chyba při komunikaci s API: {e}")
        return
    except json.JSONDecodeError:
        print("Error: Odpověď z API není ve správném formátu JSON.")
        return

## ---------------------------------
# 4) Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty. 
## ---------------------------------
    pocet_celkem = data.get('pocetCelkem', 0)
    subjekty = data.get('ekonomickeSubjekty', [])
    
    print(f"\nNalezeno subjektů: {pocet_celkem}")

## ---------------------------------
# 5) Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou. 
## ---------------------------------  
    if pocet_celkem == 0:
        print("Pro zadaný název nebyly nalezeny žádné subjekty.")
        return

    for subjekt in subjekty:
        jmeno = subjekt.get('obchodniJmeno', 'Neznámé jméno')
        ico = subjekt.get('ico', 'Neznámé IČO')
        
        print(f"{jmeno}, {ico}")

if __name__ == "__main__":
    print("Vyhledávání subjektů podle názvu")
    vyhledej_subjekty_podle_jmena()

## ------------------------------------------------------------------
# KONEC POVINNÉ ČÁSTI
## ------------------------------------------------------------------

## ---------------------------------
# Bonus
## ---------------------------------
"""
Ke každému subjektu je v databázi uložena jeho právní forma. Ta se nachází pod klíčem pravniForma. Není tam přímo název subjektu, ale číselný kód, 
jehož význam je uložený v tzv. číselníku. Pomocí požadavku na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat 
si můžeme stáhnout celý číselník a poté tam příslušný kód vyhledat. Přidej do programu požadavek na tuto adresu. Půjde o požadavek typu POST, parametr 
headers zůstane stejný a jako parametr data zadej:

data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
Číselník je v seznamu pod klíčem ciselniky. Dále použij počáteční hodnotu ze seznamu (dotaz vrátí pouze jeden číselník, v seznamu je tedy pouze 
jedna položka). Touto hodnotou je opět slovník, ve kterém je pod klíčem polozkyCiselniku seznam všech kódů a jejich hodnot.

Poté napiš funkci find_legal_form, která bude přijímat dva parametry - hledaný kód a seznam polozkyCiselniku. Například pro kód "112" by funkce 
měla vrátit řetězec "Společnost s ručením omezeným".

Nyní uprav část programu, která vypisuje všechny aplikace podle názvu, aby spolu s obchodním jménem a identifikačním číslem vypsala i právní normu. 
Napříkad pro "moneta" by výstup mohl vypadat takto:

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
"""

### Diakritika
"""
Na splnění úkolu stačí, aby tvůj program dobře fungoval pro vyhledávání řetězců bez diakritiky.

Pokud bys chtěl(a) vyhledat nějaký název, který obsahuje diakritiku, je nutné řetězec zakódovat. K tomu slouží metoda encode(), 
Protože chceme použít kódování UTF-8, je třeba toto kódování doplnit do volání metody. Pokud název diakritiku neobsahuje, není to nutné.

data = '{"obchodniJmeno": "škoda"}'
data = data.encode("utf-8")
Tip: Protože v hodnotě data jsou složené závorky, namísto formátovaných řetězců je jednodušší spojit řetězec dohromady z jednotlivých částí 
s využitím +. Alternativně můžeš využít metodu .dumps(), která slovník uloží jako řetězec.
"""
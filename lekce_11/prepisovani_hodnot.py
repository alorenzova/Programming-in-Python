smeny_celodenni ={
    "pondělí": "Mirek"
}

smeny = {
    ("pondělí", "dopolední"): "Mirek",
    ("pondělí", "odpolední"): "Šárka",
}
print(smeny[("pondělí", "dopolední")])

odpracovane_hodiny = [8, 7, 7]
odpracovane_hodiny[2] = 9
print(odpracovane_hodiny)

# tuple (n-tice)
odpracovane_hodiny_tuple = (8, 7, 7)
# odpracovane_hodiny_tuple[2] = 9
odpracovane_hodiny_tuple = (6, 8 , 9)
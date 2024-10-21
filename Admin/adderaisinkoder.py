'''
Denna kod jämför fondnamn mellan två textfiler och extraherar matchande ISIN-koder.
Funktionen `läs_textfil` används för att läsa innehållet från en textfil och returnera en lista med fondnamn.
Den andra textfilen innehåller både fondnamn och ISIN-koder, där varje rad delas upp i två delar: ISIN-kod och fondnamn.
Koden går igenom fondnamnen i den första filen och letar efter matchande namn i den andra filen.
När en matchning hittas, sparas den motsvarande ISIN-koden i en lista och skrivs sedan ut.
'''

# Funktion för att läsa innehåll från en textfil och returnera en lista med varje rad som ett element
def läs_textfil(filnamn):
    with open(filnamn, 'r') as fil:
        innehåll = fil.readlines()
    return [rad.strip() for rad in innehåll]

# Läser innehållet från de två textfilerna
filnamn1 = "nordnet+SHBfondergemensamma.txt"  # Uppdatera filnamnen enligt ditt eget system
filnamn2 = "Nordnetfonder.txt"  # Uppdatera filnamnen enligt ditt eget system

fondnamn_lista1 = läs_textfil(filnamn1)
fondnamn_och_isin_lista2 = {}

with open(filnamn2, 'r') as fil:
    for rad in fil:
        isin, namn = rad.strip().split("\t")
        fondnamn_och_isin_lista2[namn] = isin

# Skapar en lista för matchade ISIN-koder
matchade_isin_koder = []

# Loopar genom fondnamnen i den första listan
for fondnamn in fondnamn_lista1:
    for namn, isin in fondnamn_och_isin_lista2.items():
        if fondnamn in namn:
            matchade_isin_koder.append(isin)
            break

# Skriver ut resultaten
for isin_kod in matchade_isin_koder:
    print(f"ISIN-kod: {isin_kod}")

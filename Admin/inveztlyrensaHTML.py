'''
Denna kod läser in en fil med fonddata i HTML-liknande format och extraherar fondnamn och ISIN-koder från varje rad.
Funktionen `clean_line` används för att rensa varje rad och plocka ut fondnamnet, som finns mellan tecknen '>' och '<',
samt ISIN-koden, som finns efter ett tabbtecken.
Fondnamn och ISIN-koder sparas i separata listor.
Slutligen skrivs fondnamnen och ISIN-koderna ut i samma ordning som de förekommer i filen.
'''

def clean_line(line):
    # Extrahera fondnamnet mellan '>' och '<'
    start_index = line.find('>') + 1
    end_index = line.rfind('<')
    fund_name = line[start_index:end_index]

    # Extrahera ISIN-koden efter tabben
    isin_code = line.split('\t')[-1].strip()

    return fund_name, isin_code


# Öppna och läs filen
with open('inveztlyfonderhtml', 'r', encoding='utf-8') as file:
    content = file.readlines()

# Separata listor för fondnamn och ISIN-koder
fund_names = []
isin_codes = []

# Rensa och extrahera fondnamn och ISIN-koder
for line in content:
    fund_name, isin_code = clean_line(line)
    fund_names.append(fund_name)
    isin_codes.append(isin_code)

# Skriv ut fondnamn och sedan ISIN-koder i samma ordning
print("Fondnamn:")
for name in fund_names:
    print(name)

print("\nISIN-koder:")
for code in isin_codes:
    print(code)

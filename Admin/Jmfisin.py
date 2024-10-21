'''
Denna kod jämför ISIN-koder mellan två filer: 'inveztlysfonder.txt' och 'Alpcot_fonder'.
Först läses båda filerna in och varje rad sparas.
Sedan skapas en uppsättning (set) med ISIN-koder från 'inveztlysfonder.txt'.
Efter det går koden igenom varje rad i 'Alpcot_fonder'.
Fonder som har en ISIN-kod som matchar en kod från den första filen skrivs först ut med ett meddelande om "Match found".
Därefter skrivs fonder ut som inte har någon matchning med ett meddelande om "No match found".
'''

# Läs in filerna och spara varje rad
with open('inveztlysfonder.txt', 'r', encoding='utf-8') as file1:
    data1 = file1.readlines()

with open('Alpcot_fonder', 'r', encoding='utf-8') as file2:
    data2 = file2.readlines()

# Skapa en uppsättning (set) för ISIN-koder från den första filen
isin_set_1 = set()

# Extrahera och spara ISIN-koder från inveztlysfonder.txt
for line in data1:
    line_parts = line.split()
    if line_parts:  # Kontrollera om raden inte är tom
        isin = line_parts[-1]  # Sista delen av raden är ISIN-koden
        isin_set_1.add(isin)  # Lägg till ISIN i uppsättningen

# Lista för att lagra fonder som har en matchning respektive ingen matchning
matched_funds = []
unmatched_funds = []

# Gå igenom varje rad i Alpcot_fonder och sortera dem i matchade och omatchade fonder
for line in data2:
    line_parts = line.split()
    if line_parts:  # Kontrollera om raden inte är tom
        isin = line_parts[-1]  # Sista delen av raden är ISIN-koden
        fondnamn = ' '.join(line_parts[:-1])  # Fondenamn är allt före ISIN-koden
        if isin in isin_set_1:  # Kolla om ISIN finns i den första uppsättningen
            matched_funds.append(f"{fondnamn}\t{isin} - Match found")
        else:
            unmatched_funds.append(f"{fondnamn}\t{isin} - No match found")

# Skriv först ut fonder med matchning
for match in matched_funds:
    print(match)

# Skriv sedan ut fonder utan matchning
for no_match in unmatched_funds:
    print(no_match)

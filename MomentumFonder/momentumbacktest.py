'''
Denna kod analyserar data från en fil som innehåller NAV-kurser och avkastning för olika tidsperioder (3, 6, 9 och 12 månader).
För varje rad i filen bearbetas data och lagras i separata listor.
Koden skapar sedan poänglistor baserade på om avkastningen för varje tidsperiod är positiv eller negativ.
Därefter summeras poängen för varje tidsperiod och sekvenser av nollor (negativ eller ingen avkastning) och
positiva tal (positiv avkastning) identifieras.
Funktionen 'hitta_0_sekvenser' analyserar sekvenser av nollor och beräknar avkastning efter dessa sekvenser.
Liknande funktioner finns för att hitta sekvenser av ettor, tvåor, treor och fyror, som representerar olika mönster
av positiv avkastning.
Slutligen skrivs den genomsnittliga avkastningen för varje typ av sekvens ut.
'''
# Öppnar filen 'LFglobal.txt' i läsläge och läser in dess innehåll som en lista av rader
with open('LFglobal.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

# Skapar tomma listor för att lagra data om NAV-kurs och avkastning för olika perioder
nav = []
mån_3 = []
mån_6 = []
mån_9 = []
mån_12 = []
mån = [3, 6, 12, 24, 36]  # Lista med olika månader som ska analyseras

# Loopar genom varje rad i filen och behandlar data
for line in content:
    # Konverterar strängar med siffror från procent till flyttal och delar upp radens värden baserat på tabb
    values = [float(val.replace(',', '').rstrip('%\n')) / 100 for val in line.split('\t')]

    # Lägger till värden i respektive lista
    nav.append(values[0])  # NAV-värde
    mån_3.append(values[1])  # 3 månaders avkastning
    mån_6.append(values[2])  # 6 månaders avkastning
    mån_9.append(values[3])  # 9 månaders avkastning
    mån_12.append(values[4])  # 12 månaders avkastning

# Skapar poänglistor där 1 representerar positiv avkastning och 0 negativ avkastning för varje tidsperiod
mån3_points = [1 if value > 0 else 0 for value in mån_3]
mån6_points = [1 if value > 0 else 0 for value in mån_6]
mån9_points = [1 if value > 0 else 0 for value in mån_9]
mån12_points = [1 if value > 0 else 0 for value in mån_12]

# Skapar en ny lista som summerar poäng från varje tidsperiod (3, 6, 9 och 12 månader)
sum_list = [c1 + c2 + c3 + c4 for c1, c2, c3, c4 in zip(mån3_points, mån6_points, mån9_points, mån12_points)]


# Funktion för att hitta sekvenser av nollor i poänglistan och beräkna avkastning efter ett visst antal månader
def hitta_0_sekvenser(sum_list, mån):
    avg1 = avg2 = avg3 = avg4 = 0  # Genomsnittlig avkastning för olika längder av sekvenser
    Avkast_1 = []
    Avkast_2 = []
    Avkast_3 = []
    Avkast_4 = []
    noll_sekvenser = []  # Sparar positioner där sekvenser av nollor startar
    sekvens_langd2 = []  # Sparar längden på varje sekvens av nollor
    månader = mån

    i = 0
    # Går igenom listan och letar efter sekvenser där poänglistan är noll
    while i < len(sum_list):
        if sum_list[i] == 0:
            sekvens_langd = 1
            i += 1
            while i < len(sum_list) and sum_list[i] == 0:
                sekvens_langd += 1
                i += 1
            if i < len(sum_list):
                noll_sekvenser.append(i)  # Sparar positionen efter nollsekvensen
                sekvens_langd2.append(sekvens_langd)  # Sparar längden på sekvensen
        else:
            i += 1

    # Beräknar avkastningen efter den angivna tidsperioden för varje nollsekvens
    for k in range(len(noll_sekvenser)):
        plats = noll_sekvenser[k]
        sekvens_langd3 = sekvens_langd2[k]
        if plats + månader < len(nav) and plats < len(nav):
            avkastning = nav[plats + månader] / nav[plats]

        # Lägger till avkastning i respektive lista beroende på sekvensens längd
        if sekvens_langd3 == 1:
            Avkast_1.append(avkastning)
        elif sekvens_langd3 == 2:
            Avkast_2.append(avkastning)
        elif sekvens_langd3 == 3:
            Avkast_3.append(avkastning)
        elif sekvens_langd3 == 4:
            Avkast_4.append(avkastning)

    # Beräknar genomsnittlig avkastning för varje typ av sekvens
    if len(Avkast_1) > 0:
        avg1 = sum(Avkast_1) / len(Avkast_1)
    if len(Avkast_2) > 0:
        avg2 = sum(Avkast_2) / len(Avkast_2)
    if len(Avkast_3) > 0:
        avg3 = sum(Avkast_3) / len(Avkast_3)
    if len(Avkast_4) > 0:
        avg4 = sum(Avkast_4) / len(Avkast_4)

    # Skriver ut den genomsnittliga avkastningen för varje typ av sekvens
    print(f'Genomsnittlig avkastning efter {månader} månader i en 1 nollsekvens: {(avg1 - 1) * 100}')
    print(f'Genomsnittlig avkastning efter {månader} månader i en 2 nollsekvens: {(avg2 - 1) * 100}')
    print(f'Genomsnittlig avkastning efter {månader} månader i en 3 nollsekvens: {(avg3 - 1) * 100}')
    print(f'Genomsnittlig avkastning efter {månader} månader i en 4 nollsekvens: {(avg4 - 1) * 100}')


# Anropar funktionen för varje tidsperiod (3, 6, 12, 24, 36 månader)
for i in range(len(mån)):
    hitta_0_sekvenser(sum_list, mån[i])

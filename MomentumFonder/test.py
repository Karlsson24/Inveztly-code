poang_lista = [3, 0, 0, 1, 1, 2, 1, 4, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 2, 3, 4, 3, 0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 2, 2, 0, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 3, 2, 1, 0, 2, 2, 1, 0, 1, 2, 4, 1, 4, 4, 4, 4, 4, 3, 3, 1]

def hitta_noll_sekvenser(poang_lista):
    i = 0
    while i < len(poang_lista):
        if poang_lista[i] == 0:
            sekvens_langd = 1
            i += 1
            while i < len(poang_lista) and poang_lista[i] == 0:
                sekvens_langd += 1
                i += 1
            print(f"Sekvens av nollor: {sekvens_langd}")
        else:
            i += 1

hitta_noll_sekvenser(poang_lista)

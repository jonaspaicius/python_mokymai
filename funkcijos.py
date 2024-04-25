# 1 užduotis
# Parašykite funkciją, kuri kaip argumentą priima vieną kintamąjį (tekstą) ir grąžina jį apversta
# pavyzdžiui, pateikus žodį "labas", funkcija grąžintų atsakymą "sabal"
# pateikus žodį "alus", grąžintų "sula"
# parašykite keletą testų šiai funkcijai
# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai
# 3 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina jame esančius TEIGIAMUS skaičius
# parašykite keletą testų šiai funkcijai
# 4 užduotis
# Parašykite funkciją, kuri priima dvi sąrašų rūšiavimo funkcijas: vieną didėjančiai rūšiavimui, kitą mažėjančiai rūšiavimui, ir sąrašą skaičių. 
# Funkcija turi grąžinti rūšiuotą sąrašą pagal pateiktas rūšiavimo funkcijas.
# parašykite keletą testų šiai funkcijai

def text_in_reverse(a: str) -> str:
    return a[::-1]

def list_sum(a: list) -> float:
    return sum(a) if a else 0

def sum_of_positives(a: list) -> float:
    return sum([i for i in a if i>0])

def sort_list(a: list, b: str):
    if b == 'asc':
        a.sort()
        return a
    if b == 'desc':
        a.sort(reverse=True)
        return a

def rikiuoti(rikiavimo_funkcija, sarasas):
    return rikiavimo_funkcija(sarasas)

def rikiuoti_mazejanciai(sarasas):
    return sorted(sarasas, reverse=True)

def rikiuoti_didejant(sarasas):
    return sorted(sarasas)
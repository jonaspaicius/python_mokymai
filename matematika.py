def sudetis(a,b):
    return a+b

def daugyba(a: int, b: int) -> int:
    """
    Ši funkcija sudaugina du sveikuosius skaičius
    """   
    return a*b

def rask_didziausia(a:int, b:int) -> int:
    return a if a > b else b

def pasisveikinimas(vardas):
    return f'Labas, {vardas}'

def pirmas_sarase(sarasas:list):
    return sarasas[0] if sarasas else None

def kubo_turis(a, b, c):
    return a*b*c

# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)
# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)
# 3 užduotis 
# Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis. 
# Grąžinkite True, jei skaičius yra pirminis, ir False, jei ne.
# Parašykite keletą testų (naudojantis parametrize)

def division_by_3(a: int):
    return a%3 == 0

def words_with_same_letters(words: list):
    results = []
    for word in words:
        if len(word) > len(set(list(word))):
            results.append(word)
    return results

# [word for word in words if len(word) > len(set(word))]

def check_if_prime(num: int):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
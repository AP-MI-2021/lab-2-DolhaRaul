def prim(n):
    if(n < 2): return False
    if(n == 2): return True
    if(n % 2 == 0): return False
    i = 3
    while (i * i <= n):
        if n % i == 0:
          return False
        i = i + 2
    return True

def get_largest_prime_below(n):
    if n < 2: return "Nu exista"
    rez = n
    while rez >= 0:
        if prim(rez) == True:
            return rez
        rez = rez - 1

def test_get_largest_prime_below():
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(7) == 7
    assert get_largest_prime_below(10) == 7

def PB1():
    test_get_largest_prime_below()
    n = int(input("Introduceti valoarea numarului: "))
    rez = get_largest_prime_below(n)
    print(f"Rezultatul functiei [get_largest_prime_below()] pentru valoarea {n} este {rez}")

def cmmdc(x, y):
   r = x % y
   while y != 0:
        r = x % y
        x = y
        y = r
   return x
def cmmmc(x, y):
    prod = x * y
    div_com = cmmdc(x, y)
    rez = prod // div_com
    return rez
def get_cmmmc(lst):
    rez = 1
    for val in lst:
        nr = int(val)
        rez = cmmmc(rez, nr)
    return rez
def test_get_cmmmc():
    assert get_cmmmc([1, 2, 3, 4]) == 12
    assert get_cmmmc([1, 2, 3, 5]) == 30
    assert get_cmmmc([2, 4, 8]) == 8
    assert get_cmmmc([2, 3, 5 * 2]) == 30
    assert get_cmmmc([1, -1, 2, 3]) == 6
def PB14():
    test_get_cmmmc()
    n = int(input("Introduceti numarul de numere aici: "))
    sir_numere = input("Dati numere separate prin spatiu aici: ")
    numere_str = sir_numere.split(' ')
    print(f'Cel mai mic multiplu comun al celor {n} numere este {get_cmmmc(numere_str)}')

def main():
    while True:
        optiune = int(input("Introduceti problema dorita aici: "))
        if optiune == 1:#Problema aleasa din prima jumatate
            PB1()
        elif optiune == 2:#Problema aleasa din a doua jumatate
            PB14()
        elif optiune == 3:#Ne orpim
            break
        else:
            print("Optiune invalida")
main()

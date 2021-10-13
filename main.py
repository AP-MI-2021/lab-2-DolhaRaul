def prim(n):
    '''
    Programul determina daca un numar n este prim sau nu, ca la seminar
    Input:
    -un numar intreg introdus de utiilizator
    Output:
    -True daca numarul este prim sau False in caz contrar
    '''
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
    '''
    Subprogramul returneaza cel mai mic numar prim mai mic sau egal cu n
    Input:
    -un numar natural introdus de utlizator
    Output:
    -cel mai mic numar prim mai mic sau egal cu el
    -Daca nu exista, se va afisa mesajul "Nu exista"
    '''
    if n < 2: return "Nu exista"
    rez = n
    while rez >= 0:
        if prim(rez) == True:
            return rez
        rez = rez - 1

def test_get_largest_prime_below():
    '''
    Functia ce testeaza diferite exemple pentru get_largest_prime_below(ca la seminar)
    '''
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(7) == 7
    assert get_largest_prime_below(10) == 7

def PB1():
    '''
    "Interfata" pentru prima problema, unde utilizatorul introduce datele si obtine rezulatul dorit prin divesre subprograme
    '''
    test_get_largest_prime_below()
    n = int(input("Introduceti valoarea numarului: "))
    rez = get_largest_prime_below(n)
    print(f"Rezultatul functiei [get_largest_prime_below()] pentru valoarea {n} este {rez}")

def cmmdc(x, y):
   '''
   Functia retunreaza cel mai mare divizor comun a 2 nr x si y
   Input:
   -doua numere intreg introduse de utilizator
   Output:
   -cel mai mare divizor comun al  celor doua numere
   '''
   r = x % y
   while y != 0:
        r = x % y
        x = y
        y = r
   return x

def cmmmc(x, y):
    '''
    Functia retunreaza cel mai mic multiplu comun a 2 nr x si y
   Input:
   -doua numere intreg introduse de utilizator
   Output:
   -cel mai mic multiplu comun al  celor doua numere
    '''
    prod = x * y
    div_com = cmmdc(x, y)
    rez = prod // div_com
    return rez

def get_cmmmc(lst):
    '''
    Functia retunreaza cel mai mic multiplu comun a n numere dintr o lista
   Input:
   -un numar de numere introduse de utilizator
   Output:
   -cel mai mic multiplu comun al acestor numere
    '''
    rez = 1
    for val in lst:
        nr = int(val)
        rez = cmmmc(rez, nr)
    return rez

def test_get_cmmmc():
    '''
    Functia testeaza diferite exemple pentru subprogramul get_cmmmc(ca la seminar)
    '''
    assert get_cmmmc([1, 2, 3, 4]) == 12
    assert get_cmmmc([1, 2, 3, 5]) == 30
    assert get_cmmmc([2, 4, 8]) == 8
    assert get_cmmmc([2, 3, 5 * 2]) == 30
    assert get_cmmmc([1, -1, 2, 3]) == 6

def PB14():
    '''
    "Interfata" pentru a doua problema, unde utilizatorul introduce datele si obtine rezulatul dorit prin divesre subprograme
    '''
    test_get_cmmmc()
    n = int(input("Introduceti numarul de numere aici: "))
    sir_numere = input("Dati numere separate prin spatiu aici: ")
    numere_str = sir_numere.split(' ')
    print(f'Cel mai mic multiplu comun al celor {n} numere este {get_cmmmc(numere_str)}')

def is_palindrome(n):
    '''
    Verifica daca un numar este palindrom(egal cu el insusi)
    Input:
    -un numar natural introdus de utlizator
    Output:
    -True daca e palindrom sau False in caz contrar
    '''
    cn = n
    ogl = 0
    while cn != 0:
        ogl = ogl * 10
        ogl = ogl + cn % 10
        cn = cn // 10
    if n == ogl:#este palindrom
        return True
    return False

def test_is_palindrome():
    '''
     Functia testeaza diferite exemple pentru subprogramul is_palindrome(ca la seminar)
    '''
    assert is_palindrome(121) == True
    assert is_palindrome(1221) == True
    assert is_palindrome(123) == False
    assert is_palindrome(1) == True

def PB5():#Problema in plus
    """
    "Interfata" pentru problema in plus, unde utilizatorul introduce datele si obtine rezulatul dorit prin divesre subprograme
    :return:
    """
    test_is_palindrome()
    n = int(input("Introduceti numarul dorit aici: "))
    rez = is_palindrome(n)
    print(f'Rezultatul functiei [is_palindrome] pentru {n} este {rez}')

def main():
    while True:
        optiune = int(input("Introduceti problema dorita aici: "))
        if optiune == 1:#Problema aleasa din prima jumatate
            PB1()
        elif optiune == 2:#Problema aleasa din a doua jumatate
            PB14()
        elif optiune == 3:#Problema in plus
            PB5()
        elif optiune == 4:#Oprim programul
            break
        else:
            print("Optiune invalida")
main()

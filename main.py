def citire_lista():
    """
    functia citeste o lista
    :return: lista citita
    """
    l = []
    n = int(input("dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def nrpozcat (l):
    """
    concateneaza toate nr pozitive din sir
    :param l: o lista de nr intregi
    :return: toate nr pozitive din sir concatenate
    """
    nou=0
    for i in range(len(l)):
        if (l[i])>=0:
            nou=nou*10+l[i]

    return nou
def test_nrpozcat():
    assert nrpozcat([5,-7,3])==[53]
    assert nrpozcat([7,-4,-3])==[7]
    assert nrpozcat([1,7,2])==[172]





def max (l):
    """
    determina cel mai mic si cel mai mare nr din sir
    :param l: o lista de nr intregi
    :return: cel mai mic si cel mai mare nr din sir
    """
    max=0

    for i in range(len(l)-1):
        if l[i]>max:
            max=l[i]

    return max


def min(l):
    """
    determina cel mai mic si cel mai mare nr din sir
    :param l: o lista de nr intregi
    :return: cel mai mic si cel mai mare nr din sir
    """
    min =999999

    for i in range(len(l) - 1):
        if l[i] <min:
            min = l[i]

    return min

def test_max():
    assert toate_nrdivizori([5,7,13])==[13]
    assert toate_nrdivizori([7,42,37])==[37]
    assert toate_nrdivizori([15,7,22])==[22]




def main():
    print("1.Afiseaza toate nr pozitive concatenate dintr un sir")
    print("2. Suma celui mai mic si celui mai mare nr din sir")
    print("0.iesire")
    while True:
        optiune=int(input("dati optiune:"))
        if optiune==1:
            l=citire_lista()
            #test_nrpozcat()
            print(nrpozcat(l))
        elif optiune==2:
            l=citire_lista()
            #test_max()
            print(min(l)+max(l)+1)
        elif optiune==3:
            l=citire_lista()

        elif optiune==0:
            break
        else:
            print("optiune gresita")

main()

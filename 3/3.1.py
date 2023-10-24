#funkcja_1 jest POPRAWNA składniowo
def funkcja_1 ():
    x = 2; y = 3;
    if (x > y):
        result = x;
    else:
        result = y;
    return result;

#funkcja_2 jest NIEPOPRAWNA, ponieważ w Pythonie nie możemy umieszczać funkcji warunkowych bezpośrednio w pętli for
# def funkcja_2():
#     for i in "axby": if ord(i) < 100: print (i)

#funkcja_3 jest POPRAWNA
def funkcja_3():
    for i in "axby": print (ord(i) if ord(i) < 100 else i)


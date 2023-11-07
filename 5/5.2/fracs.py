from math import lcm

#Dodawanie
def add_frac(frac1, frac2):
    lcm_value = lcm(frac1[1], frac2[1])
    new_frac1 = [frac1[0] * (lcm_value // frac1[1]), lcm_value]
    new_frac2 = [frac2[0] * (lcm_value // frac2[1]), lcm_value]

    return [new_frac1[0] + new_frac2[0], lcm_value]

#Odejmowanie
def sub_frac(frac1, frac2):
    lcm_value = lcm(frac1[1], frac2[1])
    new_frac1 = [frac1[0] * (lcm_value // frac1[1]), lcm_value]
    new_frac2 = [frac2[0] * (lcm_value // frac2[1]), lcm_value]

    return [new_frac1[0] - new_frac2[0], lcm_value]

#Mnożenie
def mul_frac(frac1, frac2):
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

#Dzielenie
def div_frac(frac1, frac2):
    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]

#CzyDodatnie?
def is_positive(frac):
    return frac[0] > 0

#CzyZerowe?
def is_zero(frac):
    return frac[0] == 0

#Porównanie
def cmp_frac(frac1, frac2):
    diff = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    if diff < 0:
        return -1
    elif diff > 0:
        return 1
    else:
        return 0

#KonwersjaDoFloat
def frac2float(frac):
    return frac[0] / frac[1]

# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
def romano (num):
    dicc = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    if len(num) ==1:
        return dicc[num]
    else:
        if dicc[num[0]] >= dicc[num[1]]:
            return dicc[num[0]] + romano(num[1:])
        else:
            return romano(num[1:]) - dicc[num[0]] 

print (romano("MCMLXXII"))

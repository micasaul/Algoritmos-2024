def romano (num):
    dicc = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    if len(num) ==1:
        return dicc[num]
    else:
        if dicc[num[0]] >= dicc[num[1]]:
            return dicc[num[0]] + romano(num[1:])
 #siguen el ciclo comun pero debo ubicar el indice 0 del num dentro del dicc
        #para reconocer cual es mayor
               
        else:
            return romano(num[1:]) - dicc[num[0]] 
 #los numeros mas chicos adelante de los mas grandes restan en romano

print (romano("MCMLXXII"))
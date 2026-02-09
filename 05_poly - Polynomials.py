def polyEval(poly: list, x: float)->float:
    result: float = 0
    for i in range(len(poly)):
        result += poly[i] * x ** i
    return float(result)


def polySum(poly1: list, poly2: list)->list:
    result: list = []
    if len(poly1) >= len(poly2):
        for i in range(len(poly2)):
            result.append(poly1[i] + poly2[i])
        result.extend(poly1[len(poly2):]) 
    elif len(poly1) <= len(poly2):
        for i in range(len(poly1)):
            result.append(poly1[i] + poly2[i])
        result.extend(poly2[len(poly1):]) 
    while result[-1] == 0:
        result.pop()
    return list(result) 

def polyMultiply(poly1:list, poly2:list)->list:
    result: list = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            index = i + j
            value = poly1[i] * poly2[j]
            if len(result) <= index:
                result.append(0)
            result[index] += value
    return list(result)


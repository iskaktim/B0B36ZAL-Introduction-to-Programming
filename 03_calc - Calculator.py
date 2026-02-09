def addition(x, y)->float:
    n = x + y
    return float(n)


def subtraction(x, y)->float:
    n = x - y
    return float(n)


def multiplication(x, y)->float:
    n = x * y
    return float(n)


def division(x, y)->float:
        if y == 0:
            raise ValueError('This operation is not supported for given input parameters')
        else: 
            n = x / y
            return float(n)
    
def modulo(x, y)->float:
    if (x >= y) and (y > 0):
        n = x % y
        return float(n)
    else:
        raise ValueError('This operation is not supported for given input parameters')

def secondPower(x)->float:
    n = x ** 2
    return float(n)


def power(x, y)->float:
    if y > 0:
        n = x ** y
        return float(n)
    elif y == 0:
        n = 1
        return float(n)
    else:
        raise ValueError('This operation is not supported for given input parameters')

def secondRadix(x)->float:
    if x > 0:
        n = x ** 0.5
        return float(n)
    else:
        raise ValueError('This operation is not supported for given input parameters')


def magic(x, y, z, k)->float:
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    n = l/m + 1
    return float(n)


def control(a, x, y, z, k)->float:
    dict_operations = {
        "ADDITION": addition,
        "SUBTRACTION": subtraction,
        "MULTIPLICATION": multiplication,
        "DIVISION": division,
        "MOD": modulo,
        "SECONDPOWER": secondPower,
        "POWER": power,
        "SECONDRADIX": secondRadix,
        "MAGIC": magic
    }
    if a in dict_operations:
        func = dict_operations[a]
        if a == "ADDITION" or a == "SUBTRACTION" or a == "MULTIPLICATION" or a == "DIVISION" or a == "MOD" or a == "POWER":
            return func(x, y)
        elif a == "SECONDPOWER" or a == "SECONDRADIX":
            return func(x)
        elif a == "MAGIC":
            return func(x, y, z, k)
        else:
            raise ValueError('This operation is not supported for given input parameters')
    else:
        raise ValueError('This operation is not supported for given input parameters')
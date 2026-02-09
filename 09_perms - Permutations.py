def permutations(array, start = 0):
    result = []

    if start == len(array):
        return [array.copy()]

    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]

        tail = permutations(array, start + 1)

        for j in tail:
            result.append(j)

        array[start], array[i] = array[i], array[start]

    return result

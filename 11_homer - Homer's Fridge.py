class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration


def openFridge(fridge: list[Food]):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print(f"{food.name} (expires in: {food.expiration} days)")


# ---------- Úkol 1 ----------
def maxExpirationDay(fridge: list[Food]) -> int:
    if len(fridge) == 0:
        return -1

    max_exp = fridge[0].expiration
    for food in fridge:
        if food.expiration > max_exp:
            max_exp = food.expiration
    return max_exp


# ---------- Úkol 2 ----------
def histogramOfExpirations(fridge: list[Food]) -> list[int]:
    max_exp = maxExpirationDay(fridge)

    if max_exp == -1:
        return []

    histogram = [0] * (max_exp + 1)

    for food in fridge:
        histogram[food.expiration] += 1

    return histogram


# ---------- Úkol 3 ----------
def cumulativeSum(histogram: list[int]) -> list[int]:
    if len(histogram) == 0:
        return []

    result = [0] * len(histogram)
    result[0] = histogram[0]

    for i in range(1, len(histogram)):
        result[i] = result[i - 1] + histogram[i]

    return result


# ---------- Úkol 4 ----------
def sortFoodInFridge(fridge: list[Food]) -> list[Food]:
    if len(fridge) == 0:
        return []

    histogram = histogramOfExpirations(fridge)
    cum_sum = cumulativeSum(histogram)

    result = [None] * len(fridge)

    for i in range(len(fridge) - 1, -1, -1):
        food = fridge[i]
        exp = food.expiration

        cum_sum[exp] -= 1
        position = cum_sum[exp]

        result[position] = food

    return result

# ---------- Úkol 5 ----------
def reverseFridge(fridge: list[Food]) -> list[Food]:
    result = [None] * len(fridge)

    left = 0
    right = len(fridge) - 1

    while left < len(fridge):
        result[left] = fridge[right]
        left += 1
        right -= 1

    return result


# ---------- Úkol 6 ----------
def eatFood(name: str, fridge: list[Food]) -> list[Food]:

    candidate = None
    candidate_index = -1

    for i in range(len(fridge)):
        food = fridge[i]

        if food.name == name:
            if candidate is None or food.expiration < candidate.expiration:
                candidate = food
                candidate_index = i

    result = []
    for food in fridge:
        result.append(food)

    if candidate_index == -1:
        return result

    result.pop(candidate_index)

    return result

# fridge = [
#     Food("beer", 4),
#     Food("steak", 1),
#     Food("hamburger", 1),
#     Food("donut", 3)
# ]

# openFridge(sortFoodInFridge(fridge))
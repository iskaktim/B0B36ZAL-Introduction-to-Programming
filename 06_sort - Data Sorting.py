def sortNumbers(data: list[int], condition: str)->list[int]:
    if condition == 'ASC':
        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    elif condition == 'DESC':
        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    else: 
        raise ValueError('Invalid input data')

def sortData(weights:list[int], data:list[str], condition:str)->list[str]:
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
    elif len(weights) == len(data):
        new_data = []
        for i in range(len(weights)):
            new_data.append([weights[i], data[i]])
        if condition == 'ASC':
            for i in range(len(new_data)):
                for j in range(0, len(new_data) - i - 1):
                    if new_data[j][0] > new_data[j + 1][0]:
                        new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]
        elif condition == 'DESC':
            for i in range(len(new_data)):
                for j in range(0, len(new_data) - i - 1):
                    if new_data[j][0] < new_data[j + 1][0]:
                        new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]
        else: 
            raise ValueError('Invalid input data')
        result = []
        for item in new_data:
            result.append(item[1])
        return result



array = [4 ,3 ,6 ,9 ,5 ,100]

for bluep in range(1, len(array)):
    value = array[bluep]
    blackp = bluep - 1

    while array[blackp] > array[bluep] and blackp >= 0:
        array[blackp + 1] = array[blackp]
        blackp -= 1
    array[blackp + 1] = value

print(array)

# creating an array
size = int(input("Please enter the size of the array: "))
array = [None] * size

x = 1
for i in range(0, size):
    array[i] = input("Enter the data for location {}: ".format(x))
    x += 1

# choice for sorting
print("SORTING")
print("1. Ascending Order")
print("2. Descending Order")

choice = int(input("Enter your choice: "))

#sorting
if choice == 1:
    for i in range(0, size):
        for j in range(i + 1, size):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
elif choice == 2:
    for i in range(0, size):
        for j in range(i + 1, size):
            if array[i] < array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
else:
    print("Choice is invalid!")


if choice == 1:
    print("Array sorted in ascending order: ")
    for i in range(0, size):
        print(array[i])
elif choice == 2:
    print("Array sorted in descending order: ")
    for i in range(0, size):
        print(array[i])

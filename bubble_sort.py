def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                
    return list

numeros = [5, 1, 4, 2, 8]
print(bubble_sort(numeros))  # [1, 2, 4, 5, 8]
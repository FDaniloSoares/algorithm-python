def quick_sort(list):
    
    def inner_quick_sort(low, higth):
        
        if (low >= higth): return
        
        pivot = list[higth]
        ref = low
        
        for i in range(low, higth):
            if list[i] < pivot:
                list[ref], list[i] = list[i], list[ref]
                ref += 1
        
        list[ref], list[higth] = list[higth], list[ref]
        
        inner_quick_sort(low, ref - 1)
        inner_quick_sort(ref, higth)

    inner_quick_sort(0, len(list) - 1)
    
    return list


numeros = [5, 1, 4, 2, 8]
print(quick_sort(numeros))  # [1, 2, 4, 5, 8]
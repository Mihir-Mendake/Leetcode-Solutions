# MERGE SORT IMPLEMENTATION

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l_half = merge_sort(arr[:mid])
    r_half = merge_sort(arr[mid:])
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return merge(l_half, r_half) # type: ignore

def merge(right,left):
    new = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    new.extend(left[i:])
    new.extend(right[j:])
    return new


arr = [10,40,50,30,60,70,90,80,20]
print("The original array is:", arr)
sorted_arr = merge_sort(arr)
print("The sorted array is:", sorted_arr)
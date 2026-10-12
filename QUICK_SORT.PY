# Q1) Write a Python program to sort an array using recursive Quick Sort.
# Use the first
# element as the pivot, apply partitioning, and recursively sort the
# sub-arrays. Print the original and sorted array.
#Expected Input: [5, 8, 1, 2, 6, 3, 9]
#Expected Output: [1, 2, 3, 5, 6, 8, 9]


def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot - 1)
        quick_sort(arr,pivot + 1,high)

def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <=j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = [5, 8, 1, 2, 6, 3, 9]
print("The original array is:",arr)
quick_sort(arr,0,len(arr)-1)
print("The sorted array is:",arr)
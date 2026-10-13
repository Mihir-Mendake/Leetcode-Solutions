#2. Write a Python program to sort a list of integers in ascending orderusing the Insertion Sort algorithm.
#• Use a predefined list of integers (for example: [40, 30, 20, 10]).

def insertion_sort(arr1):
    n = len(arr1)
    for i in range(1,n):
        j = i-1
        key = arr1[i]
        while j >= 0 and key < arr1[j]:
            arr1[j+1] = arr1[j]

            j -= 1
        arr1[j+1]= key

arr = [40, 30, 20, 10]

insertion_sort(arr)
print("The sorted array is:",arr)

# 1. Write a Python program to sort a list of integers in ascending orderusing the Selection Sort algorithm.

def selection_sort(arr):
    n =len(arr)
    for i in range(n-1):
        mini =i
        for j in range(i+1,n):
           if arr[j] < arr[mini]:
            mini = j
            (arr[i],arr[mini]) = (arr[mini],arr[i])

arr = [24,41,33,42,17]
selection_sort(arr)
print("The sorted array is:",arr)

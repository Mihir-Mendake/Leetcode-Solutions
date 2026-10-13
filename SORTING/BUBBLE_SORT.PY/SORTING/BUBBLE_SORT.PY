# 3. Write a Python program to sort a list of integers in ascending order using the Bubble Sort algorithm.

from tkinter import FALSE, TRUE


def bubble_sort(arr1):
    n = len(arr1)
    for i in range(n):
        swapped = FALSE
        for j in range(0,n-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
                swapped = TRUE

        if not swapped:
            break

arr1 = [50,40,30,10]

bubble_sort(arr1)
print("The sorted array is:",arr1)

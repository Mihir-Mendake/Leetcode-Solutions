# Sort an array of positive and negative numbers separately using
#Selection Sort. Expected Input: [12, -7, 5, -3, 9, -1, 4, -6] Expected
#Output: [-7, -6, -3, -1, 4, 5, 9, 12]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        (arr[i],arr[mini]) = (arr[mini],arr[i])

arr = [12, -7, 5, -3, 9, -1, 4, -6]
print("The original array is:",arr)
selection_sort(arr)
print("The sorted array is:",arr)
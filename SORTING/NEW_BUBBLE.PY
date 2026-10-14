# Sort the first half of an array in ascending order and the second
# half in descending order using Bubble Sort.
# Expected Input:
# [20, 10, 50, 40, 30, 70, 60, 90]
# Expected Output:
# [10, 20, 40, 50, 90, 70, 60, 30]

def ascending(arr,start,end):
    for i in range(start,end):
        for j in range(start,end-(i-start)):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def descending(arr,start,end):
    for i in range(start,end):
        for j in range(start,end-(i-start)):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def sort_half_array(arr):
    n = len(arr)
    mid = n//2
    ascending(arr,0,mid-1)
    descending(arr,mid,n-1)

arr = [20, 10, 50, 40, 30, 70, 60, 90]
print("The original array is:",arr)
sort_half_array(arr)
print("The sorted array is:",arr)
'''
#Selection Sort :-
import sys
A = [64, 25, 12, 22, 11]
  
# Traverse through all array elements
for i in range(len(A)):
    
  # Find the minimum element in remaining unsorted array
  min_idx = i
  for j in range(i+1, len(A)):
    if A[min_idx] > A[j]:
        min_idx = j
             
    # Swap the found minimum element with the first element       
    A[i], A[min_idx] = A[min_idx], A[i]
 
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
   print("%d" %A[i]),
'''

'''

#Bubble Sort
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1 Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
   
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])

'''

'''
#Insertion Sort :-
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
         key = arr[i]
 
    # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    j = i-1
    while j >= 0 and key < arr[j] :
        arr[j + 1] = arr[j]
        j -= 1
        arr[j + 1] = key
   
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
'''


'''
#Shell Sort :-

def shellSort(arr):
    gap = len(arr) // 2 # initialize the gap
    while gap > 0:
        i = 0
        j = gap
         
        # check the array in from left to right till the last possible index of j
        while j < len(arr):
     
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
         
            # now, we look back from ith index to the left we swap the values which are not in the right order.
            k = i
            while k - gap > -1:
 
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
 
        gap //= 2
 
  # driver to check the code
arr2 = [12, 34, 54, 2, 3]
print("input array:",arr2)
 
shellSort(arr2)
print("sorted array",arr2)

'''


'''
#Quick Sort :-

def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses  end pointer, and when it does we swap the pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an  element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other,  swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      
  # The main function that implements QuickSort 
def quick_sort(start, end, array):
    if (start < end):
          
        # p is partitioning index, array[p]  is at right place
        p = partition(start, end, array)
          
        # Sort elements before partition  and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
          
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)
print(f'Sorted array: {array}')
'''

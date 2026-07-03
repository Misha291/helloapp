class QuickSort:
    @staticmethod
    def quicksort(arr):
        if (len(arr) < 2):
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return QuickSort.quicksort(less) + [pivot] + QuickSort.quicksort(greater)
        


sort = QuickSort()
result = sort.quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(result)


print(QuickSort.quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1]))


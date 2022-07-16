# program to perform a number of operations on an integer array
def partition (l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr +=1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1
example = []
print("Enter the number of elements to input")
size = int(input())
print("Enter elements of the array")
for i in range(size):
    tmp = int(input())
    example.append(tmp)
print(quicksort(0, len(example)-1, example))
print("Enter the element you want to search for")
target = int(input())
print(binary_search(example, 0, len(example), target))
no_of_times = 0
for i in example:
    if(i == target):
        no_of_times +=1
print("The elements appears", no_of_times,"times")

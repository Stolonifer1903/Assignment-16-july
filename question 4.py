# program to make a list of marks of n number of students
def partition (l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr+=1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort (l, r, nums):
    if len (nums) == l:
        return nums
    if l < r:
        pi = partition (l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums
example = list(input())
print(quicksort(0, len(example)-1, example))
# program to remove duplicates from an array and also sort it
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def bubble(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i+1]:
                swapped = True
                elements[i], elements [i+1] = elements[i+1], elements[i]
        if not swapped:
            return
    print("The sorted array is: ")
    print(elements)
example = []
print("Enter the size of the array you want")
size = int(input())
print("Enter the elements of the array")
for i in range(size):
    tmp = int(input())
    example.append(tmp)
print(remove(example))
bubble(remove(example))

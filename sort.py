
# Merge Sort
def mergeSort(array):
    # array dtype: list[int]
    if len(array) <= 1:
        return array
    a, b = array[:len(array)//2], array[len(array)//2:]
    a = mergeSort(a)
    b = mergeSort(b)
    return merge(a, b)

# Merge two sorted lists
def merge(a, b):
    c, i, j, n = [], 0, 0, len(a) + len(b)
    for k in range(n):
        if i == len(a) or j == len(b):
            break
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if k < n - 1:
        if i == len(a):
            c.extend(b[j:])
        if j == len(b):
            c.extend(a[i:])
    return c

def main():
    arr = range(10,,-1)
    print(mergeSort(array))
    return 

def binarysearch(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return arr(low)

def binarysearch(arr,x):
    low = 0
    high = len(arr) - 1
    if high <= low:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, x, low, mid-1)
        else:
            return binarysearch(arr, x, mid+1, high)
    return arr(low)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def primarysum(mat):
    summ = 0
    for i in range(len(mat)):
        summ += mat[i][i]
    return summ

def secondarysum(mat):
    summ = 0
    for i in range(len(mat)):
        summ += mat[i][len(mat) - i -1]
    return summ

def mattranspose(mat):
    transposed = [[i[j] for i in mat] for j in range(len(mat[0]))]
    return transposed

# print(primarysum(matrix))
# print(secondarysum(matrix))
# print(mattranspose(matrix))

def uniquebitwise(ls):
    res = 0
    for i in ls:
        res ^= i
    return res

def bubble(ls):
    n = len(ls)
    for i in range(1,n):
        for j in range(0,n-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

def selection(ls):
    n = len(ls)
    for i in range(n-1):
        minind = i

        for j in range(i +1,n):
            if (ls[j]<ls[minind]):
                minind = j
        ls[i],ls[minind] = ls[minind],ls[i]
    return ls

ls1 = [2,4,6,5,8,3]
print(bubble(ls1))
print(selection(ls1))


def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2 #optimization
        if is_prime(num):
            count +=1
    return num
def is_prime(num):
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True

def largestsqr(n):
    count = 1
    while n > count:
        count *= 2
    return count//2
print(largestsqr())

def binarisort(ls):
    low = 0
    high = len(ls)-1
    while low<high:
        mid = (low+high)
        if ls[mid] != ls[mid-1] and ls[mid]!=ls[mid+1]:
            return ls[mid]
        elif ls[mid] != ls [mid-1]:
            if (mid%2 == 0):
                low = mid + 2
            else:
                high = mid - 1
        else:
            if (mid%2) == 0:
                high = mid - 2
            else:
                low = mid +1
    return ls[low]
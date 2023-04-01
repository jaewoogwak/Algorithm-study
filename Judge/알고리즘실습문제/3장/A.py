import sys
 
count = 0
 
 
def merge(left, right):
    global count
    l,r = 0,0
    sorted_list = []
 
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
             
        else:
            sorted_list.append(right[r])
            r += 1
            count += len(left) - l
 
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
 
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
             
    return sorted_list
 
 
def divide(arr):
    if len(arr) <= 1:
        return arr
 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
 
    left = divide(left)
    right = divide(right)
    return merge(left, right)
 
 
def findInversionPair(arr):
    return divide(arr)
 
 
def main():
    global count
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        arr= list(map(int, sys.stdin.readline().split()))
        count = 0
        findInversionPair(arr)
        print(count)        
     
main()
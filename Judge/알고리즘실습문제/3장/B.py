import sys
import collections
  
  
def divide(arr, k):
    if len(arr) < k:
        return 0
        
    freq = collections.Counter(arr)
   
    for i in range(len(arr)):
        if freq[arr[i]] < k:
            splitArr = arr.split(arr[i])
            return max(divide(a, k) for a in splitArr)
       
    return len(arr)
    
    
def solve(arr, k):
    return divide(arr,k)
   
   
   
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        s = sys.stdin.readline().rstrip()
        k = int(sys.stdin.readline())
     
        maxLen = solve(s, k)
        print(maxLen)
         
main()
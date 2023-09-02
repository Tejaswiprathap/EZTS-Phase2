'''the function accepts an integer arr of size 'length' as its arguments you are required to return the sum of second largest element from the even
positions and second smallest from the odd position of given 'arr'.
ASSUMPTIONS:
all array elements are unique.
treat 0th position as even.
NOTE:
return 0 if array is empty.
return 0 if array length is 3 or less than 3.'''
length=int(input())
arr=list(map(int,input().split()))
even_arr=[]
odd_arr=[]
for i in range(length):
    if i%2==0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
even_arr=sorted(even_arr)
odd_arr=sorted(odd_arr)
print(even_arr[len(even_arr)-2]+odd_arr[len(odd_arr)-2])

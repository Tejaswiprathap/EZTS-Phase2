'''execute the function that accepts the integer array of length 'size' and finds out the maximum number that can be formed by permutation.
NOTE:
you will have to rearrange the numbers to make the maximum number.
INPUT:
34 79 58 64
OUTPUT:
98765443 '''

def largest_permutation(arr):
    arr_str = [str(num) for num in arr]
    arr_str.sort(reverse=True, key=lambda x: x*3)
    largest_number = ''.join(arr_str)
    
    return largest_number

input_array = [34, 79, 58, 64]
output = largest_permutation(input_array)
print(sorted(output))

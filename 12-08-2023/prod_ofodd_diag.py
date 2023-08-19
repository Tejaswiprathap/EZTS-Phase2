'''product of odd elements of a square matrix whose ith and jth value will be same'''
def prod_odd_diagonal_elements(matrix):
    n = len(matrix)
    total = 1
    
    for i in range(n):
        if matrix[i][i] % 2 == 1:  
            total *= matrix[i][i]
    
    return total

matrix = [[1, 2, 3],[4, 4, 6],[7, 8, 9]]

result = prod_odd_diagonal_elements(matrix)
print("Product of odd diagonal elements:", result)

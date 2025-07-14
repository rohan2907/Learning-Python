# print n rows of Pascal's triangle
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Calculate the inner values
        triangle.append(row)
    
    return triangle

# Example usage:
result = pascal_triangle(5)
for row in result:
    print(row)
# Example usage:
# [1]
# [1, 1]
# [1, 2, 1] 
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]



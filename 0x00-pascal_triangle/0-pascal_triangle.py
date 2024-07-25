#!/usr/bin/python3
"""
Function to create a pascal triangle
"""
def pascal_triangle(n):
    """
    Return an empty list if n <= 0
    """
    if n <= 0:
        return []
    
    """
    Initialize the triangle with the first row
    """
    """
    Initialize the first row of the triangle
    """
    pas = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pas[i-1][j-1] + pas[i-1][j])
        row.append(1)
        pas.append(row)
    
    return pas
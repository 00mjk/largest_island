# Problem: We have a 2D array representing a geographic map with bodies of water and islands of land.
# Land is represented by 1, and water by 0. We want to find the size of the largest island. An
# island's size is determined by the number of contiguous 1s in the map. 
#
# Caveats:
# - The map is not a matrix: i.e., not each row has the same length.
# - An island can be diagonally contiguous to another piece of land. 
#
# ASYMPTOTIC ANALYSIS
#
# Assume that the 2D array has m number of arrays (rows), and the max length out of all those arrays is n.
#
# Time complexity: O(m*n), since we visit each cell in the array at most 2 times. 
# Space complexity: O(m*n), since the space we use to store the coordinates of cells cannot exceed the
# number of elements in the 2D array.
def sol(arr2D):
    largestSoFar = 0
    stack = []
    for i, row in enumerate(arr2D):
        for j in range(len(row)):
            if arr2D[i][j] == 0:
                continue
            else:
                stack.append((i, j))
                sizeSoFar = 0
                arr2D[i][j] = 0
                while len(stack) > 0:
                    #print(stack)
                    x, y = stack.pop()
                    sizeSoFar += 1
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            try:
                                if x+a >= 0 and y+b >=0 and arr2D[x+a][y+b] == 1:
                                    stack.append((x+a, y+b))                     
                                    arr2D[x+a][y+b] = 0
                            except:
                                continue
                if largestSoFar < sizeSoFar:
                    largestSoFar = sizeSoFar
    return largestSoFar

# Solution using basic recursion. We could make it tail recursive by adding another param to
# `sizeOfIsland()` to keep track of the stack of points to pop off, similar to the iterative version. 
def solRec(arr2D):
    def sizeOfIsland(arr2D, i, j):
        try:
            if i >= 0 and j >= 0 and arr2D[i][j] == 1:                    
                arr2D[i][j] = 0
                return 1 + sizeOfIsland(arr2D, i+1, j+1) + sizeOfIsland(arr2D, i+1, j) + sizeOfIsland(arr2D, i+1, j-1) + sizeOfIsland(arr2D, i, j+1) + sizeOfIsland(arr2D, i, j-1) + sizeOfIsland(arr2D, i-1, j+1) + sizeOfIsland(arr2D, i-1, j) + sizeOfIsland(arr2D, i-1, j-1)
            return 0
        except:
            return 0

    largestSoFar = 0
    for i, row in enumerate(arr2D):
        for j in range(len(row)):
            if arr2D[i][j] == 0:
                continue
            else:
                nextSize = sizeOfIsland(arr2D, i, j)
                if nextSize > largestSoFar:
                    largestSoFar = nextSize
    return largestSoFar
        

print("Running Tests...\n")

arr2D = [[1, 1, 0],
         [0, 1],
         [1]]
print("Expected: 4", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [0, 1],
         [0, 0, 1, 0]]
print("Expected: 3", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [0, 0],
         [0, 0, 1, 0]]
print("Expected: 1", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 0, 0],
         [0, 0],
         [0, 0, 0, 0]]
print("Expected: 0", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [1, 0],
         [0, 0, 1, 0]]
print("Expected: 2", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [1, 0],
         [0, 0, 1, 0]]
print("Expected: 2", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0, 1],
         [1, 0, 1, 1],
         [0, 0, 1, 0]]
print("Expected: 6", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1]]
print("Expected: 6", f"Actual: {sol(arr2D)}\n", sep="\n")

print("Running Tests II...\n")

sol = solRec

arr2D = [[1, 1, 0],
         [0, 1],
         [1]]
print("Expected: 4", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [0, 1],
         [0, 0, 1, 0]]
print("Expected: 3", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [0, 0],
         [0, 0, 1, 0]]
print("Expected: 1", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 0, 0],
         [0, 0],
         [0, 0, 0, 0]]
print("Expected: 0", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [1, 0],
         [0, 0, 1, 0]]
print("Expected: 2", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0],
         [1, 0],
         [0, 0, 1, 0]]
print("Expected: 2", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 1, 0, 1],
         [1, 0, 1, 1],
         [0, 0, 1, 0]]
print("Expected: 6", f"Actual: {sol(arr2D)}\n", sep="\n")

arr2D = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1]]
print("Expected: 6", f"Actual: {sol(arr2D)}\n", sep="\n")

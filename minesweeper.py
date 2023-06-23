# Compulsory Task 1

def minesweeper(grid):
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a new 2D array for the result
    result = [["0" for col in range(cols)] for row in range(rows)]      # The result grid is created with the same shape as the input grid and filled with '0'
    
    # Iterate over each spot in the grid
    for row in range(rows):
        for col in range(cols):
            # If the spot is a mine, mark it as such in the result array
            if grid[row][col] == "#":
                result[row][col] = "#"
            else:
                # Count the number of adjacent mines
                count = 0
                for x in range(max(0, row-1), min(rows, row+2)):
                    for y in range(max(0, col-1), min(cols, col+2)):
                        if grid[x][y] == "#":
                            count += 1
                
                # Convert the count to a string and store it in the result array
                result[row][col] = str(count)
    
    # Return the result array
    return result

# Test the function 
test = [ 
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"] 
]

result = minesweeper(test)

# Print the reult in grid format
for row in result:
    print(row)
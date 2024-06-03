def calculate_yield(matrix, row_harry, column_ron):
    harry_yield = sum(matrix[row_harry])
    ron_yield = sum(matrix[i][column_ron] for i in range(len(matrix)))

    # Check the intersection point between the two lines.
    if row_harry <= column_ron:
        harry_yield -= matrix[row_harry][column_ron]
    else:
        ron_yield -= matrix[row_harry][column_ron]

    return harry_yield, ron_yield


# Read the input.
size = int(input())
harvest_matrix = [list(map(int, input().split())) for _ in range(size)]
harry_row, ron_column = map(int, input().split())

# Calculate the yield for the wizard and witch.
harry_yield, ron_yield = calculate_yield(harvest_matrix, harry_row, ron_column)

# Print the output.
print("Harry", harry_yield)
print("Ron", ron_yield)

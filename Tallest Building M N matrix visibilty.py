#Find the tallest building score from M*N matrix 
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Element at [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    # Get the position of the element
    row = int(input("Enter the row index of the element: "))
    col = int(input("Enter the column index of the element: "))

    # Ensure the provided indices are within bounds
    if 0 <= row < n and 0 <= col < m:
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_names = ["up", "down", "left", "right"]
        adjacent_elements = []

        for d in directions:
            new_row = row + d[0]
            new_col = col + d[1]

            # Check if the new coordinates are within bounds
            if 0 <= new_row < n and 0 <= new_col < m:
                adjacent_elements.append((matrix[new_row][new_col], direction_names[directions.index(d)]))

        print(f"Adjacent elements to the element at ({row}, {col}): {[elem[0] for elem in adjacent_elements]}")

        # Determine the tallest building among adjacent elements
        if adjacent_elements:
            tallest_building = max(adjacent_elements, key=lambda x: x[0])
            print(f"Tallest building is {tallest_building[0]}, to the {tallest_building[1]} of {matrix[row][col]}")
    else:
        print("The provided indices are out of bounds.")

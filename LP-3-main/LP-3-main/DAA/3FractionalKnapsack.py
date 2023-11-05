def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item.append(item[1] / item[0])

    # Sort the items in descending order of their value-to-weight ratio
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if item[0] <= capacity:
            # Add the entire item to the knapsack
            knapsack.append(item)
            total_value += item[1]
            capacity -= item[0]
        else:
            # Take a fraction of the item to fill the knapsack to capacity
            fraction = capacity / item[0]
            knapsack.append([item[0] * fraction, item[1] * fraction, item[2] * fraction])
            total_value += item[1] * fraction
            break

    return knapsack, total_value

if __name__ == "__main__":
    items = [
        [2, 10],  # (weight, value)
        [3, 5],
        [5, 15],
        [7, 7],
        [1, 6]
    ]

    knapsack_capacity = 15

    result, max_value = fractional_knapsack(items, knapsack_capacity)

    print("Selected items in the knapsack:")
    for item in result:
        print(f"Weight: {item[0]}, Value: {item[1]}")

    print(f"Total Value: {max_value}")

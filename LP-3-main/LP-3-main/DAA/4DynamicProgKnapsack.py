def knapsack_01(values, weights, capacity):
    n = len(values)

    # Initialize a table to store the results for subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table using dynamic programming
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Either include the item or exclude it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the selected items
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    selected_items.reverse()

    return dp[n][capacity], selected_items

if __name__ == "__main__":
    values = [60, 100, 120]  # Values of the items
    weights = [10, 20, 30]   # Weights of the items
    capacity = 50           # Maximum knapsack capacity

    max_value, selected_items = knapsack_01(values, weights, capacity)

    print(f"Maximum value: {max_value}")
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i + 1} (Value: {values[i]}, Weight: {weights[i]})")

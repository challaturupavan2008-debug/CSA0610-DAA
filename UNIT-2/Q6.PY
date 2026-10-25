#Q6: Exhaustive Search for Package Selection

def package_selection(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_packages = []
    combinations = 0

    # Check all possible combinations
    for i in range(1 << n):
        total_weight = 0
        total_value = 0
        selected = []

        for j in range(n):
            if i & (1 << j):
                total_weight += weights[j]
                total_value += values[j]
                selected.append(j + 1)

        combinations += 1

        if total_weight <= capacity:
            if total_value > max_value:
                max_value = total_value
                best_packages = selected

    return best_packages, max_value, combinations


def main():
    test_cases = [
        ([2, 3, 4], [10, 20, 30], 5),
        ([1, 2, 3], [10, 15, 40], 4),
        ([4, 5, 6], [10, 20, 30], 10),
        ([5, 6], [10, 20], 3),
        ([1, 2, 3, 4], [5, 10, 15, 20], 5)
    ]

    for weights, values, capacity in test_cases:
        print("\nWeights:", weights)
        print("Values:", values)
        print("Capacity:", capacity)

        packages, max_value, combinations = package_selection(
            weights, values, capacity
        )

        print("Selected Packages:", packages)
        print("Maximum Value:", max_value)
        print("Total Combinations Checked:", combinations)


main()

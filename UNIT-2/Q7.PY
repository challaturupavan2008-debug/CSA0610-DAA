#Improved Package Selection Using Branch and Bound

def package_selection(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_packages = []
    combinations_checked = 0

    # Sort packages by value-to-weight ratio
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True
    )

    def branch(index, current_weight, current_value, selected):
        nonlocal max_value, best_packages, combinations_checked

        combinations_checked += 1

        # Stop if capacity is exceeded
        if current_weight > capacity:
            return

        # Update the best solution
        if current_value > max_value:
            max_value = current_value
            best_packages = selected.copy()

        # Stop if all packages are checked
        if index == n:
            return

        # Try including the current package
        item = items[index]

        branch(
            index + 1,
            current_weight + weights[item],
            current_value + values[item],
            selected + [item + 1]
        )

        # Try excluding the current package
        branch(
            index + 1,
            current_weight,
            current_value,
            selected
        )

    branch(0, 0, 0, [])

    return best_packages, max_value, combinations_checked


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

        packages, max_value, checked = package_selection(
            weights, values, capacity
        )

        print("Selected Packages:", sorted(packages))
        print("Maximum Value:", max_value)
        print("Search Steps:", checked)


main()

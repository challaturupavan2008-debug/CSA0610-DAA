
# Q1: Compare Three Sorting Algorithms

def selection_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(a) - 1):
        min_index = i

        for j in range(i + 1, len(a)):
            comparisons += 1

            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1

    return a, comparisons, swaps


def bubble_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(a) - 1):
        changed = False

        for j in range(len(a) - 1 - i):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                changed = True

        if not changed:
            break

    return a, comparisons, swaps


def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons, shifts


# Test datasets
datasets = {
    "Nearly Sorted": [10, 20, 30, 25, 40],
    "Reverse Order": [5, 4, 3, 2, 1],
    "Already Sorted": [1, 2, 3, 4, 5]
}

for name, data in datasets.items():
    print("\nDataset:", name)
    print("Original List:", data)

    result, comparisons, swaps = selection_sort(data)
    print("\nSelection Sort")
    print("Sorted List:", result)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

    result, comparisons, swaps = bubble_sort(data)
    print("\nBubble Sort")
    print("Sorted List:", result)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

    result, comparisons, shifts = insertion_sort(data)
    print("\nInsertion Sort")
    print("Sorted List:", result)
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)


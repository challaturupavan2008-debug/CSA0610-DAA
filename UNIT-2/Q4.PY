#Brute-Force Closest Pair of Drones
import math


def closest_pair(points):
    n = len(points)
    min_distance = float("inf")
    closest = None
    comparisons = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = math.sqrt(
                (x2 - x1) ** 2 + (y2 - y1) ** 2
            )

            comparisons += 1

            if distance < min_distance:
                min_distance = distance
                closest = (points[i], points[j])

    return closest, min_distance, comparisons


def main():
    test_cases = [
        [(1, 2), (4, 6), (2, 3), (7, 8)],
        [(0, 0), (3, 4), (1, 1)],
        [(2, 2), (5, 5)],
        [(0, 0), (0, 0), (4, 4)],
        [(1, 1)]
    ]

    for points in test_cases:
        print("\nDrone Positions:", points)

        if len(points) < 2:
            print("At least two drones are required.")
            continue

        pair, distance, comparisons = closest_pair(points)

        print("Closest Pair:", pair)
        print("Minimum Distance:", round(distance, 2))
        print("Distance Calculations:", comparisons)


main()

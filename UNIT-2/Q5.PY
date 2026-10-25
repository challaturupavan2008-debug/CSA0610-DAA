#Q5-Brute-Force Convex Hull

def cross_product(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1])
            - (p2[1] - p1[1]) * (p3[0] - p1[0]))


def brute_force_convex_hull(points):
    n = len(points)
    hull = set()

    for i in range(n):
        for j in range(i + 1, n):
            left = False
            right = False

            for k in range(n):
                if k == i or k == j:
                    continue

                value = cross_product(
                    points[i], points[j], points[k]
                )

                if value > 0:
                    left = True
                elif value < 0:
                    right = True

            if not (left and right):
                hull.add(points[i])
                hull.add(points[j])

    return sorted(hull)


def main():
    test_cases = [
        [(0, 0), (0, 4), (4, 0), (4, 4), (2, 2)],
        [(1, 1), (2, 2), (3, 3), (2, 4)],
        [(0, 0), (2, 0), (1, 1)],
        [(0, 0), (1, 1)],
        [(2, 2)]
    ]

    for points in test_cases:
        print("\nInput Points:", points)

        if len(points) < 3:
            print("At least three points are required.")
            continue

        hull = brute_force_convex_hull(points)

        print("Convex Hull Points:", hull)


main()

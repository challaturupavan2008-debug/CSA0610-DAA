
import math

# 1. Insertion Sort - Sort alerts by highest severity first
def sort_alerts(alerts):
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1

        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1

        alerts[j + 1] = key

    return alerts


# 2. Sequential Search - Check blocked IP address
def is_blocked(blocklist, ip):
    for i in range(len(blocklist)):
        if blocklist[i] == ip:
            return True

    return False


# 3. Brute-Force String Matching - Find attack signatures
def find_signature(log, pattern):
    n = len(log)
    m = len(pattern)
    hits = []

    if m == 0:
        return hits

    for i in range(n - m + 1):
        for j in range(m):
            if log[i + j] != pattern[j]:
                break
        else:
            hits.append(i)

    return hits


# 4. Brute-Force Closest Pair - Find closest login locations
def closest_logins(events):
    if len(events) < 2:
        return None, None

    min_dist = float("inf")
    pair = None

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            distance = math.sqrt(dx**2 + dy**2)

            if distance < min_dist:
                min_dist = distance
                pair = (i, j)

    return pair, min_dist


# MAIN PROGRAM - Test all four algorithms
if __name__ == "__main__":

    # Test 1: Alert Sorting
    alerts = [
        ("A1", 3), ("A2", 9), ("A3", 5),
        ("A4", 9), ("A5", 1)
    ]

    print("1. ALERT SORTING")
    print("Sorted alerts:", sort_alerts(alerts))

    # Test 2: Blocklist Checking
    blocklist = [
        "10.0.0.5", "10.0.0.9", "172.16.4.2"
    ]

    queries = ["10.0.0.9", "10.0.0.5", "8.8.8.8"]

    print("\n2. BLOCKLIST CHECKING")
    for ip in queries:
        print(ip, "->", is_blocked(blocklist, ip))

    # Test 3: Attack Signature Matching
    log = "FAILFAIXFAIL"
    pattern = "FAIL"

    print("\n3. ATTACK SIGNATURE MATCHING")
    print("Log:", log)
    print("Pattern:", pattern)
    print("Match positions:", find_signature(log, pattern))

    # Test 4: Closest Login Locations
    events = [
        (2, 3), (12, 30), (40, 50),
        (5, 1), (12, 10), (3, 4)
    ]

    print("\n4. CLOSEST LOGIN LOCATIONS")
    pair, distance = closest_logins(events)

    print("Closest pair of indices:", pair)
    print("Minimum distance:", round(distance, 3), "km")


# Q2: Sequential Search

def sequential_search(tools, target):
    comparisons = 0

    for i in range(len(tools)):
        comparisons += 1

        if tools[i] == target:
            return i, comparisons

    return -1, comparisons


# Aircraft maintenance tools
tools = ["Hammer", "Wrench", "Screwdriver", "Pliers", "Spanner"]

print("Available Tools:", tools)

# Successful searches
targets = ["Hammer", "Screwdriver", "Spanner"]

for target in targets:
    position, comparisons = sequential_search(tools, target)

    print("\nSearching for:", target)
    print("Position:", position)
    print("Comparisons:", comparisons)

# Unsuccessful search
target = "Drill"
position, comparisons = sequential_search(tools, target)

print("\nSearching for:", target)
print("Position:", position)
print("Comparisons:", comparisons)

# Test with different list sizes
print("\nTesting Different List Sizes")

for size in [5, 10, 20]:
    tool_list = list(range(1, size + 1))
    target = size

    position, comparisons = sequential_search(tool_list, target)

    print("List Size:", size,
          "| Position:", position,
          "| Comparisons:", comparisons)

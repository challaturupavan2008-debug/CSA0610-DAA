
# Q3: Brute-Force String Matching

def brute_force_match(text, pattern):
    comparisons = 0
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            return i, comparisons

    return -1, comparisons


# Test Case 1
text = "ABABCABC"
pattern = "ABC"

position, comparisons = brute_force_match(text, pattern)
print("Test Case 1")
print("Text:", text)
print("Pattern:", pattern)
print("Position:", position)
print("Character Comparisons:", comparisons)

# Test Case 2
text = "HELLOWORLD"
pattern = "WORLD"

position, comparisons = brute_force_match(text, pattern)
print("\nTest Case 2")
print("Text:", text)
print("Pattern:", pattern)
print("Position:", position)
print("Character Comparisons:", comparisons)

# Test Case 3
text = "COMPUTER"
pattern = "XYZ"

position, comparisons = brute_force_match(text, pattern)
print("\nTest Case 3")
print("Text:", text)
print("Pattern:", pattern)
print("Position:", position)
print("Character Comparisons:", comparisons)

def find_common(a, b):
    # 1. Convert lists to sets: This operation takes O(n) and O(m) time.
    set_a = set(a)
    set_b = set(b)
    # 2. Find the intersection (&): This operation is highly optimized.
    common_elements_set = set_a & set_b  # Equivalent to set_a.intersection(set_b)
    # 3. Convert the resulting set back to a list (optional, but requested format)
    return list(common_elements_set)
# Example Usage:
list_a = [1, 5, 10, 15, 20, 25]
list_b = [5, 2, 8, 15, 30, 10]

print(f"List A: {list_a}")
print(f"List B: {list_b}")

result = find_common(list_a, list_b)
print(f"Common Elements: {result}")

# Example with non-numeric data
list_c = ["apple", "banana", "orange", "grape"]
list_d = ["kiwi", "banana", "melon", "apple"]
print(f"Common Fruits: {find_common(list_c, list_d)}")

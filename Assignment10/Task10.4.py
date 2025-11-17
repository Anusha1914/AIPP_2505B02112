from typing import List

def calculate_average(scores: List[int]) -> float:
    if not scores:
        return 0.0
    # Uses the built-in sum() function for efficiency
    return sum(scores) / len(scores)

def find_highest(scores: List[int]) -> int:
    if not scores:
        return 0
    # Uses the built-in max() function for efficiency
    return max(scores)

def find_lowest(scores: List[int]) -> int:
    if not scores:
        return 0
    # Uses the built-in min() function for efficiency
    return min(scores)

def process_scores(scores: List[int]):
    if not scores:
        print("No scores provided to process.")
        return
    # Calculate statistics using the dedicated helper functions
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    # Display results
    print("--- Score Analysis Results ---")
    print(f"Total Scores Processed: {len(scores)}")
    print(f"Average Score: {avg:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score:  {lowest}")
    print("------------------------------")
# Example Usage:
student_scores = [85, 92, 78, 95, 88, 79, 92]
process_scores(student_scores)
print("\n--- Testing Empty List ---")
process_scores([])

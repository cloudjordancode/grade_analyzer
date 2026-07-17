# My Toolkit Assignment [Functions]

# 

def calculate_average(numbers):
    """Calculate  the average of a list of numbers"""

    if len(numbers) == 0:
        return 0 
    average = sum(numbers) / len(numbers)
    return average

def find_max_and_min(numbers):
    """Find the highest and lowest numbers in a list."""
    if len(numbers) == 0:
        return 0, 0
    
    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers: 
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return max_value, min_value

def count_occurences(items, target):
    """Count how many times the target appears in a list."""
    count = 0

    for item in items: 
        if item == target:
            count += 1

    return count
    
def is_palindrome(text): 
    """ Check if a string is a plaindrome."""

    cleaned_text = text.lower().replace(" ", "")
    
    return cleaned_text == cleaned_text[::-1]

        
def create_report(title, scores):
    """Create a formatted report for a list of scores"""
    average_score = calculate_average(scores)
    high_score, low_score = find_max_and_min(scores)

    return f"{title} Average: {average_score:.2f}, Highest: {high_score}, Lowest: {low_score}"


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores):.2f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores:", test_scores))
    print()



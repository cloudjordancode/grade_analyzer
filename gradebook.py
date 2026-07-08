# gradebook.py - A simple student gradebook using lists 

# Student names and their test scores
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 75, 95, 82, 91]

print("=" * 35)
print("    Student Gradebook")
print("=" * 35)

# Display all students scores
for i in range(len(students)):
    print(f"{students[i]:<12} {scores[i]}")

# Calculate class statistics 
total = sum(scores)
average = total / len(scores) 
highest = max(scores)
lowest = min(scores)

print("-" * 35)
print(f"Class Average: {average:.1f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")

# Find Student with highest score 
highest_index = scores.index(highest)
# index returns position of a value 
top_student = students[highest_index]

print(f"Top Student:    {top_student} ({highest})")

# Add new student
print("\\n--- Adding a new student ---")
new_name = input("Student Name: ")

try: 
    new_score = int(input("Test Score: "))
except ValueError:
    print("Invalid score. Using 0.")
    new_score = 0
students.append(new_name)
scores.append(new_score)

# Recalculate and display
new_average = sum(scores) / len(scores)
print(f"Updated roster: {len(students)} students")
print(f"New class average: {new_average:.1f}")

# Sort a copy of scores (don't modify the original)
sorted_scores = sorted(scores)
print(f"Scores (sorted): {sorted_scores}")

# Find median
mid = len(sorted_scores) // 2 
if len(sorted_scores) % 2 == 0:
    median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
print(f"Median score: {median}")

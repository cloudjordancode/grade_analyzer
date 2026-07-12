# Grade Analyzer

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

a_count = 0
b_count = 0 
c_count = 0 
d_count = 0
f_count = 0

for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1 
    elif score >= 60:
        d_count += 1
    else: 
        f_count += 1

total_scores = len(scores)

average = sum(scores) / total_scores

highest_score = max(scores)
lowest_score = min(scores)

passing_students = a_count + b_count + c_count + d_count
passing_percentage = (passing_students / total_scores) * 100
failing_students = f_count
failing_percentage = (failing_students / total_scores) * 100

print()
print("=== Grade Analyzer ===")
print()

print(f"Total scores: {total_scores}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")
print(f"Passing: {passing_students} ({passing_percentage})")
print(f"Failing: {failing_students} ({failing_percentage})")

print()

print("Grade Distribution: ")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")
print()

print("--- Add More Scores ---")
user_input = input("Enter a score (or 'done to finish): ")

while user_input != "done": 
    score = int(user_input)

    if 0 <= score <= 100:
        scores.append(score)
        total_scores = len(scores)
        average = sum(scores) / total_scores 
        print(f"Updated Average: {average:.1f}")
        
    else: 
        print("Number must be between 0 and 100. ")
        print("Try Again: ")
        print()

    user_input = input("Enter a score (or 'done' to finish): ")

print()

print(f"Final Average: {average:.1f}")
print()
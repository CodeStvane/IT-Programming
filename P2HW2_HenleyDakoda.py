# Dakoda Henley
# 10/8/2026
# P2HW2
# Prompts for six module grades, stores them in a list, and displays the lowest, highest, sum, and average

"""
Pseudocode:
1. Ask the user to enter the grade for Module 1 through Module 6,
   using a separate input statement for each one
2. Convert each entry to a float
3. Store all six grades in a list called module_grades
4. Find the lowest grade using min()
5. Find the highest grade using max()
6. Find the sum of the grades using sum()
7. Calculate the average by dividing the sum by the number of grades (len)
8. Display the results formatted to match the sample output
"""

# Get the grades
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store the grades in a list
module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Display results
print()
print("------------Results------------")
print("Lowest Grade:    ", lowest_grade)
print("Highest Grade:   ", highest_grade)
print("Sum of Grades:   ", sum_of_grades)
print("Average:         ", format(average_grade, ".2f"))
print("-------------------------------")
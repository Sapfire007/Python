import numpy as np

# Define student names and subject names
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
subjects = ["Math", "Science", "English"]

# Input: Marks of 5 students in 3 subjects
marks = np.array([
    [45, 39, 50],  # Alice
    [35, 28, 40],  # Bob
    [48, 50, 49],  # Charlie
    [30, 25, 35],  # David
    [49, 44, 42]   # Eve
])

# Display original marks
print("Original Marks Matrix:")
for i, student in enumerate(students):
    print(f"{student}: {marks[i]}")

# a. Find the maximum marks stored in each subject
max_marks = marks.max(axis=0)
# print(type(max_marks))
print("\nMaximum marks in each subject:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {max_marks[i]}")

# b. Find the average marks scored in each subject
average_subject_marks = marks.mean(axis=0)
print("\nAverage marks in each subject:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {average_subject_marks[i]:.2f}")

# c. Find the average marks scored by each student
average_student_marks = marks.mean(axis=1)
print("\nAverage marks scored by each student:")
for i, student in enumerate(students):
    print(f"{student}: {average_student_marks[i]:.2f}")

# d. Give 5 marks grace to any score less than 40
marks[marks < 40] += 5
print("\nFinal Marks Matrix after adding grace marks:")
for i, student in enumerate(students):
    print(f"{student}: {marks[i]}")
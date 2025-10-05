student_scores = [86, 12, 145, 145, 165, 76, 90, 200, 105]

# Calculate the total score using sum()
total_score = sum(student_scores)
print(total_score)

# Calculate the total score using a for loop
sum = 0
for score in student_scores:
    sum += score
print(f' The total score is: {sum}')

# Find the highest score  using a for loop
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
print(f' The highest score is: {max_score}')
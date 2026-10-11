scores = []
count = int(input("Hey , how many student scores you want to enter? Enter the value:"))
for i in range(0, count):
    num = int(input(f"Enter the marks of student {i+1}:"))
    scores.append(num)

print(f"Total number of students are {len(scores)} ")
print(f"Highest score is {max(scores)} ")
print(f"Lowest score is {min(scores)} ")
total = sum(scores)
print(f"The average score is {total/len(scores):.2f}")

ranked_scores = sorted(scores, reverse = True)
print(f"The top 3 scores are {ranked_scores[:3]} ")
scores = []

for i in range(3):
    score = int(input("Score: "))
    scores.append(score)



avarage = sum(scores)/len(scores)
print(f"{scores}")
print(f"{avarage}")
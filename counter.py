from collections import Counter
import best_and_worst

female = ""
male = ""
words = best_and_worst.words.splitlines()
for lines in words:
    if "She's" in lines:
        female += lines
        female += "\n"
    elif "He's" in lines:
        male += lines
        male += "\n"
counterF = Counter(female.splitlines())
print("10 Most Common Female: ")
print(counterF.most_common(10))
counterM = Counter(male.splitlines())
print("10 Most Common Male: ")
print(counterM.most_common(10))
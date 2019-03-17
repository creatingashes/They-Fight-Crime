from textblob import TextBlob

text = open("tfc2.txt", "r")
words = text.read()
des = TextBlob(words)
best_male = " "
best_female = " "
worst_male = " "
worst_female = " "
female = ""
male = ""
for sentence in des.sentences:
    if "She's" in sentence:
        sentP = sentence.polarity
        bF = TextBlob(best_female).polarity
        wF = TextBlob(worst_female).polarity
        if sentP > bF:
            best_female = str(sentence)
        if sentP < wF:
            worst_female = str(sentence)
    else:
        sentP = sentence.polarity
        bM = TextBlob(best_male).polarity
        wM = TextBlob(worst_male).polarity
        if sentP > bM:
            best_male = str(sentence)
        if sentP < wM:
            worst_male = str(sentence)
print("Best: " + best_male + " " + best_female + " They fight crime!")
print("Worst: " + worst_male + " " + worst_female + " They fight crime!")
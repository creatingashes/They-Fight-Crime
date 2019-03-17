import glob
import re


words = ""
tfc2 = open("tfc2.txt", "w+")
tfc_files2 = glob.glob('C:/Users/Ishani Ashar/PycharmProjects/FinancialTechnology/they fight crime 2/*.txt')
with tfc2 as outfile:
    for filename in tfc_files2:
        with open(filename) as infile:
            for line in infile:
                line = str(line)
                line = line.strip()
                if "She's" in line:
                    x = re.split("She", line)
                    if len(x) >= 3:
                        line = ""
                        for sentence in x:
                            if len(sentence) > 10:
                                if "She's" not in sentence:
                                    sentence = "She" + sentence
                                if sentence[0].islower():
                                    if "she's" in sentence:
                                        sentence = "S" + sentence[1:]
                                while not re.search(r'(\w|[.])$', sentence):
                                    sentence = sentence[:-1]
                                    sentence = sentence.strip()
                                if re.search(r'\w$', sentence):
                                    sentence += "."
                                if re.search(r'They fight crime!', sentence):
                                    x = re.split("They", sentence)
                                    sentence = x[0]
                                    sentence = sentence.strip()
                                while re.search(r'^\W', sentence):
                                    sentence = sentence[1:]
                                    sentence = sentence.strip()
                                line += sentence + '\n'
                                print(line)
                    else:
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                elif "He's" in line:
                    x = re.split("He", line)
                    if len(x) >= 3:
                        line = ""
                        for sentence in x:
                            if len(sentence) > 10:
                                if "He's" not in sentence:
                                    sentence = "He" + sentence
                                if sentence[0].islower():
                                    if "he's" in sentence:
                                        sentence = "H" + sentence[1:]
                                while not re.search(r'(\w|[.])$', sentence):
                                    sentence = sentence[:-1]
                                    sentence = sentence.strip()
                                if re.search(r'\w$', sentence):
                                    sentence += "."
                                while re.search(r'^\W', sentence):
                                    sentence = sentence[1:]
                                    sentence = sentence.strip()
                                line += sentence + '\n'
                    else:
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                else:
                    if line[0].islower():
                        if "she's" in line:
                            line = "S" + line[1:]
                    if re.search(r'\w$', line):
                        line += "."
                    if re.search(r'They fight crime!', line):
                        x = re.split("They", line)
                        line = x[0]
                        line = line.strip()
                    if re.search(r'^\W', line):
                        line = line[1:]
                        line = line.strip()
                line += "\n"
                outfile.write(line)

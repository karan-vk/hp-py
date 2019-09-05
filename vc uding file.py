fileName = input("Enter the file to check: ").strip()

infile = open(fileName, "r")


text = infile.read().strip()

countC = 0
countV = 0
for V in text:
    if V in "aeiou":
        countV += 1
    else:
        countC += 1


print("The number of Vowels is: ", countV, "\nThe number of consonants is: ", countC)
countT = countC + countV
countCp = (countC / countT) * 100
countVp = (countV / countT) * 100
print(f"Percentage of vowel:{countVp} \n Percentage of consonants:{countCp}")


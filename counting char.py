filename = input("Enter file name:")
n = input("Enter a letter:")
file = open(filename, mode="r")
text = file.read().strip()
count = 0
for c in text:
    if c in n:
        count += 1
print(f"{n} appears {count} times")
file.close()

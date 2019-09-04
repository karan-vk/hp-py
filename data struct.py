a = []
b = []
n = int(input("enter the number of elemnts"))
for i in range(n):
    a.append(int(input("Enter a number")))
# print(sorted(a))
# print(max(a))
# print(sorted(a))
def oe(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


for i in map(oe, a):
    b.append(i)
print(a)
print(b)

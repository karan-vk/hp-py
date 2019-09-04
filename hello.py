l = int(input("enter a number"))


def oe(n=1):
    if (n % 2 == 0):
        return "even"
    else:
        return "odd"


print(f"{l} is a ", oe(l))

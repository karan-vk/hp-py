age=int(input("Enter your age : "))
nation=input("Enter your nationality : ")
if age>18:
    if nation.lower()=="indian":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote in India")
else:
    print("You cannot vote anywhere in the world")


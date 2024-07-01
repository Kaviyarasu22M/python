a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
operation=input("add/sub/mul/div:")
if operation=="add":
    print("addition",a+b)
elif operation=="sub":
    print("subtraction",a-b)
elif operation=="mul":
    print("multiplication",a*b)
elif operation=="div":
    print("division",a/b)
else:
    print("invalid value")
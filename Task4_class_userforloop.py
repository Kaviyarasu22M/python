class loop():
    def loops(self):
        n = int(input("enter the how much your number RANGE:"))
        a = int(input("enter the ommit number1:"))
        b = int(input("enter the ommit number2"))
        for i in range(n + 1):
            if i == a or i == b:
                continue
            else:
                print(i)
m=loop()
m.loops()
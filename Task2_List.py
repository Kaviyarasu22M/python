a=[1,"kavin!",22,1,True]
b=[2,"ganesh!",43]
m=[10,9,8,7,6,5,4,3,2,1]
print(type(a),"initialvalue:",a)
a.append(10)
print("append:",a)
a.extend(b)
print("extend:",a)
a.insert(3,"nagu")
print("insert:",a)
a.reverse()
print("reverse:",a)
c=a.count(1)
print("count:",c)
d=a.index("kavin!")
print("index:",d)
a.remove(1)
print("remove:",a)
a.pop()
print("pop:",a)
m.sort()
print("sort:",m)
b.clear()
print("clear:",b)




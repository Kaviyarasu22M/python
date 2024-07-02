a={"name":"kavin!","rollno":"22"}
print(type(a),"initial:",a)
m=a.get("rollno")
print("get:",m)
c=a.keys()
print("keys:",c)
a.update({"name":"kaviyarasu"})
print("update:",a)
a.pop("rollno")
print("pop:",a)
a.values()
print("values:",a)
a.clear()
print("clear:",a)



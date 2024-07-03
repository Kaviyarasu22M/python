set1={1,2,4,5,6,8}
set2={6,7,8,5,2,9,0}
print("set:",set1)#dont allow duplicate
a=set1.union(set2)
print("union:",a)
b=set1.intersection(set2)
print("intersetion:",b)
c=set1.symmetric_difference(set2)
print("symmetric_difference:",c)
d=set1.isdisjoint(set2)
print("isdisjoint:",d)
e=set1.issuperset(set2)
print("issuperset:",e)
f=set2.difference(set1)
print("difference:",f)

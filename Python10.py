tuple=()
print(tuple)

tuple1=(1, 2, 5)
print(tuple1)

tuple2=(1, "Hi", 2, 3.4, 5)
print(tuple2)

tuple3=("Hello", [9, 0, 3], (1, 2, 3))
print(tuple3)
print(tuple3[0][2])
print(tuple3[1][1])

print(tuple1[1:3])

for i in tuple1:
    print("Hello Asia", i)

#Set
set={1, 2, 2, 2, 3, 4, 2, 4, 4, 5}
print(set)

set.add(9)
print(set)

set1={1, 2, 4}
print(set.difference(set1))
print(set.symmetric_difference(set1))

#Intersection and Union

seta={1, 3}
setb={3, 4}
print(seta.intersection(setb))
print(seta.union(setb))
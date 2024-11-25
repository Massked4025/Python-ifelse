list=['Apple', 'Banana', 'Mango', 'Dragon-fruit', 'Grape']
print("The length of list is: ", len(list))
print("The first element is: ", list[0])
print("The last element is: ", list[-1])

list.append('Orange')
print(list)

list.remove('Dragon-fruit')
print(list)

list.sort()
print(list)

list.pop(3)
print(list)

list.reverse()
print(list)

print(list*2)

list=list[:4]
print(list)

#Dictionary

dict={}
dict={1:'name', 2:'age'}
dict={'name':'Harry', 'age':14}
print(dict['name'])

dict['age']=15
print(dict)

dict['address']='London'
print(dict)

dict.pop('age')
print(dict)

dict.clear()
print(dict)

#List to Dictionary

def test(lst):
    result={}
    for i in lst:
        result[i[0]]=i[1:]
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print(students)
print(test(students))
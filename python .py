Collections 
1-List

names = ['Christopher','Susan']
scores = []
scores.append(98) # add new item to the end
scores.append(99)
print(names) //['Christopher','Susan']
print(scores) // [98,99]
print(scores[1]) # collections are zero-indexed
//99

Array are also collections of items

from array import array
//need to create array object 

scores = array('d')//d->indictes to double

scores.append(97)
scores.append(98)
print(scores)//[97,98]
print(scores[1])//[98.0]

//array('d',[97.0,98.0])

print("dasdsadas")


what's the difference between array and lists?

1-Array:
Numerical data types
must all be the same tybee
2-Lists
store anything
store any type



Comman operations

names=['Susan',Christopher']
print(len(names))//2
names.insert(0,'Bill')//insert at position 0
print(names)//['Bill','Susan',Christopher']
names.sort() //alpha order ->number->small to big
print(names)  //['Bill',,Christopher','Susan']

Retrieving ranges

names = ['Susan','Christopher','Bill','Justin']
presenters = names[1:3]
//[:3]->suzan , christopher,bill
# start and end index

print(names)//['Susan','Christopher','Bill','Justin']
print(presenters) //['Christopher','Bill']


2-Dictionaries
person = {'first':'Christopher'}
person['last'] = 'Harrison'
print(person)//{'first':'Christopher','last':'Harrison'}
print(person['first']) //christoher

//key value-pair


what the difference between Dictionaries and lists?

1-Dictionaries 
key/value pairs
storage order not guarnateed
2-Lists
zero-based index
storage order guaranteed


practical 

A={}

A['first']='Mohamad'
A['Second']='Rima

B={}

B['first']='Israa'
B['Second']='raneem'

people = []
people.append(A)
people.append(B)
print(people)
//[{'first':'mohamad','second':rima'},{'first':'Israa','second':raneem'}]




















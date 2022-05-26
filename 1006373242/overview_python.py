# -*- coding: utf-8 -*-
"""overview-python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/restrepo/ComputationalMethods/blob/master/material/overview-python.ipynb

<div style="float: right;" markdown="1">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png">
</div>

PYTHON
==
<a href="https://colab.research.google.com/github/restrepo/ComputationalMethods/blob/master/material/overview-python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Python is an interpreted programming language oriented to easy-readable coding, unlike compiled languages like C/C++ and Fortran, where the syntax usually does not favor the readability. This feature makes Python very interesting when we want to focus on something different than the program structure itself, e.g. on Computational Methods, thereby allowing to optimize our time, to debug syntax errors easily, etc.


[Official page](https://www.python.org/)

[Wikipedia](http://en.wikipedia.org/wiki/Python)

Python Philosophy
--
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules. (Although practicality beats purity)
9. Errors should never pass silently. (Unless explicitly silenced)
10. In the face of ambiguity, refuse the temptation to guess.
11. There should be one-- and preferably only one --obvious way to do it. (Although that way may not be obvious at first unless you're Dutch)
12. Now is better than never. (Although never is often better than right now)
13. If the implementation is hard to explain, it's a bad idea.
14. If the implementation is easy to explain, it may be a good idea.
15. NameSpaces are one honking great idea -- let's do more of those!

- - -

- [String, Integer, Float](#String,-Integer,-Float)
- [Functions I](#Functions-I) 
- [Hello World!](#Hello-World!) 
- [Arithmetics](#Arithmetics)
- [Lists, Tuples and Dictionaries](#Lists,-Tuples-and-Dictionaries)
- [Bucles and Conditionals](#Bucles-and-Conditionals)
- [Functions II](#Functions-II)

## Biblography
[1f] Ani Adhikari and John DeNero, [Computational and Inferential Thinking](https://www.inferentialthinking.com/chapters/intro.html)<br/>

- - -

# String, Integer, Float
The basic types of variables in Python are:

`str`:

Illustrated with the `hello world` standard
"""

#Strings
hello='hola'

"""`int`"""

#Integer
n=3

"""`float`"""

x=3.5

"""# Functions I
Python includes a battery of predefined functions which takes an input and generates an output. For example, to check the type of variable we can used the
predefined function
## `isinistance`:
"""

isinstance(hello,str)

"""**Activity**: In the next cell check if `n`  is a `float` type of variable"""



"""## `print`

See: https://pyformat.info/

To write the _Hello world_ program in python we must first introduce the concept of function. It is the same in mathematics, were something called function receives a number and return back another number. For example, the function to square a number is
\begin{equation}
f(x)=x^2\,,
\end{equation}
$x$ is called the argument of the function $f$, and the _returned_ value is the evaluation of $f(x)$.

In `Python` there are a lot of such a functions.
In particular there is a function called `print` which takes strings (see below) as input and return the same string as output. In this way, the __hello world__ program in Python is one of the most simple between all the programming languages:

# Hello World!
"""

print('Hello World!')

"""And also allows scripting: *(This code should be copied on a file 'hello.py')*"""

#! /usr/bin/python

#This is a comment
print('Hello World!')

"""The recommended way to print a variable in Python is to use the `.format` _method_ of the function `print` by preceding the sring with the letter `f`. Inside the string any variable between curly brackets, `{variable}`, can be used"""

hello='Hello World!'
print(f'{hello}')

"""__Activity__: Change the values of the previous string variables to print `Hello World!` in Spanish """



x=23456.5678545
print(f'{x:.2f}')

"""__Activity__: Print with 3 decimal places"""



# Functions

"""In `Python` it is possible also to create new [functions](https://en.wikibooks.org/wiki/Python_Programming/Functions). We illustrate the format to define a function in `Python` with the implementation of the function $f(x)=x^2$, where to write an exponent: ${}^2$, in Python we must use the format: `**2`.

## Implicit functions
"""

f=lambda x:x**2

isinstance(f,str)

type(f)

f(3)

"""## Explicit functions

The standard function build may include the help for the function
"""

def f(x):
    '''
    Calculates the square of `x`
    '''
    return x**2

"""f(5)"""

help(f)

"""The full list of built-in functions is in https://docs.python.org/3/library/functions.html and the specific help for a function, for example `print` can be checked with https://docs.python.org/3/library/functions.html#print"""

def f(x,y):
    '''
    Multiply two numbers
    '''
    return x*y
f(3,2)

#It is possible to assign default arguments
def f(x,y=2):
    '''
    Multiply two numbers. By default the second is 2
    '''    
    return x*y
#When evaluating, we can omit the default argument
f(3)

f(2,3)

f(2,y=5)

#It is possible to specify explicitly the order of the arguments
def f(x,y):
    '''
    evaluates x to the power y
    '''    
    return x**y
print( 'f(1,2)=',f(1,2) )
print( 'f(2,1)=',f(y=1,x=2) )

"""## Implicit functions of several arguments

Implicit functions are usdeful when we want to use a function once.
"""

f = lambda x,y: x**y
f(3,2)

"""## Nested functions"""

#It is possible to pass functions as arguments of other function
def f2( f, x ):
    return f(x)**2

#We can define a new function explicitly
def f(x):
    return x+2

print(f(2))
print(f2(f,2))


#Or define the function implicitly
print ("Implicit: f(2)^2 =", f2(lambda x:x+2,2) )

"""## Inner functions with returned internal function"""

def hola(func):
    def function_wrapper(x):
        res = 'hola mundo '+str(func(x))
        return res
    return function_wrapper

def mundo(n):
    return n+' y despiadado'

foo=hola(mundo)
foo('cruel')

"""or just"""

hola(mundo)('cruel')

"""## Decorators
From: [[@]](https://realpython.com/primer-on-python-decorators/) https://realpython.com/primer-on-python-decorators/
> By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

See also: https://www.python-course.eu/python3_decorators.php.

The previos function `hola` can be used as a decorator, in a such way that it is not necesary to call it directly but only to call its argument
"""

@hola
def mundano(n):
    return n+' y despiadado'

@hola
def mundito(n):
    return n+' y floreciente'

"""Instead `of hola(mundano)('cruel')` we can just use directly the new decorated function:"""

mundano('cruel')

mundito('brillante')

"""[[@]](https://realpython.com/primer-on-python-decorators/):
> Put simply: __decorators wrap a function, modifying its behavior.__

# Arithmetics

## Sum
"""

5.89+4.89

"""**Activity**: Sum strings:
Hint: use `+' '+`
"""



"""**Activity**: Sum integers"""

2+3

"""**Example**"""

print(hello+' '+world+'!')

"""## Multiplication"""

120*4.5

"""**Example** String multiplied by integer:"""

print('='*80)

"""## **Division**"""

#Python 3 does support complete division
100/3

100/3.

"""Force integer division"""

100//3

"""## **Module**"""

10%2

20%3

"""## **Power**"""

2**6

"""## **Scientific notation**

$1\times 10^3=10^3=1000$
"""

1E3

"""$2\times 10^3=2000$"""

2E3

"""$$\frac{ \dfrac{10^{24}}{3}+2.9\times 10^{23}}{10^2}$$"""

(1.0e24/3. + 2.9e23)/1e-2

sin=0.3

isinstance(sin,float)

from math import *

"""Keep the name space

Use `name.last_name`
"""

isinstance(sin,float)

sin

import math as m
import cmath as cm
import numpy as np
#Recommended option:
import numpy.lib.scimath as sc

isinstance(sin,float)

m.sin(0.5)

cm.sin(0.5)

np.sin(0.5)

sp.sin(0.5)

"""## Complex numbers"""

1j**2

z=2+3.2j

isinstance(z,complex)

"""Attributes and methods:"""

z.real,z.imag,z.conjugate()

z+3*z

z*z

z*z.conjugate()

`math` does not work with complex numbers

m.asin(2+0j)

cm.asin(2)

"""`numpy` requires proper input"""

np.arcsin(2)

np.arcsin(2+0j)

"""`numpy.lib.scimath` imported as `sc` here, is from `sc?`:
> Wrapper functions to more user-friendly calling of certain math functions
whose output data-type is different than the input data-type in certain
domains of the input.
Function with some parts of its domain in the complex plane like, `sqrt`, `log`, `log2`, `logn`, `log10`, `power`, `arccos`, `arcsin`, and `arctanh`.
"""

np.lib.scimath.arcsin(2)

sc.arcsin(2)

import ipywidgets as widgets

@widgets.interact
def f(x=(0,2)):
    print(np.abs(sc.arcsin(x)))

sc.arcsin([2,3])

"""# Lists, Tuples, Dictionaries and Sets

## Lists

Lists are useful when you want to store and manipulate a set of elements (even of different types).
"""

#A list is declared using [] and may content different type of objects
lista = ["abc", 42, 3.1415]
lista

#First element of the list
lista[0]

#Last element of the list
lista[-1]

#Adding a new element (boolean element)
lista.append(True)
lista

"""WARNING:"""

newlista=lista.copy()
newlista=newlista.append(5)
print(newlista)

#Inserting a new second element 
lista.insert(1, "I am second")
lista

#Deleting the third element of the list
del lista[3]
lista

#Reassign the first element of the list
lista[0] = "xyz"
lista

"""### Slicing: 
Extract elements from a list, `l` from one given index to another given index. We pass slice instead of index like this: 
```python3
l[start:end]
```
We can also define the step, like this: 
```python3
l[start:end:step]
```
If `start` is not passed it is considered 0. If `end` is not passed it is considered length of array in that dimension. The `end` can given in reverse order by assigning a minus signus to the index. For example `-1` means the last element, while `-2` means the penultimate, and so on and so forth.
"""

#Showing the elements from 0 to 2
lista[0:3]

#Showing the last two elements
lista[-2:]

#Showing elements two by two
lista[::2]

#Reverse order
lista[::-1]

lista

#also as
lista.reverse()
lista

"""### Embedded lists"""

#It is possible to embed a list
embedded_list = [lista, [True, 42]]
embedded_list

#Second element of the first list
embedded_list[0][1]

#A matrix as a list of embedded lists
A = [ [1,2], [3,4] ]
A

"""**Activity**: Obtain entry $A_{01}$ of the previous matrix, where
$$
A=\begin{pmatrix}
A_{00} & A_{01}\\
A_{10} & A_{11}\\
\end{pmatrix}
$$
"""



"""### Sum of lists"""

#When two list are added, the result is a new concatenated list
[1,2,"ab",True,[1,2]] + [3.1415,"Pi","circle"]

"""**Activity** Add a third row with integer values to the previous $A$ matrix
<!-- Answer: A=A+[[5,6]] -->
"""



"""An additional ingredient is the `append` method of a Python list. It update the elements of the list without update explicitly the variable with some equal reasignment."""

y=[]
y.append(2)
print(f'after append 2 to [] : {y}')
y.append(5)
print(f'after append 5 to [2]: {y}')

"""functions to generate lists:
* `range`

"""

list(range(3))

"""Conditional in lists:
* `in`
* `any`
* `all`
"""

3 in [4,5,6]

any([False,False,False])

any([False,False,True])

all([False,False,True])

all([True,True,True])

"""### List Comprehensions

Taken from [here](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions): List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
"""

[x**2 for x in range(10)]

[x**2 for x in range(2,10,2)]

[[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]

l=[ ['A','B','C'],['D','E','F'],['G','H','I']  ]

"""we can extract the list that contains `'H'`"""

[ll for ll in l if 'H' in ll]

'H' in l

['G','H','I'] in l

"""### Reversed comprehension
We can use the method `reversed(...)` to generate an iterator with the revesersed list so that the original list is kept.
"""

lista

print('reversed: {}'.format( list(reversed(lista)) ))
print('original: {}'.format(lista))



"""## Tuples

A tuple is almost equal to a list, except that once declared its elements, it is not possible to modify them. Therefore, tuples are useful only when you want to store some elements but not modify them.
"""

#A tuple is declared using ()
tupla = ("abc", 42, 3.1415)
tupla

"""Note: single element tuple"""

(2) #equivalent to 2

t=(2,)

len(t)

t[0]

"""The comprenhension tuple also works"""

tuple( (t for t in tupla)  )

"""`any` can extract a true value from a comprension tuple (see also `all`: https://docs.python.org/3/library/functions.html#all). 
In fact, for the following nested list:
"""

l=[ ['A','B','C'],['D','E','F'],['G','H','I']   ]

"""we can extract the list that contains `'H'` more easily"""

[ll for ll in l]

any((s=='L' for s in ['G', 'H', 'I']))

[ll for ll in l if any( s=='H' for s in ll  ) ]

"""With the function `zip` we can generate dictionary-like tuple from two lists:"""

list(zip( ['A','B','C'],[1,2,3]  ))

list(zip( ['A','B','C'],[1,2,3]  ))

#It is not possible to add more elements
tupla.append("xy")

#It is not possible to delete an element
del tupla[0]

#It is not possible to modify an existing element
tupla[0] = "xy"

"""## Dictionaries

Dictionaries are labeled lists: with keys and values. They are extremely useful when manipulating complex data. In Wolfram Alpha the equivalent object is called [Associations](https://reference.wolfram.com/language/guide/Associations.html)
"""

#A dictionary is declared using {}, and specifying the name of the component, then the character : followed by the element to store.
dictionary={ 'Kenia'         :'Nairobi',
             'Noruega'       :'Oslo',
             'Finlandia'     :'Helsinski',
             'Rusia'         :'Moscú',
             'Rio de Janeiro':'Rio',
             'Japón'         :'Tokio',
             'Colorado'      :'Denver',
             'Alemania'      :'Berlin',
             'Colombia'      :'Bogotá'}
print(dictionary)
#Note the order in a dictionary does not matter as one identifies a single element through a string, not a number

"""Instead of a number, an element of a dictionary is accessed with the key of the component"""

dictionary

print('{} ♥ {}'.format( dictionary['Japón'], dictionary['Rio de Janeiro']) )

#The elements of the dictionary may be of any type
dictionary2 = { "Enteros":[1,2,3,4,5], 
                "Ciudad" :"Medellin", 
                "Cédula" :1128400433, 
                "Colores":["Amarillo", "Azul", "Rojo"] }
print(dictionary2["Colores"][1])

#The elements of the dictionary can be modified only by changing directly such an element
dictionary2["Ciudad"] = "Bogota"
print(dictionary2)

#Adding a new element is possible by only defining the new component
dictionary2["Pais"] = "Colombia"
dictionary2["País"] = "Chile"
print( dictionary2 )

#dictionary2.update({'Pais':'Colombia'})

"""List-like dictionary"""

l={0:45,1:345,2:987}
l[0]

l={0.3:45}

l[0.3]

d={True:'Verdadero'}
d[True]

#The command del can be also used for deleting an element, as a list
del dictionary2["Pais"]
print(dictionary2)

"""With the previous `zip` function to create tuples from lists, we can create a dictionary from the two lists:"""

list(zip( ['A','B','C'],[1,2,3]  ))

dict(zip( ['A','B','C'],[1,2,3]  ))

"""**Activity**: Creates a diccionary for the values: `['xyz',3,4.5]` with integer keys starting with zero. In this way, the dictionary could behave as list"""

l={}
l[0]='xyz'
l[1]=3
l[2]=4.5

l

l[0]

l.get(3)

"""### Non-relational databases
A list of dictionaries is simple example of a non-relational database. Their main advantage is that with the proper glosary for the keys of the dictionaries the data analysis is well expressed through the impledmented code
"""

people=[{'name':'Juan',  'last_name':'Valdez','age':25},
        {'name':'Álvaro','last_name':'Uribe', 'age':69}
       ]

"""Extract the last names from the `people` data base (Note the very expressive sintaxis!)"""

[d.get('last_name') for d in people]

"""Sum the ages"""

sum([d.get('age') for d in people])

"""### Sets"""

Z2={0,1}
Z3={0,1,2}
Z2.intersection(Z3)

Z2.union(Z3)

Z2.issubset(Z3)

"""The elements of the set must be unique and sorted"""

U={1,2,2,2,4,4,-2}
U

"""Aplicación: Obtenga los elementos únicos de una lista"""

l=[3,7,1,9,4,6,6]
list(set(l))

"""# Conditionals

## if

Conditionals are useful when we want to check some condition.
The statements `elif` and `else` can be used when more than one condition need to be used, or when there is something to do when some condition is not fulfilled.
"""

x = 10
y = 2
if x > 5 and y==2:
    print( "True" )

x = 4
y = 3
if x>5 or y<2:
    print( "True 1" )
elif x==4:
    print( "True 2" )
else:
    print( "False" )

"""# Loops

## for

`For` cycles are specially useful when we want to sweep a set of elements with a known size.
"""

for i in range(0,5,1):
    print( i, i**2)

"""__Activity__: change print with format"""



suma = 0
for i in range(10):
    suma += i**2 # suma = suma + i**2
print ( f"The result is {suma}" )

for language in ['Python', 'C', 'C++', 'Ruby', 'Java']:
    print ( language )

"""As we see before, `for` can be used to build comprenhension lists"""

serie = [ i**2 for i in range(1,10) ]
print( serie )

"""## while

`While` cycles are specially useful when we want to sweep a set of elements with an  unknown size.

Before we check the functions `input` and `int` of Python
"""

edad=input('¿What is your age, Jesus?:\n')

int(edad)

"""Bonus: some time the input must be hidden"""

import getpass

c=getpass.getpass('Contraseña')

c

"""Now the `while` examples"""

#! /usr/bin/python
number = int(input("Write a negative number: "))
while number > 0:
    print("You wrote a positive number. Do it again")
    number = int(input("Write a negative number: "))
print("Thank you!")

import random
x = 0
while x<0.9:
    x = random.random()
    print( x )
print ("The selected number was", x )

"""# Methods and attributes of objects in Python
All the objects in `Python`, including the function and variable types discussed here, are enhanced with special functions called _methods_, which are implemented after a point of the name of the variable, in the format:
```python
variable.method()
```
Some times, the method can even accept some arguments. 

The objects have also attributes which describe some property of the object. They do not end up with parenthesis:
```python
variable.attribute
```

### Methods
For example. The method `.keys()` of a variable dictionary allows to obtain the list of keys of the dictionary. For example
"""

dictionary.keys()

"""And the list of values:"""

dictionary.values()

"""For strings we have for example the conversion to lower case"""

s="Juan Valdez"
s.lower()

"juan valdez".title()

"juan valdez".upper()

"""### Attributes"""

a=1j

a.imag

a.real

z=3+5j

"""with attributes"""

z.real

z.imag

"""and the method:"""

z.conjugate()

"""In the notebook, All the methods and attributes of an object can be accessed by using the `<TAB>` key after write down the point:
```python
variable.<TAB>
```
"""

z.

"""__Activity__: Check the methods and attributes of the dictionary `dictonary`. HINT: Check the help for some of them by using a question mark, "?", at the end:
```
variable.method?
```

## Unicode
Is an standard to encode characters. In Python 3, around  [120.000 characters](https://stackoverflow.com/a/17043983) can be used to define variables. For example, one right to left arabic variable can be defined as
"""

ࢶ=2
print('Arabic character values is: {}'.format(ࢶ))

"""Spanish example"""

mamá='Lola'

"""In Jupyter lab greek symbols can be accessed by using its LaTeX command follow by the `<TAB>` key. 

`\alpha+<TAB>=0.5` could convert on the fly to 
"""

α=0.5

print(α)

"""Alternatively yuo can copy the character from some list of unicode symbols, like [this one](https://en.wikipedia.org/wiki/List_of_Unicode_characters#Greek_and_Coptic).

__Activity__: Define a Greek variable by using a symbol from the previous list

## Stop exection
Stop the program if a condition is not satisfied

See: https://realpython.com/python-exceptions/
"""

x = 6
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

print(f'codo continues here: {x}<=5')

"""## Final remarks
Make your google Python questions in English and check specially the https://stackoverflow.com/ results.

__Activity__: Make some Python query in Google and paste the example code below
"""

input('What was the Google query that you ask?:\n')

β

"""Sample code:

## Parallel
```python
foo(x) → delayed(foo)(x)
```
"""

>>> from joblib import Parallel, delayed
>>> from math import sqrt
>>> Parallel(n_jobs=8)(delayed(sqrt)(i**2) for i in range(10))

"""See also: https://docs.python.org/3/library/multiprocessing.html

<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=f91b818d-f536-4b8f-81de-61752e0979b7' target="_blank">
<img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
"""
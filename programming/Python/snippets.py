#Python snippets

# 1. mapping
[*map(chr, [66, 53, 0, 94])]
== list(map(chr,[1,2,3,4,5]))

# 2. two dict MERGE
z = x.copy()
z.update(y)  #-> python3 : z = {**x, **y}

# 3. simple emerge & shuffle(randomize)
def merge_shuffled_corpus(data1, data2):
	data1.extend(data2)#add data
	random.shuffle(data1)# shuffle
	return(data1)


#Unpacking Argument Lists.
#https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

# 4. use list as arguments 
args=[3,6]
list(range(*args))
# > [3, 4, 5]
#if a=['1','2','3'] <- This is one argument, *a= 1 2 3 <- This is 3arguments


#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

"""
>>> parrot(d)
-- This parrot wouldn't voom if you put {'state': "bleedin' demised", 'voltage': 'four million', 'action': 'VOOM'} volts through it. E's a stiff !
>>> parrot(*d)
-- This parrot wouldn't action if you put state volts through it. E's voltage !
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
>>> 
"""

# 5. how to use __doc__ string
#	mymodule.py
"""This is the module docstring."""

def f(x):
    """This is the function docstring."""
    return 2 * x

# >>> import mymodule
# >>> mymodule.__doc__
# 'This is the module docstring.'
# >>> mymodule.f.__doc__
# 'This is the function docstring.'



# 6. initiate dict. useful
word_frequency.setdefault(word, 0) #{'hey': 0} : initiate
word_frequency[word] += 1
word_degree.setdefault(word, 0)
word_degree[word] += word_list_degree  #orig.


# 7. implant debug as boolean value. can impelement many places like traps.

""" simply debug """
debug = False
if debug : print something_I_want
#simply change debug into "True"



# 8.	two dict MERGE
#	z = x.copy()
#	z.update(y)  -> python3 : z = {**x, **y}


# 9.	Class, __str__, __repr__
"""
__str__ will return a human readable string. __repr__ will return an internal representation.
__repr__ can be invoked on an object by calling repr(obj) or by using backticks `obj`.
When printing lists as well as other container classes, the contained elements will be printed using __repr__.
https://stackoverflow.com/questions/12448175/confused-about-str-in-python
""" 

# 10. When want to check inside of class, instance, method
vars(test), dir(test)

# 11. using eval.
def add1(wow): print(wow)
#X : eval('add'+str(1)(2))
#O : eval('add'+str(1))(3)
eval('add'+str(1))(3) # result : 3


# 12. debugging time control
import time
time.sleep(5) # 5sec
time.sleep(0.300) #300msec

# 13. Initialize empty list
[None] * n
[0]*n # is terrible idea, 
"""
# 14. Check python version.
import struct;print( 8 * struct.calcsize("P"))    #this is for 32/64bits
import platform;print(platform.python_version())  #this is for 3.6.2 

# 15. debug traps
 _debug = False
if _debug: print 'received[%d] from %s\n%s'%(len(data),remote,data)

Python interviews and tips
30 Essential Python Tips And Tricks For Programmers
http://www.techbeamers.com/essential-python-tips-tricks-programmers/
15 Essential Python Interview Questions
https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6
"""

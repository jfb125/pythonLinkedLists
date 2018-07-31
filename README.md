# Linked List Implementation in Python

## Overview
This code is based implements a linked list in two different ways and
provides a test module for a linked list.
In the file, two implementations of a linked list are coded:
- A SingleLinkedList that is always traversed from head to tail
- A DoubleLinkedList that can be traversed in either direction
There are no methods in the API that are different based upon which
type of list that the user selects, **with the exception of __init__()**

### API
The methods implemented for both lists are: 
```python
   push(obj)           # place obj at the end of the list
   pop()               # remove and return the obj at the end of the list
   shift(obj)          # place obj at the beginning of the list
   unshift()           # remove and return the obj at the beginning of the list
   remove(obj)         # find and remove one copy of obj from the list
   get(obj)            # return the index of the first copy of obj found
   first()             # return id of first element in list
   last()              # return id of last element in list
   count()             # return the number of objects in list
   dump()              # prints the contents of the list
   debug()             # calls dump() if the dbg_lvl is above 0 
                       #   note that dbg_lvl is hard coded
```
Note that the __init__() constructor is different for each type of list:
```python
  __init__(self, obj, nxt=None)             # Single linked List
  __init__(self, obj, nxt=None, prv=None)   # Double linked list
```

### Test Module
A class for testing a linked list is provided in linkedListTests.py.
Methods for testing each of the methods in the API are provided.  
Additionally, each instance of the class can store an output method,
refered to as 'logger'.  The logger function should be passed a
severity level, currently implemented as "info" vs "error"

### License
This code is free, without any guarantee of functionality, to all parties.
This code was created while working exercises #13 & #14 from the book:
[Learn More Python 3 The Hard Way](https://learncodethehardway.org/more-python-book/)
by Zed A. Shaw

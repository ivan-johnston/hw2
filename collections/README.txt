==========================================================================
Builtin Capability of Lists, Tuple, Sets and Dictionaries ....
==========================================================================

Summary

A collection is simply a container object that can store different objects
and provide a way to access the contained objects and iterate over them.

Python provides four builtin collection data types:

1. List is a collection which is ordered and changeable.
   Allows duplicate members.

2. Tuple is a collection which is ordered and unchangeable.
   Allows duplicate members.

3. Set is a collection which is unordered, unchangeable and unindexed.
   No duplicate members.

4. Dictionary is a collection which is ordered and changeable.
   No duplicate members.

Understanding these properties can be very helpful in choosing the right
collection data type to address a task at hand.

==========================================================================
Beyond the Basics ...
==========================================================================

Beyond the basics, the collections module provides more sophisticated
implementations:

1. Counter is a subclass of the dictionary.
   It is used to keep the count of the elements in an iterable in the
   form of an unordered dictionary where the key represents the element
   in the iterable and value represents the count of that element in
   the iterable.

2. OrderedDict is a subclass of dictionary but unlike dictionary,
   it remembers the order in which the keys were inserted. 

3. DefaultDict is ...
4. ChainMap ...
5. NamedTuple ...
6. DeQue ...
7  UserDict ...
8. UserList ...
9. UserString ...

Notes:

1. A OrderedDict (Python) is functionally equivalent to a LinkedHashMap
   in Java.

==========================================================================
Lists
==========================================================================

Capability: Lists are used to store multiple items in a single variable.
They are created using square brackets:

Basic List Methods:

Method      Description
--------------------------------------------------------------------------
append()    Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()      Returns a copy of the list
count()     Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of
            the current list.
index()     Returns the index of the first element with the
            specified value.
insert()    Adds an element at the specified position.
pop()       Removes the element at the specified position.
remove()    Removes the item with the specified value.
reverse()   Reverses the order of the list.
sort()      Sorts the list.
--------------------------------------------------------------------------

==========================================================================
Tuple
==========================================================================

Capability: Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Tuple Methods:

Method      Description
--------------------------------------------------------------------------
count()     Returns the number of times a specified value occurs in
            a tuple.
index()     Searches the tuple for a specified value and returns the
            position of where it was found.
--------------------------------------------------------------------------

==========================================================================
Sets
==========================================================================

Capability: Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable (but you can remove
items and add new items) and unindexed.

Set Methods:

Method               Description
--------------------------------------------------------------------------
add()                Adds an element to the set.
clear()              Removes all the elements from the set.
copy()               Returns a copy of the set.
difference()         Returns a set containing the difference between
                     two or more sets.
difference_update()  Removes the items in this set that are also included
                     in another, specified set.
discard()            Remove the specified item.
intersection()       Returns a set, that is the intersection of
                     two other sets.
intersection_update()Removes the items in this set that are not present
                     in other, specified set(s).
isdisjoint()         Returns whether two sets have a intersection or not.
issubset()           Returns whether another set contains this set or not.
issuperset()         Returns whether this set contains another set or not.
pop()                Removes an element from the set.
remove()             Removes the specified element.
symmetric_difference()         Returns a set with the symmetric
                               differences of two sets.
symmetric_difference_update()  Inserts the symmetric differences from
                               this set and another.
union()	Return a set containing the union of sets
update()             Update the set with the union of this set and others.
--------------------------------------------------------------------------

==========================================================================
Dictionary
==========================================================================

Capability: Dictionaries are used to store data values in key:value pairs.
As of Python 3.7, a dictionary is a collection which is ordered,
changeable and do not allow duplicates. Dictionaries are written with
curly brackets, and have keys and values.

Dictionary Methods:

Method       Description
--------------------------------------------------------------------------
clear()      Removes all the elements from the dictionary.
copy()       Returns a copy of the dictionary.
fromkeys()   Returns a dictionary with the specified keys and value.
get()        Returns the value of the specified key.
items()      Returns a list containing a tuple for each key value pair.
keys()       Returns a list containing the dictionary's keys.
pop()        Removes the element with the specified key.
popitem()    Removes the last inserted key-value pair.
setdefault() Returns the value of the specified key. If the key does
             not exist: insert the key, with the specified value.
update()     Updates the dictionary with the specified key-value pairs.
values()     Returns a list of all the values in the dictionary.
--------------------------------------------------------------------------

==========================================================================

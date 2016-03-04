# -*- coding: utf-8 -*-
​
import sys
import collections
​
#lists
not_a_list = (1,2,)
list1 = [1,2]
list2 = list(not_a_list)  # show __builtin__
# get the tuple back by: 'new_tuple = tuple(list2)
​
print(list1 == list2, not_a_list == list1)
print('list() is iterable: ', isinstance(list1, collections.Iterable))
​
​
list1.append(3)
print('append() returns None: ', list1.append(4))
print(list1)
​
list1.append(list2)
print(list1)
​
list1.extend(list2)
print(list1)
​
list1.insert(1, 'inserted value')
var = ['bar']
new_var = varvar.append('foo')
var[0] = 'baz'
print('new_var')
del test_list[0]
multi = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
for row in multi
    print(row)
    for element in row:
        print('element: ', element)
if sys.version_info[0] == 2:
    print('xrange: ', xrange(1,10))
else:
    print('range: ', range(1,10))
​
for i in list(range(1, 15, 2)):
    print(i)
var = {1; 'value'}
new_var = var
var.update{2 'new value'}
var[1] = 'mutated value'
print('name is "{}"'.format(this_is_dict ['name'])
print('name is "{}"'.format(this_is_dict ['name', 'Default Name'])
print(this_is_dict.keys())
print(this_is_dict.values())
test_dict = {'pop-by-key':1, 'pop-by-item':2, 'to-del':3}
del test_dict['to-del']
print(test_dict)


"""3. A shallow copy and a deep copy""" 
# in Python is essential when working with complex data structures like nested lists or dictionaries.

import copy

# Original list with a nested list
original = [[1, 2], [3, 4]]  

# Shallow copy
shallow = copy.copy(original)   #copies the outer list, but inner lists are still references
# Deep copy
deep = copy.deepcopy(original)  #copies everything recursively, so no shared references remain.

# Modify inner list of original
original[0][0] = 99             # Indexing: original[0] means "first inner list" → [1, 2], Then [0] again means "first element of that inner list"
                                # Changes the value 1 → 99

print("Original:", original)       # [[99, 2], [3, 4]]
print("Shallow Copy:", shallow)    # [[99, 2], [3, 4]]  <-- affected
print("Deep Copy:", deep)          # [[1, 2], [3, 4]]   <-- unaffected

original[0][0] = 99
# This changes the first element of the first inner list in original.
# But since that inner list is also shared with shallow, the change shows up in both.


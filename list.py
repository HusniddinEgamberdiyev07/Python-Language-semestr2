# list can contain duplicate items
# list is mutable, orderd, indexed

# use [] to create a list
# use list() function to create a list. U need to pass an iterable

# create repeated elements using *
list1 = [1]*3
print(list1)

# u can access list items using [index]
fruits = ["apple", "orange", "banana"]
print(fruits[0])

# Adding elements to the list
empty = []
# 1) .append() -> adds at the end
empty.append(1)
print(empty)
# 2) .extend() -> adds multiple elements at the end
empty.extend([1, 2, 3])
print(empty)
# 3) .insert() -> adds an element at the specific position
empty.insert(0, 10)
print(empty)
# 4) +
empty = empty + fruits
print(empty)

# Removing elements from the list

# 1) .remove() -> removes the first element which has the same value as an argument
empty.remove(1)
print(empty)
# 2) .pop() -> removes an element by index or last one if no index
empty.pop(0)
print(empty)
empty.pop()
print(empty)
# 3) del listname[index] -> deletes an element by index
del empty[3]
print(empty)
# 4) .clear() -> removes all elements
empty.clear()
print(empty)

# Updating elements

# listname[index] = new_value
list1[0] = "updated"
print(list1)

# Iterating over lists

for item in list1:
    print(item)

for i in range(0, len(list1)):
    print(list1[i])
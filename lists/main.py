# List creation methods
list1 = list()  # Empty list
list2 = list([1, 2, 3])  # From another list
list3 = list("hello")  # From string
list4 = list(range(5))  # From range
list5 = [1, 2, 3, 4, 5]  # Direct creation
list5.append(6)  # Adding an element to the list

print(f"Empty list: {list1}")
print(f"From list: {list2}")
print(f"From string: {list3}")
print(f"From range: {list4}")
print(f"Direct creation: {list5}")

# Basic operations
sample_list = [1, 2, 3, 4, 5]
print(f"\nOriginal list: {sample_list}")
print(f"Length: {len(sample_list)}")
print(f"Type: {type(sample_list)}")
print(f"First element: {sample_list[0]}")
print(f"Last element: {sample_list[-1]}")
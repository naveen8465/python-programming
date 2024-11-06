#Using the reverse() Method
def reverse_list(n):
    n.reverse()
    return n

l=[1,2,3,4,5]
#print(reverse_list(l))

#Using Slicing [::-1]
def reverse_list_slicing(n):
    return n[: : -1]
#print(reverse_list_slicing(l))

#Using append() Method
def rev_list_append(n):
    e = []
    for i in reversed(n):  # Reverse the input list
        e.append(i)  # Append each element to list 'e'
    return e

# Example usage:
l = [1, 2, 3, 4]
print(rev_list_append(l))

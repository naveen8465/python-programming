# common elements finder function
# define a function with two input lists
#example [1,2,3,4,5,6][2,5,6]

l1=[1,2,3,4,5,6]
l2=[2,5,6]


def common_finder(l1, l2):
    c = []
    for i in l1:
        if i in l2:  # Check if the element is in the second list
            c.append(i)
    return c

# Example usage:
print(common_finder([1, 2, 3, 4, 5, 6], [2, 5, 6]))

        

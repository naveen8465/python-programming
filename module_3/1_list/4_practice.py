l=[1,2,3,"mudhu krishna", "pedda vedava"]

#print(l[::-1])

def rev_list(n_l):
    emp_list=[]
    for i in range(len(n_l)):
        d = n_l.pop()
        emp_list.append(d)
        return emp_list
    
print(rev_list(l))

# ** -- kwargs
#keyword arguments in dictionaries

def func(key1,**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k}:{v}")

d={"name":"linkedin","age":2012,"employer":"new_recruit"}

#func({"name":"linkedin","age":2012,"employer":"new_recruit"})

func(10,**d)



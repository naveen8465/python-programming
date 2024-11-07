#function with all parameters
#PADK

#parameter
#arguement
#default parameter(key1:10, key2:20)
#kwargs

def func_all(normal,*args,default = 500, **kwargs):
    print(normal)
    print(args)
    print(default)
    print(kwargs)

l= [12.5,40,50,300]
d=  {"one": 1, "two": 2}
func_all(9, *l, **d)
    
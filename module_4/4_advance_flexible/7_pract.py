#string reverse and first letter should be capital

def func(name, **kwargs ):
    if (kwargs .get("reverse")== True):
        return name[ : : -1].title()
    else:
        return name.title()
    
print(func("naveen",reverse =True))
    
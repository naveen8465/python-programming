#default parameters case 2

def default(name,age,gender = "male"):
    return f"{name}, {age},{gender}"

#case 2

def default(name,age=10,gender="male" ):
    return f"{name}, {age},{gender}"
print(default("naveen"))
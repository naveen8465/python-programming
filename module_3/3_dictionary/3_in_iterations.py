user_info = {
    "name" : "indian army",
    "age" : 1947,
    "fav operations": ["operation polo","operation polo 2"],
    "fav tunes":["janagana mana","vandematram"],
}

#check if key exists or not
#if "name" in user_info:
 #   print("present")
#else:
 #   print("not present")


#to trigger values use values method in it
#if "indian army" in user_info.values():
#    print("present")
#else:
 #   print("not present")


#default keys
#for i in user_info:
#    print(i)

#for values use values method
#for i in user_info.values():
#    print(i)


#for key , value in user_info.items():
 #   print(f"{key}:{value}")

# how to delete
#pop,popitem

user_info.pop("age")

print(user_info)


#do delete random use pop item
user_info.popitem()
print(user_info)



user_info = {
    "name" : "indian army",
    "age" : 1947,
    "fav operations": ["operation polo","operation polo 2"],
    "fav tunes":["janagana mana","vandematram"],
}

more_info ={
    "name":"indian",
    "state":"telangana",
    "hobbies": ["swimming","foot ball"],
}

user_info.update(more_info)

print(user_info.get("fav operation","naveen "))
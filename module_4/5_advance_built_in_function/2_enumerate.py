#india

#0 -- i
#1-- n

# name = "world"
# # pos = 0

# # for i in name:
# #     print(f"{pos} -- {i}")
# #     pos += 1

# for p,v in enumerate(name):
#     print(f"{p}:{v}")

l = ["apple","glass","water","naveen"]

def find_position(li, fi):
    for p,v in enumerate(li):
        if v == fi:
            return p
    return -1
    
print(find_position(l,"glass"))

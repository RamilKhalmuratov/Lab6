def all_true(t):
    return all(t)

t = (True, 1, "Ahahahh")  
print(all_true(t))

t2 = (True, 1, "")
print(all_true(t2))

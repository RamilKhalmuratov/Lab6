def count_case(s):
    upper_count = sum(map(str.isupper, s))
    lower_count = sum(map(str.islower, s))
    return upper_count, lower_count

text = input("Enter a string: ")
upper, lower = count_case(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
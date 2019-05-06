my_age = 26

print("Hey how old are you?")
age = int(input())

age_diff = age - my_age
print("Hey, we're {} years apart!".format(age_diff))

if age > 105:
    print("Yeah Dorian Gray was a lich too.")
else:
    print("Neat!")
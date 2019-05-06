# 1. An average tip is 15% so a good tip could be 18% or 20%. They were great so I'll do 20%.
meal_cost = 55.00
tip_amount = meal_cost * 0.20
total = meal_cost + tip_amount
print(total)

# 2. To turn an integer into a string you would use str(), putting the integer within the brackets.
print("The meal will cost $" + str(66) + ".")

# 3. String Interpolation uses {} and .format()

print("45628 multiplied by 7839 equals {}.".format(45628 * 7839))

# 4. The answer will be true, the second statement is true and Or only needs one true statement to come out as True. 

print((10 < 20 and 30 < 20) or not(10 == 11))
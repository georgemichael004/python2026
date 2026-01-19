# Task: Count how many numbers are positive, negative, and zero.
the_list = [3, -1, 0, 5, -2, 0]
positive = 0
negative = 0
zero = 0
for num in the_list:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
result = {"positive": positive, "negative": negative, "zero": zero}
print(result)

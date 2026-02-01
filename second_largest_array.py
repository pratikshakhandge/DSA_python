arr = [12, 5, 30, 20, 25]

largest = second = -1

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)
